myApp.controller('HomeCtrl', ["$scope", '$http', function($scope, $http) {
	$scope.name = "Login please";

	$scope.FBLogin = function() {
		FB.login(function(response) {
        if (response.status === 'connected') {
          // Logged into your app and Facebook.

        	// Send the user accessToken to the server to authenticate.
        	$http({
					  method: 'GET',
					  url: '/login/facebook?access_token=' + response.authResponse.accessToken
						}).then(function successCallback(response) {
							console.log("Login success.")
					  }, function errorCallback(response) {
							console.log("Login failed.")
					  });	
					  
					// To get the user information
		      /*FB.api('/me', function(responser) {
		        console.log(responser);
					});*/
        } else if (response.status === 'not_authorized') {
          // The person is logged into Facebook, but not your app.
					console.log("You did not authorize.")
        } else {
          // The person is not logged into Facebook, so we're not sure if
          // they are logged into this app or not.
        	console.log("Did not even logged in.")
        }
    }, {scope: 'email'});
	};
}]);