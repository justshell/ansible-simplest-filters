#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'compared_change': self.compared_change,
            'FindFilterOne': self.FindFilterOne,
            'FindFilterTwo': self.FindFilterTwo,
            'SubKeyChanger': self.SubKeyChanger,
            'SubKeyRename': self.SubKeyRename,
            'DictKeyRename': self.DictKeyRename,
            'DictKeyRenameByList': self.DictKeyRenameByList,
            'ExtractKeysFromSubkeysAsList': self.ExtractKeysFromSubkeysAsList
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

    def SubKeyChanger(self, origin_dict, subkey_name, new_subkey_value,insert_if_absent=False):
        new_dict=origin_dict.copy()
        for item in new_dict.keys():
            if subkey_name in new_dict[item] or insert_if_absent:
                new_dict[item][subkey_name]=new_subkey_value
        return new_dict

    def SubKeyRename(self, origin_dict, subkey_name, new_subkey_name):
        new_dict=origin_dict.copy()
        for item in new_dict.keys():
            if subkey_name in new_dict[item]:
                new_dict[item][new_subkey_name]=new_dict[item][subkey_name]
                del new_dict[item][subkey_name]
        return new_dict

    def DictKeyRename(self, origin_dict, key_name, new_key_name):
        new_dict=origin_dict.copy()
        if key_name in new_dict:
            new_dict[new_key_name]=new_dict[key_name]
            del new_dict[key_name]
        return new_dict

    def DictKeyRenameByList(self, origin_dict,list1,list2):
        i=0
        n=len(list1)
        new_dict=origin_dict.copy()
        while i<n:
            if list1[i] in new_dict.keys():
                new_dict[list2[i]]=new_dict[list1[i]]
                del new_dict[list1[i]]
            i+=1
        return new_dict

    def ExtractKeysFromSubkeysAsList(self, origin_dict, sub_keylist,ignore_if_missing=True):
        tresult=[]
        for item in origin_dict.keys():
            for item2 in sub_keylist:
                if item2 in origin_dict[item].keys():
                    tresult.append(origin_dict[item][item2])
                elif ignore_if_missing==False:
                    raise ValueError('"'+item2+'" missing in "'+item+'"')
        return tresult

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
