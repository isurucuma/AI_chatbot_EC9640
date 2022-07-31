from django.apps import AppConfig
from django.conf import settings
import os


class PredictorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictor'

    # modelPath = os.path.join(settings.MODELS, 'data.pth')

    from . import model

    NNmodel = model.model
    NNpredict = model.predict





