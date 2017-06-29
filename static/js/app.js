angular.module("app", ['ngResource']);

angular.module('app').config(['$httpProvider','$resourceProvider', function($httpProvider, $resourceProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

angular.module('app').controller('UploadCtrl', function ($scope, $http, $resource ) {
	
	var Supplier = $resource('/upload/', {});

	$scope.uploadFile = function(){
       var file = document.getElementById('file').files[0]
       var fd = new FormData();
       fd.append('file', file);
       var headers = {'Content-Disposition':'attachment; filename=' + file.name}

       $http({
	        url: "/upload",
	        method: "POST",
	        data: fd,
	        headers: headers
	    })
	    .then(function(response) {
	    	$scope.upload_error = undefined
       		$scope.materials = response.data.results
	    }, 
	    function(response) {
	    	$scope.upload_error = response.data.error
	    });
    };

	$scope.fetch_suppliers = function(material){
		$scope.search_error = ''
		Supplier.get(material, function(data) {
			material.suppliers = data.results
		}, function(data){
		});
	}

})

 