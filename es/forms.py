from django.forms import ModelForm
from es.models import EMAIL

class EmailForm(ModelForm):
	class Meta:
		model=EMAIL
		fields=['username','firstname','lastname','Email','img']