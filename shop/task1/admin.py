from django.contrib import admin
from .models import Buyer, Game, News

# Register your models here.


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'size')
    list_filter = ('size', 'price')
    search_fields = ('title',)
    list_per_page = 20


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    search_fields = ('title',)
    list_filter = ('date',)
    list_per_page = 20
