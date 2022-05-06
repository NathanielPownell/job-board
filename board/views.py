from ast import Try
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreatePostingForm, UpdateUserForm, UpdateProfileForm, SearchForm
from . models import Posting, Profile, Employer
from register.forms import RegisterEmployerForm
from django.core.mail import send_mail
from django.conf import settings as conf_settings

# class PostingsListView(ListView):
#     model = Posting
#     paginate_by = 100
    

#     def post(self, request, **kwargs):
#         form = SearchForm(request.POST["query"])
#         if form:
#             context = super().get_context_data(**kwargs)
#             context['object_list'] = Posting.objects.filter(title__contains=form)
            
#             return context

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         context['search_form'] = SearchForm
#         return context

# ReWriting view
def PostingsListView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            postings =  Posting.objects.filter(title__contains=request.POST['query'])
    else:
        postings = Posting.objects.all()
    context = {
        'object_list': postings,
        'search_form': SearchForm,
        'now': timezone.now()
    }

    return render(request, 'board/posting_list.html', context)


class detail(DetailView):
    model = Posting

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postings_list'] = Posting.objects.all()
        return context

def apply(request, pk):
    posting = Posting.objects.get(pk=pk)

# Send email to employer
    subject = 'Application Recieved - %s' % posting.title
    message = (f'''Hello {posting.employer.name}, you have received an application for {posting.title}. 
                Name: {request.user.profile.last_name}, {request.user.profile.first_name} 
                Email: {request.user.email}''')
    email_from = conf_settings.EMAIL_HOST_USER
    recipient_list = [f'''{posting.employer.user.email}''', 'dirato2000@gmail.com']    
    send_mail( subject, message, email_from, recipient_list )
    

# Send confirmation email to applicant
    subject = 'Application Submitted - %s' % posting.title
    message = (f'''Hello {request.user.profile.first_name}, we have sent your application for {posting.title} at {posting.employer.name}. 
                Thank you.
                ''')
    email_from = conf_settings.EMAIL_HOST_USER
    recipient_list = [f'''{request.user.email}''', 'dirato2000@gmail.com']    
    send_mail( subject, message, email_from, recipient_list )

    context = {
        "posting" : posting
    }
    return render(request, 'board/apply.html', context)

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user.id)
    except:
        profile = None
    context = {
        'profile' : profile,
    }
    return render(request,'board/profile.html',  context)

@login_required
def employer(request):
    try:
        employer = Employer.objects.get(user=request.user.id)
    except:
        employer = None

    try:
        mypostings = Posting.objects.filter(employer=employer.id)
    except:
        mypostings = None
    
    context = {
        'employer' : employer,
        'postings' : mypostings,
    }
    return render(request,'board/employer.html',  context)


@login_required
def settings(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to="/profile/")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'board/settings.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def settingsEmployer(request):
    if request.method == 'POST':
        employer_form = RegisterEmployerForm(request.POST, request.FILES, instance=request.user.employer)
        if employer_form.is_valid():
            employer_form.save()

            return redirect(to="/employer/")
    else:
        employer_form = RegisterEmployerForm(instance=request.user.employer)

    return render(request, "board/settings_employer.html", {"employer_form": employer_form})


@login_required
def createPosting(request):
    if request.method == 'POST':
        posting_form = CreatePostingForm(request.POST)
        # posting_form["employer"] = request.user.employer.id

        if posting_form.is_valid():
            posting = posting_form.save(commit=False)
            posting.employer_id = request.user.employer.id
            posting.save()
            return redirect(to='/')
    else:
        posting_form = CreatePostingForm()
    return render(request, 'board/create_posting.html', {'posting_form' : posting_form})


@login_required
def editPosting(request, pk):
    posting = Posting.objects.get(pk=pk)
    if request.method == 'POST':
        posting_form = CreatePostingForm(request.POST, instance=posting)
        # posting_form["employer"] = request.user.employer.id

        if posting_form.is_valid():
            posting = posting_form.save(commit=False)
            posting.employer_id = request.user.employer.id
            posting.save()
            return redirect(to='/')
    else:
        posting_form = CreatePostingForm(instance=posting)
    return render(request, 'board/edit_posting.html', {'posting_form' : posting_form})


@login_required
def deletePosting(request, pk):
    deletePosting = Posting.objects.get(pk=pk)
    deletePosting.delete()
    context = {
        "deleted" : pk
    }
    return redirect('/employer/', context)




def searchPostings(request):
    if request.method == 'POST':

        form = SearchForm(request.POST)

        if form.is_valid():
            postings = Posting.objects.get(title__contains=form.query)

def queryPostings(request, slug):

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            postings =  Posting.objects.filter(title__contains=request.POST['query'])
            context = {
                'object_list': postings,
                'search_form': SearchForm,
                'now': timezone.now()
            }
            return render(request, 'board/posting_list.html', context)

    else:
        postings = Posting.objects.all()
    
    if slug:
        postings = Posting.objects.filter(tags__contains=slug)
    context = {
        'object_list': postings,
        "query": f'''{len(postings)} Postings Include {slug}''',
        'search_form': SearchForm,
        'now': timezone.now()
    }

    return render(request, 'board/posting_list.html', context)



