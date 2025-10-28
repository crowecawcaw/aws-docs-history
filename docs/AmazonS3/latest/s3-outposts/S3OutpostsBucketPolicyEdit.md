# Adding or editing a bucket policy for an

Amazon S3 on Outposts bucket

A bucket policy is a resource-based AWS Identity and Access Management (IAM) policy that you can use to grant
access permissions to your bucket and the objects in it. Only the bucket owner can
associate a policy with a bucket. The permissions attached to the bucket apply to
all of the objects in the bucket that are owned by the bucket owner. Bucket policies
are limited to 20 KB in size. For more information, see [Bucket policy](S3onOutposts.md#S3OutpostsBucketPolicies "S3onOutposts.md#S3OutpostsBucketPolicies").

The following topics show you how to update your Amazon S3 on Outposts bucket policy by using
the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS SDK for Java.

###### To create or edit a bucket policy

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Outposts
   buckets**.
3. Choose the Outposts bucket whose bucket policy you want to edit.
4. Choose the **Permissions** tab.
5. In the **Outposts bucket policy** section, to create or
   edit new policy, choose **Edit**.

You can now add or edit the S3 on Outposts bucket policy. For more
information, see [Setting up IAM with S3 on Outposts](S3OutpostsIAM.md "S3OutpostsIAM.md").
The following AWS CLI example puts a policy on an Outposts bucket.

1. Save the following bucket policy to a JSON file. In this example, the file
   is named `policy1.json`. Replace the
   `user input placeholders` with
   your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Id":"testBucketPolicy",
 "Statement":[
 {
 "Sid":"st1",
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::`123456789012`:root"
 },
 "Action":[
 "s3-outposts:GetObject",
 "s3-outposts:PutObject",
 "s3-outposts:DeleteObject",
 "s3-outposts:ListBucket"
 ],
 "Resource":"arn:aws:s3-outposts:`us-east-1`:`123456789012`:outpost/`op-01ac5d28a6a232904`/bucket/`amzn-s3-demo-bucket`"
 }
 ]
}`

```

2. Submit the JSON file as part of the `put-bucket-policy` CLI
   command. To run this command, replace the `user input
placeholders` with your own information.

```
aws s3control put-bucket-policy --account-id `123456789012` --bucket arn:aws:s3-outposts:`region`:`123456789012`:outpost/`op-01ac5d28a6a232904`/bucket/`example-outposts-bucket` --policy file://`policy1.json`
```

The following SDK for Java example puts a policy on an Outposts bucket.

```
import com.amazonaws.services.s3control.model.*;

public void putBucketPolicy(String bucketArn) {

    String policy = "{\"Version\":\"2012-10-17\",\"Id\":\"testBucketPolicy\",\"Statement\":[{\"Sid\":\"st1\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"" + AccountId+ "\"},\"Action\":\"s3-outposts:*\",\"Resource\":\"" + bucketArn + "\"}]}";

    PutBucketPolicyRequest reqPutBucketPolicy = new PutBucketPolicyRequest()
            .withAccountId(AccountId)
            .withBucket(bucketArn)
            .withPolicy(policy);

    PutBucketPolicyResult respPutBucketPolicy = s3ControlClient.putBucketPolicy(reqPutBucketPolicy);
    System.out.printf("PutBucketPolicy Response: %s%n", respPutBucketPolicy.toString());

}
```
