from api.source import Source

class Article(object):
    @property
    def source(self):
        return _populate_attributes(Source(), self.source)

    @source.setter
    def source(self, source):
        self.__source = source
        
    def _populate_attributes(self, obj, attr_dict):
        for key, value in attr_dict.iteritems():
            setattr(obj, key, value)
        return obj

