#!/usr/bin/env python
#Directory Tree Copier, cpdirtree v1.11
#Copyright (c) 2014 by Brian Mikolajczyk, brianm12@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import fnmatch
import os.path
from pipes import quote

def main(input_dir=None, output_dir=None, blacklist=None):
    try:
        os.mkdir(output_dir)
    except OSError:
        pass

    print('Copying...')
    for current_dir, dirnames, unfilenames in os.walk(input_dir):
        if blacklist is not None:
            blacklist = set(blacklist)
            infiles = sorted(set([f for f in os.listdir(
                                  current_dir)]) - blacklist)
            wildlist = []
            for el in blacklist:
                wildlist = wildlist + fnmatch.filter(infiles, el)

            blacklist = blacklist | set(wildlist)
            dirnames[:] = set(dirnames) - blacklist
        else:
            blacklist = set([])

        filenames = sorted(unfilenames)
        relative_dir = os.path.relpath(current_dir, input_dir)
        current_out_dir = os.path.join(output_dir,
                          relative_dir)
        if os.path.split(current_out_dir)[1] == '.':
           current_out_dir = os.path.split(current_out_dir)[0]

        try:
            os.makedirs(current_out_dir)
        except OSError:
            pass

        for filename in [f for f in filenames if f not in blacklist]:
            out_file_path = os.path.join(current_out_dir, filename)
            open(out_file_path, 'a').close()
            
    print('Copying Complete.')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir')
    parser.add_argument('output_dir')
    parser.add_argument('--version', action='version',
                        version='cpdirtree v1.1')
    parser.add_argument('-b', '--blacklist', nargs='+',
        help='Add arguments separated by spaces to omit\
              directories/filenames')

    main(**vars(parser.parse_args()))
