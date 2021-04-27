from django.contrib import admin

from .models import Comment, Item, User

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_no','user_no','item_title', 'item_views','item_price','item_detail','item_img','item_status','item_soldtime','item_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_no','item_no', 'comment_create_date','comment_modify_date','comment_nickname','comment_content','comment_nickname']

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_no', ]

admin.site.register(Comment, CommentAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(User, UserAdmin)