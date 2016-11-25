myApp.config(["$routeProvider", function($routeProvider) {
	$routeProvider
		.when("/", {
			templateUrl : 'views/login.html',
			controller : 'HomeCtrl'
		})
		.otherwise('/', {
			templateUrl : 'home.html',
			controller : 'HomeCtrl'
		});
}]);