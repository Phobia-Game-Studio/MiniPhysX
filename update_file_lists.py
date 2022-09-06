#!/usr/bin/python3

import os
import re
import posixpath
import mmap

import time

startTime = time.perf_counter()

ignore = re.compile(r"^\./\.git")
cppsrc = re.compile(r"\.(?:cpp|hpp|hxx|c|h)$")


def updateProjectsCMakeLists(path, name):
    print(name + " - updating file list...")
    
    header = "target_sources(" + name + " PRIVATE\n"
    outstr = header
    outfiles = []
    outwin = []
    outunix = []
    include = set()

    for rawRoot, dirs, files in os.walk(path):
        root = rawRoot.replace(os.sep, '/')

        if ignore.match(root):
            dirs.clear()
            continue
        
        for dir in dirs:
            if dir == "include":
                include.add(posixpath.join(root, dir).strip())

        for file in files:
            if cppsrc.search(file):
                filename = (posixpath.join(root, file)).strip()
                out = outfiles

                if "windows/" in filename:
                    out = outwin

                if "unix/" in filename:
                    out = outunix
                
                if file.endswith(".h"):
                    include.add(root)
               

                out.append(filename)

    outfiles.sort()
    outwin.sort()
    outunix.sort()

    for p in outfiles:
        outstr += "\t\"" + p + "\"\n"

    outstr += ")\nif(WIN32)\n" + header + "\n"

    for p in outwin:
        outstr += "\t\"" + p + "\"\n"

    outstr += ")\nendif()\n"
    outstr += "if(UNIX)\n" + header + "\n"

    for p in outunix:
        outstr += "\t\"" + p + "\"\n"

    outstr += ")\nendif()\n"
    outstr += "target_include_directories(" + name + " PUBLIC\n"
    
    for p in include:
        outstr += "\t\"" + p + "\"\n"

    outstr +=")\n"
    
    filename = os.path.join(path, "_source_files.cmake")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(outstr)


updateProjectsCMakeLists(".", "PhysX")

print("Done. Took: {:.4f}s".format(time.perf_counter() - startTime))
