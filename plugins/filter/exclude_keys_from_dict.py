#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'exclude_keys_from_dict': self.exclude_keys_from_dict
        }

    def exclude_keys_from_dict(self, origin_dict, exclude_key_list):
        tresult={}
        for key in origin_dict.keys():
            if key not in exclude_key_list:
                tresult[key]=origin_dict[key]
        return tresult
