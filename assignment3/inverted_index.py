import MapReduce
import sys


def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for word in words:
        mr.emit_intermediate(word, key)


def reducer(key, list_of_values):
    list = []
    for value in list_of_values:
        if value not in list:
            list.append(value)
    mr.emit((key, list))


mr = MapReduce.MapReduce()
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
