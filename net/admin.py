from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from net.models import Net, Product


# действие для обновления задолженности перед поставщиком
@admin.action(description=_("Обнуление задолженности перед поставщиком"))
def make_published(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Net)
class NetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email', 'country', 'city', 'treet', 'house', 'net', 'debt', 'created_at')
    list_filter = ('city',)
    actions = [make_published]

    # def object_link(self, obj):
    #     return obj.provider


@admin.register(Product)
class NetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'product_launch_date', 'net')
