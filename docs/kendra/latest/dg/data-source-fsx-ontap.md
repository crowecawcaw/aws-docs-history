# Amazon FSx (NetApp ONTAP)

Amazon FSx (NetApp ONTAP) is a fully managed, cloud based file server system that offers shared
storage capabilities. If you're an Amazon FSx (NetApp ONTAP) user, you can use Amazon Kendra
to index your Amazon FSx (NetApp ONTAP) data source.

You can connect Amazon Kendra to your Amazon FSx (NetApp ONTAP) data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/"), or the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra Amazon FSx (NetApp ONTAP) data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-fsx-ontap "#supported-features-fsx-ontap")
- [Prerequisites](#prerequisites-fsx-ontap "#prerequisites-fsx-ontap")
- [Connection instructions](#data-source-procedure-fsx-ontap "#data-source-procedure-fsx-ontap")

## Supported features

Amazon Kendra Amazon FSx (NetApp ONTAP) data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion and exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Amazon FSx (NetApp ONTAP) data source,
check the details of your Amazon FSx (NetApp ONTAP) and AWS accounts.

**For Amazon FSx (NetApp ONTAP), make sure you have**:

- Set up Amazon FSx (NetApp ONTAP) with read and mounting permissions.
- Noted your file system ID. You can find your file system ID on the File
  Systems dashboard in the Amazon FSx (NetApp ONTAP) console.
- Noted the storage virtual machine (SVM) ID used with your file system. You can
  find your SVM ID by going to the File Systems dashboard in the
  Amazon FSx (NetApp ONTAP) console, selecting your file system ID, and then selecting
  **Storage virtual machines**.
- Configured a virtual private cloud using Amazon VPC where your
  Amazon FSx (NetApp ONTAP) file system resides.
- Noted your Amazon FSx (NetApp ONTAP) authentication credentials for an Active
  Directory user account. This includes your Active Directory user
  name with your DNS domain name (for example,
  *user@corp.example.com*) and password. If you use the
  Network File System (NFS) protocol for your Amazon FSx (NetApp ONTAP) file system, the
  authentication credentials include a left ID, right ID, and pre-shared
  key.

###### Note

Use only the necessary credentials required for the connector to function.
Do not use privileged credentials like domain admin.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Checked each document is unique in Amazon FSx (NetApp ONTAP) and across other
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

- Stored your Amazon FSx (NetApp ONTAP) authentication credentials in an
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
connect your Amazon FSx (NetApp ONTAP) data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Amazon FSx (NetApp ONTAP) data source, you must provide
the necessary details of your Amazon FSx (NetApp ONTAP) data source so that Amazon Kendra can access
your data. If you have not yet configured Amazon FSx (NetApp ONTAP) for Amazon Kendra,
see [Prerequisites](#prerequisites-fsx-ontap "#prerequisites-fsx-ontap").

Console
**To connect Amazon Kendra to your
Amazon FSx (NetApp ONTAP) file system**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Amazon FSx (NetApp ONTAP) connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Amazon FSx (NetApp ONTAP) connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. **Source**—Provide your file
      system information.
      - **File system
        protocol**—Choose the protocol of
        your Amazon FSx (NetApp ONTAP) file system. You can
        choose either Common Internet File System (CIFS)
        protocol, or the Network File System
        (NFS) protocol for Linux.
      - **Amazon FSx (NetApp ONTAP) file system
        ID**—Select from the dropdown your
        existing file system ID, fetched from
        Amazon FSx (NetApp ONTAP). Or, create an [Amazon FSx (NetApp ONTAP) file
        system](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/"). You can find your file system ID
        on the File Systems dashboard in the
        Amazon FSx (NetApp ONTAP) console.
      - **SVM ID**
        (Amazon FSx (NetApp ONTAP) for NetApp
        ONTAP only)—Provide the storage
        virtual machine (SVM) ID of your
        Amazon FSx (NetApp ONTAP) NetApp ONTAP.
        You can find your SVM ID by going to the File
        Systems dashboard in the Amazon FSx (NetApp ONTAP)
        console, selecting your file system ID, and
        selecting **Storage virtual
        machines**.

   2. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   3. **Authentication**—Choose an
      existing AWS Secrets Manager secret, or create a new
      secret to store your file system credentials. If you
      choose to create a new secret, an AWS Secrets Manager
      secret window opens.

   Provide a secret that stores your authentication
   credentials of your user name and password. The user
   name must include your DNS domain name. For example,
   *user@corp.example.com*.

   If you use the NFS protocol for your
   Amazon FSx (NetApp ONTAP) file system, provide a secret that
   stores your authentication credentials of left ID, right
   ID, and pre-shared key.

   Save and add your secret. 4. **Virtual Private Cloud
   (VPC)**—You must select an Amazon VPC where your Amazon FSx (NetApp ONTAP) resides.
   You include the VPC subnet and security groups. See
   [Configuring an Amazon VPC](vpc-configuration.md "vpc-configuration.md"). 5. **IAM role**—Choose an existing IAM
   role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 6. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. **Sync scope, Regex patterns**—Add regular
      expression patterns to include or exclude certain files.
   2. **Sync mode**—Choose how you want to update
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

   3. **Sync run schedule**—For
      **Frequency**, choose how often
      to sync your data source content and update your index.
   4. Choose **Next**.

8. On the **Set field mappings** page, enter the
   following information:
   1. Select from the Amazon Kendra generated default
      fields of your files that you want to map to your index.
      To add custom data source fields, create an index field
      name to map to and the field data type.
   2. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to your
Amazon FSx (NetApp ONTAP) file system**

You must specify a JSON of the [data source
schema](ds-schemas.md#ds-fsx-ontap-schema "ds-schemas.md#ds-fsx-ontap-schema") using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API. You must
provide the following information:

- **Data
  source**—Specify the data source type as
  `FSXONTAP` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **File system ID**—The
  identifier of the Amazon FSx (NetApp ONTAP) file system. You can find
  your file system ID on the File Systems dashboard in the
  Amazon FSx (NetApp ONTAP) console.
- **SVM ID**—The storage
  virtual machine (SVM) ID used with your file system. You can
  find your SVM ID by going to the File Systems dashboard in the
  Amazon FSx (NetApp ONTAP) console, selecting your file system ID, and
  then selecting **Storage virtual
  machines**.
- **Protocol type**—Specify
  whether you use the Common Internet File System (CIFS) protocol,
  or the Network File System (NFS) protocol for
  Linux.
- **File system
  type**—Specify the type of file system as either
  `FSXONTAP`.
- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").

###### Note

You must select an Amazon VPC
where your Amazon FSx (NetApp ONTAP) resides. You include the VPC
subnet and security groups.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Amazon FSx (NetApp ONTAP) account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "username": "`user@corp.example.com`",
    "password": "`password`"
}
```

If you use the NFS protocol for your Amazon FSx (NetApp ONTAP) file
system, the secret is stored in a JSON structure with the
following keys:

```
{
    "leftId": "`left ID`",
    "rightId": "`right ID`",
    "preSharedKey": "`pre-shared key`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Amazon FSx (NetApp ONTAP) connector and Amazon Kendra.
  For more information, see [IAM roles for Amazon FSx (NetApp ONTAP)
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

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

- **Inclusion and exclusion
  filters**—Specify whether to include or
  exclude certain files.

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

###### Note

To test user context filtering on a user, you must include
the DNS domain name as part of the user name when you issue
the query. You must have administrative permissions of the
Active Directory domain. You can also test user context
filtering on a group name.

- **Field mappings**—Choose to map your Amazon FSx (NetApp ONTAP)
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Amazon FSx (NetApp ONTAP) template schema](ds-schemas.md#ds-fsx-ontap-schema "ds-schemas.md#ds-fsx-ontap-schema").
