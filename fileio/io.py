from io import BytesIO,StringIO
from pathlib import Path
from typing import Any,Callable,Dict,List,Optional,TextIO,Union

from .handlers import BaseFileHandler,JsonHandler,YamlHandler,PickleHandler

FileLikeObject =Union[TextIO,StringIO,BytesIO]

file_handlers={
    'json':JsonHandler(),
    'yaml':YamlHandler(),
    'yml':YamlHandler(),
    'pickle':PickleHandler(),
    'pkl':PickleHandler()
}

def load(file:Union[str,Path,FileLikeObject],
        file_format:Optional[str]=None,
        file_client_args:Optional[Dict]=None,
        **kwargs):

        if isinstance(file,Path):
            file=str(file)
        if file_format is None and isinstance(file,str):
            file_format=file.split('.')[-1]
        if file_format not in file_handlers:
            raise TypeError(f'Unsupported format:{file_format}')
        
        handler=file_handlers[file_format]
        f:FileLikeObject
        if isinstance(file,str):
            
