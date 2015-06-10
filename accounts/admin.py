from django.contrib import admin
from accounts.relatedfield_admin import *
from .models import *

class ExampleAdmin(RelatedFieldAdmin):
    fieldsets = (
    ('',{
      'fields':()
    }),
    )
    list_display = ()
    list_filter = () 
    """
    exclude = ('user',)
  
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    """               
admin.site.register(,)



class ExampleAdmin(RelatedFieldAdmin):
    fieldsets = (
    ('',{
      'fields':()
    }),
    )
    list_display = ()
    list_filter = () 
    """
    exclude = ('user',)
  
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    """               
admin.site.register(,)
    
