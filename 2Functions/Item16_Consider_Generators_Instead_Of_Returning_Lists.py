def index_file(handle):
    offset=0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('Effective_Python/2Functions/test.txt','r') as f:
    it=index_file(f)
#    results = islice(it,0,3)
    print(list(it))
