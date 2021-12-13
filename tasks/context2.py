from contextlib import contextmanager

f_obj = None

@contextmanager
def file_open(path):
    global f_obj

    try:
        f_obj = open(path, 'w')
        yield f_obj
    except (OSError, ValueError) as wer:
        raise wer
        print("We had an error!")
    finally:
        print('Closing file')
        if f_obj:
            f_obj.close()


if __name__ == '__main__':
    with file_open('E:\\test1.txt') as fobj:
        fobj.write('Testing context managers')