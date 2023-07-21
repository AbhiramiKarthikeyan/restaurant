from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from restaurantapp.models import UserType, add_blogs,  add_loc, add_menu, add_photo, add_specials, customer_reg, customer_reviews, restaurant_reg
# from college.models import UserType, shop_reg,user_reg



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        b = add_blogs.objects.all()       
        context['bl'] = b
        return context


class Restaurant_reg(TemplateView):
    template_name = 'restaurant_reg.html'


    def post(self, request, *args, **kwargs):
        # user = User.objects.get(pk=self.request.user.id)
        # club1 = Club.objects.get(user_id=self.request.user.id)

        rn = request.POST['rname']
        # rad = request.POST['raddress']
        on = request.POST['oname']
        ph = request.POST['mobile']
        em = request.POST['email']
        oad = request.POST['oaddress']
        uname=request.POST['username']

        password = request.POST['password']
        image = request.FILES['image']
        im = FileSystemStorage()
        images = im.save(image.name, image)
      

      
        try:
            user = User.objects.create_user(first_name=rn,email=em,password=password,username=uname,last_name='0')
            user.save()
            se=restaurant_reg()
            se.user=user
            se.oname=on
            se.mobile=ph
            se.oaddress=oad
            se.license=images
            se.payment='Not paid'
            # se.raddress=rad
            se.save()

            usertype = UserType()
            usertype.user = user
            usertype.type ='restaurant'
            usertype.save()
            return render(request,'payment.html',{'user':user})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})

class payment(TemplateView):
    template_name= 'payment.html'
    def dispatch(self,request,*args,**kwargs):

        id=request.POST['id']

        # user = User.objects.get(pk=id)
        user=restaurant_reg.objects.get(user_id=id)
        user.payment='Paid'
        user.save()
        return render(request,'index.html',{'message':" Payment Successfull"})


class login_view(TemplateView):
    template_name="login.html"
    def post(self,request,*args,**kwargs):
            uname=request.POST['username']
            password =request.POST['password']
            user=auth.authenticate(username=uname,password=password)
            if user is not  None:
                login(request,user)
                if user.last_name=='1':
                    if user.is_superuser:
                        return redirect('/admin')
                    elif UserType.objects.get(user_id=user.id).type=="restaurant":
                        return redirect('/restaurant')
                    elif UserType.objects.get(user_id=user.id).type == "customer":
                        return redirect('/customer')
                    
                    
                    else:
                        return render(request,'login.html',{'message':" User Account Not Authenticated"})

                else:
                    return render(request,'login.html',{'message':" User Account Not Authenticated"})
            else:
                return render(request,'index.html',{'message':"Invalid Username or Password"})




class view_restaurant(TemplateView):
    template_name = 'viewrestaurant.html'
    # login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(view_restaurant, self).get_context_data(**kwargs)
        
        sh = add_loc.objects.all()       
        context['sh'] = sh
        return context

    def post(self, request, *args, **kwargs):
        addresss = request.POST['address']
        host = add_loc.objects.filter(location__icontains=addresss)
        return render(request, 'search.html', {'sh': host})



class view_res(TemplateView):
    template_name = 'viewrestaurant.html'
        


class single_res(TemplateView):
    template_name = 'vierestaurant_details.html'

    def get_context_data(self, **kwargs):
        context = super(single_res,self).get_context_data(**kwargs)
        id =self.request.GET['id']
        obj=add_loc.objects.get(id=id)
        res=obj.restaurant_id
        r=add_loc.objects.filter(restaurant_id=res)
        id2=add_photo.objects.filter(restaurant_id=res)
        menu = add_menu.objects.filter(restaurant_id = res)
        # event=add_events.objects.filter(restaurant_id=res)
        review=customer_reviews.objects.filter(restaurant_id=res)
        specials=add_specials.objects.filter(restaurant_id=res)


        # image=obj.
        context['app'] = obj
        context['r'] = r
        context['app1'] = id2
        context['app_menu'] =menu
        # context['app_event'] =event
        context['app_review'] =review
        context['app_sp'] =specials


        return context
    


class feed_back(TemplateView):
    template_name='feedback.html'
    def get_context_data(self, **kwargs):
        context = super(feed_back,self).get_context_data(**kwargs)
        # id=self.request.user.id
        fe = restaurant_reg.objects.all()

        context['fe'] = fe
        return context
    
    def post(self , request,*args,**kwargs):
        # user = User.objects.get(pk=self.request.user.id)
        id= request.POST['id']
        feed= request.POST['feedback']
        name= request.POST['name']

        
        fee =customer_reviews()
        fee.name = name
        fee.restaurant_id = id
        fee.feedback = feed
        # fee.subject="nooo"
        fee.save()

        return render(request, 'index.html', {'message':"successfully Submit Your Feedback"})
    
