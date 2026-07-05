Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Authorizing access to the Amazon Redshift Data API

To access the Data API, a user must be authorized. You can authorize a user to
access the Data API by adding a managed policy, which is a predefined AWS Identity and Access Management
(IAM) policy, to that user. As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md"). To see the permissions allowed and
denied by managed policies, see the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")).
