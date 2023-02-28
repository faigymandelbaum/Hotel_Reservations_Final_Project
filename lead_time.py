import math
import functools
from multiprocessing import Pool
import an_filled
import numpy as np
import pandas as pd
import random

df_hotels = pd.read_csv(an_filled.INFO_FOLDER + '/' + an_filled.HOTELS_INFO_FILE)

ls_targets = [123, 117, 709, 25, 234, 32, 27, 323, 4, 34]
ls_sorted_lead_times = sorted(df_hotels['lead_time'])

def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows / num_chunks)
    chunks = [(df[i:i + chunk_size]) for i in range(0, num_rows, chunk_size)]
    return chunks

def look_up(sorted_times, target_list):
    my_dict = {}
    for num in target_list:
        if num in sorted_times:
            if num in my_dict:
                my_dict[num] +=1
            else:
                my_dict[num] = 1

        else:
            my_dict[num] = 0

    return my_dict

def map_reduce(df, num_processes, mapper, reducer):
    chunks = make_chunks(df, num_processes)
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)

def reducer(freq_chunk1, freq_chunk2):
    freq_chunk1.update(freq_chunk2)
    return freq_chunk1

def main():

    dic_time_freq = map_reduce(df_hotels, 5, look_up, reducer)
    print (dic_time_freq)

if __name__ == '__main__':
    main()