# Troubleshoot storage and encryption issues

This section describes possible solutions for issues with storage and encryption.

###### Topics

- [Troubleshoot policies for encrypted Amazon S3
  buckets](#encrypted-buckets "#encrypted-buckets")
- [Troubleshoot ResourceNotFound
  exception](#resource-not-found "#resource-not-found")

## Troubleshoot policies for encrypted Amazon S3

buckets

Description

You have an encrypted Amazon S3 bucket that you are using as storage for your Transfer Family server.
If you try to upload a file to the server, you receive the error `Couldn't close
 file: Permission denied`.

And if you view the server logs, you see the following errors:

```
ERROR Message="Access denied" Operation=CLOSE Path=/bucket/user/test.txt BytesIn=13
ERROR Message="Access denied"
```

Cause

The policy for your IAM user does not have permission to access the encrypted
bucket.

Solution

You must specify additional permissions in your policy to grant the required
AWS Key Management Service (AWS KMS) permissions. For details, see [Data protection and encryption](encryption-at-rest.md "encryption-at-rest.md").

## Troubleshoot `ResourceNotFound`

exception

Description

You receive an error where the resource cannot be found. For example, if you run
`UpdateServer`, you might get the following error:

```
An error occurred (ResourceNotFoundException) when calling the UpdateServer operation: Unknown server
```

Cause

There are several reasons for receiving a
**`ResourceNotFoundException`** message. In most cases, the
resource that you specified in your API command does not exist. If you did specify an
existing resource, then the most probable cause is that your default region is different
than the region for your resource. For example, if your default region is
**us-east-1**, and your Transfer Family server is in
**us-east-2**, you will receive an **`Unknown
 resource`** exception.

For details about setting a default region, see [Quick configuration with `aws configure`](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config").

Solution

Add a region parameter to your API command to explicitly specify where to find a
particular resource.

```
aws transfer -describe-server --server-id `server-id` --region us-east-2
```
