from django.contrib import admin
from .models import PaymentMethods, Transactions, DetailTransaction


class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "create_at", "update_at")


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ("member", "sales", "payment_method", "card_number", "paid_of", "create_at", "update_at")


class DetailTransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction", "detail_item", "quantity")


admin.site.register(PaymentMethods, PaymentMethodAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(DetailTransaction, DetailTransactionAdmin)
