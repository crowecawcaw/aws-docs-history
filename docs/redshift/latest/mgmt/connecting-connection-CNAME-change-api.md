Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Associating a custom domain

with a different certificate

In order to change the certificate association for a custom domain name, the following
IAM permissions are required:

- `redshift:ModifyCustomDomainAssociation`
- `acm:DescribeCertificate`
  As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
  needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

Use the following command to associate the custom domain with a different certificate.
The `––custom-domain-name` and
`custom-domain-certificate-arn` arguments are mandatory. The ARN for the
new certificate must be different than the existing ARN.

```
aws redshift modify-custom-domain-association ––cluster-id `redshiftcluster` ––custom-domain-name `customdomainname` ––custom-domain-certificate-arn `certificatearn`
```

The following sample shows how to associate the custom domain with a different
certificate for an Amazon Redshift Serverless workgroup.

```
aws redshift-serverless modify-custom-domain-association ––workgroup-name `redshiftworkgroup` ––custom-domain-name `customdomainname` ––custom-domain-certificate-arn `certificatearn`
```

There is a maximum delay of 30 seconds before you can connect to the cluster. Part of
the delay occurs as the Amazon Redshift cluster updates its properties, and there is some
additional delay as DNS is updated. For more information about the API and each property
setting, see [ModifyCustomDomainAssociation](../APIReference/API_ModifyCustomDomainAssociation.md "../APIReference/API_ModifyCustomDomainAssociation.md").
