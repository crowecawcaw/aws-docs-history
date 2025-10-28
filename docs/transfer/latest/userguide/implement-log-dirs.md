# Implementing logical directories

###### Important

Root directory requirements

- If you are not using Amazon S3 performance optimization settings your root
  directory must exist on startup.
- For Amazon S3, this means creating a zero-byte object that ends with a forward
  slash (`/`).
- To avoid this requirement, consider enabling Amazon S3 performance optimization
  when you create or update your server.
- When specifying a HomeDirectory with LOGICAL HomeDirectoryType, the value
  must map to one of your logical directory mappings. The service validates
  this during both user creation and updates to prevent configurations that
  would not work.

Logical home directory configuration

When using LOGICAL as your HomeDirectoryType, note the following:

- The HomeDirectory value must correspond to one of your existing logical
  directory mappings.
- The system automatically validates this during user creation and
  updates.
- This validation prevents configurations that would cause access
  issues.

## Enable logical directories

To use logical directories for a user, set the `HomeDirectoryType`
parameter to `LOGICAL`. Do this when you create a new user or update an
existing user.

```
"HomeDirectoryType": "LOGICAL"
```

## Enable `chroot` for users

For **chroot**, create a directory structure that consists of a
single `Entry` and `Target` pairing for each user. The Entry
**/** represents the root folder, while
**Target** specifies the actual location in your bucket or file
system.

Example for Amazon S3

```
[{"Entry": "/", "Target": "/amzn-s3-demo-bucket/jane"}]
```

Example for Amazon EFS

```
[{"Entry": "/", "Target": "/fs-faa1a123/jane"}]
```

You can use an absolute path as in the previous example, or you can use a dynamic
substitution for the username with `${transfer:UserName}`, as in the
following example.

```
[{"Entry": "/", "Target":
"/`amzn-s3-demo-bucket`/${transfer:UserName}"}]
```

In the preceding example, the user is locked to their root directory and cannot
traverse up higher in the hierarchy.

## Virtual directory structure

For a virtual directory structure, you can create multiple `Entry`
`Target` pairings, with targets anywhere in your S3 buckets or EFS file
systems, including across multiple buckets or file systems, as long as the user’s
IAM role mapping has permissions to access them.

In the following virtual structure example, when the user logs into AWS SFTP,
they are in the root directory with sub-directories of `/pics`,
`/doc`, `/reporting`, and
`/anotherpath/subpath/financials`.

###### Note

Unless you choose to optimize performance for your Amazon S3 directories (when you
create or update a server), either the user or an administrator needs to create
the directories if they don't already exist. Avoiding this issue is a reason to
consider optimizing Amazon S3 performance.

For Amazon EFS, you still need the administrator to create the logical mappings or
the `/` directory.

```
[
{"Entry": "/pics", "Target": "/amzn-s3-demo-bucket1/pics"},
{"Entry": "/doc", "Target": "/amzn-s3-demo-bucket1/anotherpath/docs"},
{"Entry": "/reporting", "Target": "/amzn-s3-demo-bucket2/Q1"},
{"Entry": "/anotherpath/subpath/financials", "Target": "/amzn-s3-demo-bucket2/financials"}]
```

###### Note

You can only upload files to the specific folders that you map. This means
that in the previous example, you cannot upload to `/anotherpath` or
`anotherpath/subpath` directories; only
`anotherpath/subpath/financials`. You also cannot map to those
paths directly, as overlapping paths are not allowed.

For example, assume that you create the following mappings:

```
{
   "Entry": "/pics",
   "Target": "/amzn-s3-demo-bucket/pics"
},
{
   "Entry": "/doc",
   "Target": "/amzn-s3-demo-bucket/mydocs"
},
{
   "Entry": "/temp",
   "Target": "/amzn-s3-demo-bucket2/temporary"
}
```

You can only upload files to those buckets. When you first connect through
`sftp`, you are dropped into the root directory, `/`.
If you attempt to upload a file to that directory, the upload fails. The
following commands show an example sequence:

```
sftp> pwd
Remote working directory: /
sftp> put file
Uploading file to /file
remote open("/file"): No such file or directory
```

To upload to any `directory/sub-directory`, you must explicitly map
the path to the `sub-directory`.

For more information about configuring logical directories and
**chroot** for your users, including an AWS CloudFormation template that
you can download and use, see [Simplify your AWS SFTP Structure with chroot and logical directories](https://aws.amazon.com/blogs/storage/simplify-your-aws-sftp-structure-with-chroot-and-logical-directories/ "https://aws.amazon.com/blogs/storage/simplify-your-aws-sftp-structure-with-chroot-and-logical-directories/")
in the AWS Storage Blog.
