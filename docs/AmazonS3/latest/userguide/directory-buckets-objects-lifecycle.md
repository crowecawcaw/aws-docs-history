# Working with S3 Lifecycle for directory buckets

S3 Lifecycle helps you store objects in S3 Express One Zone in directory buckets cost
effectively by deleting expired objects on your behalf. To manage the lifecycle of your
objects, create an S3 Lifecycle configuration for your directory bucket. An S3 Lifecycle
configuration is a set of rules that define actions that Amazon S3 applies to a group of
objects. You can set an Amazon S3 Lifecycle configuration on a directory bucket by using the
AWS Command Line Interface (AWS CLI), the AWS SDKs, the Amazon S3 REST API and AWS
CloudFormation.

In your lifecycle configuration, you use rules to define actions that you want Amazon S3 to take on your objects.
For objects stored in directory buckets, you can create lifecycle rules to expire objects as they age.
You can also create lifecycle rules to delete incomplete multipart uploads in directory buckets at a daily frequency.

When you add a Lifecycle configuration to a bucket, the configuration rules apply to both
existing objects and objects that you add later. For example, if you add a Lifecycle
configuration rule today with an expiration action that causes objects with a specific
prefix to expire 30 days after creation, S3 will queue for removal any existing objects that
are more than 30 days old and that have the specified prefix.

## How S3 Lifecycle for directory buckets is different

For objects in directory buckets, you can create lifecycle rules to expire objects and delete incomplete multipart uploads.
However, S3 Lifecycle for directory buckets doesn't support transition actions between storage classes. S3 Lifecycle for directory buckets requires you to grant explicit permissions to the S3 Lifecycle service principal.

### S3 Lifecycle permissions

S3 Lifecycle uses the `DeleteObject`, `DeleteObjects`, and `AbortMultipartUpload` API operations to expire objects in directory buckets.
To call these operations, S3 Lifecycle uses the `CreateSession` API to obtain temporary security credentials. You must grant the
`s3express:CreateSession` permission with `ReadWrite` session mode to the S3 Lifecycle service principal
(`lifecycle.s3.amazonaws.com`). If you don't grant this permission, or if an active policy explicitly denies delete permissions
to the S3 Lifecycle service principal, S3 Lifecycle cannot expire objects in your directory bucket. For more information about
`CreateSession`, see [CreateSession in the _Amazon S3 API Reference_](../API/API_CreateSession.md "../API/API_CreateSession.md").

### Using a bucket policy to grant permissions to the S3 Lifecycle service principal

The following bucket policy grants the S3 Lifecycle service principal permission to create sessions for performing operations such as
`DeleteObject` and `DeleteObjects`. When no session mode is specified in a `CreateSession` request,
the session is created with the maximum allowable privilege by the permissions in (attempting `ReadWrite` first, then `ReadOnly`
if `ReadWrite` is not permitted). However, `ReadOnly` sessions are insufficient for lifecycle operations that modify
or delete objects. Therefore, this example explicitly requires a `ReadWrite` session mode by using the
`s3express:SessionMode` condition key.

###### Example Bucket policy to allow `CreateSession` with an explicit `ReadWrite` session mode for lifecycle operations

```

 {
   "Version":"2008-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Principal": {
            "Service":"lifecycle.s3.amazonaws.com"
          },
          "Action":"s3express:CreateSession",
          "Condition": {
             "StringEquals": {
                "s3express:SessionMode": "ReadWrite"
              }
           },
           "Resource":"arn:aws:s3express:us-east-2:412345678921:bucket/amzn-s3-demo-bucket--use2-az2--x-s3"
       }
   ]
}

```

### Monitoring lifecycle rules

For objects stored in directory buckets, S3 Lifecycle generates AWS CloudTrail management and data event logs.
For more information, see [CloudTrail log file examples for directory buckets](s3-express-log-files.md "s3-express-log-files.md").

For more information about creating lifecycle configurations and troubleshooting S3 Lifecycle related issues, see the following topics:

###### Topics
