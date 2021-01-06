from django.contrib import admin
from .models import Order, LineItem


class LineItemAdminInline(admin.TabularInline):
    model = LineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (LineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'shipping_cost', 'order_total',
                       'grand_total', 'original_bag', 
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'shipping_cost',
              'order_total', 'grand_total','original_bag', 
              'stripe_pid' )

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'shipping_cost',
                    'grand_total', 'original_bag', 
                    'stripe_pid')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)