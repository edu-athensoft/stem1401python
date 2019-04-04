#!/usr/bin/env python3
# _*_ code:utf-8 _*_

"""datatype of number"""


# type()
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

# skip isinstance()
a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

