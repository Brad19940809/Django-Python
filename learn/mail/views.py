from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from mail.forms import ContactForm


def EmailForm(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['info@example.com']
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('/thanks/')
