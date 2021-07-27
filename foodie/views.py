from django.shortcuts import redirect

from django.views.generic import View

from django.contrib.auth import authenticate,login,logout ,get_user_model
from account.forms import UserForm

from django.template import loader
from django.shortcuts import render
from food.models import Product
from django.db.models import Q



def main(request):
    #product = Product.objects.all()
    product = Product.objects.filter(available=True)
    template = loader.get_template('food/main.html')#we do not wrtei template becuse by defulat django is set up to see in templates folder so take care


    return render(request, 'food/main.html', {
            'product': product,

        })


class UserFormView(View):
    form_class=UserForm
    template_name='account/registration_form.html'
    #display blank form
    def get(self,request):
        form=self.form_class(None)#this means we are not using any data by default it is not passing any data and form will be displayed empty
        return render(request,self.template_name,{'form':form})



#process form data
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  ##we are sotring oti locally not in admini database
            # cleaned(normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['cpassword']
            phone_no = form.cleaned_data['phone_no']
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            # how to set the user password user.passwords='ayush' u can not change by this method

            users = authenticate(email=email,password=password)  # it checks that they exit i database or not

            if users is None:  # this means that if there  is no user that is false hten it runs if loop

                if len(phone_no) == 10:
                    if password == cpassword:
                        user.set_password(password)

                        user.last_name=phone_no

                        user.first_name=full_name

                        user.save()

                        print("doneajajshjahsjhajhjhsjkh ayush ayush")

                      #return user objets if credentials are correct
                        user=authenticate(username=username,password=password)#it checks that they exit i database or not

                        if user is not None:  # this means that if there  is no user that is false hten it runs if loop
                            if user.is_active:  # check that user is not banned or it is active account

                                login(request, user)  # it logi after testing all if
                                # request.user.user# u can request to home page or any otheer page
                                return redirect('main')

                            else:
                                error_message = "user has been deactivated"

                        else:
                            error_message = "user not exists"
                            # if user has done all thing true then it will be logeed in other wise below it will enter the details again

                    else:
                        error_message = 'Password does not match'

                else:
                    error_message = 'Enter Valid phone no'
            else:
                    error_message = 'Email exists'

        else:
            error_message="fill correctly"

        return render(request,self.template_name,{'form':form,'error_message':error_message})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:

                login(request,user)


                #albums=Vegetables.objects.filter(user=request.user)
                return redirect('main')


            else:
                return render(request,'account/login.html',{'error_message':'Your account has been disbled'})
        else:
            return render(request,'account/login.html',{'error_message':'Invalid login'})
    return render(request,'account/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'account/login.html', context)
