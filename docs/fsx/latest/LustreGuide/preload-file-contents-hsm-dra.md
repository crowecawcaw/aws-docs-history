# Preloading files into your file

system

You can optionally preload contents individual files or directories into your file system.

## Importing files using HSM commands

Amazon FSx copies data from your Amazon S3 data repository when a file is first accessed. Because
of this approach, the initial read or write to a file incurs a small amount of latency. If
your application is sensitive to this latency, and you know which files or directories your
application needs to access, you can optionally preload contents of individual files or
directories. You do so using the `hsm_restore` command, as follows.

You can use the `hsm_action` command (issued with the `lfs` user
utility) to verify that the file's contents have finished loading into the file system. A
return value of `NOOP` indicates that the file has successfully been loaded. Run
the following commands from a compute instance with the file system mounted. Replace
`path/to/file` with the path of the file you're preloading into
your file system.

```
sudo lfs hsm_restore `path/to/file`
sudo lfs hsm_action `path/to/file`
```

You can preload your whole file system or an entire directory within your file system by
using the following commands. (The trailing ampersand makes a command run as a background
process.) If you request the preloading of multiple files simultaneously, Amazon FSx loads your
files from your Amazon S3 data repository in parallel. If a file has already been loaded to the
file system, the `hsm_restore` command doesn't reload it.

```
nohup find `local/directory` -type f -print0 | xargs -0 -n 1 -P 8 sudo lfs hsm_restore &
```

###### Note

If your linked S3 bucket is larger than your file system, you should be able to import
all the file metadata into your file system. However, you can load only as much actual
file data as will fit into the file system's remaining storage space. You'll
receive an error if you attempt to access file data when there is no more storage left on
the file system. If this occurs, you can increase the amount of storage capacity as
needed. For more information, see [Managing storage capacity](managing-storage-capacity.md "managing-storage-capacity.md").

## Validation step

You can run the bash script listed below to help you discover how many files or objects
are in an archived (released) state.

To improve the script's performance, especially across file systems with a large number of
files, CPU threads are automatically determined based in the `/proc/cpuproc` file.
That is, you will see faster performance with a higher vCPU count Amazon EC2 instance.

1. Set up the bash script.

```
`#!/bin/bash

# Check if a directory argument is provided
if [ $# -ne 1 ]; then
 echo "Usage: $0 /path/to/lustre/mount"
 exit 1
fi

# Set the root directory from the argument
ROOT_DIR="$1"

# Check if the provided directory exists
if [ ! -d "$ROOT_DIR" ]; then
 echo "Error: Directory $ROOT_DIR does not exist."
 exit 1
fi

# Automatically detect number of CPUs and set threads
if command -v nproc &> /dev/null; then
 THREADS=$(nproc)
elif [ -f /proc/cpuinfo ]; then
 THREADS=$(grep -c ^processor /proc/cpuinfo)
else
 echo "Unable to determine number of CPUs. Defaulting to 1 thread."
 THREADS=1
fi

# Output file
OUTPUT_FILE="released_objects_$(date +%Y%m%d_%H%M%S).txt"

echo "Searching in $ROOT_DIR for all released objects using $THREADS threads"
echo "This may take a while depending on the size of the filesystem..."

# Find all released files in the specified lustre directory using parallel
# If you get false positives for file names/paths that include the word 'released',
# you can grep 'released exists archived' instead of just 'released'
time sudo lfs find "$ROOT_DIR" -type f | \
parallel --will-cite -j "$THREADS" -n 1000 "sudo lfs hsm_state {} | grep released" > "$OUTPUT_FILE"

echo "Search complete. Released objects are listed in $OUTPUT_FILE"
echo "Total number of released objects: $(wc -l <"$OUTPUT_FILE")"`
```

2. Make the script executable:

```
`$ chmod +x find_lustre_released_files.sh`
```

3. Run the script, as in the following example:

```
`$ ./find_lustre_released_files.sh /fsxl/sample`
`Searching in /fsxl/sample for all released objects using 16 threads
This may take a while depending on the size of the filesystem...
real 0m9.906s
user 0m1.502s
sys 0m5.653s
Search complete. Released objects are listed in released_objects_20241121_184537.txt
Total number of released objects: 30000`
```

If there are released objects present, then perform a bulk restore on the desired
directories to bring the files into FSx for Lustre from S3, as in the following example:

```
`$ DIR=/path/to/lustre/mount
$ nohup find $DIR -type f -print0 | xargs -0 -n 1 -P 8 sudo lfs hsm_restore &`
```

Note that `hsm_restore` will take a while where there are millions
of files.
