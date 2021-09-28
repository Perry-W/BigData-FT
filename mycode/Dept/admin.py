from django.contrib import admin

# Register your models here.
"""
from .models import Question
admin.site.register(Question)
"""
from .models import FtTest

class FtTestAdmin(admin.ModelAdmin):
    # ...
    list_display = ('pk','test_person', 'test_product', 'test_date')
    list_filter = ['test_date']
    list_per_page = 50
admin.site.register(FtTest,FtTestAdmin)


from .models import CALL
class CALLAdmin(admin.ModelAdmin):
    # ...
    list_display = ('pk','call_operator', 'call_environment','fttest')
    list_filter = ['call_operator']
    list_per_page = 50
admin.site.register(CALL,CALLAdmin)


from .models import SS
class SSAdmin(admin.ModelAdmin):
    # ...
    list_display = ('pk','call_operator', 'fttest')
    list_filter = ['call_operator']
    list_per_page = 50
admin.site.register(SS,SSAdmin)


from .models import TTFF
class TTFFAdmin(admin.ModelAdmin):
    # ...
    list_display = ('pk','test_person', 'test_product','test_hdware','test_state','test_date')
    list_filter = ['test_person']
    list_per_page = 50
admin.site.register(TTFF,TTFFAdmin)




