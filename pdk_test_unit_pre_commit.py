#!/usr/bin/env python3
""" Pre-commit script to execute pdk unit tests """
import os
import sys
import subprocess as sp


def main():
    """ Run PDK unit tests if /spec/ dir exists in provided path """
    if len(sys.argv) < 2:
        print("Please provide a path.")
        sys.exit(1)
    files = sys.argv[1:]
    module_paths = []

    for pfile in files:
        if 'modules' in pfile:
            path_split = pfile.split('/modules/')
            module_name = path_split[1].split('/')[0]
            module_path = '%s/modules/%s' % (os.path.abspath(path_split[0]),
                                             module_name)
            module_paths.append(module_path)

    for module in set(module_paths):
        try:
            mod_files = os.listdir(module)
            # only attempt to run PDK if we have a spec directory in this
            # module
            if 'spec' in mod_files:
                if os.path.isdir('%s/spec' % module):
                    cmd = "pdk test unit"
                    printout = "Running PDK for %s" % module
                    spacer = "="*len(printout)
                    print(spacer)
                    print(printout)
                    print(spacer)
                    try:
                        cmd_out = sp.check_output(cmd,
                                                  shell=True,
                                                  stderr=sp.DEVNULL,
                                                  cwd=module)
                    except sp.CalledProcessError as cmd_err:
                        print("%s" % cmd_err.output.decode())
                        sys.exit(cmd_err.returncode)
                    print(cmd_out.decode())  # only displayed if one fails
        except Exception as exp:  # pylint: disable=broad-except
            print("Exception found: %s" % exp)


if __name__ == "__main__":
    main()
