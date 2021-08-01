from django.contrib import admin

# Register your models here.
from chatapp.models import Intent, State, Option, Response, Query

admin.site.register(Intent)
admin.site.register(State)
admin.site.register(Option)
admin.site.register(Response)
admin.site.register(Query)
