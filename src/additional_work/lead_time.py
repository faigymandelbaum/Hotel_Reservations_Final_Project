import math
import functools
from multiprocessing import Pool
import an_filled
import numpy as np
import pandas as pd
import random

df_hotels = pd.read_csv(an_filled.INFO_FOLDER + '/' + an_filled.HOTELS_INFO_FILE)

ls_targets = [123, 117, 709, 25, 234, 32, 27, 323, 4, 34]

def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows / num_chunks)
    chunks = [(df[i:i + chunk_size]) for i in range(0, num_rows, chunk_size)]
    return chunks

def find_time(df , target_list = ls_targets):
    val_dict = {}
    values = df['lead_time'].value_counts(dropna=False).keys().tolist()
    counts = df['lead_time'].value_counts(dropna=False).tolist()
    dic_lead_time_values = dict(zip(values, counts))
    for num in target_list:
        if num in dic_lead_time_values:
            val_dict[num] = dic_lead_time_values[num]
    return val_dict 

def map_reduce(df, num_processes, mapper, reducer):
    chunks = make_chunks(df, num_processes)
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)

def reducer(freq_chunk1, freq_chunk2):
    freq = {k: v for d in (freq_chunk1, freq_chunk2) for k, v in d.items()}
    return freq


def main():
    
    dic_time_freq = map_reduce(df_hotels, 5, find_time, reducer)
    print (dic_time_freq)

if __name__ == '__main__':
    main()