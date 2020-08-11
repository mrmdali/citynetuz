from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as lgn, logout as lgt, authenticate
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            lgn(request, user)
            return redirect('requests_t0_admin_new')
        else:
            messages.info(request, 'Something get wrong')
    return render(request, 'citynet/login.html')

@login_required(login_url='login')
def logout(request):
    lgt(request)
    return redirect('index')

def index(request):
    banner = Banner.objects.order_by('-id')[:2]
    service_header = ServiceHeader.objects.last()
    service_item = ServiceItem.objects.all()
    counter = Counter.objects.all()
    about = About.objects.last()
    about_item = AboutItem.objects.all()
    tariff_header = TariffHeader.objects.last()
    tariff = Tariff.objects.all()
    partner = PartnerHeader.objects.last()
    partner_img = PartnerImage.objects.order_by('-id')
    client = ClientHeader.objects.last()
    client_img = ClientImage.objects.order_by('-id')
    news_header = NewsHeader.objects.last()
    news_item_last_two = NewsItem.objects.order_by('-id')[:2]
    news_item = NewsItem.objects.order_by('-id')
    context = {'banner': banner, 'service_header': service_header,
               'service_item': service_item, 'counter': counter,
               'about': about, 'about_item': about_item,
               'tariff_header': tariff_header, 'tariff': tariff,
               'partner': partner, 'partner_img': partner_img,
               'client': client, 'client_img': client_img,
               'news_header': news_header, 'news_item': news_item,
               'news_item_last_two': news_item_last_two,
               }
    return render(request, 'citynet/index.html', context)

def about(request):
    about = About.objects.last()
    about_item = AboutItem.objects.all()
    counter = Counter.objects.all()
    partner = PartnerHeader.objects.last()
    partner_img = PartnerImage.objects.order_by('-id')

    context = {'about': about,'about_item': about_item, 'counter': counter,
               'partner': partner, 'partner_img': partner_img,
               }
    return render(request, 'citynet/about.html', context)

def internet(request):
    tariff_header = TariffHeader.objects.last()
    tariff = Tariff.objects.all()
    tariff_about = TariffAbout.objects.last()
    client = ClientHeader.objects.last()
    client_img = ClientImage.objects.order_by('-id')
    context = {'tariff_header': tariff_header, 'tariff': tariff,
               'tariff_about': tariff_about, 'client': client, 'client_img': client_img,
               }
    return render(request, 'citynet/internet.html', context)

def speedtest(request):

    return render(request, 'citynet/speedtest.html')

def blog(request):
    news_item = NewsItem.objects.order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(news_item, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users': users}
    return render(request, 'citynet/blog.html', context)

def singl_blog(request, pk):
    single_post = NewsItem.objects.get(id=pk)
    context = {'single_post': single_post}
    return render(request, 'citynet/blog_details.html', context)

def contact(request):
    contact = FooterAddress.objects.all()
    form = GetInTouchForm()
    if request.method == 'POST':
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {'contact': contact, 'form': form}
    return render(request, 'citynet/contact.html', context)

@login_required(login_url='login')
def requests_t0_admin_new(request):
    requests = GetInTouch.objects.order_by('-id').filter(read_or_not=False)
    requests_new = GetInTouch.objects.order_by('-id').filter(read_or_not=False).count()
    requests_done = GetInTouch.objects.order_by('-id').filter(read_or_not=True).count()
    request_all = GetInTouch.objects.all().count()
    page = request.GET.get('page', 1)
    paginator = Paginator(requests, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users, 'requests_new': requests_new,
               'requests_done': requests_done, 'request_all': request_all
               }
    return render(request, 'citynet/requests_t0_admin_new.html', context)

@login_required(login_url='login')
def requests_t0_admin_done(request):
    requests = GetInTouch.objects.order_by('-id').filter(read_or_not=True)
    requests_new = GetInTouch.objects.order_by('-id').filter(read_or_not=False).count()
    requests_done = GetInTouch.objects.order_by('-id').filter(read_or_not=True).count()
    request_all = GetInTouch.objects.all().count()
    page = request.GET.get('page', 1)
    paginator = Paginator(requests, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users, 'requests_new': requests_new,
               'requests_done': requests_done, 'request_all': request_all}
    return render(request, 'citynet/requests_t0_admin_done.html', context)

@login_required(login_url='login')
def request_edit(request, pk):
    edit_request = GetInTouch.objects.get(id=pk)
    requests_new = GetInTouch.objects.order_by('-id').filter(read_or_not=False).count()
    requests_done = GetInTouch.objects.order_by('-id').filter(read_or_not=True).count()
    request_all = GetInTouch.objects.all().count()
    form = GetInTouchBoolen(instance=edit_request)
    if request.method == 'POST':
        form = GetInTouchBoolen(request.POST, instance=edit_request)
        if form.is_valid():
            form.save()
            return redirect('requests_t0_admin_new')
    context = {'edit_request': edit_request, 'form': form, 'requests_new': requests_new,
               'requests_done': requests_done, 'request_all': request_all}
    return render(request, 'citynet/edit_request.html', context)

def docs(request):
    doc = Doc.objects.all()
    doc_type = DocType.objects.all()
    context = {'doc': doc, 'doc_type': doc_type}
    return render(request, 'citynet/docs.html', context)