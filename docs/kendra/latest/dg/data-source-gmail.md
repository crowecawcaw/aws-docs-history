# Gmail

Gmail is email client developed by Google through which you can send email
messages with file attachments. Gmail messages can be sorted and stored inside
your email inbox using folders and labels. You can use Amazon Kendra to index your
email messages and message attachments. You can also configure Amazon Kendra to include
or exclude specific email messages, message attachments, and labels for indexing.

You can connect Amazon Kendra to your Gmail data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra Gmail data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-gmail "#supported-features-gmail")
- [Prerequisites](#prerequisites-gmail "#prerequisites-gmail")
- [Connection instructions](#data-source-procedure-gmail "#data-source-procedure-gmail")
- [Learn more](#gmail-learn-more "#gmail-learn-more")
- [Notes](#gmail-notes "#gmail-notes")

## Supported features

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Gmail data source,
make these changes in your Gmail and AWS accounts.

**In Gmail, make sure you have:**

- Created a Google Cloud Platform admin account and have created a Google Cloud
  project.
- Activated Gmail API and Admin SDK API in your admin
  account.
- Created a service account and downloaded a JSON private key for your
  Gmail. For information on how to create and access your private
  key, see Google Cloud documentation on how to [Create a
  service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating "https://cloud.google.com/iam/docs/keys-create-delete#creating") and [Service account credentials](https://cloud.google.com/iam/docs/service-account-creds#key-types "https://cloud.google.com/iam/docs/service-account-creds#key-types").
- Copied your admin account email, your service account email, and your private
  key to use as your authentication credentials.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Added the following Oauth scopes (using an admin role) for your user and the
  shared directories you want to index:
  - https://www.googleapis.com/auth/admin.directory.user.readonly
  - https://www.googleapis.com/auth/gmail.readonly

- Checked each document is unique in Gmail and across other
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

- Stored your Gmail authentication credentials in an
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
connect your Gmail data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Gmail data source you must provide
details of your Gmail credentials so that Amazon Kendra can access
your data. If you have not yet configured Gmail for Amazon Kendra, see
[Prerequisites](#prerequisites-gmail "#prerequisites-gmail").

Console
**To connect Amazon Kendra to
Gmail**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Gmail connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Gmail connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security** page,
    enter the following information:
    1. **Authorization**—Turn on or off access control list (ACL) information for your
       documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
       and groups can access. The ACL information is used to filter search results based on the user or
       their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
    2. In **Authentication** for
       **AWS
       Secrets Manager secret**—Choose
       an existing secret or create a new Secrets Manager
       secret to store your Gmail authentication
       credentials. If you choose to create a new secret an
       AWS
       Secrets Manager secret window opens.
       1. Enter following information in the
          **Create an AWS
          Secrets Manager secret
          window**:
          1. **Secret Name**—A
             name for your secret.
          2. **Client email**—The
             client email that you copied from your Google
             service account.
          3. **Admin account
             email**—The admin account email
             that you would like to use.
          4. **Private key**—The
             private key you copied from your Google service
             account.
          5. Save and add your secret.

    3. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
       so, you must add **Subnets** and **VPC security groups**.
    4. **IAM role**—Choose an existing IAM
       role or create a new IAM role to access your repository credentials and index content.

    ###### Note

    IAM roles used for indexes cannot be used for data sources. If you are unsure
    if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
    errors. 5. Choose **Next**.

7.  On the **Configure sync settings** page,
    enter the following information:
    1. For**Entity types**—Choose to
       sync message attachments.
    2. (Optional) For **Additional
       configuration**, enter the following
       information:
       1. **Date range**—Enter a
          date range to specify the start and end date of
          emails you want to crawl.
       2. **Email
          domains**—Include or exclude
          certain emails based on "to", "from", "cc" and "bcc"
          email domains.
       3. **Keywords in
          subjects**—Include or exclude
          emails based on keywords in their email subjects.

       ###### Note

       You can also choose to include any documents
       that match all the subject keywords you have
       entered. 4. **Labels**—Add regular
       expression patterns to include or exclude certain
       email labels. 5. **Attachments**—Add
       regular expression patterns to include or exclude
       certain email attachments.

    3. **Sync mode**—Choose how you want to update
       your index when your data source content changes. When you sync your
       data source with Amazon Kendra for the first time, all content
       is crawled and indexed by default. You must run a full sync of your
       data if your initial sync failed, even if you don't choose full sync
       as your sync mode option.
       - Full sync: Freshly index all content, replacing existing
         content each time your data source syncs with your index.
       - New, modified, deleted sync: Index only new, modified,
         and deleted content each time your data source syncs with
         your index. Amazon Kendra can use your data source's
         mechanism for tracking content changes and index content
         that changed since the last sync.

    ###### Important

    Because there is no API to update
    permanently deleted Gmail messages,
    new, modified, or deleted content
    sync:

        * Won't remove messages that were permanently
         deleted from Gmail from your Amazon Kendra
         index
        * Won't sync changes in Gmail email
         labelsTo sync your Gmail data source label changes

    and permanently deleted email messages to your
    Amazon Kendra index, you must run full crawls
    periodically. 4. In **Sync run schedule**, for
    **Frequency**—Choose how often
    to sync your data source content and update your index. 5. Choose **Next**.

8.  On the **Set field mappings** page, enter the
    following information:
    1. **Default data source
       fields**—Select from the Amazon Kendra generated
       default data source fields you want to map to your index.

    ###### Note

    Amazon Kendra Gmail data source
    connector does not support creating custom index
    fields due to API limitations. 2. Choose **Next**.

9.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
Gmail**

You must specify a JSON of the [data source
schema](ds-schemas.md#ds-gmail-schema "ds-schemas.md#ds-gmail-schema") using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API. You must
provide the following information:

- **Data
  source**—Specify the data source type as
  `GMAIL` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **Sync mode**—Specify
  how Amazon Kendra should update your index when your data source
  content changes. When you sync your data source with Amazon Kendra
  for the first time, all content is crawled and indexed by default.
  You must run a full sync of your data if your initial sync failed,
  even if you don't choose full sync as your sync mode option. You can
  choose between:
  - `FORCED_FULL_CRAWL` to freshly index all content,
    replacing existing content each time your data source syncs with
    your index.
  - `FULL_CRAWL` to index only new, modified, and deleted
    content each time your data source syncs with your index. Amazon Kendra
    can use your data source’s mechanism for tracking content changes and
    index content that changed since the last sync.

###### Important

Because there is no API to update permanently deleted
Gmail messages, new, modified, or deleted content sync:

    + Won't remove messages that were permanently
     deleted from Gmail from your Amazon Kendra
     index
    + Won't sync changes in Gmail email labelsTo sync your Gmail data source label changes and

permanently deleted email messages to your Amazon Kendra index, you must run full crawls periodically.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Gmail account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "adminAccountEmailId": "`service account email`",
    "clientEmailId": "`user account email`",
    "privateKey": "`private key`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Gmail connector and Amazon Kendra.
  For more information, see [IAM roles for Gmail
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion
  filters**—Specify whether to include
  or exclude certain "to", "from", "cc", "bcc" emails.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **User context filtering and access control**—Amazon Kendra
  crawls the access control list (ACL) for your documents,
  if you have an ACL for your documents. The ACL
  information is used to filter search results based on the user or their
  group access to documents. For more information, see [User context
  filtering](user-context-filter.md#datasource-context-filter "user-context-filter.md#datasource-context-filter").
- **Field mappings**—Choose to map your Gmail
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

###### Note

Amazon Kendra Gmail data source
connector does not support creating custom index fields due
to API limitations.

For a list of other important JSON keys to configure, see [Gmail template
schema](ds-schemas.md#ds-gmail-schema "ds-schemas.md#ds-gmail-schema").

## Learn more

To learn more about integrating Amazon Kendra with your Gmail data
source, see:

- [Perform intelligent search across emails in your Google workspace using the
  Gmail connector for Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/perform-intelligent-search-across-emails-in-your-google-workspace-using-the-gmail-connector-for-amazon-kendra/ "https://aws.amazon.com/blogs/machine-learning/perform-intelligent-search-across-emails-in-your-google-workspace-using-the-gmail-connector-for-amazon-kendra/").

## Notes

- Because there is no API to update permanently deleted Gmail messages, a
  `FULL_CRAWL`/**New, modified, or deleted content
  sync**:

      + Won’t remove messages that were permanently deleted from Gmail from
       your Amazon Kendra index
      + Won’t sync changes in Gmail email labels

  To sync your Gmail data source label changes and permanently deleted email
  messages to your Amazon Kendra index, you must run full crawls
  periodically.

- Amazon Kendra Gmail data source connector does not support
  creating custom index fields due to API limitations.
