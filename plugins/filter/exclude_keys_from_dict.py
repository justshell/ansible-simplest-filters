#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'exclude_keys_from_dict': self.exclude_keys_from_dict,
            'save_only_dict_keys': self.save_only_dict_keys
        }

    def exclude_keys_from_dict(self, origin_dict, exclude_key_list):
        tresult={}
        for key in origin_dict.keys():
            if key not in exclude_key_list:
                tresult[key]=origin_dict[key]
        return tresult

    def save_only_dict_keys(self, origin_dict, save_keylist):
        tresult={}
        for key in origin_dict.keys():
            if key in save_keylist:
                tresult[key]=origin_dict[key]
        return tresult

    def replace_subkey_value(self, origin_dict, behaviour, key_name, new_key_value, old_key_value):
        tresult=origin_dict.copy()
        if behaviour=='replace_old':
            for key in tresult.keys():
                if key_name in tresult[key].keys() and tresult[key][key_name]==old_key_value:
                    tresult[key][key_name]=new_key_value
        elif behaviour=='force_place':
            for key in tresult.keys():
                tresult[key][key_name]=new_key_value
        return tresult
