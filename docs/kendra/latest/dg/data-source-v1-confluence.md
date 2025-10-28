# Confluence connector V1.0

Confluence is a collaborative work-management tool designed for sharing, storing, and working on
project planning, software development, and product management. You can use Amazon Kendra to
index your Confluence spaces, pages (including nested pages), blogs, and comments and attachments to
indexed pages and blogs.

###### Note

Confluence connector V1.0 / ConfluenceConfiguration API ended in 2023. We recommend
migrating to or using Confluence connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Confluence data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v1-confluence "#supported-features-v1-confluence")
- [Prerequisites](#prerequisites-v1-confluence "#prerequisites-v1-confluence")
- [Connection instructions](#data-source-procedure-v1-confluence "#data-source-procedure-v1-confluence")
- [Learn more](#confluence-v1-learn-more "#confluence-v1-learn-more")

## Supported features

Amazon Kendra Confluence data source connector supports the following features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- (For Confluence Server only) Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Confluence data source, make these changes
in your Confluence and AWS accounts.

**In Confluence, make sure you have:**

- Granted Amazon Kendra permissions to view all content within your Confluence instance
  by:
  - Making Amazon Kendra a member of `confluence-administrators`
    group.
  - Granting site-admin permissions for all existing spaces, blogs, and pages.

- Copied the URL of your Confluence instance.
- **For SSO (Single Sign-On) users:** Activated the
  **Show on login page** for the user name and password when you configure
  Confluence **Authentication methods** in Confluence Data Center.
- **For Confluence Server**
  - Noted your basic authentication credentials containing your Confluence administrative
    account user name and password to connect to Amazon Kendra.

  ###### Note

  We recommend that you regularly refresh or rotate your credentials
  and secret. Provide only the necessary access level for your own security.
  We do **not** recommend that you re-use
  credentials and secrets across data sources, and connector versions 1.0 and
  2.0 (where applicable).
  - **Optional:**Generated a personal access token in your
    Confluence account to connect to Amazon Kendra. For more information, see [Confluence documentation on generating personal access tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html "https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html").

- **For Confluence Cloud**
  - Noted your basic authentication credentials containing your Confluence administrative
    account user name and password to connect to Amazon Kendra.

- Checked each document is unique in Confluence and across other
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

- Stored your Confluence authentication credentials in an
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
connect your Confluence data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Confluence data source, you must provide details of your
Confluence credentials so that Amazon Kendra can access your data. If you have not yet
configured Confluence for Amazon Kendra see [Prerequisites](#prerequisites-v1-confluence "#prerequisites-v1-confluence").

Console
**To connect Amazon Kendra to Confluence**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose
   the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control**
settings under **Index settings**. 3. On the **Getting started** page, choose **Add data
source**. 4. On the **Add data source** page, choose **Confluence connector
V1.0**, and then choose **Add data source**. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page, enter the following
   information:
   1. Choose between **Confluence Cloud** and **Confluence
      Server**.
   2. If you choose **Confluence Cloud**, enter the following
      information:
      1. **Confluence URL**—Your Confluence URL.
      2. **AWS Secrets Manager secret**—Choose an existing secret or create a new
         Secrets Manager secret to store your Confluence authentication
         credentials. If you choose to create a new secret an AWS Secrets Manager
         secret window opens.
         1. Enter following information in the **Create an AWS
            Secrets Manager secret window**:
            1. **Secret name**—A name for your secret. The prefix
               ‘AmazonKendra-Confluence-’ is automatically added to your secret name.
            2. For **User name** and
               **Password**—Enter your Confluence user name and
               password.
            3. Choose **Save authentication**.

   3. If you choose **Confluence Server**, enter the following
      information:
      1. **Confluence URL**—Your Confluence user name and
         password.
      2. (Optional) For **Web proxy** enter the following
         information:
         1. **Host name**—Host name for your Confluence account.
         2. **Port number**—Port used by the host URL transport
            protocol.

      3. For **Authentication**, Choose either **Basic
         authentication** or (Confluence Server only) **Personal Access
         Token**.
      4. **AWS Secrets Manager secret**—Choose an existing secret or create a new
         Secrets Manager secret to store your Confluence authentication
         credentials. If you choose to create a new secret an AWS Secrets Manager
         secret window opens.
         1. Enter following information in the **Create an AWS
            Secrets Manager secret window**:
            1. **Secret name**—A name for your secret. The prefix
               ‘AmazonKendra-Confluence-’ is automatically added to your secret name.
            2. For **User name** and
               **Password**—Enter the authentication credential values
               you configured in Confluence. If using basic authentication, use your Confluence user
               name (email ID) and password (API token). If using personal access token, enter
               the details of the **Personal Access Token** you configured in
               Confluence account.
            3. Save and add your secret.

   4. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 5. Choose **Next**.

7. On the **Configure sync settings** page, enter the following
   information:
   1. For **Include personal spaces** and **Include archived
      spaces**—Choose the optional space types to include in this data
      source.
   2. For **Additional configuration**—Specify regular expression
      patterns to include or exclude certain content. You can add up to 100 patterns.
   3. You can also choose to **Crawl attachments within chosen
      spaces**.
   4. In **Sync run schedule**, for
      **Frequency**—Choose how often Amazon Kendra will sync with
      your data source.
   5. Choose **Next**.

8. On the **Set field mappings** page, enter the following
   information:
   1. For **Space**, **Page**,
      **Blog**—Select from the Amazon Kendra generated default
      data source fields or **Additional suggested field mappings** to add
      index fields.
   2. **Add field**—To add custom data source fields to create an
      index field name to map to and the field data type.
   3. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to Confluence**

You must specify the following using [ConfluenceConfiguration](../APIReference/API_ConfluenceConfiguration.md "../APIReference/API_ConfluenceConfiguration.md") API:

- **Confluence version**—Specify the version of the
  Confluence instance you are using as `CLOUD` or `SERVER`.
- **Secret Amazon Resource Name (ARN)**—Provide the
  Amazon Resource Name (ARN) of an Secrets Manager secret that contains your Confluence
  authentication credentials.

If you use Confluence Server, you can use either your Confluence user name and password, or
your personal access token as the authentication credentials.

If you use your Confluence user name and password as authentication credentials, you
store the following credentials as a JSON structure in your Secrets Manager
secret:

```
{
    "username": "`user name`",
    "password": "`password`"
}
```

If you use a personal access token to connect Confluence Server to Amazon Kendra,
you store the following credentials as a JSON structure in your Secrets Manager
secret:

```
{
    "patToken": "`personal access token`"
}
```

If you use Confluence Cloud, you use your Confluence user name and an API token, configured
in Confluence, as your password. You store the following credentials as a JSON structure in
your Secrets Manager secret:

```
{
    "username": "`user name`",
    "password": "`API token`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Confluence connector and Amazon Kendra.
  For more information, see [IAM roles for Confluence
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Web proxy**—Whether to connect to your Confluence
  URL instance via a web proxy. You can use this option for Confluence Server.
- (For Confluence Server only) **Virtual Private Cloud
  (VPC)**—Specify `VpcConfiguration` as part of the data source
  configuration. See [Configuring Amazon Kendra to use a
  VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion filters**—Specify regular
  expression patterns to include or exclude certain spaces, blog posts, pages, spaces, and
  attachments. If you choose to index attachments, only attachments to the indexed pages and
  blogs are indexed.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Field mappings**—Choose to map your Confluence
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

To learn more about integrating Amazon Kendra with your Confluence data source,
see:

- [Configuring your Amazon Kendra Confluence Server connector](https://aws.amazon.com/blogs/machine-learning/configuring-your-amazon-kendra-confluence-server-connector/ "https://aws.amazon.com/blogs/machine-learning/configuring-your-amazon-kendra-confluence-server-connector/")
