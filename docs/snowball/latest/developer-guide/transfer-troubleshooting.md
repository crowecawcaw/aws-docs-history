AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Troubleshooting data transfer

problems with Snowball Edge

If you encounter performance issues while transferring data to or from a Snowball
Edge, see [Recommendations for best data transfer performance to or from a Snowball Edge](BestPractices.md#performance "BestPractices.md#performance") for recommendations
and guidance on improving transfer performance. The following can help you troubleshoot
issues that you might have with your data transfer to or from a Snowball Edge:

- You can't transfer data into the root directory of the Snowball Edge. If you
  have trouble transferring data into the device, make sure that you're
  transferring data into a subdirectory. The top-level subdirectories have the
  names of the Amazon S3 buckets that you included in the job. Put your data in those
  subdirectories.
- If you're using Linux and you can't upload files with UTF-8 characters to an
  AWS Snowball Edge device, it might be because your Linux server doesn't recognize UTF-8
  character encoding. You can correct this issue by installing the
  `locales` package on your Linux server and configuring it to use
  one of the UTF-8 locales like `en_US.UTF-8`. You can configure the
  `locales` package by exporting the environment variable
  `LC_ALL`, for example: `export
LC_ALL=en_US.UTF-8`
- When you use the Amazon S3 interface with the AWS CLI, you can work with
  files or folders with spaces in their names, such as `my photo.jpg`
  or `My Documents`. However, make sure that you handle the spaces
  properly. For more information, see [Specify parameter values for the
  AWS CLI](../../../cli/latest/userguide/cli-usage-parameters.md "../../../cli/latest/userguide/cli-usage-parameters.md") in the _AWS Command Line Interface User Guide_.

## Troubleshooting import job problems with Snowball Edge

Sometimes files fail to import into Amazon S3. If the following issue occurs, try the
actions specified to resolve your issue. If a file fails import, you might need to try
importing it again. Importing it again might require a new job for Snowball
Edge.

###### Files failed import into Amazon S3 due to invalid characters in object names

This problem occurs if a file or folder name has characters that aren't supported
by Amazon S3. Amazon S3 has rules about what characters can be in object names. For more
information, see [Creating object key names](../../../AmazonS3/latest/userguide/object-keys.md "../../../AmazonS3/latest/userguide/object-keys.md") in Amazon S3 User Guide.

###### Action to take

If you encounter this issue, you see the list of files and folders that failed
import in your job completion report.

In some cases, the list is prohibitively large, or the files in the list are too large
to transfer over the internet. In these cases, you should create a new Snowball import
job, change the file and folder names to comply with Amazon S3 rules, and transfer the files
again.

If the files are small and there isn't a large number of them, you can copy them to
Amazon S3 through the AWS CLI or the AWS Management Console. For more information, see [How do I upload files and folders to an S3
bucket?](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the _Amazon Simple Storage Service User Guide._

## Troubleshooting export job problems with Snowball Edge

Sometimes files fail to export into your workstation. If the following issue occurs,
try the actions specified to resolve your issue. If a file fails export, you might need
to try exporting it again. Exporting it again might require a new job for Snowball
Edge.

###### Files failed export to a Microsoft Windows Server

A file can fail export to a Microsoft Windows Server if it or a related folder is
named in a format not supported by Windows. For example, if your file or folder name
has a colon (`:`) in it, the export fails because Windows doesn't allow
that character in file or folder names.

###### Action to take

1. Make a list of the names that are causing the error. You can find the names of
   the files and folders that failed export in your logs. For more information, see
   [Viewing and downloading logs from Snowball Edge](using-client-commands.md#logs "using-client-commands.md#logs").
2. Change the names of the objects in Amazon S3 that are causing the issue to remove
   or replace the unsupported characters.
3. If the list of names is prohibitively large, or if the files in the list are
   too large to transfer over the internet, create a new export job specifically
   for those objects.

If the files are small and there isn't a large number of them, copy the
renamed objects from Amazon S3 through the AWS CLI or the AWS Management Console. For more
information, see [How do I
download an object from an S3 bucket?](../../../AmazonS3/latest/userguide/download-objects.md "../../../AmazonS3/latest/userguide/download-objects.md") in the*Amazon Simple Storage Service User Guide.*

## Troubleshooting NFS interface problems with Snowball Edge

The Snowball Edge may indicate the status of the NFS interface is `DEACTIVATED`. This might occur if the Snowball Edge was powered off without first stopping the NFS interface.

###### Action to take

To correct the problem, stop and restart the NFS service using the following steps.

1. Use the `describe-service` command to determine the status of the
   service:

```

snowballEdge describe-service --service-id nfs

```

The command returns the following.

```

{
  "ServiceId" : "nfs",
  "Status" : {
  "State" : "DEACTIVATED"
  }
}

```

2. Use the `stop-service` command to stop the NFS service.

```

snowballEdge stop-service --service-id nfs
```

3. Use the `start-service` command to start the NFS service. For more information, see [Managing the NFS interface](shared-using-nfs.md "shared-using-nfs.md").

```

snowballEdge start-service  --virtual-network-interface-arns `vni-arn` --service-id nfs  `--service-configuration AllowedHosts=0.0.0.0/0`

```

4. Use the `describe-service` command to make sure the service is running.

```

snowballEdge describe-service --service-id nfs
```

If the value of the `State` name is `ACTIVE`, the NFS interface service is active.

```

{
 "ServiceId" : "nfs",
 "Status" : {
 "State" : "ACTIVE"
 },
 "Endpoints" : [ {
 "Protocol" : "nfs",
 "Port" : 2049,
 "Host" : "192.0.2.0"
 } ],
 "ServiceConfiguration" : {
 "AllowedHosts" : [ "10.24.34.0/23", "198.51.100.0/24" ]
 }
}

```

## Troubleshooting an access denied error when transferring data using the S3 interface

When using the S3 interface to transfer data to or from a Snowball Edge device, you might encounter an access denied error. This error may be the result of IAM user or bucket policies.

###### Action to take

1. Check the policy of the S3 bucket you are using for the following syntax issues.
   1. If the policy only allows data to be uploaded if KMS headers are passed, ensure the policy specifies an principal ARN instead of a user ID. The example below shows the correct syntax.

   ```

       {
       "Sid": "Statement3",
       "Effect": "Deny",
       "Principal": "*",
       "Action": "s3:PutObject",
       "Resource": "`arn:aws:s3:::amzn-s3-demo-bucket/*`",
       "Condition": {
           "StringNotLike": {
               "aws:PrincipalArn": "`arn:aws:iam::111122223333:role/JohnDoe`"
           },
           "StringNotEquals": {
               "s3:x-amz-server-side-encryption": [
                   "aws:kms",
                   "AES256"
               ]
           }
       }
   },
   {
       "Sid": "Statement4",
       "Effect": "Deny",
       "Principal": "*",
       "Action": "s3:PutObject",
       "Resource": "`arn:aws:s3:::amzn-s3-demo-bucket/*`",
       "Condition": {
           "StringNotLike": {
               "aws:PrincipalArn": "`arn:aws:iam::111122223333:role/JohnDoe`"
           },
           "Null": {
               "s3:x-amz-server-side-encryption": "true"
           }
       }
   }

   ```

   2. If the bucket policy only allows upload to the bucket if the correct headers are passed, uploads from Snowball Edge devices don't pass any headers by default. Modify the policy to allow an exception for the IAM user used to upload the data. Below is an example of the correct syntax for this.

   ```

   {
       "Sid": "Statement3",
       "Effect": "Deny",
       "Principal": "",
       "Action": "s3:PutObject",
       "Resource": "`arn:aws:s3:::amzn-s3-demo-bucket/`",
       "Condition": {
           "StringNotEquals": {
               "s3:x-amz-server-side-encryption": "AES256"
           },
           "StringNotLike": {
               "aws:PrincipalArn": "`arn:aws:iam::111122223333:role/JohnDoe`"
           }
       }
   },
   {
       "Sid": "Statement4",
       "Effect": "Deny",
       "Principal": "",
       "Action": "s3:PutObject",
       "Resource": "`arn:aws:s3:::amzn-s3-demo-bucket/`",
       "Condition": {
           "Null": {
               "s3:x-amz-server-side-encryption": "true"
           },
           "StringNotLike": {
               "aws:PrincipalArn": "`arn:aws:iam::111122223333:role/JohnDoe`"
           }
       }
   }

   ```

2. Check the policy of the KMS key you are using for the correct syntax in the Principal element. See the example below shows the correct syntax.

```

{
    "Sid": "Statement2",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam::111122223333:role/service-role/JohnDoe"
        ]
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*"
}

```

## Troubleshooting an 403 forbidden error when transferring data using the S3 interface

When using the S3 interface to transfer data to or from a Snowball Edge device, you might encounter an 403 forbidden error. This error may be the result of IAM user or bucket policies. Check the policy of the S3 bucket you are using for the following syntax issues.

###### Action to take

1. The policy does not provide the PrincipalArn. Use the following policy as an example to use the aws:PrincipalArn header and provide the IAM role ARN without `:*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "DenyIncorrectEncryptionHeader",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "Condition": {
 "StringNotLike": {
 "aws:PrincipalArn": "arn:aws:iam::111122223333:role/`ExampleRoleName`"
 },
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption": [
 "aws:kms",
 "AES256"
 ]
 }
 }
 },
 {
 "Sid": "DenyUnEncryptedObjectUploads",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "Condition": {
 "StringNotLike": {
 "aws:PrincipalArn": "arn:aws:iam::111122223333:role/`ExampleRoleName`"
 },
 "Null": {
 "s3:x-amz-server-side-encryption": "true"
 }
 }
 },
 {
 "Sid": "DenyInsecureTransport",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ],
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 },
 {
 "Sid": "AllowSnowballPutObjectAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:role/`ExampleRoleName`"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
 }
 ]
}`

```

2. If the KMS policy uses the incorrect IAM Role format, a 403 error may occur. Modify the policy to allow an exception for the IAM user used to upload the data. Below is an example of the correct syntax for this.

```

{{
            "Sid": "Allow use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::1234567890:role/service-role/RoleName"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey*"
            ],
            "Resource": "*"
        }

```

3. The IAM role may need to bypass the encryption header condition. By default, all objects stored on a Snowball Edge device are encrypted with SSE-S3 encryption. Use the policy below to provide an exception for the IAM role to upload objects without encryption headers.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PutObjPolicy",
 "Statement": [{
 "Sid": "DenyIncorrectEncryptionHeader",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::BucketName/",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption": "AES256"
 },
 "StringNotLike": {
 "aws:PrincipalArn": "arn:aws:iam::1234567890:role/RoleName"
 }
 }
 },
 {
 "Sid": "DenyUnEncryptedObjectUploads",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::BucketName/*",
 "Condition": {
 "Null": {
 "s3:x-amz-server-side-encryption": "true"
 },
 "StringNotLike": {
 "aws:PrincipalArn": "arn:aws:iam::1234567890:role/RoleName"
 }
 }
 }
 ]
}`

```

4. The error message indicates access is denied to PutObject using NotPrincipal with IP condition. Add an exception as shown below for the Snowball Edge IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:role/`RoleName`"
 ]
 },
 "Action": [
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::BucketName/*",
 "arn:aws:s3:::BucketName"
 ],
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "203.0.113.0/24"
 ]
 },
 "StringNotEquals": {
 "aws:PrincipalArn": "arn:aws:iam::1234567890:role/RoleName"
 }
 }
 }
 ]
}`

```
