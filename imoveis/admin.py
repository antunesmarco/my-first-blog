from django.contrib import admin

from .models import Country
from .models import Real_State
from .models import Property_Type
from .models import Neighborhood
from .models import Property

admin.site.register(Country)
admin.site.register(Real_State)
admin.site.register(Property_Type)
admin.site.register(Neighborhood)
admin.site.register(Property)


