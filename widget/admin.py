from django.contrib import admin

from .models import thingster, Thingy

class ThingsterAdmin(admin.ModelAdmin):
  pass

class ThingyAdmin(admin.ModelAdmin):
  pass

admin.site.register(Thingy, ThingyAdmin)
admin.site.register(thingster, ThingsterAdmin)
