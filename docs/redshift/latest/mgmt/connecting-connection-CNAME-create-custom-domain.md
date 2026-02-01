Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring a custom

domain

You can use the Amazon Redshift or Amazon Redshift Serverless console to create your custom domain URL. If
you haven't configured it, the **Custom domain name** property appears
as a dash (**–**) under **General
information**. After you create your CNAME record and the certificate, you
associate the custom domain name for the cluster or workgroup.

In order to create a custom domain association, the following IAM permissions are
required:

- `redshift:CreateCustomDomainAssociation` – You can restrict
  permission to a specific cluster by adding its ARN.
- `redshiftServerless:CreateCustomDomainAssociation` – You can
  restrict permission to a specific workgroup by adding its ARN.
- `acm:DescribeCertificate`
  As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
  needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

You assign the custom domain name by performing the following steps.

1. Choose the cluster in the Redshift console, or the workgroup in the
   Amazon Redshift Serverless console, and choose **Create custom domain
   name** under the **Action** menu. A dialogue
   appears.
2. Enter the custom domain name.
3. Select the ARN from AWS Certificate Manager for the **ACM
   Certificate**. Confirm your changes. Per the guidance in the steps
   you took to create the certificate, we recommend that you choose a DNS validated
   certificate that's eligible for managed renewal through AWS Certificate Manager.
4. Verify in the cluster properties that the **Custom domain
   name** and **Custom domain certificate ARN** are
   populated with your entries. The **Custom domain certificate expiry
   date** is also listed.
   After the custom domain is configured, using `sslmode=verify-full` works
   only for the new, custom domain. It doesn't work for the default endpoint. But you can
   can still connect to the default endpoint by using other ssl modes, such as
   `sslmode=verify-ca`.

###### Note

As a point of reminder, [cluster relocation](managing-cluster-recovery.md "managing-cluster-recovery.md") isn't a prerequisite for configuring additional
Redshift networking features. You don't have to turn it on to enable the
following:

- **Connecting from a cross-account or cross-region VPC
  to Redshift** – You can connect from one AWS virtual
  private cloud (VPC) to another that contains a Redshift database. This
  makes it easier to manage, for example, client access from disparate
  accounts or VPCs, without having to provide local VPC access to identities
  connecting to the database. For more information, see [Connecting to Amazon Redshift Serverless from a Redshift VPC endpoint in
  another account or region](serverless-connecting.md#serverless-cross-vpc "serverless-connecting.md#serverless-cross-vpc").
- **Setting up a custom domain name** –
  You can create a custom domain name, as described in this topic, to make the
  endpoint name more relevant and simple.
