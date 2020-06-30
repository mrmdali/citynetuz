from citynet import models
def get_logo():
    return models.NavbarLogo.objects.last()