

# Understanding how synchronization works
<a name="s3-files-synchronization"></a>

S3 Files keeps your file system and the linked S3 bucket synchronized automatically. The data you actively use is copied to the file system, so you can read and write files using standard Linux file operations at low latency. S3 Files requires S3 Versioning to be enabled on the linked S3 bucket. When you edit files on the file system, S3 Files copies your changes back to the S3 bucket as new versions of the corresponding objects, making sure the old versions are preserved. When other applications add, modify, or delete objects in your S3 bucket, S3 Files automatically reflects those changes in your file system. When a conflict occurs due to concurrent changes to the same data in both the file system and the S3 bucket, S3 Files treats the [S3 bucket as the source of truth in case of conflicts](#s3-files-sync-source-of-truth).

To optimize storage costs, S3 Files removes data you have not used recently from the file system. Your data remains durably stored in the linked S3 bucket and is fetched back onto the file system the next time you access it.

## S3 bucket is accessible through the file system
<a name="s3-files-sync-bucket-accessible"></a>

After you create an S3 file system, you can [mount your S3 buckets on compute resources](s3-files-attach-compute.md) and start accessing your S3 bucket data right away. By default, when you first access a directory by listing its contents or opening a file within it, S3 Files imports the metadata for all files in that directory, along with the data for files smaller than the import size threshold (default 128 KiB) from the S3 bucket. The first access to a directory might have higher latency, but subsequent reads and writes are significantly faster. By importing metadata upfront, S3 Files enables you to browse directory contents, view file sizes, and check permissions at low latency.

For example, suppose your S3 bucket contains a prefix `data/images/` with 1,000 objects. The first time you run `ls /mnt/s3files/data/images/`, S3 Files imports metadata for all 1,000 files and asynchronously copies data for files below the import size threshold onto the file system. This initial listing may take several seconds, but subsequent commands such as `ls -la`, `stat`, or `cat` on individual files in that directory return at low latency.

For files larger than the import size threshold, S3 Files imports only metadata, while data is not copied to the file system and is instead read directly from the S3 bucket when you access it. You can adjust this threshold to better match your workload. For example, you can increase it to import more data up front for workloads that repeatedly access the same files and benefit from low-latency reads. For workloads that stream data sequentially, a lower threshold can be more cost effective, as the latency benefit of importing data up front is less meaningful when data is read sequentially in large chunks rather than in small, random reads. For more information, see [Customizing synchronization for S3 Files](s3-files-synchronization-customizing.md).

## Changes in your file system automatically reflect in your S3 bucket
<a name="s3-files-sync-changes-to-bucket"></a>

When you create, modify, or delete files in the file system, S3 Files automatically copies those changes to your S3 bucket. New files become new S3 objects, changes to existing files become new object versions, and deleted files become S3 delete markers.

POSIX permissions that you set on files and directories through the file system, such as owner (UID), group (GID), and permission bits, are stored as user-defined S3 object metadata on the corresponding S3 objects. When you change permissions using `chmod`, `chown`, or `chgrp`, S3 Files exports those changes to your S3 bucket along with any data changes. When S3 Files imports objects from your S3 bucket, it reads this metadata and applies the corresponding POSIX permissions on the file system. Objects that do not have POSIX permission metadata are assigned default permissions.

When a file is modified on the file system, S3 Files waits for a period of write inactivity (60 seconds) before exporting those changes back to your S3 bucket. Rapid successive writes to the same file are captured in a single S3 PUT request rather than generating multiple object versions for each individual change. This reduces both your S3 request costs and storage costs. You can use this 60-second inactivity window as an export trigger. For example, if your application appends data to a file every 30 seconds for a total of 5 minutes, S3 Files starts the export process at minute 6. If you make additional changes, the process repeats after each 60-second period of no write activity.

## Changes in your S3 bucket automatically appear in your file system
<a name="s3-files-sync-changes-from-bucket"></a>

S3 Files monitors changes in your S3 bucket using S3 Event Notifications. When another application working with the S3 API adds, modifies, or deletes objects in your S3 bucket, S3 Files automatically reflects those changes in the file system for files whose data is currently stored in the file system's high performance storage. Files whose data has been expired from the file system are not updated until the next time you access them, at which point S3 Files retrieves the latest version from the S3 bucket.

## Understanding the impact of rename and move operations
<a name="s3-files-sync-rename-move"></a>

Amazon S3 uses a flat storage structure where objects are identified by their key names. While S3 Files lets you organize your data in directories, S3 has no native concept of directories. What appears as a directory in your file system is a common prefix shared by the keys of the objects within the S3 bucket. Additionally, S3 objects are immutable and do not support atomic renames. As a result, when you rename or move a file, S3 Files must write the data to a new object with the updated key and delete the original. When you rename or move a directory, S3 Files must repeat this process for every object that shares that prefix. Therefore, when you rename or move a directory containing tens of millions of files, your S3 request costs and the synchronization time increase significantly.

S3 Files returns an error when you attempt to create a file system scoped to a prefix with a large number of objects such that a rename can take up to 4 hours (approximately up to 12 million objects). This error alerts you that large recursive rename or move operations may impact file system performance, as every file requires separate write and delete requests to your S3 bucket. If you still want to create a file system scoped to that prefix, you can add the `--AcceptBucketWarning` parameter.

Since S3 Files renames objects individually on the S3 bucket, both directories will be visible on the S3 bucket until the rename is fully completed. Objects written after the directory was renamed but before that rename is fully synchronized will not be moved. To simplify data reorganization work, we recommend you do not create new objects through the S3 bucket while renaming a matching directory.

For example, if you run `mv /mnt/s3files/projects/alpha /mnt/s3files/projects/beta`, the rename completes instantly on the file system. On the S3 bucket, S3 Files begins copying and deleting each object to its new key within the S3 bucket (replacing the `projects/alpha/` prefix with `projects/beta/`) and deleting the original. During this process, the S3 bucket temporarily contains objects under both `projects/alpha/` and `projects/beta/`. Once all objects have been moved, only `projects/beta/` remains.

## Unused data is expired from the file system to optimize storage
<a name="s3-files-sync-expiration"></a>

S3 Files optimizes storage costs by automatically removing file data that has not been read recently from the file system. Your data remains safely stored in your S3 bucket. S3 Files only removes the copy from the file system. File metadata, such as names, sizes, and permissions, is never removed from the file system so you can continue browsing your file system at low latency.

If a file in your file system has not been read for 30 days (configurable) and its changes have already been synchronized to the S3 bucket, S3 Files removes the file data from the file system. The next time you read that file, S3 Files retrieves the latest version of the corresponding object from the S3 bucket and copies it back onto the file system.

For example, suppose you process a dataset in `/mnt/s3files/data/batch-jan.parquet` in January and do not access it again. After 30 days, S3 Files removes the file data from the file system. The file still appears in directory listings with its correct size and permissions, but the data is no longer on the file system. When you read the file again in April, S3 Files retrieves it from the S3 bucket and copies it back onto the file system. The first read may have higher latency, but subsequent reads are fast.

## S3 bucket is the source of truth in case of conflicts
<a name="s3-files-sync-source-of-truth"></a>

A conflict occurs when the same file has been modified through the file system and the corresponding S3 object has also changed before S3 Files has synchronized the file system changes back to the S3 bucket. For example, you might edit a file through your mounted file system while another application uploads a new version of the corresponding object, or deletes it, directly in the linked S3 bucket.

S3 Files detects conflicts when it attempts to synchronize your file system changes back to the S3 bucket, or when it receives an S3 event notification indicating that the object has changed. Your S3 bucket serves as the long-term store for your data, so S3 Files considers the S3 bucket as the source of truth when a conflict occurs. This provides predictable consistency, ensuring that the version in your S3 bucket always takes precedence. In case of a conflict, S3 Files moves the conflicting file from its current location in your file system to a lost and found directory and imports the latest version from the linked S3 bucket into the file system.

For example, suppose you edit `/mnt/s3files/report.csv` through the file system. Before S3 Files synchronizes your changes back to the S3 bucket, another application uploads a new version of `report.csv` directly to the S3 bucket. When S3 Files detects the conflict, it moves your version of `report.csv` to the lost and found directory and replaces it with the version from the S3 bucket.

The lost and found directory is located in your file system's root directory under the name `.s3files-lost+found-{{file-system-id}}`. If you mount your file system through an access point that specifies a root directory, the lost and found directory is not visible from that mount because it is located above the access point's root directory. To access the lost and found directory, mount the file system without an access point or use an access point without a root directory restriction so that you can access the full file system's scope via the access point.

When S3 Files moves a file to the lost and found directory, it prepends the file name with an identifier to distinguish multiple versions of the same file that may be moved over time. Files in the lost and found directory are not copied to your S3 bucket. You can delete files and copy files from this directory, but you cannot move or rename files within it or delete the directory itself. If you want to keep your file system changes instead of the latest version in the S3 bucket, copy the file from the lost and found directory back to its original path. You can retrieve the file's original path from the extended attributes of the file in the lost and found directory. S3 Files will then copy it to your S3 bucket as a new version of the object. For more information, see [Troubleshooting S3 Files](s3-files-troubleshooting.md).

**Note**  
Conflicting files that S3 Files moves to the lost and found directory remain there indefinitely and count toward your file system storage costs. You should delete files from the lost and found directory to free up storage when they are no longer needed.

The default synchronization settings will work for most workloads for low-latency, file-based access to S3 data. For more details about how to configure these parameters, see [Customizing synchronization for S3 Files](s3-files-synchronization-customizing.md).

**Topics**
+ [S3 bucket is accessible through the file system](#s3-files-sync-bucket-accessible)
+ [Changes in your file system automatically reflect in your S3 bucket](#s3-files-sync-changes-to-bucket)
+ [Changes in your S3 bucket automatically appear in your file system](#s3-files-sync-changes-from-bucket)
+ [Understanding the impact of rename and move operations](#s3-files-sync-rename-move)
+ [Unused data is expired from the file system to optimize storage](#s3-files-sync-expiration)
+ [S3 bucket is the source of truth in case of conflicts](#s3-files-sync-source-of-truth)
+ [Customizing synchronization for S3 Files](s3-files-synchronization-customizing.md)