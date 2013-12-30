import zipfile
import os
import os.path
import sys

def extract(filename):
    print("file: %s" % filename)
    basename = os.path.basename(filename)

    root_name, ext = os.path.splitext(basename)
    root_name = root_name.decode("utf-8")

    if not os.path.exists(root_name):
        os.mkdir(root_name)

    zf = zipfile.ZipFile(filename)
    info_list = zf.infolist()
    if len( info_list ) > 0:
        first = info_list[0]
        utf8 = False
        try:
            name = first.filename.decode("gb2312")
        except:
            utf8 = True

        for n in zf.infolist():
            if utf8:
                name = n.filename
            else:
                name = n.filename.decode("gb2312")

            print("name:%s" % name )
            path = os.path.join(root_name,name)
            if n.file_size == 0:
                if not os.path.exists(path):
                    os.makedirs(path)
                continue

            f = open(path,"w+")
            f.write(zf.read(n.filename))
            f.close()

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        extract(filename)

if __name__ == "__main__":
    main()

