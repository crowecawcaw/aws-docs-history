# Google Drive connector V2.0

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

- [Supported features](#supported-features-v2-google-drive "#supported-features-v2-google-drive")
- [Prerequisites](#prerequisites-v2-google-drive "#prerequisites-v2-google-drive")
- [Connection
  instructions](#data-source-procedure-v2-google-drive "#data-source-procedure-v2-google-drive")
- [Notes](#google-drive-notes "#google-drive-notes")

## Supported features

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Google Drive data
source, make these changes in your Google Drive and AWS
accounts.

**In Google Drive, make sure you have:**

- **Either** been granted access by a super
  admin role **or** are a user with
  administrative privileges. You do not need a super admin role for yourself
  if you have been granted access by a super admin role.
- Configured Google Drive Service Account connection credentials
  containing your admin account email, client email (service account email),
  and private key. See [Google Cloud
  documentation on creating and deleting service account
  keys](https://cloud.google.com/iam/docs/keys-create-delete "https://cloud.google.com/iam/docs/keys-create-delete").

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Created a Google Cloud Service Account (an account with delegated
  authority to assume a user identity) with **Enable G Suite
  Domain-wide Delegation** activated for server-to-server
  authentication, and then generated a JSON private key using the
  account.

###### Note

The private key should be generated after the creation of the service
account.

- Added Admin SDK API and Google Drive API in your user
  account.
- **Optional:** Configured Google Drive
  OAuth 2.0 connection credentials containing client ID, client secret, and
  refresh token as connection credentials for a specific user. You need this
  to crawl individual account data. See [Google
  documentation on using OAuth 2.0 to access APIs](https://developers.google.com/identity/protocols/oauth2 "https://developers.google.com/identity/protocols/oauth2").
- Added (or asked a user with a super admin role to add) the following OAuth
  scopes to your service account using a super admin role. These API scopes
  are needed to crawl all documents, and access control (ACL) information for
  all users in a Google Workspace domain:
  - https://www.googleapis.com/auth/drive.readonly—View and
    download all your Google Drive files
  - https://www.googleapis.com/auth/drive.metadata.readonly—View
    metadata for files in your Google Drive
  - https://www.googleapis.com/auth/admin.directory.group.readonly—Scope
    for only retrieving group, group alias, and member information. This
    is needed for the Amazon Kendra Identity Crawler.
  - https://www.googleapis.com/auth/admin.directory.user.readonly—Scope
    for only retrieving users or user aliases. This is needed for
    listing users in the Amazon Kendra Identity Crawler and for
    setting ACLs.
  - https://www.googleapis.com/auth/cloud-platform—Scope for
    generating access token for fetching content of large
    Google Drive files.
  - https://www.googleapis.com/auth/forms.body.readonly—Scope
    for fetching data from Google Forms.
    **To support the Forms API, add the following
    additonal scope:**

  - https://www.googleapis.com/auth/forms.body.readonly

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
Google Drive for Amazon Kendra see [Prerequisites](#prerequisites-v2-google-drive "#prerequisites-v2-google-drive").

Console
**To connect Amazon Kendra to
Google Drive**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Google Drive connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Google Drive connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security**
    page, enter the following information:
    1. **Authorization**—Turn on or off access control list (ACL) information for your
       documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
       and groups can access. The ACL information is used to filter search results based on the user or
       their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
    2. For
       **Authentication**—Choose
       between **Google service account**
       and **OAuth 2.0 authentication**
       based on your use case.
    3. **AWS
       Secrets Manager secret**—Choose
       an existing secret, or create a new Secrets Manager secret to store your Google Drive
       authentication credentials. If you choose to create
       a new secret an AWS
       Secrets Manager secret window opens.
       1. If you chose **Google service
          account**, enter a name for your secret,
          the email ID of the admin user or "Service Account
          User" in your service account configuration (admin
          email), the email ID of the service account
          (client email), and the private key that you
          created in your service account.

       Save and add your secret 2. If you chose **OAuth 2.0
       authentication**, enter a name for your
       secret, client ID, client secret, and refresh
       token that you created in your OAuth account. The
       user mail id (user whose connection details are
       configured) will be set as ACL. The connector
       doesn't set other user/group principal info as ACL
       due to API limitations.

       Save and add your secret.

    4. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
       so, you must add **Subnets** and **VPC security groups**.
    5. (For Google service account authentication users
       only)

    **Identity crawler**—Specify whether to turn on
    Amazon Kendra’s identity crawler. The identity crawler uses the access control list
    (ACL) information for your documents to filter search results based on the user or their
    group access to documents. If you have an ACL for your documents and choose to use your ACL,
    you can then also choose to turn on Amazon Kendra’s identity crawler to configure
    [user
    context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") of search results. Otherwise, if identity crawler is turned off,
    all documents can be publicly searched. If you want to use access control for your documents
    and identity crawler is turned off, you can alternatively use the
    [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
    API to upload user and group access information for user context filtering. 6. **IAM role**—Choose an existing IAM
    role or create a new IAM role to access your repository credentials and index content.

    ###### Note

    IAM roles used for indexes cannot be used for data sources. If you are unsure
    if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
    errors. 7. Choose **Next**.

7.  On the **Configure sync settings** page,
    enter the following information:
    1.  **Sync contents**—Select
        which options or the content that you want to crawl.
        You can choose to crawl My Drive (personal folders),
        Shared Drive (folders shared with you), or both. You
        can also include file comments.
    2.  In **Additional configuration -
        optional** You can also enter the
        following optional information:
        1. **Maximum file
           size**—Set the maximum size limit
           in MBs of files to crawl.
        2. **User email**—Add
           user emails that you want to include or
           exclude.
        3. **Shared
           drives**—Add the shared drive
           names that you want to include or exclude.
        4. **Mime types**—Add
           MIME types that you want to include or
           exclude.
        5. **Entity regex
           patterns**—Add regular expression
           patterns to include or exclude certain attachments
           for all supported entities. You can add up to 100
           patterns.

        You can configure include/exclude regex
        patterns for **File name**,
        **File type**, and **File
        path**.

            * **File name** – The
             name of the file to include or exclude. For
             example, to index a file with name
             `teamroster.txt`, provide
             `teamroster`.
            * **File type** – The
             type of the file to include or exclude. For
             example, .pdf .txt .docx.
            * **File path** – The
             path of the file to include or exclude. For
             example, to index files only inside the folder
             `Products list` of a drive, provide
             `/Products list`.

    3.  **Sync mode**—Choose how
        you want to update your index when your data source
        content changes. When you sync your data source with
        Amazon Kendra for the first time, all content
        is crawled and indexed by default. You must run a
        full sync of your data if your initial sync failed,
        even if you don't choose full sync as your sync mode
        option.
        - Full sync: Freshly index all content,
          replacing existing content each time your data
          source syncs with your index.
        - New, modified sync: Index only new and
          modified content each time your data source syncs
          with your index. Amazon Kendra can use your
          data source's mechanism for tracking content
          changes and index content that changed since the
          last sync.
        - New, modified, deleted sync: Index only new,
          modified, and deleted content each time your data
          source syncs with your index. Amazon Kendra
          can use your data source's mechanism for tracking
          content changes and index content that changed
          since the last sync.

    ###### Important

    Google Drive API does not support retrieving
    comments from a permanently deleted file. Comments
    from trashed files are retrievable. When a file is
    trashed, the connector will delete comments from
    the Amazon Kendra index. 4. In **Sync run schedule**, for
    **Frequency**—choose how
    often to sync your data source content and update
    your index. 5. In **Sync run history**, choose
    to store auto-generated reports in an Amazon S3 when syncing your data source. This is
    useful for tracking issues when sycning your data
    source. 6. Choose **Next**.

8.  On the **Set field mappings** page, enter
    the following information:
    1. For **Files**—Select from
       the Amazon Kendra generated default data source
       fields that you want to map to your index.

    ###### Note

    Google Drive API does not support creating
    custom fields. Custom field mapping is not
    available for the Google Drive connector. 2. Choose **Next**.

9.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
Google Drive**

You must specify a JSON of the [data source
schema](ds-schemas.md "ds-schemas.md") using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the
following information:

- **Data
  source**—Specify the data source type as
  `GOOGLEDRIVEV2` when you
  use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **Authentication
  type**—Specify whether to use service
  account authentication or OAuth 2.0 authentication.
- **Sync mode**—Specify
  how Amazon Kendra should update your index when your
  data source content changes. When you sync your data source
  with Amazon Kendra for the first time, all content is
  crawled and indexed by default. You must run a full sync of
  your data if your initial sync failed, even if you don't
  choose full sync as your sync mode option. You can choose
  between:
  - `FORCED_FULL_CRAWL` to freshly index
    all content, replacing existing content each time
    your data source syncs with your index.
  - `FULL_CRAWL` to index only new,
    modified, and deleted content each time your data
    source syncs with your index. Amazon Kendra can
    use your data source’s mechanism for tracking
    content changes and index content that changed since
    the last sync.
  - `CHANGE_LOG` to index only new and
    modified content each time your data source syncs
    with your index. Amazon Kendra can use your
    data source’s mechanism for tracking content changes
    and index content that changed since the last
    sync.

###### Important

Google Drive API does not support retrieving comments
from a permanently deleted file. Comments from trashed
files are retrievable. When a file is trashed, the
connector will delete comments from the Amazon Kendra index.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource Name
  (ARN) of a Secrets Manager secret that contains the
  authentication credentials you created in your
  Google Drive account. If you use Google service
  account authentication, the secret is stored in a JSON
  structure with the following keys:

```
{
    "clientEmail": "`user account email`",
    "adminAccountEmail": "`service account email`",
    "privateKey": "`private key`"
}
```

If you use OAuth 2.0 authentication, the secret is stored
in a JSON structure with the following keys:

```
{
    "clientID": "`OAuth client ID`",
    "clientSecret": "`client secret`",
    "refreshToken": "`refresh token`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Google Drive connector and Amazon Kendra.
  For more information, see [IAM roles for Google Drive
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **My Drives, Shared Drives,
  Comments**—You can specify whether to
  crawl these types of content.
- **Inclusion and exclusion
  filters**—You can specify whether to
  include or exclude certain user accounts, shared drives, and
  MIME types.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Access control list (ACL)**—Specify
  whether to crawl ACL information for your documents, if you have an
  ACL and want to use it for access control. The ACL specifies which
  documents that users and groups can access. The ACL
  information is used to filter search results based on the user or
  their group access to documents. For more information, see
  [User
  context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
- **Identity crawler**—Specify whether to turn on
  Amazon Kendra’s identity crawler. The identity crawler uses the access control list
  (ACL) information for your documents to filter search results based on the user or their
  group access to documents. If you have an ACL for your documents and choose to use your ACL,
  you can then also choose to turn on Amazon Kendra’s identity crawler to configure
  [user
  context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") of search results. Otherwise, if identity crawler is turned off,
  all documents can be publicly searched. If you want to use access control for your documents
  and identity crawler is turned off, you can alternatively use the
  [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
  API to upload user and group access information for user context filtering.
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

For a list of other important JSON keys to configure, see [Google Drive template schema](ds-schemas.md#ds-google-drive-schema "ds-schemas.md#ds-google-drive-schema").

## Notes

- Custom field mapping is not available for Google Drive connector as
  the Google Drive UI does not support creating custom fields.
- Google Drive API does not support retrieving comments from a
  permamently deleted file. Comments are retrievable, however, for trashed
  files. When a file is trashed, the Amazon Kendra connector will delete
  comments from the Amazon Kendra index.
- Google Drive API does not return comments present in a .docx
  file.
- If permission for a particular Google document (document,
  spreadsheet, slide, etc) is set to **General access: Anyone with the
  link** or **Shared to your specific company
  domain**, the document will not be visible to Amazon Kendra search
  users until the user making the query has accessed the document.
