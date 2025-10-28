# ServiceNow connector V2.0

ServiceNow provides a cloud-based service management system to create and manage
organization-level workflows, such as IT services, ticketing systems, and support. You can use
Amazon Kendra to index your ServiceNow catalogs, knowledge articles, incidents, and
their attachments.

For troubleshooting your Amazon Kendra ServiceNow data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v2-servicenow "#supported-features-v2-servicenow")
- [Prerequisites](#prerequisites-v2-servicenow "#prerequisites-v2-servicenow")
- [Connection instructions](#data-source-procedure-v2-servicenow "#data-source-procedure-v2-servicenow")
- [Learn more](#servicenow-learn-more "#servicenow-learn-more")

## Supported features

Amazon Kendra ServiceNow data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- ServiceNow instance versions: Rome, Sandiego, Tokyo, Others
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your ServiceNow data source, make
these changes in your ServiceNow and AWS accounts.

**In ServiceNow, make sure you have:**

- Created a Personal or Enterprise Developer Instance and have a ServiceNow
  instance with an administrative role.
- Copied the host of your ServiceNow instance URL. The format for the host URL you
  enter is `your-domain.service-now.com`. You need your
  ServiceNow instance URL to connect to Amazon Kendra.
- Noted your basic authentication credentials of a user name and password to allow Amazon Kendra to connect to your ServiceNow instance.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- **Optional:** Configured OAuth 2.0 client credentials that
  can identify Amazon Kendra using a user name, password, and a generated client ID, and a
  client secret. See [ServiceNow documentation on OAuth 2.0 authentication](https://www.servicenow.com/docs/bundle/utah-platform-security/page/integrate/single-sign-on/concept/c_Authentication.html "https://www.servicenow.com/docs/bundle/utah-platform-security/page/integrate/single-sign-on/concept/c_Authentication.html") for more information.
- Added the following permissions:
  - kb_category
  - kb_knowledge
  - kb_knowledge_base
  - kb_uc_cannot_read_mtom
  - kb_uc_can_read_mtom
  - sc_catalog
  - sc_category
  - sc_cat_item
  - sys_attachment
  - sys_attachment_doc
  - sys_user_role

- Checked each document is unique in ServiceNow and across other
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

- Stored your ServiceNow authentication credentials in an
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
connect your ServiceNow data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your ServiceNow data source, you must provide the
necessary details of your ServiceNow data source so that Amazon Kendra can access
your data. If you have not yet configured ServiceNow for Amazon Kendra see [Prerequisites](#prerequisites-v2-servicenow "#prerequisites-v2-servicenow").

Console
**To connect Amazon Kendra to ServiceNow**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **ServiceNow connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **ServiceNow connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page, enter the following
   information:
   1. **ServiceNow host**—Enter the ServiceNow
      host URL. The format for the host URL you enter is
      `your-domain.service-now.com`.
   2. **ServiceNow version**—Select your
      ServiceNow instance version. You can select from Rome, Sandiego, Tokyo, or
      Others.
   3. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   4. **Authentication**—Choose between **Basic
      authentication** and **Oauth 2.0 authentication**.
   5. **AWS
      Secrets Manager secret**—Choose an existing secret or create a new
      Secrets Manager secret to store your ServiceNow authentication credentials.
      If you choose to create a new secret an AWS
      Secrets Manager secret window opens. Enter the following information in the
      window:
      1. **Secret name**—A name for your secret. The prefix
         ‘AmazonKendra-ServiceNow-’ is automatically added to your secret name.
      2. If using Basic Authentication—Enter the **Secret name**,
         **Username**, and **Password** for your
         ServiceNow account.

      If using OAuth2.0 Authentication—Enter the **Secret
      name**, **Username**, **Password**,
      **Client ID**, and **Client Secret** you created in
      your ServiceNow account. 3. Save and add your secret.

   6. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
      so, you must add **Subnets** and **VPC security groups**.
   7. **Identity crawler**—Specify whether to turn on
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
   8. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 9. Choose **Next**.

7. On the **Configure sync settings** page, enter the following
   information:
   1. For **Knowledge articles**, choose from the following options
      :
      - **Knowledge articles**—Choose to index knowledge
        articles.
      - **Knowledge article attachments**—Choose to index
        knowledge article attachments.
      - **Type of knowledge articles**—Choose between
        **Only public articles** and **Knowledge articles based on
        ServiceNow filter query** based on your use case. If you select
        **Include articles based on ServiceNow filter query**, you
        must enter a **Filter query** copied from your ServiceNow
        account. Example filter queries include:
        `workflow_state=draft^EQ`,
        `kb_knowledge_base=dfc19531bf2021003f07e2c1ac0739ab^text
ISNOTEMPTY^EQ`,
        `article_type=text^active=true^EQ`.

      ###### Important

      If you choose to crawl **Only public articles**, Amazon Kendra crawls only knowledge articles assigned a public access role in
      ServiceNow.
      - **Include articles based on short description
        filter**—Specify regular expression patterns to include or exclude
        specific articles.

   2. For **Service catalog items**:
      - **Service catalog items**—Choose to index service catalog
        items.
      - **Service catalog item attachments**—Choose to index
        service catalog item attachments.
      - **Active service catalog items**—Choose to index active
        service catalog items.
      - **Inactive service catalog items**—Choose to index
        inactive service catalog items.
      - **Filter query**—Choose to include service catalog items
        based on a filter defined in your ServiceNow instance. Example filter queries
        include:
        `short_descriptionLIKEAccess^category=2809952237b1300054b6a3549dbe5dd4^EQ`,
        `nameSTARTSWITHService^active=true^EQ`.
      - **Include service catalog items based on short description
        filter**—Specify a regex pattern to include specific catalog
        items.

   3. For **Incidents**:
      - **Incidents**—Choose to index service incidents.
      - **Incident attachments**—Choose to index incident
        attachments.
      - **Active incidents**—Choose to index active
        incidents.
      - **Inactive incidents**—Choose to index inactive
        incidents.
      - **Active incident type**—Choose between **All
        incidents**, **Open incidents**, **Open -
        unassigned incidents**, and **Resolved incidents**
        depending on your use case.
      - **Filter query**—Choose to include incidents based on a
        filter defined in your ServiceNow instance. Example filter queries include:
        `short_descriptionLIKETest^urgency=3^state=1^EQ`,
        `priority=2^category=software^EQ` .
      - **Include incidents based on short description
        filter**—Specify a regex pattern to include specific incidents.

   4. For **Additional configuration**:
      - **ACL information**—Access control lists for entities you
        have selected are included by default. Deselecting an access control list will make
        all files in that category public. ACL options are automatically deactivated for
        entities not selected. For public articles ACL is not applied.
      - For **Maximum file size** – Specify the file size limit
        in MBs that Amazon Kendra will crawl. Amazon Kendra will crawl only the files within the size limit
        you define. The default file size is 50MB. The maximum file size should be greater
        than 0MB and less than or equal to 50MB.
      - **Attachment regex patterns**—Add regular expression
        patterns to include or exclude certain attached files of catalogs, knowledge articles,
        and incidents. You can add up to 100 patterns.

   5. **Sync mode**—Choose how you want to update your index when
      your data source content changes. When you sync your data source with Amazon Kendra
      for the first time, all content is crawled and indexed by default. You must run a full
      sync of your data if your initial sync failed, even if you don't choose full sync as
      your sync mode option.
      - Full sync: Freshly index all content, replacing existing content each time your
        data source syncs with your index.
      - New, modified, deleted sync: Index only new, modified, and deleted content each
        time your data source syncs with your index. Amazon Kendra can use your data
        source's mechanism for tracking content changes and index content that changed since
        the last sync.

   6. In **Sync run schedule**, for
      **Frequency**—Choose how often to sync your data source content
      and update your index.
   7. Choose **Next**.

8. On the **Set field mappings** page, enter the following
   information:
   1. **Default field mappings**—Select from the Amazon Kendra generated default data source fields that you want to map to your index.
   2. **Add field**—To add custom data source fields to create an
      index field name to map to and the field data type.
   3. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to
ServiceNow**

You must specify a JSON of the [data source schema](ds-schemas.md "ds-schemas.md") using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the following information:

- **Data source**—Specify the data source type as
  `SERVICENOWV2` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON schema. Also specify the data source
  as `TEMPLATE` when you call the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md")
  API.
- **Host URL**—Specify the ServiceNow host
  instance version. For example,
  `your-domain.service-now.com`.
- **Authentication type**—Specify the type of
  authentication you use, whether `basicAuth` or `OAuth2` for your
  ServiceNow instance.
- **ServiceNow instance version**—Specify
  the ServiceNow instance you use, whether `Tokyo`,
  `Sandiego`, `Rome`, or `Others`.
- **Sync mode**—Specify how Amazon Kendra
  should update your index when your data source content changes. When you sync your data
  source with Amazon Kendra for the first time, all content is crawled and indexed by
  default. You must run a full sync of your data if your initial sync failed, even if you
  don't choose full sync as your sync mode option. You can choose between:
  - `FORCED_FULL_CRAWL` to freshly index all content, replacing existing
    content each time your data source syncs with your index.
  - `FULL_CRAWL` to index only new, modified, and deleted content each time
    your data source syncs with your index. Amazon Kendra can use your data source’s
    mechanism for tracking content changes and index content that changed since the last
    sync.

- **Secret Amazon Resource Name (ARN)**—Provide the
  Amazon Resource Name (ARN) of a Secrets Manager secret that contains the authentication
  credentials you created in your ServiceNow account.

If you use basic authentication, the secret is stored in a JSON structure with the
following keys:

```
{
    "username": "`user name`",
    "password": "`password`"
}
```

- If you use OAuth2 client credentials, the secret is stored in a JSON structure with
  the following keys:

```
{
    "username": "`user name`",
    "password": "`password`",
    "clientId": "`client id`",
    "clientSecret": "`client secret`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the ServiceNow connector and Amazon Kendra.
  For more information, see [IAM roles for ServiceNow
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion filters**—You can specify
  whether to include or exclude certain attached files using the file names and the file
  types of knowledge articles, service catalogs, and incidents.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Specific documents to index**—You can use a
  ServiceNow query to specify the documents you want from one or more knowledge
  bases, including private knowledge bases. Access to the knowledge bases is determined by
  the user that you use to connect to the ServiceNow instance. For more information,
  see [Specifying
  documents to index with a query](servicenow-query.md "servicenow-query.md").
- **Indexing parameters**—You can also choose to
  specify whether to:
  - Index knowledge articles, service catalogs, and incidents or all of these. If you
    choose to index knowledge articles, service catalog items and incidents, you must
    provide the name of the ServiceNow field that is mapped to the index document
    contents field in the Amazon Kendra index.
  - Index attachments to knowledge articles, service catalog items and
    incidents.
  - Include knowledge articles, service catalog items and incidents based on the
    `short description` filter pattern.
  - Choose to filter active and inactive service catalog items and incidents.
  - Choose to filter incidents based on incident type.
  - Choose which entities should have their ACL crawled.
  - You can use a ServiceNow query to specify the documents you want from one
    or more knowledge bases, including private knowledge bases. Access to the knowledge
    bases is determined by the user that you use to connect to the ServiceNow
    instance. For more information, see [Specifying documents to index with a
    query](servicenow-query.md "servicenow-query.md").

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
- **Field mappings**—Choose to map your ServiceNow
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [ServiceNow template
schema](ds-schemas.md#ds-servicenow-schema "ds-schemas.md#ds-servicenow-schema").

## Learn more

To learn more about integrating Amazon Kendra with your ServiceNow data
source, see:

- [Getting started with Amazon KendraAnnouncing the updated ServiceNow connector
  (V2) for Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/announcing-the-updated-servicenow-connector-v2-for-amazon-kendra/ "https://aws.amazon.com/blogs/machine-learning/announcing-the-updated-servicenow-connector-v2-for-amazon-kendra/")
