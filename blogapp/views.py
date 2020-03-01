from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    # 获取所有的分类
    menus = Cate.objects.all()
    # 获取一级分类下的 前六名博客
    data = {}
    datalist = []
    for menu in menus:
        temp = {}
        blogs = Blog.objects.filter(cate_id=menu.id).order_by("-cat")[0:6]  # 取前十个
        temp["menu"] = menu
        temp["blogs"] = blogs
        datalist.append(temp)
    data["menus"] = menus
    data["datalist"] = datalist
    print(data)
    return render(request, "index.html", data)


def list(request):
    # 获取选择分类的id
    # 获取页码
    page_num = request.GET.get("page", 1)

    page_num = int(page_num)

    tid = request.GET.get("tid")
    tid = int(tid)  # 这里要 转类型，不然在模板中 == 判断 会出问题

    menus = Cate.objects.all()
    queryset = Blog.objects.filter(cate_id=tid)  # 根据 分类 id 查询所有的博客
    paginator = Paginator(queryset, per_page=5)

    page_data = paginator.get_page(page_num)

    if page_num <= 1:
        pre_num = 1
    else:
        pre_num = page_num - 1

    if page_num >= paginator.num_pages:
        next_num = paginator.num_pages
    else:
        next_num = page_num + 1

    page = {}
    page["totalnum"] = paginator.num_pages
    page["data"] = page_data
    page["cur_num"] = page_num
    page["pre_num"] = pre_num
    page["next_num"] = next_num

    data = {"menus": menus, "tid": tid, "page": page}

    return render(request, "list.html", data)


def info(request):
    menus = Cate.objects.all()
    bid = request.GET.get("bid")
    blog = Blog.objects.filter(id=bid).first()
    return render(request, "info.html", {"blog": blog, "menus": menus})
