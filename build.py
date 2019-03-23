#!/usr/bin/env python

import os
import sys
from os.path import dirname, realpath
from zipfile import ZipFile, ZIP_DEFLATED


def zip(name, version):
    print('Creating theme...')
    file_list = ['colors.tdesktop-theme', 'tiled.png']
    zipname = name + '-' + version + '.zip'
    zip_files = ZipFile(zipname, 'w', ZIP_DEFLATED)
    with zip_files as z:
        for files in file_list:
            z.write(files)
    os.rename(zipname, name + '-' + version + '.tdesktop-theme')


def main():
    runpath = os.getcwd()
    rawpath = dirname(realpath(sys.argv[0]))
    name = 'SwiftDark'
    version = '2.1'
    print()
    os.chdir(rawpath)
    zip(name, version)
    os.chdir(runpath)
    print()
    print('--- done ---')
    print()


if __name__ == '__main__':
    main()
