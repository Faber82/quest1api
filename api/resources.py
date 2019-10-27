from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
	#Model Resource - w REST (REpresentationa State Transfer - Transfer Stanu REpresentatywnego )
	#wszystko jest zasobem (resource), więc obiekty też są zasobami. Więc dla stworzenia 
	#RESTowej API na Tastpie należy utworzyć class zasobów. 
	# W celu utworzenia zasobu tworzymy metaclass dla class ModelResource.
	#ta wejściowa class sprawdzi wszystkie pola nie zdolne do relacji
	#i utworzy własne własne pola API
	#działa tak jak Model Form dla Formularzy (forms) w django
	class Meta:
		#lista (queryset) zawiera wszystkie obiekty naszej note
		queryset = Note.objects.all()
		resource_name='note'
		#żeby można było nie tylko wysłać ale i pozwolić na modyfikację 
		#z zewnątrz importujemy a następnie implementujemy poniższe:
		authorization=Authorization()
		fields = ['success', 'img_url']