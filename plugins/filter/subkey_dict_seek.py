#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'subkey_dict_seek': self.subkey_dict_seek
        }

    def subkey_dict_seek(self, origin_dict, subkey, value, default_behaviour):
        tresult=[]
        for key in origin_dict.keys():
            if subkey in origin_dict[key]:
                if value=='<anyvalue>':
                    tresult.append(key)
                elif origin_dict[key][subkey]==value:
                    tresult.append(key)
            else:
                if default_behaviour=='append':
                    tresult.append(key)
        return tresult

# Example:
# mydict={
#   dict_key1:
#     name: 'key1name'
#     field: 'key1field'
#   dict_key2:
#     name: 'key2name'
#     field: 'key2field'
#   dict_key3:
#     name: 'key3name: field less'

# mydict|subkey_dict_seek('field',<anyvalue>,'append') --> [ dict_key1, dict_key2, dict_key3 ]
# mydict|subkey_dict_seek('field',<anyvalue>,'') --> [ dict_key1, dict_key2 ]                     # dict_key3 don't append, 'field' undefined (default_behaviour == '')
# mydict|subkey_dict_seek('field','key1field','append') --> [ dict_key1,dict_key3 ]               # dict_key3 appended, 'field' undefined (default_behaviour == 'append')
# mydict|subkey_dict_seek('field','key1field','') --> [ dict_key1 ]
# mydict|subkey_dict_seek('field','myvalue','') --> []
# mydict|subkey_dict_seek('field','myvalue','append') --> [ dict_key3 ]                           # dict_key1.field!=dict_key2.field!='myvalue', but dict_key3.field undefined ==> default: append
