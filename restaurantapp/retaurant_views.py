from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.generic import TemplateView,View
from django.contrib.auth import login
from django.core.files.storage import FileSystemStorage

from django.core.mail import EmailMessage
from django.conf import settings
from restaurantapp.models import  add_loc, add_menu, add_photo, add_specials, customer_reviews, restaurant_feedback, restaurant_reg



class RestaurantIndexView(TemplateView):
    template_name = 'restaurant/restaurant_index.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantIndexView,self).get_context_data(**kwargs)
        user = restaurant_reg.objects.get(user_id=self.request.user.id)
        images = add_photo.objects.filter(restaurant_id = user.id)
        menu = add_menu.objects.filter(restaurant_id= user.id)
        location = add_loc.objects.filter(restaurant_id = user.id) 
        # event = add_events.objects.filter(restaurant_id= user.id)
        review=customer_reviews.objects.filter(restaurant_id=user.id)
        specials=add_specials.objects.filter(restaurant_id=user.id)



        # context['app_event'] = event
        context['app_img'] = images
        context['app_menu'] = menu
        context['app_loc'] = location
        context['app_review'] =review
        context['app_specials'] =specials



        return context


    
    
class ImageAdd(TemplateView):
    template_name = 'restaurant/addphoto.html'
    def post(self,request,*arg,**kwargs):
        
        # user = User.objects.get(pk=self.request.user.id)
        res=restaurant_reg.objects.get(user_id=self.request.user.id)

        image = request.FILES['images']
        im = FileSystemStorage()
        images = im.save(image.name, image)
             
        try:
            table_user= add_photo()
            table_user.restaurant_id=res.id
            table_user.image=images       
            table_user.save()
           
            return render(request,'restaurant/index.html',{'message':'successfully Added'})
        except:
            messages = "Can't add image, re check the code"
            return render(request,'restaurant/index.html',{'message':messages})

class LocAdd(TemplateView):
    template_name = 'restaurant/add_location.html'
    def post(self,request,*arg,**kwargs):
        
        # user = User.objects.get(pk=self.request.user.id)
        res=restaurant_reg.objects.get(user_id=self.request.user.id)
        loc=request.POST['location']
        map=request.POST['map']
        ot=request.POST['otime']
        ct=request.POST['ctime']
             
        try:
            table_user= add_loc()
            table_user.restaurant_id=res.id
            table_user.location=loc 
            table_user.lmap=map 
            table_user.otime=ot 
            table_user.ctime=ct      
            table_user.save()
           
            return render(request,'restaurant/index.html',{'message':'successfully Added'})
        except:
            messages = "Can't add image, re check the code"
            return render(request,'restaurant/index.html',{'message':messages})


class MenuAdd(TemplateView):
    template_name = 'restaurant/add_menu.html'
    def post(self,request,*arg,**kwargs):
        
        # user = User.objects.get(pk=self.request.user.id)
        res=restaurant_reg.objects.get(user_id=self.request.user.id)
        mn=request.POST['mname']
        price=request.POST['price']
        image = request.FILES['image']
        im = FileSystemStorage()
        images = im.save(image.name, image)
             
        try:
            table_user= add_menu()
            table_user.restaurant_id=res.id
            table_user.mname=mn
            table_user.image=images  
            table_user.price=price    
            table_user.availability='availabile'
            table_user.save()
           
            return render(request,'restaurant/index.html',{'message':'successfully Added'})
        except:
            messages = "Can't add image, re check the code"
            return render(request,'restaurant/index.html',{'message':messages})

class AddSpecials(TemplateView):
    template_name = 'restaurant/add_specials.html'
    def post(self,request,*arg,**kwargs):
        
        # user = User.objects.get(pk=self.request.user.id)
        res=restaurant_reg.objects.get(user_id=self.request.user.id)
        tn=request.POST['stype']
        sn=request.POST['sname']

        price=request.POST['price']
        des=request.POST['sdes']

        image = request.FILES['image']
        im = FileSystemStorage()
        images = im.save(image.name, image)
             
        try:
            table_user= add_specials()
            table_user.restaurant_id=res.id
            table_user.sstype=tn
            table_user.sname=sn

            table_user.image=images  
            table_user.sdes=des
            table_user.price=price    
            table_user.save()
           
            return render(request,'restaurant/restaurant_index.html',{'message':'successfully Added'})
        except:
            messages = "Can't add image, re check the code"
            return render(request,'restaurant/restaurant_index.html',{'message':messages})



# class AddEvents(TemplateView):
#     template_name = 'restaurant/add_events.html'
#     def post(self,request,*arg,**kwargs):
        
#         # user = User.objects.get(pk=self.request.user.id)
#         res=restaurant_reg.objects.get(user_id=self.request.user.id)
#         en=request.POST['ename']
#         price=request.POST['price']
#         des=request.POST['edes']

#         image = request.FILES['image']
#         im = FileSystemStorage()
#         images = im.save(image.name, image)
             
#         try:
#             table_user= add_events()
#             table_user.restaurant_id=res.id
#             table_user.ename=en
#             table_user.image=images  
#             table_user.edes=des
#             table_user.price=price    
#             table_user.save()
           
