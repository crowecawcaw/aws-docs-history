# Creating data grants on AWS Data Exchange

At a high level, this is how to create a data grant on AWS Data Exchange:

1. **Create an AWS account** – You must sign up for AWS
   and create a user before you can create data grants. For more information, see [Setting up AWS Data Exchange](setting-up.md "setting-up.md").
2. **Create a data set, a revision, and import assets** –
   You can create data sets through the AWS Data Exchange console or API. Then, you can create revisions in the
   data set, and add assets to that revision.
3. **Create a data grant** – To create a data grant, you
   must provide a data grant name and description, select the data set you wish to include in the
   data grant, specify the AWS account ID of the recipient you with to share the data grant with,
   and optionally set an end date on which the data grant should expire. For more information, see
   the following topics.
4. **Publish a new revision** – You can update dynamic data
   sets over time by creating a new revision using the AWS Data Exchange API or console. These revisions can
   then be published to active data grants.

###### Note

Before creating a data grant on AWS Data Exchange, review the information on [Setting up AWS Data Exchange](setting-up.md "setting-up.md").

The following topics explains more about how to publish a new data product on AWS Data Exchange.

###### Topics

- [Programmatic access](#programmatic-access "#programmatic-access")
- [Containing
  file-based data](creating-a-data-grant-file-based-data.md "creating-a-data-grant-file-based-data.md")
- [Containing
  APIs](creating-a-data-grant-api.md "creating-a-data-grant-api.md")
- [Containing Amazon Redshift data
  sets](data-grant-publish-Redshift-product.md "data-grant-publish-Redshift-product.md")
- [Containing Amazon S3 data
  access](data-grant-publish-s3-data-access-product.md "data-grant-publish-s3-data-access-product.md")
- [Containing AWS Lake Formation
  data permission data sets (Preview)](data-grant-publish-LF-data-product.md "data-grant-publish-LF-data-product.md")

## Programmatic access

AWS Data Exchange also offers programmatic access to its resources using the following API:

- **AWS Data Exchange API** – Use these API operations to create,
  view, update, and delete data sets and revisions. You can also use these API operations to
  import and export assets to and from those revisions. For more information, see the [AWS Data Exchange API Reference](../apireference/welcome.md "../apireference/welcome.md").
