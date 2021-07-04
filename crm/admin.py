from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


# Register your models here.
# добавление ссылки на коментарий в заказе
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_date_create', 'comment_text')
    readonly_fields = ('comment_date_create',)
    extra = 0  # отображать только один реквизит


# настройка полей в админ панеле
class OrderAdm(admin.ModelAdmin):
    # Настройка списка
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_date_create')  # Отображение колонок
    list_display_links = ('id', 'order_name')  # Настройка ссылки записи
    search_fields = ('id', 'order_name', 'order_phone', 'order_date_create')  # Поиск данных
    list_filter = ('order_status',)  # фильтр данных
    list_editable = ('order_status', 'order_phone')  # редактирование записей в списке не из формы
    list_per_page = 10  # Сколько полей на странице
    list_max_show_all = 100  # Сколько показывать если показать все
    # Настройка формы
    fields = ('id', 'order_status', 'order_date_create', 'order_name', 'order_phone')  # порядок полей в форме
    readonly_fields = ('id', 'order_date_create')  # какие поля только для чтения
    # поле коментарий в форме
    inlines = [Comment, ]


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
