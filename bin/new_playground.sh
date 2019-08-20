#!/bin/bash

set -e

name="$1"

function clone {
    cp -r template "$name"
}

function fill_template {
    sed -i '' "s#PLAYGROUND_NAME#$name#g" "$name/Makefile"
}

clone && fill_template
