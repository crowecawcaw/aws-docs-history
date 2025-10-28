Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift

Integration with Amazon S3 Access Grants

Using integration with Amazon S3 Access Grants, you can seamlessly propagate
your IAM Identity Center identities to control access to Amazon S3 data. This integration lets you authorize Amazon S3 data
access based on IAM Identity Center users and groups.

For information about Amazon S3 Access Grants, see
[Managing access with S3 Access Grants](../../../AmazonS3/latest/userguide/access-grants.md "../../../AmazonS3/latest/userguide/access-grants.md").

Using Amazon S3 Access Grants gives your application the following benefits:

- Fine-grained access control to Amazon S3 data, based on IAM Identity Center identities.
- Centralized management of IAM Identity Center identities across Amazon Redshift and Amazon S3.
- You can avoid managing separate IAM permissions for Amazon S3 access.

## How it works

To integrate your application with Amazon S3 access grants, you do the following:

- First, you configure Amazon Redshift to integrate with Amazon S3 Access Grants using the AWS Management Console or AWS CLI.
- Next, a user with IdC administrator privileges grants Amazon S3 bucket or prefix
  access to specific IdC users/groups, using the Amazon S3 Access Grants service. For more information, see
  [Working with grants in S3 Access Grants](../../../AmazonS3/latest/userguide/access-grants-grant.md "../../../AmazonS3/latest/userguide/access-grants-grant.md").
- When an IdC user authenticated to Redshift runs a query accessing S3 (such as a
  COPY, UNLOAD, or Spectrum operation), Amazon Redshift retrieves temporary S3 access credentials scoped to that
  IdC identity from the Amazon S3 Access Grants service.
- Amazon Redshift then uses the retrieved temporary credentials to access the authorized
  Amazon S3 locations for that query.

## Setting up integration with Amazon S3 Access Grants

To set up integration with integration with Amazon S3 Access Grants for Amazon Redshift, do the following:

###### Topics

- [Setting up integration with Amazon S3 Access Grants
  using the AWS Management Console](#redshift-iam-access-control-sso-s3idc-setup-console "#redshift-iam-access-control-sso-s3idc-setup-console")
- [Enabling integration with Amazon S3 Access Grants
  using the AWS CLI](#redshift-iam-access-control-sso-s3idc-setup-cli "#redshift-iam-access-control-sso-s3idc-setup-cli")

### Setting up integration with Amazon S3 Access Grants

using the AWS Management Console

1. Open the Amazon Redshift console.
2. Choose your cluster from the **Clusters** pane.
3. In your cluster's details page, in the **Identity provider integration**
   section, enable integration with the **S3 Access Grants** service.

###### Note

The **Identity provider integration** section doesn't appear if you don't have
IAM Identity Center configured. For more information, see
[Enabling AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md").

### Enabling integration with Amazon S3 Access Grants

using the AWS CLI

1. To create a new Amazon Redshift IdC application with S3 integration enabled, do the following:

```
aws redshift create-redshift-idc-application <other parameters>
  --service-integrations '[ {"S3AccessGrants": [{"ReadWriteAccess": {"Authorization": "Enabled"}}]} ]'
```

2. To modify an existing application to enable S3 Access Grants integration, do the following:

```
aws redshift modify-redshift-idc-application <other parameters>
  --service-integrations '[ {"S3AccessGrants": [{"ReadWriteAccess": {"Authorization": "Enabled"}}]} ]'
```

3. To modify an existing application to disable S3 Access Grants integration, do the following:

```
aws redshift modify-redshift-idc-application <other parameters>
  --service-integrations '[ {"S3AccessGrants": [{"ReadWriteAccess": {"Authorization": "Disabled"}}]} ]'
```

## Using integration with S3 Access Grants

After you configure S3 Access Grants integration, queries that access S3 data (such as `COPY`,
`UNLOAD`, or Spectrum queries) use the IdC identity for authorization. Users who are not authenticated using
IdC can also run these queries, but those user accounts don't take advantage of the centralized administration that IdC provides.

The following example shows queries that
run with S3 Access Grants integration:

```
COPY table FROM 's3://mybucket/data';  // -- Redshift uses IdC identity
UNLOAD ('SELECT * FROM table') TO 's3://mybucket/unloaded/'    // -- Redshift uses IdC identity
```
