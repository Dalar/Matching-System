MatchingApp.service('Api', function($http){
  this.updateBio = function(newBio){
    return $http.post('/update_bio', { bio_new_text: newBio });
  }

  this.getProfile = function(){
    return $http.get('/profile');
  }

  this.updateArticle = function(article){
    $http.post('/article/' + article.key + '/edit', { new_title: article.title, new_abstract: article.abstract });
  }

  this.getArticleWithKey = function(key){
    return $http.get('/article/' + key);
  }

  this.topics = function(keyword){
    console.log(encodeURIComponent(keyword));
    
    return {
      success: function(callback){
        var topics = [
          {
            weight: Math.round(Math.random()*100),
            selected: false
          },
          {
            weight: Math.round(Math.random()*100),
            selected: false
          },
          {
            weight: Math.round(Math.random()*100),
            selected: false
          },
          {
            weight: Math.round(Math.random()*100),
            selected: false
          },
          {
            weight: Math.round(Math.random()*100),
            selected: false
          },
          {
            weight: Math.round(Math.random()*100),
            selected: false
          }
        ];

        topics.forEach(function(topic){
          topic.relatedArticles = [];
          topic.keywords = [];

          _.times(10, function(){
            topic.keywords.push({
              content: 'lorem',
              weight: Math.random()
            });
          });

          _.times(5, function(){
            topic.relatedArticles.push({
              title: 'Lorem ipsum dolor sit amet',
              authors: 'Lorem ipsum, Dolor sit',
              abstract: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sodales ex eget nibh facilisis, eget condimentum neque sollicitudin. Sed rutrum tempus malesuada. Donec laoreet nec sapien quis dictum. Nulla ultrices pretium lorem, sit amet malesuada magna sagittis nec. Nullam id purus posuere, pretium quam non, pulvinar elit. Suspendisse purus elit, sodales et magna sit amet, molestie tempus turpis. Phasellus ut accumsan purus.',
              weight: Math.random()
            });
          });
        });

        callback(topics);
      }
    }
  }
});
