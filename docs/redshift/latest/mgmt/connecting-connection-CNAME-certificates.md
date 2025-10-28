Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Registering a domain

name

Setting up the custom domain name consists of a several tasks: These include
registering the domain name with your DNS provider and creating a certificate. After you
perform these pieces of work, you configure the custom domain name in the Amazon Redshift console,
or in the Amazon Redshift Serverless console, or configure it with AWS CLI commands.

You must have a registered internet domain name to configure a custom domain name in
Amazon Redshift. You can register an internet domain using Route 53, or using a third-party domain
registration provider. You complete these tasks outside of the Amazon Redshift console. A
registered domain is a prerequisite for completing the remaining procedures to create a
custom domain.

###### Note

If you're using a provisioned cluster, prior to performing the steps to configure
the custom domain name, it must be relocation enabled. For more information, see
[Relocating a cluster](managing-cluster-recovery.md "managing-cluster-recovery.md"). This step isn't required for
Amazon Redshift Serverless.

The custom domain name typically includes the root domain and a subdomain, like
`mycluster.example.com`. To configure it, perform the following
steps:

###### Create a DNS CNAME entry for your custom domain name

1.  Register a root domain, for example `example.com`. Optionally, you
    can use an existing domain. Your custom name can be limited by restrictions on
    particular characters, or other naming validation. For more information about
    registering a domain with Route 53, see [Registering a new
    domain](../../../Route53/latest/DeveloperGuide/domain-register.md "../../../Route53/latest/DeveloperGuide/domain-register.md").
2.  Add a DNS CNAME record that points your custom domain name to the Redshift
    endpoint for your cluster or workgroup. You can find the endpoint in the
    properties for the cluster or workgroup, in the Redshift console or in the
    Amazon Redshift Serverless console. Copy the **JDBC URL** that's
    available in the cluster or workgroup properties, under **General
    information**. The URLs appear like the following:

        * For an Amazon Redshift cluster:
         `redshift-cluster-sample.abc123456.us-east-1.redshift.amazonaws.com`
        * For an Amazon Redshift Serverless workgroup:
         `endpoint-name.012345678901.us-east-1-dev.redshift-serverless-dev.amazonaws.com`

    If the URL has a JDBC prefix, remove it.

###### Note

DNS records are subject to availability, because each name must be unique
and available for use within your organization.
**Limitations**

There are a couple restraints regarding creating CNAME records for a custom
domain:

- Creating multiple custom domain names for the same provisioned cluster or
  Amazon Redshift Serverless workgroup isn't supported. You can associate only one CNAME
  record.
- Associating a CNAME record with more than one cluster or workgroup isn't
  supported. The CNAME for each Redshift resource must be unique.
  After you register your domain and create the CNAME record, you select a new or
  existing certificate. You perform this step using AWS Certificate Manager:

We recommend that you create a [DNS validated certificate](../../../acm/latest/userguide/dns-renewal-validation.md "../../../acm/latest/userguide/dns-renewal-validation.md") that meets eligibility for managed renewal, which
is available with AWS Certificate Manager. Managed renewal means that ACM either renews your
certificates automatically or it sends you email notices when expiration is approaching.
For more information, see [Managed renewal
for ACM certificates](../../../acm/latest/userguide/managed-renewal.md "../../../acm/latest/userguide/managed-renewal.md").
