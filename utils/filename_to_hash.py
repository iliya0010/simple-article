import os
import uuid
from django.utils.deconstruct import deconstructible
from django.conf import settings


@deconstructible
class MediaNameToHash(object):
    def __init__(self, path):
        self.address = settings.MEDIA_ROOT + "/" + path
        self.path = path
        if not os.path.exists(self.address):
            os.makedirs(self.address, exist_ok=True)

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path + "/" + str(uuid.uuid4()) + extension
