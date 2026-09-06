

# Enable requester pays Amazon S3 buckets in Athena for Spark
<a name="notebooks-spark-requester-pays"></a>

When an Amazon S3 bucket is configured as requester pays, the account of the user running the query is charged for data access and data transfer fees associated with the query. For more information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon S3 User Guide*.

In Athena for Spark, requester pays buckets are enabled per session, not per workgroup. At a high level, enabling requester pays buckets includes the following steps:

1. In the Amazon S3 console, enable requester pays on the properties for the bucket and add a bucket policy to specify access.

1. In the IAM console, create an IAM policy to allow access to the bucket, and then attach the policy to the IAM role that will be used to access the requester pays bucket.

1. In Athena for Spark, add a session property to enable the requester pays feature.

## Step 1: Enable requester pays on an Amazon S3 bucket and add a bucket policy
<a name="notebooks-spark-requester-pays-enable-requester-pays-on-an-amazon-s3-bucket"></a>

**To enable requester pays on an Amazon S3 bucket**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the list of buckets, choose the link for the bucket that you want to enable requester pays for.

1. On the bucket page, choose the **Properties** tab.

1. Scroll down to the **Requester pays** section, and then choose **Edit**.

1. On the **Edit requester pays** page, choose **Enable**, and then choose **Save changes**.

1. Choose the **Permissions** tab.

1. In the **Bucket policy** section, choose **Edit**.

1. On the **Edit bucket policy** page, apply the bucket policy that you want to the source bucket. The following example policy gives access to all AWS principals (`"AWS": "*"` ), but your access can be more granular. For example, you might want to specify only a specific IAM role in another account.

------
#### [ JSON ]

****  

   ```
   { "Version":"2012-10-17",		 	 	  "Statement": [ { "Sid": "Statement1", "Effect": "Allow",
       "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:root" },
       "Action": "s3:*", "Resource": [
           "arn:aws:s3:::{{111122223333}}-{{us-east-1}}-{{amzn-s3-demo-bucket}}",
           "arn:aws:s3:::{{555555555555}}-{{us-east-1}}-{{amzn-s3-demo-bucket}}/*"
       ] } ] }
   ```

------

## Step 2: Create an IAM policy and attach it to an IAM role
<a name="notebooks-spark-requester-pays-create-an-iam-policy-and-attach-it-to-an-iam-role"></a>

Next, you create an IAM policy to allow access to the bucket. Then you attach the policy to the role that will be used to access the requester pays bucket.

**To create an IAM policy for the requester pays bucket and attach the policy to a role**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the IAM console navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. Choose **JSON**.

1. In the **Policy editor**, add a policy like the following:

------
#### [ JSON ]

****  

   ```
   { "Version":"2012-10-17",		 	 	  "Statement": [ { "Action": [ "s3:*" ], "Effect": "Allow",
       "Resource": [
           "arn:aws:s3:::{{111122223333}}-{{us-east-1}}-{{amzn-s3-demo-bucket}}",
           "arn:aws:s3:::{{111122223333}}-{{us-east-1}}-{{amzn-s3-demo-bucket}}/*"
       ] } ] }
   ```

------

1. Choose **Next**.

1. On the **Review and create** page, enter a name for the policy and an optional description, and then choose **Create policy**.

1. In the navigation pane, choose **Roles**.

1. On the **Roles** page, find the role that you want to use, and then choose the role name link.

1. In the **Permissions policies** section, choose **Add permissions**, **Attach policies**.

1. In the **Other permissions policies** section, select the check box for the policy that you created, and then choose **Add permissions**.

## Step 3: Add an Athena for Spark session property
<a name="notebooks-spark-requester-pays-add-a-session-property"></a>

After you have configured the Amazon S3 bucket and associated permissions for requester pays, you can enable the feature in an Athena for Spark session.

**To enable requester pays buckets in an Athena for Spark session**

1. In the notebook editor, from the **Session** menu on the upper right, choose **Edit session**.

1. Expand **Spark properties**. 

1. Choose **Edit in JSON**. 

1. In the JSON text editor, enter the following:

   ```
   {
     "spark.hadoop.fs.s3.useRequesterPaysHeader":"true"
   }
   ```

1. Choose **Save**.