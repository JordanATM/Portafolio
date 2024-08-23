from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Restringe la creación de un nuevo Contact si ya existe uno
        if Contact.objects.exists():
            return False
        return True

    def save_model(self, request, obj, form, change):
        # Asegura que solo se pueda guardar un objeto Contacto
        if not change and Contact.objects.exists():
            raise ValidationError("Solo se puede crear un Contacto.")
        super().save_model(request, obj, form, change)

admin.site.register(Contact, ContactAdmin)
