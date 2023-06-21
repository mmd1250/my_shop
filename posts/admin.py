from django.contrib import admin
from .models import Article,Category,IPAddress
# Register your models here.

#admin header changes
#این یه شورتکاته در اصل من باید برم از تو تمپلیت خود اپ تغییر بدم
admin.site.site_header = "وبلاگ"

# @admin.action(description="انتشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
    rows_updated =  queryset.update(status="P")
    if rows_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شدند"
    modeladmin.message_user(request, " {}مقاله {}".format(rows_updated, message_bit))
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status="D")
    if rows_updated == 1:
        message_bit = "پیشنویس شد"
    else:
        message_bit = "پیشنویس شدند"
    modeladmin.message_user(request, " {}مقاله {}".format(rows_updated, message_bit))
make_draft.short_description = "پیشنویس کردن مقالات انتخاب شده"

class CategoryADMIN (admin.ModelAdmin):
    list_display = ('position','title','slug','parent','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category,CategoryADMIN,)
class ARTICLEADMIN (admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag','slug', 'author','jpublish','is_special','status','Category_to_str')
    list_filter = ('published','status', 'author')
    search_fields = ('title','description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status','-published']
    actions = [make_published, make_draft]

    # " ،".join([category.title for category in obj.Categoey.all()])
admin.site.register(Article,ARTICLEADMIN,)
admin.site.register(IPAddress)