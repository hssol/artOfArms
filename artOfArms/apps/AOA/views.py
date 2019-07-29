from django.shortcuts import render

def main_page(request):
    return render(request, 'AOA/main_page.html')

def blog_page(request):
    return render(request, 'AOA/blog_page.html')
