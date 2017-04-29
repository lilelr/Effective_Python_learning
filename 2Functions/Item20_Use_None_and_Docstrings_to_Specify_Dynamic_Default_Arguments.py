import json
# Default arguments are only evaluated once: during function definition at module load time.
# This can cause odd behaviors for dynamic values(like {} and []).
# def decode(data, default={}):
#     try:
#         return json.loads(data)
#     except ValueError:
#         return default
#
# foo=decode('bad data')
# foo['stuff']=5
# bar=decode('also bad')
# bar['meep']=1
# print('Foo:',foo)
# print('Bar:',bar)

def decode(data,default=None):
    """load JSON data from a string.

    :param data: JSON data to decode.
    :param default: Vaule to return if decoding fails.
    :return:
    """
    if default is None:
        default={}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo=decode('bad data')
foo['stuff']=5
bar=decode('also bad')
bar['meep']=1
print('Foo:',foo)
print('Bar:',bar)