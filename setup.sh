#!/bin/bash
#Setup File
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

if [ $1 == "install" ]; then
	sudo cp cpdirtree.py /usr/local/bin/cpdirtree
	sudo chmod a+x /usr/local/bin/cpdirtree
	echo "cpdirtree installed successfully"
elif [[ $1 == "uninstall" ]]; then
	sudo rm /usr/local/bin/cpdirtree
	echo "cpdirtree uninstalled successfully"
else
	echo "Usage"
	echo "'sudo ./setup.sh install' to install"
	echo "'sudo ./setup.sh uninstall' to uninstall"
fi
