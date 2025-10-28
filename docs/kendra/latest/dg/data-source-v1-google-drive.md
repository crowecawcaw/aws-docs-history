# Google Drive connector

V1.0

Google Drive is a cloud-based file storage service. You can use Amazon Kendra to index documents and comments stored in shared drives, My Drives, and Shared with
me folders in your Google Drive data source. You can index Google Workspace
documents, as well as documents listed in [Types of documentation](index-document-types.md "index-document-types.md"). You
can also use inclusion and exclusion filters to index content by file name, file type,
and file path.

###### Note

Google Drive connector V1.0 / Google DriveConfiguration API ended in 2023. We recommend
migrating to or using Google Drive connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Google Drive data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v1-google-drive "#supported-features-v1-google-drive")
- [Prerequisites](#prerequisites-v1-google-drive "#prerequisites-v1-google-drive")
- [Connection
  instructions](#data-source-v1-procedure-google-drive "#data-source-v1-procedure-google-drive")
- [Learn more](#google-drive-learn-more "#google-drive-learn-more")

## Supported features

- Field mappings
- User access control
- Inclusion/exclusion filters

## Prerequisites

Before you can use Amazon Kendra to index your Google Drive data
source, make these changes in your Google Drive and AWS
accounts.

**In Google Drive, make sure you have:**

- **Either** been granted access by a super
  admin role **or** are a user with
  administrative privileges. You do not need a super admin role for yourself
  if you have been granted access by a super admin role.
- Created a service account with **Enable G Suite Domain-wide
  Delegation** activated and a JSON key as private key using the
  account.
- Copied your user account email and your service account email. When you
  connect to Amazon Kendra you enter your user account email as admin
  account email and your service account email as client email in your AWS Secrets Manager secret.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Added Admin SDK API and Google Drive API in your account.
- Added (or asked a user with a super admin role to add) the following
  permissions to your service account using a super admin role:
  - https://www.googleapis.com/auth/drive.readonly
  - https://www.googleapis.com/auth/drive.metadata.readonly
  - https://www.googleapis.com/auth/admin.directory.user.readonly
  - https://www.googleapis.com/auth/admin.directory.group.readonly

- Checked each document is unique in Google Drive and across other
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

- Stored your Google Drive authentication credentials in an
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
connect your Google Drive data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection

instructions

To connect Amazon Kendra to your Google Drive data source, you must
provide the necessary details of your Google Drive data source so that Amazon Kendra can access your data. If you have not yet configured
Google Drive for Amazon Kendra see [Prerequisites](#prerequisites-v1-google-drive "#prerequisites-v1-google-drive").

Console
**To connect Amazon Kendra to
Google Drive**

1. Sign in to the AWS Management Console and
   open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose
   **Indexes** and then choose the index
   you want to use from the list of indexes.

###### Note

You can choose to configure or edit your
**User access control** settings
under **Index settings**. 3. On the **Getting started** page, choose
**Add data source**. 4. On the **Add data source** page, choose
**Google Drive connector V1.0** ,
and then choose **Add connector**. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security**
   page, enter the following information:
   1. For **Type of
      authentication**—Choose between
      **Existing** and
      **New**. If you choose to use an
      existing secret, use **Select
      secret** to choose your secret.
   2. If you choose to create a new secret an AWS
      Secrets Manager secret option opens.
      1. Enter following information in the
         **Create an AWS
         Secrets Manager secret
         window**:
         1. **Secret name**—A
            name for your secret. The prefix
            ‘AmazonKendra-Google Drive-’ is
            automatically added to your secret name.
         2. For **Admin account
            email**, **Client
            email**, and **Private
            key**—Enter the authentication
            credential values you generated and downloaded
            from your Google Drive account.
         3. Choose **Save
            authentication**.

   3. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 4. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. **Exclude user
      accounts**—The Google Drive
      users you want to exclude from the index. You can
      add up to 100 user accounts.
   2. **Exclude shared
      drives**—The Google Drive
      shared drives you want to exclude from your index.
      You can add up to 100 shared drives.
   3. **Exclude file types
      drives**—The Google Drive file
      types you want to exclude from your index. You can
      also choose to edit MIME type selections.
   4. **Additional
      configurations**—Regular expression
      patterns to include or exclude certain content. You
      can add up to 100 patterns.
   5. **Frequency**—How often
      Amazon Kendra will sync with your data
      source.
   6. Choose **Next**.

8. On the **Set field mappings** page, enter
   the following information:
   1. For **GoogleDrive field name**
      and **Additional suggested field
      mappings**—Select from the Amazon Kendra generated default data source fields
      you want to map to your index.
   2. **Add field**—To add custom
      data source fields to create an index field name to
      map to and the field data type.
   3. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to
Google Drive**

You must specify the following using the [GoogleDriveConfiguration](../APIReference/API_GoogleDriveConfiguration.md "../APIReference/API_GoogleDriveConfiguration.md") API:

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Google Drive account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "clientAccount": "`service account email`",
    "adminAccount": "`user account email"`",
    "privateKey": "`private key`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Google Drive connector and Amazon Kendra.
  For more information, see [IAM roles for Google Drive
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Inclusion and exclusion
  filters**—By default Amazon Kendra
  indexes all documents in Google Drive. You can specify
  whether to include or exclude certain content in shared
  drives, user accounts, document MIME types, and files. If
  you choose to exclude user accounts, none of the files in
  the My Drive owned by the account are indexed. Files shared
  with the user are indexed unless the owner of the file is
  also excluded.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Field mappings**—Choose to map your Google Drive
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

## Learn more

To learn more about integrating Amazon Kendra with your Google Drive
data source, see:

- [Getting started with the Amazon Kendra Google Drive
  connector](https://aws.amazon.com/blogs/machine-learning/getting-started-with-the-amazon-kendra-google-drive-connector/ "https://aws.amazon.com/blogs/machine-learning/getting-started-with-the-amazon-kendra-google-drive-connector/")
