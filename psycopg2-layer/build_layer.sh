#!/bin/bash
set -e

LAYER_DIR="python"
ZIP_FILE="layer.zip"
REQUIREMENTS="requirements.txt"

# Clean up any previous builds
rm -rf $LAYER_DIR $ZIP_FILE

# Create requirements.txt if it doesn't exist
if [ ! -f "$REQUIREMENTS" ]; then
  echo "psycopg2-binary" > $REQUIREMENTS
fi

# Use Lambda-compatible Docker image to install packages
docker run --rm \
  -v "$PWD":/var/task \
  -w /var/task \
  python:3.9-slim \
  /bin/bash -c "pip install -r requirements.txt -t python"

# Zip the layer contents
zip -r $ZIP_FILE python
