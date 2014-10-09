#!/usr/bin/env python
#Directory Tree Copier, cpdirtree v1.0
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

import os.path
import argparse

def main(input_dir=None, output_dir=None, blacklist=None):
    try:
        os.mkdir(output_dir)
    except OSError:
        pass

    if blacklist is not None:
        blacklist = set(blacklist)

    _, top_input_dir = os.path.split(os.path.abspath(input_dir))
    for current_dir, dirnames, _ in os.walk(input_dir):
        if blacklist is not None:
            dirnames[:] = set(dirnames) - blacklist
        
        relative_dir = os.path.relpath(current_dir, input_dir)
        current_out_dir = os.path.join(output_dir, top_input_dir, 
                                       relative_dir).replace('/.', '/')
        try:
            os.makedirs(current_out_dir)
        except OSError:
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir')
    parser.add_argument('output_dir')
    parser.add_argument('-b', '--blacklist', nargs='+',
        help='Add arguments separated by spaces to omit filenames')

    main(**vars(parser.parse_args()))
