from django.shortcuts import render, get_object_or_404, redirect
from .forms import StoryForm, ReaderForm, ReadingForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Story, Reading, Reader, Themes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# Create your views here.


@login_required()
def story_create(request):
    form = StoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "story_create.html", context)


def story_detail(request, id):
    instance = get_object_or_404(Story, id=id)
    reads = instance.reading_set.all()
    form = ReadingForm(request.POST or None, initial={'story': instance}, hide_condition=True)
    if form.is_valid():
        reading_form = form.save(commit=False)
        reading_form.save()
        form.save_m2m()
        messages.success(request, "Successfully Scheduled")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "reads": reads,
        "form": form,

    }
    return render(request, 'story_detail.html', context)


@login_required()
def story_edit(request, id):
    instance = get_object_or_404(Story, id=id)
    form = StoryForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, "Successfully Edited")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "story_create.html", context)


def story_list(request):
    queryset_list = Story.objects.all()
    query = request.GET.get("q")
    thems_filter = Themes.objects.all()
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains=query)|Q(author__icontains=query)|Q(themes__name__icontains=query)).distinct()
    themes = request.GET.get("themes")
    if themes:
        queryset_list = queryset_list.filter(Q(themes__name__icontains=themes)).distinct()
    paginator = Paginator(queryset_list, 15)  # Show 15 contacts per page
    page_request_var = 'storylist'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "list",
        "page_request_var": page_request_var,
        "themes_filter": thems_filter,
    }
    return render(request, "story_home.html", context)


@login_required()
def story_delete(request, id):
    instance = get_object_or_404(Story, id=id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Successfully Deleted")
        return render(request, "story_home.html")
    context = {
        "object": instance,
    }
    return render(request, "story_delete.html", context)


def reading_list(request):
    queryset_list = Reading.objects.all()
    query = request.GET.get("q")
    form = ReadingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect("reading_list")
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains=query)|Q(author__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 15)  # Show 25 contacts per page
    page_request_var = 'readinglist'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "list",
        "page_request_var": page_request_var,
        "form": form,
    }
    return render(request, "reading_home.html", context)


def reading_detail(request, id):
    instance = get_object_or_404(Reading, id=id)
    context = {
        "event": instance.event,
        "instance": instance,
    }
    return render(request, 'reading_detail.html', context)


@login_required()
def reading_create(request):
    form = ReadingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "reading_create.html", context)


@login_required()
def reading_delete(request, id):
    instance = get_object_or_404(Reading, id=id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Successfully Deleted")
        return redirect("reading_list")
    context = {
        "object": instance,
    }
    return render(request, "reading_delete.html", context)


@login_required()
def reading_edit(request, id):
    instance = get_object_or_404(Reading, id=id)
    form = ReadingForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Edited")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "event": instance.event,
        "instance": instance,
        "form": form,
    }
    return render(request, "reading_create.html", context)

@login_required()
def reader_create(request):
    form = ReaderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "reader_create.html", context)


def reader_detail(request, id):
    instance = get_object_or_404(Reader, id=id)
    context = {
        # "event": instance.event,
        "instance": instance,
    }
    return render(request, 'reader_detail.html', context)


def top_read(request):
    storylist = Story.objects.annotate(Count('reading')).order_by('-reading__count')[:5]
    readerlist = Reader.objects.annotate(Count('reading')).order_by('-reading__count')[:5]
    context = {
        "storylist": storylist,
        "readerlist": readerlist,
    }
    return render(request, 'top_read.html', context)
