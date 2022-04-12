from .models.Poruchenie import *

menu = [{'title':'Добавить поручение','url_name' : 'home'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # otvotpos = Poruchenie.objects.all()
        context['menu'] = menu
        # context['otvotpos'] = otvotpos
        # if 'otvotpo_selected' not in context:
        #     context['otvotpo_selected'] = 0

        # c_def = self.get_user_context(title='Авторизация')
        # return dict(list(context.items()) + list(c_def.items()))
        return context