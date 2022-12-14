from abc import  ABCMeta,abstractmethod

class BaseFileHandler(metaclass=ABCMeta):


    str_like=True#是否是字符串类型的文件对象的标志，false表示字节类型的文件对象

    @abstractmethod
    def load_from_fileobj(self,file,**kwargs):
        pass

    @abstractmethod
    def dump_to_fileobj(self,obj,file,**kwargs):
        pass

    @abstractmethod
    def dump_to_str(self,obj,**kwargs):
        pass

    def load_from_path(self,filepath:str,mode:str='r',**kwargs):
        with open(filepath,mode) as f:
            return self.load_from_fileobj(f,**kwargs)

    def dump_to_path(self,obj,filepath:str,mode:str ='w',**kwargs):
        with open(filepath,mode) as f:
            self.dump_to_fileobj(obj,f,**kwargs)