# Troubleshooting storage issues

In some cases, you may experience storage issues with your file system. You can
troubleshoot these issues by using `lfs` commands, such as the
`lfs migrate` command.

## Write error due to no space on storage target

You can check the storage usage of your file system by using the `lfs df -h`
command, as described in [File system storage layout](performance.md#storage-layout "performance.md#storage-layout").
The `filesystem_summary` field reports the total file system storage usage.

If the file system disk usage is 100%, consider increasing the storage capacity of your
file system. For more information, see [Managing storage capacity](managing-storage-capacity.md "managing-storage-capacity.md").

If the file system storage usage is not 100% and you still get write errors, the file you
are writing to may be striped on an OST that is full.

**Action to take**

- If many of your OSTs are full, increase the storage capacity of your file system. Check
  for unbalanced storage on OSTs by following the actions of the
  [Unbalanced storage on OSTs](#lfs-migrate-unbalanced-storage "#lfs-migrate-unbalanced-storage") section.
- If your OSTs are not full, tune the client dirty page buffer size by applying
  the following tuning to all your client instances:

```
`sudo lctl set_param osc.*.max_dirty_mb=64`
```

## Unbalanced storage on OSTs

Amazon FSx for Lustre distributes new file stripes evenly across OSTs. However, your file system may still
become unbalanced due to I/O patterns or file storage layout. As a result, some storage
targets can become full while others remain relatively empty.

You use the `lfs migrate` command to move files or directories from
more-full to less-full OSTs. You can use the `lfs migrate` command in either
block or non-block mode.

- **Block mode** is the default mode for the
  `lfs migrate` command. When run in block mode, `lfs migrate`
  first acquires a group lock on the files and directories before data migration to
  prevent modifications to the files, then releases the lock when migration
  completes. By preventing other processes from modifying the files, block mode prevents
  these processes from interrupting the migration. The downside is that preventing an
  application from modifying a file may result in delays or errors for the application.
- **Non-block mode** is enabled for the
  `lfs migrate` command with the `-n` option. When running
  `lfs migrate` in non-block mode, other processes can still modify the
  files that are being migrated. If a process modifies a file before `lfs migrate`
  finishes migrating it, `lfs migrate` will fail to migrate that file,
  leaving the file with its original stripe layout.

We recommend you use non-block mode, as it is less likely to interfere with your application.

**Action to take**

1. Launch a relatively large client instance (such as the Amazon EC2 `c5n.4xlarge`
   instance type) to mount to the file system.
2. Before running the non-block mode script pr the block-mode script, first run
   the following commands on each client instance to speed up the process:

```
`sudo lctl set_param 'mdc.*.max_rpcs_in_flight=60'
sudo lctl set_param 'mdc.*.max_mod_rpcs_in_flight=59'`
```

3. Start a screen session and run the non-block mode script or the block mode script.
   Make sure to change the appropriate variables in the scripts:
   - Non-block mode script:

   ```
   `#!/bin/bash

   # UNCOMMENT THE FOLLOWING LINES:
   #
   # TRY_COUNT=0
   # MAX_MIGRATE_ATTEMPTS=100
   # OSTS="fsname-OST0000_UUID"
   # DIR_OR_FILE_MIGRATED="/mnt/subdir/"
   # BATCH_SIZE=10
   # PARALLEL_JOBS=16 # up to max-procs processes, set to 16 if client is c5n.4xlarge with 16 vcpu
   # LUSTRE_STRIPING_CONFIG="-E 100M -c 1 -E 10G -c 8 -E 100G -c 16 -E -1 -c 32" # should be consistent with the existing striping setup
   #

   if [ -z "$TRY_COUNT" -o -z "$MAX_MIGRATE_ATTEMPTS" -o -z "$OSTS" -o -z "$DIR_OR_FILE_MIGRATED" -o -z "$BATCH_SIZE" -o -z "$PARALLEL_JOBS" -o -z "$LUSTRE_STRIPING_CONFIG" ]; then
    echo "Some variables are not set."
    exit 1
   fi

   echo "lfs migrate starts"
   while true; do
    output=$(sudo lfs find ! -L released --ost $OSTS --print0 $DIR_OR_FILE_MIGRATED | shuf -z | /bin/xargs -0 -P $PARALLEL_JOBS -n $BATCH_SIZE sudo lfs migrate -n $LUSTRE_STRIPING_CONFIG 2>&1)
    if [[ $? -eq 0 ]]; then
    echo "lfs migrate succeeds for $DIR_OR_FILE_MIGRATED at the $TRY_COUNT attempt, exiting."
    exit 0
    elif [[ $? -eq 123 ]]; then
    echo "WARN: Target data objects are not located on these OSTs. Skipping lfs migrate"
    exit 1
    else
    echo "lfs migrate fails for $DIR_OR_FILE_MIGRATED at the $TRY_COUNT attempt, retrying..."
    if (( ++TRY_COUNT >= MAX_MIGRATE_ATTEMPTS )); then
    echo "WARN: Exceeds max retry attempt. Skipping lfs migrate for $DIR_OR_FILE_MIGRATED. Failed with the following error"
    echo $output
    exit 1
    fi
    fi
   done`
   ```

   - Block mode script:
     - Replace the values in `OSTS` with the values of your OSTs.
     - Provide an integer value to `nproc` to set the number of max-procs processes
       to run in parallel. For example, the Amazon EC2 `c5n.4xlarge` instance type has 16 vCPUs, so
       you can use `16` (or a value < 16) for `nproc`.
     - Provide your mount directory path in `mnt_dir_path`.

   ```
   `# find all OSTs with usage above a certain threshold; for example, greater than or equal to 85% full
   for OST in $(lfs df -h |egrep '( 8[5-9]| 9[0-9]|100)%'|cut -d' ' -f1); do echo ${OST};done|tr '\012' ','

   # customer can also just pass OST values directly to OSTS variable
   OSTS='dzfevbmv-OST0000_UUID,dzfevbmv-OST0002_UUID,dzfevbmv-OST0004_UUID,dzfevbmv-OST0005_UUID,dzfevbmv-OST0006_UUID,dzfevbmv-OST0008_UUID'

   nproc=<Run up to max-procs processes if client is c5n.4xlarge with 16 vcpu, this value can be set to 16>

   mnt_dir_path=<mount dir, e.g. '/my_mnt'>

   lfs find ${mnt_dir_path} --ost ${OSTS}| xargs -P ${nproc} -n2 lfs migrate -E 100M -c 1 -E 10G -c 8 -E 100G -c 16 -E -1 -c 32`
   ```

**Notes**

- If you notice that there is an impact on the performance of the reads of the file system,
  you can stop the migrations at any time by using `ctrl-c` or k`ill -9`,
  and reduce the number of threads (`nproc` value) back to a lower number (such as
  8), and resume migrating files.
- The `lfs migrate` command will fail on a file that is also opened by the client
  workload. It will throw an error and move to the next file; therefore, it is possible if there
  are many files being accessed, the script will not be able to migrate any files, and it will
  be reflected as the migration is making very slow progress.
- You can monitor OST usage using either of the following methods
  - On client mount, run the following command to monitor OST usage and find the
    OST with usage greater than 85%:

  ```
  `lfs df -h |egrep '( 8[5-9]| 9[1-9]|100)%'`
  ```

  - Check the Amazon CloudWatch metric, `OST FreeDataStorageCapacity`, check
    `Minimum`. If your script is finding OSTs that are over 85% full, then when the
    metric is close to 15%, use `ctrl-c` or `kill -9` to stop the migration.

- You may also consider changing the stripe configuration of your file system or a
  directory, so that new files are striped across multiple storage targets. For more
  information, see in [Striping data in your file system](performance.md#striping-data "performance.md#striping-data").
