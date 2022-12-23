from datetime import time
import decimal
from django import http
from django.contrib.auth import SESSION_KEY, authenticate, login, logout
from django.db import IntegrityError
from django.db.models.query import EmptyQuerySet
from django.db.utils import Error
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import User, Product, Bid, Reviews

from django.db.models import Max
from decimal import Decimal


def index(request):

    listings = Product.objects.filter(status='available')
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def listing(request, lis_id, method=""):
    if method != "":
        request.method = method
    if request.user.is_authenticated:
        user = request.user
        username = user.username
        product = Product.objects.get(id=lis_id)
        if request.method == "POST":
            bid = request.POST['bid']
            r = Bid.objects.filter(product__id=lis_id).prefetch_related(
                'product').aggregate(Max('bid'))
            m = r['bid__max']
            if int(bid) <= int(m):
                return render(request, 'auctions/listing.html', {'message': 'You have to raise your bid',
                                                                 'listing': product})
            Bid.objects.create(bid=bid, user=user,
                               product=product, username=username)
            return listing(request, lis_id, "GET")
        else:
            creator = "no"
            ww = "no"
            winner = 'no'

            # getting the status value of the product whether its closed bid or still available
            p = Product.objects.get(id=lis_id)
            creat = p.creator
            status = p.status

            # checking if the product in watchlist or not
            products = user.product.all()
            answer = p in products

            # getting all the comments of that product
            comments = Reviews.objects.filter(product_id=lis_id)

            #
            print(creat)
            print(user)
            print(str(request.user) == creat)
            creator = str(request.user) == str(creat)

            # checking if the logged in user is the winner or not
            if status == "available":
                if creator != True:
                    creator = False
                ww = True

            else:
                # fetching the highest bid of that product
                bidWin = Bid.objects.filter(product__id=lis_id).prefetch_related(
                    'product').aggregate(Max('bid'))
                bidd = bidWin['bid__max']

                w = Bid.objects.get(bid=bidd, product_id=lis_id)
                winner = w.username
                print(winner)
                p.winner = winner

                p.win = True
                ww = 'yes'
                # if creator != 'yes':
                #     creator = "no"
            # v = Bid.objects.filter(product__id=lis_id).prefetch_related(
            #     'product').aggregate(Max('bid'))
            # print(v)
            # print(answer)/
            print(status)
            print(creator)
            print(status == 'available')
            print(ww)
            print(p.winner)
            # print(winner)
            # print(p.creator)

        return render(request, "auctions/listing.html", {
            "listing": p,
            "answer": answer,
            "comments": comments,
            # "win": won,
            "creator": creator,
            "winner": p.winner,
            'ww': ww,
            'message': ''

        })

    return render(request, "auctions/login.html")


def watchlist(request, lis_id):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            lis = Product.objects.get(id=lis_id)
            user.product.add(lis)

            return listing(request, lis_id, method="GET")
        else:
            context = user.product.all()
            return render(request, "auctions/watchlist.html", {
                "listings": context
            })
    return render(request, "auctions/login.html")


def create(request):

    if request.method == "POST":

        createdby = request.user
        title = request.POST["title"]
        description = request.POST["description"]
        category = request.POST["category"]
        sb = request.POST['sb']
        url = request.POST["url"]

        pro = Product.objects.create(title=title, description=description,
                                     category=category, url=url, sb=sb, creator=createdby.username)
        Bid.objects.create(bid=sb, user=request.user, product=pro)
        return index(request)

    else:
        return render(request, "auctions/create.html")


def remove(request, lis_id):
    if request.method == "POST":
        product = Product.objects.get(id=lis_id)
        user = request.user
        user.product.remove(product)
    context = user.product.all()
    return render(request, "auctions/watchlist.html", {
        "listings": context
    })


def comments(request, lis_id):
    userr = request.user
    if request.method == "POST":
        comment = request.POST["comment"]
        Reviews.objects.create(
            comment=comment, product_id=lis_id, user=userr, username=userr.username, rate=5)
    context = userr.product.all()
    return render(request, "auctions/watchlist.html", {
        "listings": context
    })


def close(request, lis_id):
    if request.method == 'POST':
        product = Product.objects.get(id=lis_id)
        product.status = 'closed'
        product.save()
        print(product.status)
    return listing(request, lis_id, "GET")


def cat(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    print(categories)
    return render(request, 'auctions/categories.html', {'categories': categories})


def cat_product(request, category):
    products = Product.objects.filter(category=category)

    return render(request, 'auctions/watchlist.html', {'listings': products})
