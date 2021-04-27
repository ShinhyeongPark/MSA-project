from datetime import datetime

from django.db import models

class Comment(models.Model):
    comment_no = models.AutoField(primary_key=True)
    item_no = models.IntegerField()
    comment_modify_date = models.DateTimeField(blank=True, null=True)
    comment_create_date = models.DateTimeField(blank=True, null=True)
    comment_content = models.CharField(max_length=100)
    comment_nickname = models.CharField(db_column='comment_nickName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'comment'

class Item(models.Model):
    item_no = models.AutoField(primary_key=True)
    user_no = models.IntegerField()
    item_title = models.CharField(max_length=100)
    item_category = models.CharField(max_length=20, choices=(("clothes","의류"), ("device","가전/디지털"), ("furniture","가구/인테리어")))
    item_views = models.IntegerField(default=0)
    item_price = models.IntegerField()
    item_detail = models.TextField()
    item_img = models.CharField(max_length=100)
    item_status = models.CharField(max_length=10, default="판매중")
    item_soldtime = models.DateTimeField(blank=True, null=True)
    item_date = models.DateTimeField(blank=True, null=True, default=datetime.now)

    class Meta:
        db_table = 'item'
        ordering = ['item_no']

    def __str__(self):
        return self.item_title


class SoldItem(models.Model):
    item_no = models.AutoField(primary_key=True)
    user_no = models.IntegerField()
    item_title = models.CharField(max_length=100)
    item_views = models.IntegerField()
    item_price = models.IntegerField()
    item_detail = models.TextField()
    item_soldtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'sold_item'


class User(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_password = models.CharField(max_length=100)
    user_email = models.CharField(max_length=50)
    user_nickname = models.CharField(max_length=20)
    user_location = models.CharField(max_length=20)
    user_gender = models.CharField(max_length=20)
    user_birthdate = models.DateField(blank=True, null=True)
    user_createat = models.DateField(blank=True, null=True)
    user_caution = models.IntegerField(blank=True, null=True)
    user_sellcount = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'

# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class Item(models.Model):
#     item_id = models.AutoField(primary_key=True)
#     item_name = models.CharField(max_length=70)
#     item_views = models.IntegerField(blank=True, null=True)
#     item_location = models.CharField(max_length=70)
#     item_sellorname = models.CharField(db_column='item_sellorName', max_length=70)  # Field name made lowercase.
#     item_sellorid = models.CharField(db_column='item_sellorId', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     item_date = models.DateTimeField(blank=True, null=True)
#     item_price = models.IntegerField(blank=True, null=True)
#     item_detail = models.CharField(max_length=300, blank=True, null=True)
#     item_img = models.CharField(max_length=1, blank=True, null=True)
#     item_status = models.CharField(max_length=20, blank=True, null=True)
#     item_dealtime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'ITEM'
#         ordering = ['item_id']
#
#     def __str__(self):
#         return self.item_name
#
# class Search(models.Model):
#     search_name = models.CharField(max_length=50, blank=True, null=True)
#     search_category = models.CharField(max_length=50, blank=True, null=True)
#     search_keyword = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'SEARCH'
#
#
# class SelledItem(models.Model):
#     item_id = models.AutoField(primary_key=True)
#     item_name = models.CharField(max_length=70)
#     item_location = models.CharField(max_length=70)
#     item_sellorid = models.CharField(db_column='item_sellorId', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     item_price = models.IntegerField(blank=True, null=True)
#     item_img = models.CharField(max_length=1, blank=True, null=True)
#     item_status = models.CharField(max_length=20, blank=True, null=True)
#     item_dealtime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'SELLED_ITEM'
#
#
# class User(models.Model):
#     user_id = models.CharField(primary_key=True, max_length=50)
#     user_name = models.CharField(max_length=50)
#     user_pwd = models.CharField(max_length=50)
#     user_location = models.CharField(max_length=50)
#     user_phonenumber = models.CharField(db_column='user_phoneNumber', max_length=20)  # Field name made lowercase.
#     user_sell_count = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'USER'
#
#
# class UserDetail(models.Model):
#     user_no = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, models.DO_NOTHING)
#     user_pwd = models.CharField(max_length=50)
#     user_caution = models.IntegerField(blank=True, null=True)
#     user_gender = models.CharField(max_length=1)
#     user_date = models.DateTimeField(blank=True, null=True)
#     user_email = models.CharField(max_length=30, blank=True, null=True)
#     user_age = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'USER_DETAIL'
