# Step 1: Create a Firehose delivery

stream

###### Important

Before you complete the following steps, you must use an access policy,
so Firehose can access your Amazon S3 bucket. For more information, see [Controlling Access](../../../firehose/latest/dev/controlling-access.md#using-iam-s3 "../../../firehose/latest/dev/controlling-access.md#using-iam-s3") in the _Amazon Data Firehose Developer
Guide_.

All of the steps in this section (Step 1) must be done in the log data
recipient account.

US East (N. Virginia) is used in the following sample commands. Replace this
Region with the correct Region for your deployment.

###### To create a Firehose delivery stream to be used as the destination

1. Create an Amazon S3 bucket:

```
aws s3api create-bucket --bucket amzn-s3-demo-bucket --create-bucket-configuration LocationConstraint=us-east-1
```

2. Create the IAM role that grants Firehose permission to put data into
   the bucket.
   1. First, use a text editor to create a trust policy in a file
      `~/TrustPolicyForFirehose.json`.

   ```
   { "Statement": { "Effect": "Allow", "Principal": { "Service": "firehose.amazonaws.com" }, "Action": "sts:AssumeRole", "Condition": { "StringEquals": { "sts:ExternalId":"222222222222" } } } }
   ```

   2. Create the IAM role, specifying the trust policy file that
      you just made.

   ```
   aws iam create-role \
       --role-name FirehosetoS3Role \
       --assume-role-policy-document file://~/TrustPolicyForFirehose.json
   ```

   3. The output of this command will look similar to the following.
      Make a note of the role name and the role ARN.

   ```
   {
       "Role": {
           "Path": "/",
           "RoleName": "FirehosetoS3Role",
           "RoleId": "AROAR3BXASEKW7K635M53",
           "Arn": "arn:aws:iam::222222222222:role/FirehosetoS3Role",
           "CreateDate": "2021-02-02T07:53:10+00:00",
           "AssumeRolePolicyDocument": {
               "Statement": {
                   "Effect": "Allow",
                   "Principal": {
                       "Service": "firehose.amazonaws.com"
                   },
                   "Action": "sts:AssumeRole",
                   "Condition": {
                       "StringEquals": {
                           "sts:ExternalId": "222222222222"
                       }
                   }
               }
           }
       }
   }

   ```

3. Create a permissions policy to define the actions that Firehose can
   perform in your account.
   1. First, use a text editor to create the following permissions
      policy in a file named
      `~/PermissionsForFirehose.json`.
      Depending on your use case, you might need to add more
      permissions to this file.

   ```
   {
       "Statement": [{
           "Effect": "Allow",
           "Action": [
               "s3:PutObject",
               "s3:PutObjectAcl",
               "s3:ListBucket"
           ],
           "Resource": [
               "arn:aws:s3:::amzn-s3-demo-bucket",
               "arn:aws:s3:::amzn-s3-demo-bucket/*"
           ]
       }]
   }
   ```

   2. Enter the following command to associate the permissions
      policy that you just created with the IAM role.

   ```
   aws iam put-role-policy --role-name FirehosetoS3Role --policy-name Permissions-Policy-For-Firehose-To-S3 --policy-document file://~/PermissionsForFirehose.json
   ```

4. Enter the following command to create the Firehose delivery stream.
   Replace `my-role-arn` and
   `amzn-s3-demo-bucket2-arn` with the correct
   values for your deployment.

```
aws firehose create-delivery-stream \
   --delivery-stream-name 'my-delivery-stream' \
   --s3-destination-configuration \
  '{"RoleARN": "arn:aws:iam::222222222222:role/FirehosetoS3Role", "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket"}'

```

The output should look similar to the following:

```
{
    "DeliveryStreamARN": "arn:aws:firehose:us-east-1:222222222222:deliverystream/my-delivery-stream"
}
```
