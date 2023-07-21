from django.urls import path
from django.views.generic import TemplateView


from restaurantapp.retaurant_views import  AddSpecials, LocAdd, MenuAdd, RestaurantIndexView,ImageAdd, feedback, loc_delete, loc_edit, menu_delete, menu_edit, photo_delete, special_delete, special_edit, viewimage, viewloc, viewmenu


urlpatterns = [
    path('',RestaurantIndexView.as_view()),
    path('add_image',ImageAdd.as_view()),
    path('view_image',viewimage.as_view()),
    path('add_loc',LocAdd.as_view()),
    path('view_loc',viewloc.as_view()),
    path('menu_add',MenuAdd.as_view()),
    path('feedback',feedback.as_view()),
    path('add_specials',AddSpecials.as_view()),

    path('view_menu',viewmenu.as_view()),
    path('menu_delete',menu_delete.as_view()),
    path('menu_edit',menu_edit.as_view()),
    # path('event_delete',event_delete.as_view()),
    # path('event_edit',event_edit.as_view()),
    path('loc_delete',loc_delete.as_view()),
    path('loc_edit',loc_edit.as_view()),
    path('photo_delete',photo_delete.as_view()),
    path('special_delete',special_delete.as_view()),
    path('special_edit',special_edit.as_view()),





    path('feedback',feedback.as_view()),

]

def urls():
    return urlpatterns, 'restaurant', 'restaurant'
