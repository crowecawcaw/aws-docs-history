# POSIX permissions in S3 Files

POSIX file systems require ownership and permissions on every file. Amazon S3 stores
data as objects with access controlled by IAM policies and bucket policies and does not
natively store file ownership or permission attributes. S3 Files bridges this difference by
storing POSIX metadata, including the owner, group, and file permissions, as user-defined
metadata on each S3 object. When you create or modify a file through S3 Files, the service
writes all permission metadata automatically. When an object is written to your S3 bucket
outside the file system, for example through the Amazon S3 console, AWS CLI, or AWS SDK,
no POSIX metadata exists on that object. S3 Files assigns those objects a default value of
`root:root` ownership and `644` permissions, which allow non-root
users to read the file but not write to it. If these defaults meet your access requirements,
no action is required. If your application requires it, you can override the default
permissions on those objects. This tutorial walks through applying custom
permissions.

## How S3 Files stores POSIX metadata

S3 Files stores POSIX information as user-defined metadata on each object. The
following metadata keys control ownership and permissions:

| Metadata key                  | Description                           | Example value |
| ----------------------------- | ------------------------------------- | ------------- |
| `x-amz-meta-file-owner`       | POSIX user ID (UID)                   | `1000`        |
| `x-amz-meta-file-group`       | POSIX group ID (GID)                  | `1000`        |
| `x-amz-meta-file-permissions` | File type and permission bits (octal) | `0100644`     |

When an object has no POSIX metadata, S3 Files applies the following defaults:

- **Files:** `root:root` ownership
  with `0644` permissions
  (`-rw-r--r--`)
- **Directories:** `root:root`
  ownership with `0755` permissions
  (`drwxr-xr-x`)

Under these defaults, all users can read files and traverse directories, but only
the owner (root) can write. Files are not executable by default.

## Setting POSIX metadata on existing objects

Use the following procedure to apply POSIX ownership and permissions to objects that
already exist in your bucket.

### Step 1: Identify the target user's UID and GID

For this example, the target user is `ec2-user` with UID 1000:

```
$ id ec2-user
uid=1000(ec2-user) gid=1000(ec2-user) groups=1000(ec2-user)
```

### Step 2: Update object metadata using copy-object

The `aws s3api copy-object` command copies the object in place with
updated metadata. Replace `BUCKET_NAME` and
`OBJECT_KEY` with your values.

The `--metadata-directive REPLACE` option replaces all user-defined
metadata on the object. Include `--content-type` to preserve the
object's content type, because `REPLACE` resets it to the default
(`binary/octet-stream`). If you use other metadata fields, include them
in the `--metadata` parameter.

```
aws s3api copy-object \
    --bucket BUCKET_NAME \
    --key OBJECT_KEY \
    --copy-source BUCKET_NAME/OBJECT_KEY \
    --metadata-directive REPLACE \
    --content-type CONTENT_TYPE \
    --metadata '{"file-owner":"1000", "file-group":"1000", "file-permissions":"0100644"}'
```

### Step 3: Verify metadata was applied

Run the following command to confirm the metadata:

```
aws s3api head-object --bucket BUCKET_NAME --key OBJECT_KEY
```

The response includes your POSIX metadata:

```
{
    "AcceptRanges": "bytes",
    "LastModified": "Mon, 18 May 2026 14:43:00 GMT",
    "ContentLength": 7214,
    "ETag": "\"abc123...\"",
    "ContentType": "image/png",
    "Metadata": {
        "file-owner": "1000",
        "file-group": "1000",
        "file-permissions": "0100644"
    }
}
```

### Step 4: Verify permissions on the S3 file system

```
$ ls -ltr /mnt/s3files/
-rw-r--r--. 1 ec2-user ec2-user 7214 May 18 14:43 s3.png
```

The file is now owned by `ec2-user` and no longer requires root to
access.

## Setting POSIX metadata on new uploads

You can include POSIX metadata when you upload objects to your bucket.

### Using aws s3 cp

```
aws s3 cp localfile.txt s3://BUCKET_NAME/localfile.txt \
    --metadata '{"file-owner":"1000", "file-group":"1000", "file-permissions":"0100644"}'
```

### Using aws s3api put-object

```
aws s3api put-object \
    --bucket BUCKET_NAME \
    --key localfile.txt \
    --body localfile.txt \
    --metadata '{"file-owner":"1000", "file-group":"1000", "file-permissions":"0100644"}'
```

### Verify metadata on the uploaded object

```
aws s3api head-object --bucket BUCKET_NAME --key localfile.txt
```

## Permission values reference

The following table lists common POSIX permission values and their use cases.

| Octal value | File mode    | Use case                                                        |
| ----------- | ------------ | --------------------------------------------------------------- |
| `0100644`   | `-rw-r--r--` | Standard file: owner read/write, others read-only               |
| `0100664`   | `-rw-rw-r--` | Shared file: owner and group read/write, others read-only       |
| `0100755`   | `-rwxr-xr-x` | Executable: owner full access, others read and execute          |
| `0100666`   | `-rw-rw-rw-` | World-writable file: all users can read and write               |
| `0040755`   | `drwxr-xr-x` | Standard directory: owner full access, others read and traverse |

## Best practices

Upload files through the S3 file system whenever possible. S3 Files automatically
stores the file's ownership and permissions as object metadata, so no additional steps
are required. When uploading directly to the S3 bucket, include POSIX metadata in the
upload command to ensure the correct ownership and permissions are set from the
start.
