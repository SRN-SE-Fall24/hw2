''' Random array generator. '''
import subprocess


def random_array(arr):
    ''' Accepts a blank array and fills it with random values. '''
    shuffled_num = None
    for _, i in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