#             return render(request,'restaurant/index.html',{'message':'successfully Added'})
#         except:
#             messages = "Can't add image, re check the code"
#             return render(request,'restaurant/index.html',{'message':messages})

class viewimage(TemplateView):
    template_name = 'restaurant/view_photo.html'
    
    def get_context_data(self, **kwargs):
        context = super(viewimage,self).get_context_data(**kwargs)
        user = restaurant_reg.objects.get(user_id=self.request.user.id)
        images = add_photo.objects.filter(restaurant_id = user.id)

        context['app_img'] = images
        return context


class viewloc(TemplateView):
    template_name = 'restaurant/restaurant_index.html'
    
    def get_context_data(self, **kwargs):
        context = super(viewloc,self).get_context_data(**kwargs)
        user = restaurant_reg.objects.get(user_id=self.request.user.id)
        location = add_loc.objects.filter(restaurant_id = user.id) 

        context['app_loc'] = location
        return context

class viewmenu(TemplateView):
    template_name = 'restaurant/restaurant_index.html'
    
    def get_context_data(self, **kwargs):
        context = super(viewmenu,self).get_context_data(**kwargs)
        user = restaurant_reg.objects.get(user_id=self.request.user.id)
        menu = add_menu.objects.filter(restaurant_id= user.id)

        context['app_menu'] = menu
        return context

# class viewevent(TemplateView):
#     template_name = 'restaurant/restaurant_index.html'
    
#     def get_context_data(self, **kwargs):
#         context = super(viewevent,self).get_context_data(**kwargs)
#         user = restaurant_reg.objects.get(user_id=self.request.user.id)
#         menu = add_events.objects.filter(restaurant_id= user.id)
        

#         context['app_event'] = menu
#         return context

class menu_delete(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        add_menu.objects.get(id=id).delete()

        return render(request,'restaurant/restaurant_index.html',{'message':"menu Removed"})
    
class menu_edit(TemplateView):
    template_name = 'restaurant/edit_menu.html'


    def get_context_data(self, **kwargs):
        context = super(menu_edit,self).get_context_data(**kwargs)
        ids =self.request.GET['id']

        app_user = add_menu.objects.filter(id=ids)
        context['app_update'] = app_user
        return context
    

    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        usr = add_menu.objects.get(pk=id)
        image = request.FILES['image']
        im = FileSystemStorage()
        images = im.save(image.name, image)
        usr.price = request.POST['price']
        usr.mname = request.POST['mname']
        usr.availability = request.POST['availability']

        usr.image=images
        usr.save()
        return render(request,'restaurant/restaurant_index.html',{'message':"Menu Updated"})

     

class feedback(TemplateView):
    template_name = 'restaurant/add_review.html'
   
    def post(self,request,*arg,**kwargs):
        user = User.objects.get(pk=self.request.user.id)
        sb=request.POST['subject']
        fb=request.POST['feedback']
                        
        try:
            f= restaurant_feedback()
            f.user=user
            f.subject=sb
            f.feedback=fb
            f.save()
                             
            return render(request,'restaurant/restaurant_index.html',{'message':'feedback successfully Added'})
        except:
            messages = "Can't add feedback, re check the code"
            return render(request,'restaurant/restaurant_index.html',{'message':messages})



class loc_delete(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        add_loc.objects.get(id=id).delete()

        return render(request,'restaurant/restaurant_index.html',{'message':"location removed"})
    
class loc_edit(TemplateView):
    template_name = 'restaurant/edit_location.html'


    def get_context_data(self, **kwargs):
        context = super(loc_edit,self).get_context_data(**kwargs)
        ids =self.request.GET['id']

        app_user = add_loc.objects.filter(id=ids)
        context['app_update'] = app_user
        return context
    

    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        usr = add_loc.objects.get(pk=id)
        # image = request.FILES['image']
        # im = FileSystemStorage()
        # images = im.save(image.name, image)
        usr.location = request.POST['location']
        usr.lmap = request.POST['map']
        usr.otime= request.POST['otime']
        usr.ctime= request.POST['ctime']
        usr.save()
        return render(request,'restaurant/restaurant_index.html',{'message':"Location Updated"})
    


class photo_delete(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        add_photo.objects.get(id=id).delete()

        return render(request,'restaurant/restaurant_index.html',{'message':"Image removed"})
    


class special_delete(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        add_specials.objects.get(id=id).delete()

        return render(request,'restaurant/restaurant_index.html',{'message':"Item removed"})
    
class special_edit(TemplateView):
    template_name = 'restaurant/edit_specials.html'


    def get_context_data(self, **kwargs):
        context = super(special_edit,self).get_context_data(**kwargs)
        ids =self.request.GET['id']

        app_user = add_specials.objects.filter(id=ids)
        context['app_update'] = app_user
        return context
    

    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        usr = add_specials.objects.get(pk=id)
        image = request.FILES['image']
        im = FileSystemStorage()
        images = im.save(image.name, image)
        usr.stype = request.POST['stype']
        usr.price = request.POST['price']
        usr.sname= request.POST['sname']
        usr.sdes= request.POST['sdes']
        usr.save()
        return render(request,'restaurant/restaurant_index.html',{'message':"Special item updated successfully"})





    

