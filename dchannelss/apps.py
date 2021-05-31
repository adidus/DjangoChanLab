from django.apps import AppConfig


class DchannelssConfig(AppConfig):
    name = 'dchannelss'

    def ready(self):
        import dchannelss.signals