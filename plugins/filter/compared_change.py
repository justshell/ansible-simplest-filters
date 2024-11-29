#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'compared_change': self.compared_change
        }

    def compared_change(self, origin_string, value_to_compare, if_this_value, value_to_change, result_value):
        if value_to_compare == if_this_value:
            origin_string=origin_string.replace(value_to_change,result_value)
        return origin_string


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
