# Managing directory bucket policies

You can add, delete, update, and view bucket policies for Amazon S3 directory buckets by
using the Amazon S3 console, the AWS SDKs and the AWS CLI. For more information, see the
following topics. For more information about supported AWS Identity and Access Management (IAM) actions, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md"). For example
bucket policies for directory buckets, see [Example bucket
policies for directory buckets](s3-express-security-iam-example-bucket-policies.md "s3-express-security-iam-example-bucket-policies.md").

###### Topics

- [Adding a bucket policy](#directory-bucket-bucket-policy-add "#directory-bucket-bucket-policy-add")
- [Viewing a bucket policy](#directory-bucket-bucket-policy-view "#directory-bucket-bucket-policy-view")
- [Deleting a bucket policy](#directory-bucket-bucket-policy-delete "#directory-bucket-bucket-policy-delete")

## Adding a bucket policy

To add a bucket policy to a directory bucket, you can use the Amazon S3 console, the
AWS SDKs, or the AWS CLI.

###### To create or edit a bucket policy

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Directory buckets**.
3. In the **Directory buckets** list, choose the name of the bucket that you
   want to add a policy to.
4. Choose the **Permissions** tab.
5. Under **Bucket policy**, choose **Edit**. The
   **Edit bucket policy** page appears.
6. To generate a policy automatically, choose **Policy
   generator**.

If you choose **Policy generator**, the AWS Policy Generator opens
in a new window.

If you don't want to use the AWS Policy Generator, you can add or edit JSON
statements in the **Policy** section.

    1. On the **AWS Policy Generator** page, for **Select
     Type of Policy**, choose **S3 Bucket
     Policy**.
    2. Add a statement by entering the information in the provided fields, and then
     choose **Add Statement**. Repeat this step for as many
     statements as you want to add. For more information about these fields, see the
     [IAM JSON policy
     elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the *IAM User Guide*.


    ###### Note

    For your convenience, the **Edit bucket policy** page
     displays the **Bucket ARN**  (Amazon Resource Name) of the
     current bucket above the **Policy** text field. You can
     copy this ARN for use in the statements on the **AWS Policy
     Generator** page.
    3. After you finish adding statements, choose **Generate
     Policy**.
    4. Copy the generated policy text, choose **Close**, and return
     to the **Edit bucket policy** page in the Amazon S3 console.

7. In the **Policy** box, edit the existing policy or paste the
   bucket policy from the AWS Policy Generator. Make sure to resolve security
   warnings, errors, general warnings, and suggestions before you save your
   policy.

###### Note

Bucket policies are limited to 20 KB in size. 8. Choose **Save changes**, which returns you to the
**Permissions** tab.

SDK for Java 2.x`PutBucketPolicy` AWS SDK for Java 2.x

```
public static void setBucketPolicy(S3Client s3Client, String bucketName, String policyText) {

       //sample policy text
       /**
        * policy_statement = {
         *         'Version': '2012-10-17',
         *         'Statement': [
         *             {
         *                 'Sid': 'AdminPolicy',
         *                 'Effect': 'Allow',
         *                 'Principal': {
         *                     "AWS": "`111122223333`"
         *                 },
         *                 'Action': 's3express:*',
         *                 'Resource': 'arn:aws:s3express:`region`:`111122223333`:bucket/`bucket-base-name`--`zone-id`--x-s3'
         *             }
         *         ]
         *     }
         */
         System.out.println("Setting policy:");
         System.out.println("----");
         System.out.println(policyText);
         System.out.println("----");
         System.out.format("On Amazon S3 bucket: \"%s\"\n", bucketName);

         try {
             PutBucketPolicyRequest policyReq = PutBucketPolicyRequest.builder()
                     .bucket(bucketName)
                     .policy(policyText)
                     .build();
             s3Client.putBucketPolicy(policyReq);
             System.out.println("Done!");
         }

         catch (S3Exception e) {
             System.err.println(e.awsErrorDetails().errorMessage());
             System.exit(1);
         }
    }
```

This example shows how to add a bucket policy to a directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

```
aws s3api put-bucket-policy --bucket `bucket-base-name`--`zone-id`--x-s3 --policy file://bucket_policy.json
```

bucket_policy.json:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AdminPolicy",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`111122223333`"
 },
 "Action": "s3express*",
 "Resource": "arn:aws:s3express:us-west-2:`111122223333`:bucket/amzn-s3-demo-bucket--usw2-az1--x-s3"
 }
 ]
}`

```

For more information, see [put-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-policy.html") in the AWS Command Line Interface.

## Viewing a bucket policy

To view a bucket policy for a directory bucket, use the following
examples.

This example shows how to view the bucket policy attached to a
directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

```
aws s3api get-bucket-policy --bucket `bucket-base-name`--`zone-id`--x-s3
```

For more information, see [get-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy.html") in the AWS Command Line Interface.

## Deleting a bucket policy

To delete a bucket policy for a directory bucket, use the following
examples.

SDK for Java 2.x`DeleteBucketPolicy` AWS SDK for Java 2.x

```
public static void deleteBucketPolicy(S3Client s3Client, String bucketName) {
      try {
          DeleteBucketPolicyRequest deleteBucketPolicyRequest = DeleteBucketPolicyRequest
                  .builder()
                  .bucket(bucketName)
                  .build()
          s3Client.deleteBucketPolicy(deleteBucketPolicyRequest);
          System.out.println("Successfully deleted bucket policy");
      }

      catch (S3Exception e) {
          System.err.println(e.awsErrorDetails().errorMessage());
          System.exit(1);
      }
```

This example shows how to delete a bucket policy for a directory bucket by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

```
aws s3api delete-bucket-policy --bucket `bucket-base-name`--`zone-id`--x-s3
```

For more information, see [delete-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-policy.html") in the AWS Command Line Interface.
