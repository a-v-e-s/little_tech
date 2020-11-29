#!/bin/bash

# make a directory for the desktop if it doesn't exist:
if ! [[ -d ~/Desktop ]]
then
    mkdir ~/Desktop
fi

# this puts a link to the top-level script on your desktop:
ln -Trs ./gui.py ~/Desktop/btos_cnat_raed_tihs