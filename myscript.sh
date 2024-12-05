#!/bin/bash

# Set the target directory
TARGET_DIR="/etc"

# Use find to locate regular files and count them 
file_count=$(find "$TARGET_DIR" -type f | wc -l)

# Display the result 
echo "Number of regular files in $TARGET_DIR: $file_count"
 
