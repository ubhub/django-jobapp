from django.shortcuts import render, redirect
from django.urls import reverse
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):

    subscribe_form = SubscribeForm()
    email_error_empty = ""
    #  The form is a bounded form--bounded to the data-- at subscribe_form = SubscribeForm()
    #  the form, if refreshed, will keep the data entered even if not saved
    if request.POST:
        print("POST issued")
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            print("valid form ")
            name = subscribe_form.cleaned_data['first_name'] + '(' + subscribe_form.cleaned_data['email'] + ')'
            print(name)
            return redirect(reverse('thank_you', args=[name]))
            # return redirect(reverse('thank_you'))
        else:
            print ("subscribe_form isn't valid")
    elif request.GET:
        print("submit issued a GET not a POST")
    # I need to clear the form here if it was saved
    context={"form": subscribe_form, "email_error_empty":email_error_empty}
    return render(request, "subscribe/subscribe.html", context)

def thank_you(request, name):
    print("name passed is ", name)
    context = {"name": name}
    return render(request, "subscribe/thank_you.html", context)
    # return render(request, "subscribe/thank_you.html")
