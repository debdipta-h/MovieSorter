import fileOp

import Util
def main():
    path=input("enter the path to the directory\n");
    files=fileOp.fileList(path);
   # files=Util.refine(files);
    #print(files);
    report=Util.associate(files);
    print(report);


if __name__=="__main__":main()
