import os
import shutil

if __name__ == "__main__":
    s = "C:\\Users\\shind.y\\source\\repos\\STLib\\Test.exe"
    # src = "C:\\Users\\shindy\\source\\repos\\STLib\\Test\\シンプル水準器サンプル動画.mp4"
    # dst = "C:\\Users\\shindy\\source\\repos\\STLib\\Test\\シンプル水準器サンプル動画 こぴー.mp4"
    src = "C:\\Users\\shindy\\source\\repos\\STLib\\Test\\シンプル水準器サンプル動画.mp4"
    dst = "C:\\Users\\shindy\\source\\repos\\STLib\\Test\\Test3\\"

    print(os.path.dirname(os.path.abspath(s)))
    print(os.path.splitext(s))
    shutil.copy(src, dst)
