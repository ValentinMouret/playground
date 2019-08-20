#!/bin/bash

set -e

function archive {
    folder_to_archive="$1"
    echo "archiving $folder_to_archive"
    tar -cvf \
      "build/${folder_to_archive}.tar.gz" \
      "$folder_to_archive"
}

archive "$1"
