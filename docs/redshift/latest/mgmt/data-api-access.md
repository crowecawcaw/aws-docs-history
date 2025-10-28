Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Authorizing access to the Amazon Redshift Data API

To access the Data API, a user must be authorized. You can authorize a user to
access the Data API by adding a managed policy, which is a predefined AWS Identity and Access Management
(IAM) policy, to that user. As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md"). To see the permissions allowed and
denied by managed policies, see the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")).
