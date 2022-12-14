
import yaml

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader,Dumper #type:ignore

from .base_handler import BaseFileHandler

class YamlHandler(BaseFileHandler):

    def load_from_fileobj(self,file,**kwargs):
        kwargs.setdefault('default',)