from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

# 笔记本
def noteBook(request):
#	post_list = Article.objects.all()
	return render(request, 'notebook.html')
# 最近的笔记（时间轴）
def timeLine(request):
	return render(request, 'recentnote.html')

# 管理笔记本
def manageNote(request):
	return render(request,'manage_notebook.html')

# 回收站

def trash(request):
	return render(request,'trash.html')