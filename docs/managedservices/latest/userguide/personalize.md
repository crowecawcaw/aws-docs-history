# Use AMS SSP to provision Amazon Personalize in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Personalize capabilities directly in your AMS managed account. Amazon Personalize is a machine learning service that makes it easy for developers to create individualized
recommendations for customers using their applications.

Machine learning is being increasingly used to improve customer engagement by powering personalized
product and content recommendations, tailored search results, and targeted marketing promotions.
However, developing the machine-learning capabilities necessary to produce these sophisticated
recommendation systems has been beyond the reach of most organizations today due to the complexity.
Amazon Personalize allows developers with no prior machine learning experience to easily build
sophisticated personalization capabilities into their applications, using machine learning
technology perfected from years of use on Amazon.com.

With Amazon Personalize, you provide an activity stream from your application – clicks, page views,
signups, purchases, and so forth – as well as an inventory of the items you want to recommend, such
as articles, products, videos, or music. You can also choose to provide Amazon Personalize with additional
demographic information from your users such as age, or geographic location. Amazon Personalize will
process and examine the data, identify what is meaningful, select the right algorithms, and train and
optimize a personalization model that is customized for your data. All data analyzed by Amazon Personalize
is kept private and secure, and only used for your customized recommendations. You can start serving
personalized recommendations via a simple API call. You pay only for what you use, and there are no
minimum fees and no upfront commitments.

To learn more, see [Amazon Personalize](https://aws.amazon.com/personalize/ "https://aws.amazon.com/personalize/").

## Amazon Personalize in AWS Managed Services FAQ

**Q: How do I request access to Amazon Personalize in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type,
and you need to specify which S3 bucket contains the data to be used by AWS personalize to
generate the recommendations.
This RFC provisions the following IAM roles to your account:
`customer_personalize_console_role` and `customer_personalize_service_role`.

- Once the `customer_personalize_console_role` is provisioned in your account,
  you must onboard the role in your federation solution. You can also attach the
  `customer_personalize_console_policy` to another existing role other than
  `Customer_ReadOnly_Role`.
- After the `customer_personalize_service_role` is provided to your account,
  then you can refer its ARN when creating a new dataset group.

At this time, AMS Operations will also deploy this service role in your account:
`aws_code_pipeline_service_role_policy`.

**Q: What are the restrictions to using Amazon Personalize in my AMS account?**

Amazon Personalize configuration is limited to resources without 'ams-' or 'mc-' prefixes, to prevent
any modifications to AMS infrastructure.

**Q: What are the prerequisites or dependencies to using Amazon Personalize in my AMS account?**

- If the S3 bucket where data is stored is encrypted, the KMS key ID must be provided,
  so we can allow the role used by Amazon Personalize to decrypt the bucket.

Amazon Personalize does not support the default KMS S3 key. If required to use KMS, create a custom key
and add the following policy to it by opening an RFC with change type
KMS Key | Create (Managed automation):

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-consolepolicy-3",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "Service": "personalize.amazonaws.com"
 },
 "Action": "kms:*",
 "Resource": "*"
 }
 ]
}`

```

- An S3 bucket must be created with the following bucket policy. Do this by submitting
  an RFC with change type S3 Storage | Create Policy. This policy allows Amazon Personalize to access data;
  that bucket will contain the data to be used by Amazon Personalize.

JSON

```
`{
"Version":"2012-10-17",
"Id": "PersonalizeS3BucketAccessPolicy",
"Statement": [
{
"Sid": "PersonalizeS3BucketAccessPolicy",
"Effect": "Allow",
"Principal": {
"Service": "personalize.amazonaws.com"
},
"Action": [
"s3:GetObject",
"s3:ListBucket"
],
"Resource": [
"arn:aws:s3:::bucket-name",
"arn:aws:s3:::bucket-name/*"
]
}
]
}`

```
