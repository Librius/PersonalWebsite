from django.shortcuts import render
from blog.models import Category, Article
from django.http import HttpResponse

# Create your views here.


def article(request, article_title_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    category_list = Category.objects.order_by('id')
    context_dict['categories'] = category_list

    try:
        print article_title_slug
        theArticle = Article.objects.get(slug=article_title_slug)
        context_dict['article'] = theArticle
        context_dict['article_name'] = theArticle.title
        context_dict['article_content'] = theArticle.text
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'blog/article.html', context_dict)

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    category_list = Category.objects.order_by('id')
    context_dict['categories'] = category_list

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        articles = Article.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['articles'] = articles
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'blog/category.html', context_dict)


def index(request):

    context_dict = {}

    category_list = Category.objects.order_by('id')
    context_dict['categories'] = category_list
    article_list = Article.objects.order_by('-created')
    last_article = article_list[0]
    context_dict['articles'] = article_list
    context_dict['last_article'] = last_article

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'blog/index.html', context_dict)