import os
import shutil
import sys


def collect_files(path_to_current_dir, path_to_output_dir):
    for name in os.listdir(path_to_current_dir):
        path = os.path.join(path_to_current_dir, name)
        if os.path.isfile(path):
            out = os.path.join(path_to_output_dir, name)
            shutil.copy(path, out)
        elif os.path.isdir(path):
            collect_files(path, path_to_output_dir)


def main():
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    collect_files(input_dir, output_dir)


if __name__ == '__main__':
    main()
