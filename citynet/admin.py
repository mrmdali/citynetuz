from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import *

# Register your models here.

class BannerAdmin(TranslatableAdmin):
    list_display = ('banner_cap', 'banner_title', )

class ServiceHeaderAdmin(TranslatableAdmin):
    list_display = ('service_cap', 'service_title', )

class ServiceItemAdmin(TranslatableAdmin):
    list_display = ('item_title', 'item_text', )

class CounterAdmin(TranslatableAdmin):
    list_display = ('counter_title', )

class AboutAdmin(TranslatableAdmin):
    list_display = ('about_cap', 'about_title', 'about_top_title', 'about_top_text', 'about_main_text', 'about_second_text', 'about_third_text', 'about_bottom_title', 'about_bottom_text', )

class AboutItemAdmin(TranslatableAdmin):
    list_display = ('item_text', )

class TariffHeaderAdmin(TranslatableAdmin):
    list_display = ('tariff_cap', 'tariff_title', )

class TariffAdmin(TranslatableAdmin):
    list_display = ('tariff_name', 'tariff_button', )

class TariffAboutAdmin(TranslatableAdmin):
    list_display = ('tariff_header_first', 'tariff_about_first', 'tariff_header_second', 'tariff_about_second', 'tariff_header_third', 'tariff_about_third', )


class PartnerHeaderAdmin(TranslatableAdmin):
    list_display = ('partner_cap', 'partner_title', )


class ClientHeaderAdmin(TranslatableAdmin):
    list_display = ('client_cap', 'client_title', )


class NewsHeaderAdmin(TranslatableAdmin):
    list_display = ('news_cap', 'news_title', )


class NewsItemAdmin(TranslatableAdmin):
    list_display = ('news_type', 'news_title',  'news_text_main',  'news_quote',  'news_text_secondary',  'created_date', )

class FooterAddressAdmin(TranslatableAdmin):
    list_display = ('address_title', 'address_hint', )


class FooterSocialTextAdmin(TranslatableAdmin):
    list_display = ('title', 'text', )


class FooterAuthorAdmin(TranslatableAdmin):
    list_display = ('author', )

admin.site.register(TitleImage)
admin.site.register(LoaderImage)
admin.site.register(NavbarLeftIcon)
admin.site.register(NavbarMail)
admin.site.register(NavbarPhoneNumber)
admin.site.register(NavbarLogo)
admin.site.register(Banner, BannerAdmin)
admin.site.register(ServiceHeader, ServiceHeaderAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
admin.site.register(Counter, CounterAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(AboutItem, AboutItemAdmin)
admin.site.register(TariffHeader, TariffHeaderAdmin)
admin.site.register(TypeCustomer)
admin.site.register(Tariff, TariffAdmin)
admin.site.register(TariffAbout,TariffAboutAdmin)
admin.site.register(PartnerHeader, PartnerHeaderAdmin)
admin.site.register(PartnerImage)
admin.site.register(ClientHeader, ClientHeaderAdmin)
admin.site.register(ClientImage)
admin.site.register(NewsHeader, NewsHeaderAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(FooterMenu)
admin.site.register(FooterAddress,FooterAddressAdmin)
admin.site.register(FooterSocialText,FooterSocialTextAdmin)
admin.site.register(FooterSocialIcon)
admin.site.register(FooterAuthor, FooterAuthorAdmin)
admin.site.register(GetInTouch)