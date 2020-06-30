from django.db import models

# Create your models here.
# ================= Title =================
class TitleImage(models.Model):
    image = models.ImageField(upload_to='img/logos')
# ================= Loader =================
class LoaderImage(models.Model):
    image = models.ImageField(upload_to='img/logos')
# ================= Navbar =================
class NavbarLeftIcon(models.Model):
    social_icon = models.CharField(max_length=50)
    social_link = models.CharField(max_length=50)
    def __str__(self):
        return self.social_link
class NavbarMail(models.Model):
    mail_text = models.CharField(max_length=50)
    mail_link = models.CharField(max_length=50)
    def __str__(self):
        return self.mail_text
class NavbarPhoneNumber(models.Model):
    phone_text = models.CharField(max_length=50)
    phone_link = models.CharField(max_length=50)
    def __str__(self):
        return self.phone_text
class NavbarLogo(models.Model):
    logo_img = models.ImageField(upload_to='img/logos')
# ================= Banner =================
class Banner(models.Model):
    banner_cap = models.CharField(max_length=100)
    banner_title = models.CharField(max_length=254)
    banner_img = models.ImageField(upload_to='img/banners')
    def __str__(self):
        return self.banner_title
# ================= Service =================
class ServiceHeader(models.Model):
    service_cap = models.CharField(max_length=100)
    service_title = models.CharField(max_length=254)
    def __str__(self):
        return self.service_title
class ServiceItem(models.Model):
    item_icon = models.CharField(max_length=100)
    item_title = models.CharField(max_length=50)
    item_text = models.TextField()
    def __str__(self):
        return self.item_title
# ================= Counter =================
class Counter(models.Model):
    counter_number = models.IntegerField()
    counter_title = models.CharField(max_length=50)
    def __str__(self):
        return self.counter_title
# ================= More About =================
class About(models.Model):
    about_img = models.ImageField(upload_to='img/about')
    about_cap = models.CharField(max_length=50)
    about_title = models.CharField(max_length=100)
    about_top_title = models.CharField(max_length=100)
    about_top_text = models.TextField()
    about_main_text = models.TextField()
    about_second_text = models.TextField(null=True, blank=True)
    about_third_text = models.TextField(null=True, blank=True)
    about_bottom_title = models.CharField(max_length=100)
    about_bottom_text = models.TextField()
    def __str__(self):
        return self.about_title
class AboutItem(models.Model):
    about = models.ForeignKey(About, null=True, on_delete=models.SET_NULL)
    item_icon = models.CharField(max_length=50, null=True, blank=True)
    item_text = models.CharField(max_length=50)
    def __str__(self):
        return self.item_text
# ================= Tariffs =================
class TariffHeader(models.Model):
    tariff_cap = models.CharField(max_length=100)
    tariff_title = models.CharField(max_length=254)
    def __str__(self):
        return self.tariff_title
class TypeCustomer(models.Model):
    type_customer = models.CharField(max_length=50)
    def __str__(self):
        return "{}. {}".format(self.id,self.type_customer)
class Tariff(models.Model):
    type_customer = models.ForeignKey(TypeCustomer, on_delete=models.CASCADE)
    tariff_name = models.CharField(max_length=50)
    tariff_speed = models.IntegerField()
    tariff_speed_night = models.IntegerField()
    tariff_speed_tasix = models.IntegerField()
    tariff_price = models.IntegerField()
    tariff_button = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.tariff_name
class TariffAbout(models.Model):
    tariff_header_first = models.CharField(max_length=100)
    tariff_about_first = models.TextField()
    tariff_header_second = models.CharField(max_length=100)
    tariff_about_second = models.TextField()
    tariff_header_third = models.CharField(max_length=100)
    tariff_about_third = models.TextField()
# ================= Partners =================
class PartnerHeader(models.Model):
    partner_cap = models.CharField(max_length=50)
    partner_title = models.CharField(max_length=100)
    def __str__(self):
        return self.partner_title
class PartnerImage(models.Model):
    partner_image = models.ImageField(upload_to='img/partners')
# ================= Clients =================
class ClientHeader(models.Model):
    client_cap = models.CharField(max_length=50)
    client_title = models.CharField(max_length=100)
    def __str__(self):
        return self.client_title
class ClientImage(models.Model):
    client_image = models.ImageField(upload_to='img/clients')
# ================= News =================
class NewsHeader(models.Model):
    news_cap = models.CharField(max_length=50)
    news_title = models.CharField(max_length=100)
    def __str__(self):
        return self.news_title
class NewsItem(models.Model):
    image = models.ImageField(upload_to='img/news', null=True, blank=True)
    news_type = models.CharField(max_length=50, null=True, blank=True)
    news_title = models.CharField(max_length=100)
    news_text_main = models.TextField()
    news_quote = models.TextField(null=True, blank=True)
    news_text_secondary = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.news_title
# ================= Footer ================
class FooterMenu(models.Model):
    menu_title = models.CharField(max_length=50)
    menu_link = models.CharField(max_length=254)
    def __str__(self):
        return self.menu_link
class FooterAddress(models.Model):
    address_title = models.CharField(max_length=50)
    address_link = models.CharField(max_length=254)
    address_hint = models.CharField(max_length=50)
    def __str__(self):
        return self.address_title
class FooterSocialText(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
class FooterSocialIcon(models.Model):
    icon = models.CharField(max_length=50)
    icon_link = models.CharField(max_length=254)
    def __str__(self):
        return self.icon_link
class FooterAuthor(models.Model):
    link = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    def __str__(self):
        return self.author
# ================= GetInTouch ================
class GetInTouch(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    message_subject = models.CharField(max_length=100)
    message_text = models.TextField()
    read_or_not = models.BooleanField(default=False)