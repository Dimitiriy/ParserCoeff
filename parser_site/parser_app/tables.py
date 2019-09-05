import django_tables2 as tables
from .models import PariMatch

class PariMatchTable(tables.Table):
    class Meta:
        model = PariMatch
        template_name = "django_tables2/bootstrap4.html"
        fields = ("game", "league", "total", "more", "less",)
