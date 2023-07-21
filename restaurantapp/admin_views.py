from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.generic import TemplateView,View
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from restaurantapp.models import UserType, add_blogs, add_loc, add_menu, add_photo, customer_feedback, restaurant_feedback, restaurant_reg



class AdminIndexView(TemplateView):
    template_name = 'admin/index.html'
    
    
class rs_verify(TemplateView):
    template_name = 'admin/approve_restaurants.html'

    def get_context_data(self, **kwargs):
        context = super(rs_verify,self).get_context_data(**kwargs)

        app_rs = restaurant_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['app_rs'] = app_rs
        return context
    
class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})
    
class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Rejected"})
    

class view_restaurant(TemplateView):
    template_name = 'admin/viewrestaurant.html'
    # login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(view_restaurant, self).get_context_data(**kwargs)
        
        sv = add_loc.objects.all()       
        context['sv'] = sv
        return context

    # def post(self, request, *args, **kwargs):
    #     addresss = request.POST['address']
    #     host = add_loc.objects.filter(location__icontains=addresss)
    #     return render(request, 'customer/search.html', {'sh': host})



class viewresdetails(TemplateView):
    template_name = 'admin/viewrestaurant_details.html'
    
    def get_context_data(self, **kwargs):
        context = super(viewresdetails,self).get_context_data(**kwargs)
        # user = restaurant_reg.objects.get(user_id=self.request.user.id)
        res =self.request.GET['id']
        location = add_loc.objects.filter(restaurant_id = res) 

        context['app_loc'] = location
        images = add_photo.objects.filter(restaurant_id = res)

        context['app_img'] = images
   
            
        menu = add_menu.objects.filter(restaurant_id = res)

        context['app_menu'] = menu

        return context


class single_res(TemplateView):
    template_name = 'admin/viewrestaurant_details.html'

    def get_context_data(self, **kwargs):
        context = super(single_res,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        obj=add_loc.objects.get(id=id)
        res=obj.restaurant_id
        r=add_loc.objects.filter(restaurant_id=res)
        id2=add_photo.objects.filter(restaurant_id=res)
        menu = add_menu.objects.filter(restaurant_id = res)

        # image=obj.
        context['app'] = obj
        context['r'] = r
        context['app1'] = id2
        context['app_menu'] =menu

        return context

class view_feedback(TemplateView):
    template_name = 'admin/view_feedback.html'
    # login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(view_feedback, self).get_context_data(**kwargs)
        
        cf = customer_feedback.objects.all()       
        context['cf'] = cf
        return context
    
class view_review(TemplateView):
    template_name = 'admin/view_review.html'
    # login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(view_review, self).get_context_data(**kwargs)
        
        cf = restaurant_feedback.objects.all()       
        context['cf'] = cf
        return context

        
class BlogAdd(TemplateView):
    template_name = 'admin/addblogs.html'
    def post(self,request,*arg,**kwargs):
        
        # user = User.objects.get(pk=self.request.user.id)
        # res=restaurant_reg.objects.get(user_id=self.request.user.id)
        bn=request.POST['bname']
        bl=request.POST['blog']
        image = request.FILES['images']
        im = FileSystemStorage()
        images = im.save(image.name, image)
             
        try:
            table_user= add_blogs()
            table_user.bname=bn
            table_user.blog=bl   
            table_user.image=images  

            table_user.save()
           
            return render(request,'admin/index.html',{'message':'successfully Added'})
        except:
            messages = "Can't add image, re check the code"
            return render(request,'admin/index.html',{'message':messages})






    

    

