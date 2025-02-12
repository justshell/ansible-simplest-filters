#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'compared_change': self.compared_change,
            'FindFilterOne': self.FindFilterOne,
            'FindFilterTwo': self.FindFilterTwo,
            'SubKeyChanger': self.SubKeyChanger
        }

    def compared_change(self, origin_string, value_to_compare, if_this_value, value_to_change, result_value):
        if value_to_compare == if_this_value:
            origin_string=origin_string.replace(value_to_change,result_value)
        return origin_string

    def FindFilterOne(self, origin_list, path_replace_it, path_replace_to, return_key):
        tresult=[]
        for item in origin_list:
            if return_key in item and item[return_key]==True:
                if path_replace_it!='':
                    item['path']=item['path'].replace(path_replace_it,path_replace_to)
                tresult.append(item['path'])
        return tresult

    def FindFilterTwo(self, origin_list, path_replace_it, path_replace_to, return_key):
        tresult={}
        for item in origin_list:
            if return_key in item and item[return_key]==True:
                keyname=item['path']
                if path_replace_it!='':
                    keyname=item['path'].replace(path_replace_it,path_replace_to)
                tresult[keyname]={ 'path':item['path'] }
        return tresult

    def SubKeyChanger(self, origin_dict, subkey_name, new_subkey_value,skip_not_present):
        new_dict=origin_dict.copy()
        for item in new_dict.keys():
            if subkey_name not in new_dict[item] and skip_not_present==False:
                new_dict[item][subkey_name]=new_subkey_value
        return new_dict

# compared_change = filter for string. replaces <value_to_change> to <result_value> if <value_to_compare>==<if_this_value>
# example:
# defines:
#   string='a,b,c,d,e,f'
#   value_to_compare = 'change_it_please'
#   if_this_value = 'change_it_please'
#   value_to_change = 'с'
#   result_value = 'bgg'
# 
# because value_to_compare == if_this_value == 'change_it_please' ==>
#   replace: 'c' to 'bgg'
#   result: 'a,b,bgg,d,e,f'
