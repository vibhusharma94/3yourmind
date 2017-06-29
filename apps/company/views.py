import os

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from rest_framework import (
    response as rest_response,
    generics as rest_generics,
    status as rest_status,
)
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import JSONParser, FileUploadParser

from apps.company import utils
from apps.company.serializer import QueryParamsSerializer, ManufacturerSerializer
from apps.company.models import Manufacturer, Company


class HomeView(rest_generics.GenericAPIView):

    permission_classes = ()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request):
        return rest_response.Response(template_name='company/home.html')


class UploadApi(rest_generics.GenericAPIView):
    """Upload API View.

    Upload .stl file to get material and price data.
    """

    permission_classes = ()
    queryset = Company.objects.all()
    parser_classes = (FileUploadParser, JSONParser)

    def get(self, request):
        """Return available suppliers for provide material."""
        serializer = QueryParamsSerializer(data=request.query_params)
        # check if all necessary query params are provided or not
        if not serializer.is_valid():
            return rest_response.Response(serializer.errors,
                                          status=rest_status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data['name']
        volume = serializer.validated_data['volume']

        # find supplier match for material
        qs = Manufacturer.objects.filter(material__name__iexact=name)
        serializer = ManufacturerSerializer(qs, many=True, context={'volume': volume})
        return rest_response.Response({'results': serializer.data})

    def post(self, request):
        """Upload api.

        Return list of materials.
        """
        file_obj = request.FILES['file']
        ext = os.path.splitext(file_obj.name)[1][1:].lower()
        if ext != 'stl':
            data = {'error': "Unsupported file type. Only .stl files are allowed."}
            return rest_response.Response(data, status=rest_status.HTTP_400_BAD_REQUEST)

        file_name = "media/" + file_obj.name
        path = default_storage.save(file_name, ContentFile(file_obj.read()))
        full_path = os.path.join(settings.MEDIA_ROOT, path)

        # upload stl file 3yourmind server
        error, upload_uuid = utils.upload_file_to_3yourmind(full_path)
        if not error and upload_uuid:
            # fetch available  materials from 3yourmind api
            data = utils.get_material_info(upload_uuid)
            return rest_response.Response({'results': data})
        else:
            data = {'error': error}
            return rest_response.Response(data, status=rest_status.HTTP_400_BAD_REQUEST)
