import os
import subprocess

dir = os.getcwd()
build_order_list_file = os.path.join(dir, 'buildorder.txt')

with open(build_order_list_file, 'r') as file:
    floder_names = file.read().splitlines()

for folder_name in floder_names:
    floder_path = os.path.join(dir,floder_names)

    if os.path.exists(floder_path):
        process_script = os.path.join(floder_path, 'process.py')

        if os.path.exists(process_script):
            try:
                subprocess.check_call(['python', process_script], cwd=floder_path)
                print(f"successfylly process.py in {folder_name}.")
            except subprocess.CalledProcessError as e:
                print(f"process.py not found in {folder_name}:{e}")
        else:
            print(f"process.py not found in {folder_name}.")
    else:
        print(f"floder{folder_name} does not exist.")

print("process completed")
