import shutil
import tempfile
import os
import sys
import zipfile


def extractAll(base, zip_file):
    for f in zip_file.namelist():
        if f.endswith('/'):
            os.makedirs(os.path.join(base, f))
        else:
            zip_file.extract(f, path=base)


def force_lib_copying(file_, package_name, version):
    to_dir = os.path.dirname(file_)
    temp_dir = tempfile.gettempdir() + "/beep"
    try:
        os.makedirs(to_dir)
    except:
        pass

    if os.path.exists(os.path.join(to_dir, package_name)):
        shutil.rmtree(os.path.join(to_dir, package_name))
    if os.path.exists(os.path.join(temp_dir, package_name)):
        shutil.rmtree(os.path.join(temp_dir, package_name))

    from_dir = os.path.join(os.path.dirname(to_dir), "Packages")
    from_name = "{filename}-{version}.rvpkg".format(filename=os.path.splitext(os.path.basename(file_))[0],
                                                    version=version)
    zFile = zipfile.ZipFile(os.path.join(from_dir, from_name), 'r')
    extractAll(temp_dir, zFile)
    shutil.copytree(os.path.join(temp_dir, package_name), os.path.join(to_dir, package_name))
    sys.path.append(os.path.join(to_dir, package_name))


if __name__ == "__main__":
    force_lib_copying(r"C:\Program Files\Shotgun\RV-7.0.1\plugins\Python\qconsole.py", "QtPythonConsole", '0.1.39')
