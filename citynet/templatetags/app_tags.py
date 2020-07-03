from django import template
from django.utils.translation import get_language
from citynet.models import *

register = template.Library()

@register.simple_tag
def get_url_tag(request, lang):
    active_language = get_language()
    return request.get_full_path().replace(active_language, lang, 1)

@register.simple_tag
def get_title_img():
    return TitleImage.objects.last()

@register.simple_tag
def get_loader_img():
    return LoaderImage.objects.last()

# ============= Navbar =============
@register.simple_tag
def get_logo_img():
    return NavbarLogo.objects.last()

@register.simple_tag
def get_nav_left_icon():
    return NavbarLeftIcon.objects.order_by('-id')[:4]

@register.simple_tag
def get_nav_mail():
    return NavbarMail.objects.last()

@register.simple_tag
def get_nav_phone_number():
    return NavbarPhoneNumber.objects.last()

# ============= Footer =============
@register.simple_tag
def get_footer_nemu():
    return FooterMenu.objects.last()

@register.simple_tag
def get_footer_address():
    return FooterAddress.objects.all()

@register.simple_tag
def get_footer_about_social():
    return FooterSocialText.objects.last()

@register.simple_tag
def get_footer_social_icon():
    return FooterSocialIcon.objects.all()

@register.simple_tag
def get_footer_author():
    return FooterAuthor.objects.last()
