from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.urls import reverse
from jsonfield import JSONField
from .payment import BaseOrder


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)  # 카테고리 이름
    icon = models.ImageField(blank=True)  # 이미지 사진 (일단 없는 경우까지 허용)
    is_public = models.BooleanField(default=False, db_index=True)  # 카테고리에 대해 비공개 처리

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_detail', args=[self.pk])


class Shop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)  # 가게 이름
    desc = models.TextField(blank=True)
    latlng = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(blank=True)  # 가게 대표 이미지
    is_public = models.BooleanField(default=False, db_index=True)
    meta = JSONField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:shop_detail', args=[self.pk])

    @property
    def address(self):
        return self.meta.get('address')


class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)  # 메뉴 이름
    desc = models.TextField(blank=True)  # 메뉴 설명
    amount = models.PositiveIntegerField()  # 가격
    photo = models.ImageField(blank=True)  # 메뉴 사진
    is_public = models.BooleanField(default=False, db_index=True)
    meta = JSONField()

    def __str__(self):
        return self.name


class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='shop/image/%Y/%m/%d', blank=True)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                      help_text='별점 점수 1~5점으로 적어주세요!')
    message = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.message


class Order(BaseOrder):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, validators=[RegexValidator(r'010[1-9]\d{7}$')])


# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
#     amount = models.PositiveIntegerField()
#     address = models.CharField(max_length=100)
#     phone = models.CharField(max_length=11)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    @property
    def amount(self):
        return self.quantity * self.item.amount
