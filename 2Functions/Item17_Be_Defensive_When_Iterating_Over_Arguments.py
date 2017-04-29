# def index_file(handle):
#     offset=0
#     for line in handle:
#         if line:
#             yield offset
#         for letter in line:
#             offset += 1
#             if letter == ' ':
#                 yield offset


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path, 'r') as handle:
            offset = 0
            for line in handle:
                if line:
                    yield offset
                for letter in line:
                    offset += 1
                    if letter == ' ':
                        yield offset

    def fun(self):
        print('abc')

it = ReadVisits('/Users/yuxiao/PycharmProjects/Effective_Python/2Functions/test.txt')
print(list(it))

print(list(it))
