# Using logical directories to simplify your Transfer Family

directory structures

Logical directories simplify your AWS Transfer Family server directory structure. With logical
directories, you can create a virtual directory structure with user-friendly names that
users navigate when connecting to your Amazon S3 bucket or Amazon EFS file system. This prevents users
from seeing the actual directory paths, bucket names, and file system names.

###### Note

You should use session policies so that your end users can only perform operations
that you allow them to perform.

You should use logical directories to create a user-friendly, virtual directory for
your end users and abstract away bucket names. Logical directory mappings only allow
users to access their designated logical paths and subdirectories, and forbid relative
paths that traverse the logical roots.

Transfer Family validates every path that might include relative elements and actively blocks
these paths from resolving before we pass these paths to Amazon S3; this prevents your users
from moving beyond their logical mappings.

Even though Transfer Family prevents your end users from accessing directories outside of their
logical directory, we recommend you also use unique roles or session policies to enforce
least privilege at the storage level.

## Understanding chroot and directory

structure

A **chroot** operation lets you set a user's root
directory to any location in your storage hierarchy. This restricts users to their
configured home or root directory, preventing access to higher-level directories.

Consider a case where an Amazon S3 user is limited to
`amzn-s3-demo-bucket/home/${transfer:UserName}`. Without **chroot**, some clients might allow users to move up to
/amzn-s3-demo-bucket/home, requiring a logout and login to return to their proper
directory. Performing a **chroot** operation prevents this
issue.

You can create custom directory structures across multiple buckets and prefixes. This
is useful if your workflow requires a specific directory layout that bucket prefixes
alone can't provide. You can also link to multiple non-contiguous locations within Amazon S3,
similar to creating a symbolic link in a Linux file system where your directory path
references a different location in the file system.

## Rules for using logical directories

This section describes some rules and other considerations for using logical
directories.

### Mapping limits

- Only one mapping is allowed when `Entry` is `"/"`
  (no overlapping paths are allowed).
- Logical directories support mappings of up to 2.1 MB for custom IDP and AD
  users, and 2,000 entries for service-managed users. You can calculate your
  mappings size as follows:

      1. Write out a typical mapping in the format
       `{"Entry":"/`entry-path`","Target":"/`target-path`"}`,
       where ``entry-path`` and
       ``target-path`` are the
       actual values that you will use.
      2. Count the characters in that string, then add one (1).
      3. Multiply that number by the approximate number of mappings that
       you have for your server.

  If the number that you estimated in step 3 is less than 2.1 MB, then your
  mappings are within the acceptable limit.

### Target path requirements

- Use `${transfer:UserName}` variable if the bucket or file
  system path has been parameterized based on the username.
- Targets can be configured to point to different Amazon S3 buckets or file
  systems, as long as the associated IAM role has the necessary permissions
  to access those storage locations.
- All targets must begin with a forward slash (`/`) but can't end
  with one. For example, `/amzn-s3-demo-bucket/images` is correct,
  while `amzn-s3-demo-bucket/images` and
  `/amzn-s3-demo-bucket/images/` are not.

### Storage considerations

- Amazon S3 is an object store where folders exist only as a virtual concept.
  When using Amazon S3 storage, Transfer Family reports prefixes as directories in STAT
  operations, even if there is no zero-byte object with a trailing slash. A
  proper zero-byte object with a trailing slash is also reported as a
  directory in STAT operations. This behavior is described in [Organizing objects
  in the Amazon S3 console using folders](../../../AmazonS3/latest/userguide/using-folders.md "../../../AmazonS3/latest/userguide/using-folders.md") in the _Amazon Simple Storage Service User Guide_.
- For applications that need to distinguish between files and folders, use
  Amazon Elastic File System (Amazon EFS) as your Transfer Family storage option.
- If you're specifying logical directory values for your user, the parameter
  that you use depends on the type of user:
  - For service-managed users, provide logical directory values in `HomeDirectoryMappings`.
  - For custom identity provider users, provide logical directory values in `HomeDirectoryDetails`.

### User directory values

- The parameter for specifying logical directory values depends on your user
  type:
  - For service-managed users, provide logical directory values in `HomeDirectoryMappings`.
  - For custom identity provider users, provide logical directory values in `HomeDirectoryDetails`.

- When using LOGICAL HomeDirectoryType, you can specify a HomeDirectory
  value for Service Managed users, Active Directory access, and Custom
  Identity Provider implementations where the HomeDirectoryDetails are
  provided in the response. If not specified, HomeDirectory defaults to
  `/`.

For details on how to implement logical directories, see [Implementing logical directories](implement-log-dirs.md "implement-log-dirs.md").

## Configure logical directories for Amazon EFS

If your Transfer Family server uses Amazon EFS, the home directory for the user must be created with
read and write access before the user can work in their logical home directory. The user
cannot create this directory themselves, as they would lack permissions for
`mkdir` on their logical home directory.

If the user's home directory does not exist, and they run an `ls` command, the system
responds as follows:

```
sftp> ls
remote readdir ("/"): No such file or directory
```

A user with administrative access to the parent directory needs to create the user's logical home directory.

## Custom AWS Lambda response

You can use logical directories with a Lambda function that connects to your custom
identity provider. To do so, in your Lambda function, you specify the
`HomeDirectoryType` as `LOGICAL`, and add
`Entry` and `Target` values for the
`HomeDirectoryDetails` parameter. For example:

```
HomeDirectoryType: "LOGICAL"
HomeDirectoryDetails: "[{\"Entry\": \"/\", \"Target\": \"/amzn-s3-demo-bucket/theRealFolder"}]"
```

The following code is an example of a successful response from a custom Lambda
authentication call.

```
aws transfer test-identity-provider \
    --server-id s-1234567890abcdef0 \
    --user-name myuser
{
    "Url": "https://a1b2c3d4e5.execute-api.us-east-2.amazonaws.com/prod/servers/s-1234567890abcdef0/users/myuser/config",
    "Message": "",
    "Response": "{\"Role\": \"arn:aws:iam::123456789012:role/bob-usa-role\",
                  \"HomeDirectoryType\": \"LOGICAL\",
                  \"HomeDirectoryDetails\": \"[{\\\"Entry\\\":\\\"/myhome\\\",\\\"Target\\\":\\\"/amzn-s3-demo-bucket/theRealFolder\\\"}]\",
                  \"PublicKeys\": \"[ssh-rsa myrsapubkey]\"}",
    "StatusCode": 200
}
```

###### Note

The `"Url":` line is returned only if you are using an API Gateway
method as your custom identity provider.
