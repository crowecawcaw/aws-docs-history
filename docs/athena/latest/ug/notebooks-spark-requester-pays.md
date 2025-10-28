# Enable requester pays Amazon S3 buckets in Athena

for Spark

When an Amazon S3 bucket is configured as requester pays, the account of the user running the
query is charged for data access and data transfer fees associated with the query. For more
information, see [Using Requester Pays buckets
for storage transfers and usage](../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md") in the
_Amazon S3 User Guide_.

In Athena for Spark, requester pays buckets are enabled per session, not per workgroup. At
a high level, enabling requester pays buckets includes the following steps:

1. In the Amazon S3 console, enable requester pays on the properties for the bucket and
   add a bucket policy to specify access.
2. In the IAM console, create an IAM policy to allow access to the bucket, and
   then attach the policy to the IAM role that will be used to access the requester
   pays bucket.
3. In Athena for Spark, add a session property to enable the requester pays
   feature.

## Step 1: Enable requester pays on an Amazon S3 bucket and add a bucket policy

###### To enable requester pays on an Amazon S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the list of buckets, choose the link for the bucket that you want to enable
   requester pays for.
3. On the bucket page, choose the **Properties** tab.
4. Scroll down to the **Requester pays** section, and then
   choose **Edit**.
5. On the **Edit requester pays** page, choose
   **Enable**, and then choose **Save
   changes**.
6. Choose the **Permissions** tab.
7. In the **Bucket policy** section, choose
   **Edit**.
8. On the **Edit bucket policy** page, apply the bucket policy
   that you want to the source bucket. The following example policy gives access to
   all AWS principals (`"AWS": "*"` ), but your
   access can be more granular. For example, you might want to specify only a
   specific IAM role in another account.

JSON

```
`{ "Version":"2012-10-17", "Statement": [ { "Sid": "Statement1", "Effect": "Allow",
 "Principal": { "AWS": "arn:aws:iam::`111122223333`:root" },
 "Action": "s3:*", "Resource": [
 "arn:aws:s3:::`111122223333`-`us-east-1`-`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`555555555555`-`us-east-1`-`amzn-s3-demo-bucket`/*"
 ] } ] }`

```

## Step 2: Create an IAM policy and attach it to an IAM role

Next, you create an IAM policy to allow access to the bucket. Then you attach the
policy to the role that will be used to access the requester pays bucket.

###### To create an IAM policy for the requester pays bucket and attach the policy to

a role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the IAM console navigation pane, choose
   **Policies**.
3. Choose **Create policy**.
4. Choose **JSON**.
5. In the **Policy editor**, add a policy like the
   following:

JSON

```
`{ "Version":"2012-10-17", "Statement": [ { "Action": [ "s3:*" ], "Effect": "Allow",
 "Resource": [
 "arn:aws:s3:::`111122223333`-`us-east-1`-`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`111122223333`-`us-east-1`-`amzn-s3-demo-bucket`/*"
 ] } ] }`

```

6. Choose **Next**.
7. On the **Review and create** page, enter a name for the
   policy and an optional description, and then choose **Create
   policy**.
8. In the navigation pane, choose **Roles**.
9. On the **Roles** page, find the role that you want to use,
   and then choose the role name link.
10. In the **Permissions policies** section, choose **Add
    permissions**, **Attach policies**.
11. In the **Other permissions policies** section, select the
    check box for the policy that you created, and then choose **Add
    permissions**.

## Step 3: Add an

Athena for Spark session property

After you have configured the Amazon S3 bucket and associated permissions for requester
pays, you can enable the feature in an Athena for Spark session.

###### To enable requester pays buckets in an Athena for Spark session

1. In the notebook editor, from the **Session** menu on the upper
   right, choose **Edit session**.
2. Expand **Spark properties**.
3. Choose **Edit in JSON**.
4. In the JSON text editor, enter the following:

```
{
  "spark.hadoop.fs.s3.useRequesterPaysHeader":"true"
}
```

5. Choose **Save**.
