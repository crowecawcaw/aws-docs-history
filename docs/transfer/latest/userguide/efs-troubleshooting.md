# Troubleshoot EFS issues

This section describes possible solutions for issues with Amazon EFS storage.

###### Topics

- [Troubleshoot Amazon EFS issues](#efs-issues "#efs-issues")

## Troubleshoot Amazon EFS issues

This section describes possible solutions for the following Amazon EFS issues.

###### Topics

- [Troubleshoot Amazon EFS service-managed
  users](#transfer-service-managed-efs "#transfer-service-managed-efs")
- [Troubleshoot missing POSIX profile](#missing-posix-profile "#missing-posix-profile")
- [Troubleshoot logical directories with
  Amazon EFS](#logical-dir-efs-no-directory "#logical-dir-efs-no-directory")

### Troubleshoot Amazon EFS service-managed

users

Description

You run the `sftp` command and the prompt doesn't appear, and instead
you see the following message:

```
Couldn't canonicalize: Permission denied
           Need cwd
```

Cause

Your AWS Identity and Access Management (IAM) user's role does not have permission to access Amazon Elastic File System
(Amazon EFS).

Solution

Increase the policy permissions for your user's role. You can add an AWS managed
policy, such as `AmazonElasticFileSystemClientFullAccess`.

### Troubleshoot missing POSIX profile

Description

If you're using Amazon EFS storage for your server and you're using a custom identity
provider, you must provide your AWS Lambda function with a POSIX profile.

Cause

One possible cause is that the templates that we provide for creating an
AWS Lambda-backed Amazon API Gateway method do not currently contain POSIX
information.

If you did provide POSIX information, the format that you used for providing the
POSIX information might not be getting parsed correctly by Transfer Family.

Solution

Make sure that you are providing a JSON element to Transfer Family for the
`PosixProfile` parameter.

For example, if you're using Python, you could add the following line where you
parse the `PosixProfile` parameter:

```
if PosixProfile:
        response_data["PosixProfile"] = json.loads(PosixProfile)
```

Or, in JavaScript, you could add the following line, where the
`uid-value` and
`gid-value` are integers, 0 or
greater, that represent the User ID (UID) and Group ID (GID) respectively:

```
PosixProfile: {"Uid": `uid-value`, "Gid": `gid-value`},
```

These code examples send the `PosixProfile` parameter to Transfer Family as a JSON
object, rather than as a string.

Also, within AWS Secrets Manager, you must store the `PosixProfile` parameter as
follows. Replace `your-uid` and
`your-gid` with your actual values for
the GID and UID.

```
{"Uid": `your-uid`, "Gid": `your-gid`, "SecondaryGids": []}
```

### Troubleshoot logical directories with

Amazon EFS

Description

If the user's home directory does not exist, and they run an `ls` command, the system
responds as follows:

```
sftp> ls
remote readdir ("/"): No such file or directory
```

Cause

If your Transfer Family server uses Amazon EFS, the home directory for the user must be created with
read and write access before the user can work in their logical home directory. The user
cannot create this directory themselves, as they would lack permissions for
`mkdir` on their logical home directory.

Solution

A user with administrative access to the parent directory needs to create the user's logical home directory.
