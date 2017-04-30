# Rostyslav Dzinko's answer is very appropriate. I thought I could highlight one other reason you should choose @classmethod over @staticmethod.
#
# In the example above, Rostyslav used the @classmethod from_string as a Factory to create Date objects from otherwise unacceptable parameters. The same can be done with @staticmethod as is shown in the code below:

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return "{0}-{1}-{2}".format(self.month, self.day, self.year)

    @staticmethod
    def millenium(month, day):
        return Date(month, day, 2000)


new_year = Date(1, 1, 2013)  # Creates a new Date object
millenium_new_year = Date.millenium(1, 1)  # also creates a Date object.

# Proof:
new_year.display()  # "1-1-2013"
millenium_new_year.display()  # "1-1-2000"

isinstance(new_year, Date)  # True
isinstance(millenium_new_year, Date)  # True


# Thus both new_year and millenium_new_year are instances of Date class.
#
# But, if you observe closely, the Factory process is hard-coded to create Date objects no matter what. What this means is that even if the Date class is subclassed, the subclasses will still create plain Date object (without any property of the subclass). See that in the example below:

class DateTime(Date):
    def display(self):
        return "{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year)


datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)

isinstance(datetime1, DateTime)  # True
isinstance(datetime2, DateTime)  # False

datetime1.display()  # returns "10-10-1990 - 00:00:00PM"
datetime2.display()  # returns "10-10-2000" because it's not a DateTime object but a Date object. Check the implementation of the millenium method on the Date class


# datetime2 is not an instance of DateTime? WTF? Well that's because of the @staticmethod decorator used.
#
# In most cases, this is undesired. If what you want is a Factory method that is aware of the class that called it, then @classmethod is what you need.
#
# Rewriting the Date.millenium as (that's the only part of the above code that changes)

@classmethod
def millenium(cls, month, day):
    return cls(month, day, 2000)


# ensures that the class is not hard-coded but rather learnt. cls can be any subclass. The resulting object will rightly be an instance of cls. Let's test that out.

datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)

isinstance(datetime1, DateTime)  # True
isinstance(datetime2, DateTime)  # True

datetime1.display()  # "10-10-1990 - 00:00:00PM"
datetime2.display()  # "10-10-2000 - 00:00:00PM"
# The reason is, as you know by now, @classmethod was used instead of @staticmethod

from tempfile import TemporaryDirectory
import random
import os


def write_test_files(tmpdir):
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), 'w') as f:
            f.write('\n' * random.randint(0, 100))


# with TemporaryDirectory() as tmpdir:
#     write_test_files(tmpdir)
#     r

class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


from threading import Thread


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    config = {'data_dir': tmpdir}
    result = mapreduce(LineCountWorker, PathInputData, config)
print('There are', result, 'lines')
