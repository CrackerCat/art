# -*- coding: utf-8 -*-
"""Art main."""
from .art import *
from .art_param import FONT_MAP
import sys
import doctest
import os
import zipfile
import coverage

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        if args[1].upper() == "TESTCOV":
            cov = coverage.Coverage()
            cov.start()
            error_flag = doctest.testfile(
                "test.py",
                optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
                | doctest.IGNORE_EXCEPTION_DETAIL,
                verbose=False)[0]
            cov.stop()
            cov.report()
            cov.save()
            sys.exit(error_flag)
        elif args[1].upper() == "TEST":
            error_flag = doctest.testfile(
                "test.py",
                optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.IGNORE_EXCEPTION_DETAIL,
                verbose=False)[0]
            if error_flag == 0:
                print("\nTest Passed")
                sys.exit(error_flag)
            else:
                print("\nTest Failed")
                sys.exit(error_flag)
        elif args[1].upper() == "TESTCOV2":
            cov = coverage.Coverage()
            cov.start()
            error_flag_1 = doctest.testfile(
                "test.py",
                optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
                            | doctest.IGNORE_EXCEPTION_DETAIL,
                verbose=False)[0]
            error_flag_2 = doctest.testfile(
                "test2.py",
                optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS | doctest.IGNORE_EXCEPTION_DETAIL,
                verbose=False)[0]
            error_flag = error_flag_1 + error_flag_2
            cov.stop()
            cov.report()
            cov.save()
            if error_flag == 0:
                print("\nTest2 Passed")
                sys.exit(error_flag)
            else:
                print("\nTest2 Failed")
                sys.exit(error_flag)
        elif args[1].upper() in ["LIST", "ARTS"]:
            art_list()
        elif args[1].upper() == "FONTS":
            font_list()
        elif len(args) > 2:
            if args[1].upper() == "ALL":
                if "ARTFonts" not in os.listdir(os.getcwd()):
                    os.mkdir("ARTFonts")
                zipf = zipfile.ZipFile(
                    os.path.join(
                        "ARTFonts",
                        "ALL_FONT" + '.zip'),
                    'w',
                    zipfile.ZIP_DEFLATED)
                print("Generating . . . ")
                for font in FONT_MAP.keys():
                    tsave(
                        args[2],
                        filename=os.path.join(
                            "ARTFonts",
                            font + ".txt"),
                        print_status=False,
                        font=font)
                    zipf.write(
                        os.path.join(
                            "ARTFonts",
                            font + ".txt"),
                        font + ".txt")
                zipf.close()
                print("Done!")
                print("File -- > " +
                      str(os.path.join("ARTFonts", "ALL_FONT" + '.zip')))
            elif args[1].upper() == "TEXT":
                if len(args) > 3:
                    tprint(args[2], font=args[3])
                else:
                    tprint(args[2])
            elif args[1].upper() == "SAVE":
                if len(args) > 3:
                    tsave(args[2], font=args[3])
                else:
                    tsave(args[2])
            elif args[1].upper() in ["SHAPE", "ART"]:
                try:
                    aprint(args[2])
                except artError as e:
                    print(str(e))
                except UnicodeEncodeError:
                    print("[Warning] This art is not printable in this environment")
            else:
                help_func()
        else:
            help_func()
    else:
        help_func()
