MathJax.Hub.Config({
	tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
  }
});

MathJax.Hub.Configured();

var MatchingApp = angular.module('MatchingApp', ['ngRoute', 'ngSanitize', 'ui.gravatar', 'btford.markdown', 'ui.slider']);

MatchingApp.config(function($routeProvider){
  $routeProvider
    .when('/profile', {
      controller: 'ProfileController',
      templateUrl: 'static/app/views/profile.html'
    })
    .when('/engine/topics/:keyword', {
      controller: 'IterationController',
      templateUrl: 'static/app/views/engine.html'
    })
    .when('/engine/search', {
      controller: 'SearchController',
      templateUrl: 'static/app/views/search.html'
    })
    .otherwise({
      redirectTo: '/engine/search'
    });
});

MatchingApp.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
});
