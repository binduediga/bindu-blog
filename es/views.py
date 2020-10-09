from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from emailsend import settings
from django.http import HttpResponse
import random
from es.models import EMAIL
from es.forms import EmailForm
def message(req):
	if req.method=='POST':
		tomail=req.POST['email']
		sub=req.POST['sub']
		msg=req.POST['msg']
		sender=settings.EMAIL_HOST_USER
		receiver=tomail
		send_mail(sub,msg,sender,[receiver])
		return HttpResponse("EMAIL SENT")
	return render(req,'message.html')
# Create your views here.
#def register(req):
	"""if req.method=='POST':
		f=req.POST['FIRSTNAME']
		l=req.POST['LASTNAME'] 
		e=req.POST['EMAIL']
		p=str(random.random())
		p=f[:2]+p+l[:2]
		EMAIL.objects.create(firstname=f,lastname=l,email=e,password=p)
		sub='your login details'
		body="your {} and {} are firstname and lastname and password is{}".format(f,l,p)
		sender=settings.EMAIL_HOST_USER
		receiver=e
		send_mail(sub,body,sender,[receiver])
		return HttpResponse("registered successfully")

	return render(req,'register.html')"""
def register(request):
	if request.method=='POST':
		form=EmailForm(request.POST,request.FILES)
		if form.is_valid():
			username=request.POST['username']
			password=str(random.random())
			receiver=request.POST['Email']
			sender=settings.EMAIL_HOST_USER
			sub="Reg to your Login details..."
			body="""Hello {}\n\n This is Your Username:{} \n\n 
			Your Password: {}\n\n """.format(username,username,password)
			email=EmailMessage(sub,body,sender,[receiver])
			email.content_subtype='html'
			file=request.FILES['img']
			email.attach(file.name,file.read(),file.content_type)
			email.send()
			form.save()
			return HttpResponse('Done')
	form=EmailForm()
	return render(request,'register.html',{'form':form})