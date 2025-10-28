After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Accessing Amazon S3 Bucket from FinSpace notebook

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

An Amazon FinSpace environment can be configured to access your Amazon S3 buckets from FinSpace notebook.

###### Note

In order to setup access to an S3 bucket, you must be authorized to access the FinSpace page in AWS Management Console and make changes to bucket-level permissions in Amazon S3.

###### To find your infrastructure account number

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. On the FinSpace console, from the list of environments, choose the environment that you want to setup to access an S3 bucket. If there are no environments available, create one by following the steps listed in [Create an Amazon FinSpace environment](create-an-amazon-finspace-environment.md "create-an-amazon-finspace-environment.md").
3. On the environment page, copy and save the FinSpace infrastructure account name.

###### To setup access for FinSpace infrastructure account in S3 bucket policy

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket that you want to access from your FinSpace environment.
3. Set a bucket policy for the bucket with following json code. For example, if your bucket name is `example-bucket` and your FinSpace infrastructure account number is `123456789101` below would be the example
   policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "CrossAccountAccess",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789101:role/FinSpaceServiceRole"
 ]
 },
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::example-bucket/*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789101:role/FinSpaceServiceRole"
 ]
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::example-bucket"
 }
 ]
}`

```

Using the above policy, you should be able to access `example-bucket` from the Jupyter notebook of a FinSpace environment, which is associated with the FinSpace infrastructure account number `123456789101`.
