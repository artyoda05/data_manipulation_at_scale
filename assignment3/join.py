import MapReduce
import sys


def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    for order_records in list_of_values:
        if order_records[0] == 'order':
            for line_records in list_of_values:
                if line_records[0] == 'line_item':
                    mr.emit(order_records + line_records)


mr = MapReduce.MapReduce()
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
