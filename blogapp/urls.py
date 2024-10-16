from django.urls import path
from.import views

urlpatterns = [
    path('signup/', views.signupfn),
    path('', views.loginfn, name='login'),
    path('logout/', views.logoutfn),

    path('home/', views.bloghome),
    path('createblogpost/', views.create_blog_post),
    path('userblogs/', views.userblog ),
    path('updateblogpost/<int:pk>/', views.updateblogpost),
    path('blogv/<int:pk>/', views.snglblogview),
    path('deleteblogpost/<int:pkd>/', views.deleteblogpost),

    path('profileedit/', views.profileedit), 
    path('profileview/', views.profile_view),


    path('create/', views.create_blog_post_api),
    path('gblog/<int:pk>', views.get_blog_post),
    path('blog/', views.get_all_blog_posts),
    path('update/<int:pk>', views.update_blog_post),
    path('delete/<int:pk>', views.delete_blog_post),
          
]
