from django.contrib import admin

from .models import PariMatch

# Настройка предсатвления модели
class PariMatchAdmin(admin.ModelAdmin):
    # последовательность имен полей, которые должны выводится в списке записей
    list_display = ('id', 'game', 'total', 'more', 'less', 'league')
    # последовательность имен полей, которые должны быть преобразованны в гипперсылку, ведущей на страницу правки записи
    list_display_links = ('game',)
    # последовательность имен полей, по которым должны выполнятся фильтация
    search_fields = ('game', 'content')
# Подключаем модели к админке
admin.site.register(PariMatch, PariMatchAdmin)

# class PariMatchLeagueAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('name',)
#     search_fields = ('name', 'content')
# admin.site.register(League, PariMatchLeagueAdmin)
#
# class PariMatchKindOfSportAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('name',)
#     search_fields = ('name', 'content')
# admin.site.register(KindOfSport, PariMatchKindOfSportAdmin)
