Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Describing custom domain

associations

Use the commands in this section to get a list of custom domain names associated with
a specific provisioned cluster or with an Amazon Redshift Serverless workgroup.

You need the following permissions:

- For a provisioned cluster:
  `redshift:DescribeCustomDomainAssociations`
- For an Amazon Redshift Serverless workgroup:
  `redshiftServerless:ListCnameAssociations`
  As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
  needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

The following shows a sample command to list the custom domain names for a given Amazon Redshift
cluster:

```
aws redshift describe-custom-domain-associations ––custom-domain-name `customdomainname`
```

You can run this command when you have a custom domain name enabled to determine the
custom domain names associated with the cluster. For more information about the CLI
command for for describing custom domain associations, see [describe-custom-domain-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-custom-domain-associations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-custom-domain-associations.html").

Similarly, the following shows a sample command to list the custom domain names for a
given Amazon Redshift Serverless workgroup. There are a few different ways to do this. You can
provide only the custom domain name:

```
aws redshift-serverless list-custom-domain-associations ––custom-domain-name `customdomainname`
```

You can also get the associations by providing only the certificate ARN:

```
aws redshift-serverless list-custom-domain-associations ––custom-domain-certificate-arn `certificatearn`
```

You can run these commands when you have a custom domain name enabled to determine the
custom domain names associated with the workgroup. You can also run a command to get the
properties of a custom domain association. To do this, you must provide the custom
domain name and workgroup name as parameters. It returns the certificate ARN, the
workgroup name, and the custom domain's certificate expiration time:

```
aws redshift-serverless get-custom-domain-association ––workgroup-name `workgroupname` ––custom-domain-name `customdomainname`
```

For more information about CLI reference commands available for Amazon Redshift Serverless, see
[redshift-serverless](../../../cli/latest/reference/redshift-serverless.md "../../../cli/latest/reference/redshift-serverless.md").
