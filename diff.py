
import os
import hashlib

def calculate_md5(file_path):
    """¼ÆËãÎÄ¼þµÄ MD5 Öµ"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def compare_directories(dir1, dir2):
    """±È½ÏÁ½¸öÎÄ¼þ¼ÐÏÂµÄÍ¬Ãû .o ÎÄ¼þÊÇ·ñÏàÍ¬"""
    for root, _, files in os.walk(dir1):
        for file in files:
            if file.endswith('.o'):
                file1_path = os.path.join(root, file)
                #print("debug point file1_path", file1_path)
                file2_path = os.path.join(dir2, os.path.basename(file1_path))
                #print("debug point file2_path", file2_path)

                if os.path.exists(file2_path):
                    md5_file1 = calculate_md5(file1_path)
                    md5_file2 = calculate_md5(file2_path)

                    if md5_file1 == md5_file2:
                        print(f"pass {file1_path}  {file2_path}")
                    else:
                        print(f"fail {file1_path}  {file2_path}")
                else:
                    print(f"miss {file2_path} ÔÚ {dir2} ÖÐ²»´æÔÚ")

# Ê¹ÓÃÊ¾Àý
dir1 = '/ssd_fes/jiongz/desktop/github/sifive/scons_demo'
dir2 = '/ssd_fes/jiongz/desktop/github/smart_run_work'
compare_directories(dir1, dir2)
