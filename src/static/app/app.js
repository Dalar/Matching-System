var MatchingApp = angular.module('MatchingApp', ['ngRoute', 'ngSanitize', 'btford.markdown']);

/*MatchingApp.config(function($routeProvider){
  $routeProvider
    .when('/profile', {
      controller: 'ProfileController',
      templateUrl: 'static/app/views/profile.html'
    })
    .otherwise({
      redirectTo: '/profile'
    });
});*/

MatchingApp.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
});
