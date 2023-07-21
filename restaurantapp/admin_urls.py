from django.urls import path
from django.views.generic import TemplateView

from restaurantapp.admin_views import AdminIndexView, ApproveView, BlogAdd, RejectView,rs_verify, single_res, view_feedback, view_restaurant, view_review, viewresdetails


urlpatterns = [
    path('', AdminIndexView.as_view()),
    path('rs_verify',rs_verify.as_view()),
    path('s_approve',ApproveView.as_view()),
    path('s_reject',RejectView.as_view()),
    path('res', view_restaurant.as_view()),
    path('view_details', viewresdetails.as_view()),
    path('view', single_res.as_view()),
    path('feedback',view_feedback.as_view()),
    path('review',view_review.as_view()),

    path('blog',BlogAdd.as_view()),


]

def urls():
    return urlpatterns, 'admin', 'admin'
