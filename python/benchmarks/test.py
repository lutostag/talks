import time

def test_my_stuff(benchmark):
    benchmark(time.sleep, 0.02)
