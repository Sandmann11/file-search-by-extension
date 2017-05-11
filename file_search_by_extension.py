import fnmatch
import os
import shutil

results = []
for root, dirs, files in os.walk("C:\\"):
    for _file in files:
        if fnmatch.fnmatch(_file, '*.docx'):
            results.append(os.path.join(root, _file))

for fl in results:
    shutil.copy2(fl, "C:\\test_dir")

print(results)
