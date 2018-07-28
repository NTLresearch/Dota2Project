
import Tools.exportdata as tla
import dota2api
import os
import pandas as pd
import time


def test_final_data_io(acc_id, n):
    start = time.time()
    print("Hello")
    data = tla.final_data_io(acc_id, n, "opendota")
    end = time.time()
    print(end-start)
    print("Done")
    return data

final_result = test_final_data_io(107940251, 1000)

final_result.to_csv("107940251.csv")

final_result2 = test_final_data_io(181798082, 1000)

final_result2.to_csv("181798082.csvx")

















print("done")
