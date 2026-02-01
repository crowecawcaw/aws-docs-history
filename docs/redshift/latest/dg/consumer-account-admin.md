Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Consumer account administrator

actions

With Amazon Redshift, you can manage consumer accounts and control their access to your
data warehousing resources.

**If you are a consumer account administrator**
– follow these steps:

To associate one or more datashares that are shared from other accounts with
your entire AWS account or specific namespaces in your account, use the Amazon Redshift
console.

Sign in to the [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/"). Then, associate one or more datashares that
are shared from other accounts with your entire AWS account or specific
namespaces in your account. For more information, see [Associating a datashare from a different
AWS account in Amazon Redshift](writes-associating.md "writes-associating.md").

After the AWS account or specific namespaces are associated, the datashares
become available for consumption. You can also change datashare association at any
time. When changing association from individual namespaces to an AWS account,
Amazon Redshift overwrites the namespaces with the AWS account information. When
changing association from an AWS account to specific namespaces, Amazon Redshift
overwrites the AWS account information with the namespace information. All
namespaces in the account get access to the data.
