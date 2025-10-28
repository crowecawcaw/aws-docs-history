# ServiceNow connector V1.0

ServiceNow provides a cloud-based service management system to create and manage
organization-level workflows, such as IT services, ticketing systems, and support. You can use
Amazon Kendra to index your ServiceNow catalogs, knowledge articles, and their
attachments.

###### Note

ServiceNow connector V1.0 / ServiceNowConfiguration API ended in 2023. We recommend
migrating to or using ServiceNow connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra ServiceNow data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v1-servicenow "#supported-features-v1-servicenow")
- [Prerequisites](#prerequisites-v1-servicenow "#prerequisites-v1-servicenow")
- [Connection instructions](#data-source-procedure-v1-servicenow "#data-source-procedure-v1-servicenow")
- [Learn more](#servicenow-v1-learn-more "#servicenow-v1-learn-more")

## Supported features

Amazon Kendra ServiceNow data source connector supports the following
features:

- ServiceNow instance versions: London, Others
- Inclusion/exclusion patterns: Service catalogs, knowledge articles, and their
  attachments

## Prerequisites

Before you can use Amazon Kendra to index your ServiceNow data source, make
these changes in your ServiceNow and AWS accounts.

**In ServiceNow, make sure you have:**

- Created a ServiceNow administrator account and have created a ServiceNow
  instance.
- Copied the host of your ServiceNow instance URL. For example, if the URL of the
  instance is `https://your-domain.service-now.com`, the format for the
  host URL you enter is `your-domain.service-now.com`.
- Noted your basic authentication credentials containing a user name and password to allow
  Amazon Kendra to connect to your ServiceNow instance.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- **Optional:** Configured an OAuth 2.0 credential token that
  can identify Amazon Kendra and generate a user name, password, a client ID, and a client
  secret. The user name and password must provide access to the ServiceNow knowledge
  base and service catalog. See [ServiceNow documentation on OAuth 2.0 authentication](https://www.servicenow.com/docs/bundle/utah-platform-security/page/integrate/single-sign-on/concept/c_Authentication.html "https://www.servicenow.com/docs/bundle/utah-platform-security/page/integrate/single-sign-on/concept/c_Authentication.html") for more information.
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
your data. If you have not yet configured ServiceNow for Amazon Kendra see [Prerequisites](#prerequisites-v1-servicenow "#prerequisites-v1-servicenow").

Console
**To connect Amazon Kendra to ServiceNow**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose
   the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control**
settings under **Index settings**. 3. On the **Getting started** page, choose **Add data
source**. 4. On the **Add data source** page, choose **ServiceNow
connector V1.0**, and then choose **Add data source**. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page, enter the following
   information:
   1. **ServiceNow host**—Enter the ServiceNow
      host URL.
   2. **ServiceNow version**—Select your
      ServiceNow version.
   3. Choose between **Basic authentication** and **Oauth 2.0
      authentication** based on your use case.
   4. **AWS Secrets Manager secret**—Choose an existing secret or create a new
      Secrets Manager secret to store your ServiceNow authentication
      credentials. If you choose to create a new secret an AWS Secrets Manager
      secret window opens.
      1. **Secret name**—A name for your secret. The prefix
         ‘AmazonKendra-ServiceNow-’ is automatically added to your secret name.
      2. If using Basic Authentication—Enter the **Secret name**,
         **Username**, and **Password** for your
         ServiceNow account.

      If using OAuth2 Authentication—Enter the **Secret name**,
      **Username**, **Password**, **Client
      ID**, and **Client Secret** you created in your
      ServiceNow account. 3. Choose **Save and add secret**.

   5. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 6. Choose **Next**.

7. On the **Configure sync settings** page, enter the following
   information:
   1. **Include knowledge articles**—Choose to index knowledge
      articles.
   2. **Type of knowledge articles**—Choose between
      **Include only public articles** and **Include articles based
      on ServiceNow filter query** based on your use case. If you select
      **Include articles based on ServiceNow filter query**, you
      must enter a **Filter query** copied from your ServiceNow
      account.
   3. **Include knowledge articles attachments**—Choose to index
      knowledge article attachments. You can also select specific file types to index.
   4. **Include catalog items**—Choose to index catalog
      items.
   5. **Include catalog item attachments**—Choose to index
      catalog item attachments. You can also select specific file types to index.
   6. **Frequency**—How often Amazon Kendra will sync with
      your data source.
   7. Choose **Next**.

8. On the **Set field mappings** page, enter the following
   information:
   1. **Knowledge articles** and **Service catalog**
      —Select from the Amazon Kendra generated default data source fields and
      additional suggested field mappings that you want to map to your index.
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

You must specify the following using [ServiceNowConfiguration API](../APIReference/API_ServiceNowConfiguration.md "../APIReference/API_ServiceNowConfiguration.md"):

- **Data source URL**—Specify the
  ServiceNow URL. The host endpoint should look like the following:
  `your-domain.service-now.com`.
- **Data source host instance**—Specify the
  ServiceNow host instance version as either `LONDON` or
  `OTHERS`.
- **Secret Amazon Resource Name (ARN)**—Provide the
  Amazon Resource Name (ARN) of a Secrets Manager secret that contains the authentication
  credentials you created in your ServiceNow account.

If you are using basic authentication, the secret is stored in a JSON structure with
the following keys:

```
{
    "username": `"user name"`,
    "password": `"password"`
}
```

If you are using OAuth2 authentication, the secret is stored in a JSON structure with
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

- **Inclusion and exclusion filters**—Specify whether to
  include or exclude certain file attachments of catalogs and knowledge articles.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Indexing parameters**—You can also choose to
  specify whether to:
  - Index knowledge articles and service catalogs, or both of these. If you choose to
    index knowledge articles and service catalog items, you must provide the name of the
    ServiceNow field that is mapped to the index document contents field in the
    Amazon Kendra index.
  - Index attachments to knowledge articles and catalog items.
  - Use a ServiceNow query that selects documents from one or more knowledge
    bases. The knowledge bases can be public or private. For more information, see [Specifying documents
    to index with a query](servicenow-query.md "servicenow-query.md").

## Learn more

To learn more about integrating Amazon Kendra with your ServiceNow data
source, see:

- [Getting started with Amazon Kendra ServiceNow Online connector](https://aws.amazon.com/blogs/machine-learning/getting-started-with-amazon-kendra-servicenow-online-connector/ "https://aws.amazon.com/blogs/machine-learning/getting-started-with-amazon-kendra-servicenow-online-connector/")
