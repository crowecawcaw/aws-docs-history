# Microsoft OneDrive connector

V1.0

Microsoft OneDrive is a cloud-based storage service that you can use to store,
share, and host your content. You can use Amazon Kendra to index your Microsoft
OneDrive data source.

###### Note

Support for OneDrive connector V1.0 / Microsft OneDrive API is
scheduled to end by June 2023. We recommend using OneDrive connector V2.0 /
TemplateConfiguration API.

For troubleshooting your Amazon Kendra OneDrive data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v1-onedrive "#supported-features-v1-onedrive")
- [Prerequisites](#prerequisites-v1-onedrive "#prerequisites-v1-onedrive")
- [Connection instructions](#data-source-v1-procedure-onedrive "#data-source-v1-procedure-onedrive")

## Supported features

- Field mappings
- Inclusion/exclusion filters

## Prerequisites

Before you can use Amazon Kendra to index your OneDrive data source, make
these changes in your OneDrive and AWS accounts.

**In your Azure Active Directory (AD), make sure you
have:**

- Created an Azure Active Directory (AD) application.
- Used the AD application ID to register a secret key for the application on the AD site.
  The secret key must contain the application ID and a secret key.
- Copied the AD domain of the organization.
- Added the following application permissions to your AD application on the Microsoft Graph
  option:
  - Read files in all site collections (File.Read.All)
  - Read all users' full profile (User.Read.All)
  - Read directory data (Directory.Read.All)
  - Read all groups (Group.Read.All)
  - Read items in all site collections (Site.Read.All)

- Copied the list of users whose documents must be indexed. You can choose to provide a
  list of user names, or you can provide the user names in a file stored in an Amazon S3. After you create the data source, you can:
  - Modify the list of users.
  - Change from a list of users to a list stored in an Amazon S3 bucket.
  - Change the Amazon S3 bucket location of a list of users. If you change the
    bucket location, you must also update the IAM role for the data source so
    that it has access to the bucket.

  ###### Note

  If you store the list of user names in an Amazon S3 bucket, the IAM policy for the data source must provide access to the bucket and access to the
  key that the bucket was encrypted with, if any.

- Checked each document is unique in OneDrive and across other
  data sources you plan to use for the same index. Each data source that you
  want to use for an index must not contain the same document across the data
  sources. Document IDs are global to an index and must be unique per index.

**In your AWS account, make sure you
have:**

- [Created
  an Amazon Kendra index](create-index.md "create-index.md") and, if using the API, noted the index
  ID.
- [Created an IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if
  using the API, noted the ARN of the IAM role.

###### Note

If you change your authentication type and credentials, you must
update your IAM role to access the correct AWS Secrets Manager secret ID.

- Stored your OneDrive authentication credentials in an
  AWS Secrets Manager secret and, if using the API, noted the ARN of the
  secret.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

If you don’t have an existing IAM role or secret, you can use the
console to create a new IAM role and Secrets Manager secret when you
connect your OneDrive data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your OneDrive data source you must provide
details of your OneDrive credentials so that Amazon Kendra can access your data.
If you have not yet configured OneDrive for Amazon Kendra see [Prerequisites](#prerequisites-v1-onedrive "#prerequisites-v1-onedrive").

Console
**To connect Amazon Kendra to OneDrive**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **OneDrive connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **OneDrive connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page, enter the following
   information:
   1. **OneDrive tenant ID**—Enter the OneDrive tenant ID without
      the protocol.
   2. **Type of authentication**—Choose between
      **New** and **Existing**.
   3. 1. If you choose **Existing**, select an existing secret for
         **Select secret**.
      2. If you choose **New**, enter following information in the
         **New AWS
         Secrets Manager secret** section:
         1. **Secret name**—A name for your secret. The prefix
            ‘AmazonKendra-OneDrive-’ is automatically added to your secret
            name.
         2. For **Application ID** and **Application
            password**—Enter the authentication credential values from your
            OneDrive account and then choose **Save authentication**.

   4. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 5. Choose **Next**.

7. On the **Configure sync settings** page, enter the following
   information:
   1. Choose between **List file** and **Names list**
      based on your use case.
      1. If you choose **List file**, enter the following
         information:
         1. **Select location**—Enter the path to your Amazon S3
            bucket.

         **Add user list file to Amazon S3**—Select to add
         your user list files to your Amazon S3 bucket.

         **User local group mappings**—Select to use local group
         mapping to filter your content.

      2. If you choose **Names list**, enter the following
         information:
         1. **User name**—Enter up to 10 user drives to index. To add
            more than 10 users, create a file that contains the names.

         **Add another**—Choose to add more users.

         **User local group mappings**—Select to use local group
         mapping to filter your content.

   2. For **Additional configurations**—Add regular expression
      patterns to include or exclude certain files. You can add up to 100 patterns.
   3. In **Sync run schedule**, for
      **Frequency**—Choose how often Amazon Kendra will sync with
      your data source.
   4. Choose **Next**.

8. On the **Set field mappings** page, enter the following
   information:
   1. For **Default data source fields** and **Additional
      suggested field mappings**—Select from the Amazon Kendra generated
      default data source fields you want to map to your index.
   2. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to
OneDrive**

You must specify the following using the [OneDriveConfiguration](../APIReference/API_OneDriveConfiguration.md "../APIReference/API_OneDriveConfiguration.md") API:

- **Tenant ID**—Specify the Azure Active Directory
  domain of the organization.
- **OneDrive Users**—Specify the list of user
  accounts whose documents should be indexed.
- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your OneDrive account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "username": "`OAuth client ID`",
    "password": "`client secret`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the OneDrive connector and Amazon Kendra.
  For more information, see [IAM roles for OneDrive
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Inclusion and exclusion filters**—Specify whether to
  include or exclude certain documents.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Field mappings**—Choose to map your OneDrive
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

- **User context filtering and access control**—Amazon Kendra
  crawls the access control list (ACL) for your documents,
  if you have an ACL for your documents. The ACL
  information is used to filter search results based on the user or their
  group access to documents. For more information, see [User context
  filtering](user-context-filter.md#datasource-context-filter "user-context-filter.md#datasource-context-filter").
