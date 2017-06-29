import requests
from django.conf import settings


def upload_file_to_3yourmind(file_path):
    """Upload file to 3yourmind server and return upload uid."""
    stl_file = open(file_path)
    url = 'https://api.3yourmind.com/v1/uploads/'
    showname = 'Johnsshipmodel'
    files = {'file': (showname, stl_file, 'application/sla')}
    try:
        response = requests.post(url, files=files)
        data = response.json()
    except Exception as e:
        return str(e), None
    return None, data.get('uuid')


def get_material_info(uuid):
    """Return materials info."""
    api_key = settings.THREEYOURMIND_KEY
    url = "https://api.3yourmind.com/v1/uploads/%s/" % uuid
    header = {"Authorization": "ApiKey " + api_key}
    response = requests.get(url, headers=header)
    try:
        materials = response.json()
    except Exception as e:
        print str(e)
        materials = dummy_materials
    data = []
    for item in materials:
        d = {'name': item['name'], 'volume': item['parameter']['volume']}
        data.append(d)
    return data


# junk data
dummy_materials = [
{
  "status": "finished",
  "scale": 1.0,
  "unit": "mm",
  "name": "platinum",
  "uuid ": "b5fd966a-349e-4538-9514-a4183976b793",
  "is_multicolor": False,
  "share_url": "http://prodemo.3yourmind.com/en/demo/",
  "creation_date": "2016-07-12T10:41:53Z",
  "thumbnail_url": "https://3yourmind.s3.amazonaws.com/uploads/b5fd966a-349e-4538-9514-a4183976b793/thumbnail.png",
  "parameter": {
    "max_scale": 4.302040223189342,
    "volume": 18536.8515625,
    "d": 91.35800170898438,
    "w": 91.35200500488281,
    "area": 19955.99609375,
    "h": 10.280000686645508,
    "faces": 16644,
    "shells": 1,
    "holes": 0
  }
},
{
  "status": "finished",
  "scale": 1.0,
  "unit": "mm",
  "name": "silver",
  "uuid ": "b5fd966a-349e-4538-9514-a4183976b793",
  "is_multicolor": False,
  "share_url": "http://prodemo.3yourmind.com/en/demo/",
  "creation_date": "2016-07-12T10:41:53Z",
  "thumbnail_url": "https://3yourmind.s3.amazonaws.com/uploads/b5fd966a-349e-4538-9514-a4183976b793/thumbnail.png",
  "parameter": {
    "max_scale": 4.302040223189342,
    "volume": 18536.8515625,
    "d": 91.35800170898438,
    "w": 91.35200500488281,
    "area": 19955.99609375,
    "h": 10.280000686645508,
    "faces": 16644,
    "shells": 1,
    "holes": 0
  }
}

]