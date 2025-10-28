# Jira

Jira is a project management tool for software development, product
management, and bug tracking. You can use Amazon Kendra to index your
Jira projects, issues, comments, attachments, worklogs, and statuses.

Amazon Kendra currently only supports Jira Cloud.

You can connect Amazon Kendra to your Jira data source using either the
[Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") or the [JiraConfiguration](../APIReference/API_JiraConfiguration.md "../APIReference/API_JiraConfiguration.md") API. For a list of features supported by each,
see [Supported features](#supported-features-jira "#supported-features-jira").

For troubleshooting your Amazon Kendra Jira data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-jira "#supported-features-jira")
- [Prerequisites](#prerequisites-jira "#prerequisites-jira")
- [Connection instructions](#data-source-procedure-jira "#data-source-procedure-jira")
- [Learn more](#jira-learn-more "#jira-learn-more")

## Supported features

Amazon Kendra Jira data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Jira data source,
make these changes in your Jira and AWS accounts.

**In Jira, make sure you have:**

- Configured API token authentication credentials, which include a
  Jira ID (user name or email) and a Jira credential (Jira API token). See [Atlassian documentation on managing API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/ "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/").

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Noted the Jira account URL from your Jira account
  settings. For example,
  `https://company.atlassian.net/`.
- Checked each document is unique in Jira and across other
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

- Stored your Jira authentication credentials in an
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
connect your Jira data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Jira data source, you must provide
the necessary details of your Jira data source so that Amazon Kendra can access
your data. If you have not yet configured Jira for Amazon Kendra,
see [Prerequisites](#prerequisites-jira "#prerequisites-jira").

Console
**To connect Amazon Kendra to
Jira**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Jira connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Jira connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. **Jira account URL**—Enter
      your Jira Account URL. For example:
      `https://company.atlassian.net/`.
   2. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   3. **AWS Secrets Manager secret**—Choose an existing secret or create a new
      Secrets Manager secret to store your Jira authentication
      credentials. If you choose to create a new secret an AWS Secrets Manager
      secret window opens.
      1. Enter following information in the
         **Create an AWS
         Secrets Manager secret
         window**:
         1. **Secret name**—A
            name for your secret. The prefix
            ‘AmazonKendra-Jira-’ is
            automatically added to your secret name.
         2. For **Jira
            ID**—Enter the Jira user name or
            email.
         3. For
            **Password/Token**—Enter
            the Jira API token configured in
            Jira.

      2. Save and add your secret.

   4. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
      so, you must add **Subnets** and **VPC security groups**.
   5. **Identity crawler**—Specify whether to turn on
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
   6. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 7. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. **Select which Jira projects to
      index**—Choose to crawl all project
      or specific projects.
   2. **Additional configuration**—Specify
      certain statuses, and issue types. Choose to crawl comments,
      attachments, and worklogs. Use regular expression patterns to
      include or exclude certain content.
   3. **Sync mode**—Choose how you want to update
      your index when your data source content changes. When you sync your
      data source with Amazon Kendra for the first time, all content
      is crawled and indexed by default. You must run a full sync of your
      data if your initial sync failed, even if you don't choose full sync
      as your sync mode option.
      - Full sync: Freshly index all content, replacing existing
        content each time your data source syncs with your index.
      - New, modified sync: Index only new and modified content
        each time your data source syncs with your index. Amazon Kendra
        can use your data source's mechanism for tracking content
        changes and index content that changed since the last sync.
      - New, modified, deleted sync: Index only new, modified,
        and deleted content each time your data source syncs with
        your index. Amazon Kendra can use your data source's
        mechanism for tracking content changes and index content
        that changed since the last sync.

   4. In **Sync run schedule**, for
      **Frequency**—Choose how often
      to sync your data source content and update your index.
   5. Choose **Next**.

8. On the **Set field mappings** page, enter the
   following information:
   1. **Default data source
      fields**—Select from the Amazon Kendra generated default data source fields you
      want to map to your index.
   2. **Add field**—To add custom data
      source fields to create an index field name to map to
      and the field data type.
   3. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to
Jira**

You must specify the following using the [JiraConfiguration](../APIReference/API_JiraConfiguration.md "../APIReference/API_JiraConfiguration.md") API:

- **Data source
  URL**—Specify your Jira account URL. For
  example,
  `company.atlassian.net`.
- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Jira account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "jiraId": "`Jira user name or email`",
    "jiraCredential": "`Jira API token`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Jira connector and Amazon Kendra.
  For more information, see [IAM roles for Jira
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify `VpcConfiguration` as
  part of the data source configuration. See [Configuring
  Amazon Kendra to use a VPC](vpc-configuration.md "vpc-configuration.md").
- **Change log**—Whether
  Amazon Kendra should use the Jira data
  source change log mechanism to determine if a document must be
  updated in the index.

###### Note

Use the change log if you don’t want Amazon Kendra
to scan all of the documents. If your change log is large,
it might take Amazon Kendra less time to scan the
documents in the Jira data source than to
process the change log. If you are syncing your Jira
data source with your index for the first time, all documents are scanned.

- **Inclusion and exclusion
  filters**—You can specify whether to include or
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

- **Comment, attachments, and work logs**—You
  can specify whether to crawl certain comments, attachments, and work logs of issues.
- **Projects, Issues, Statuses**—You
  can specify whether to crawl certain project IDs, issue types, and
  statuses.
- **User context filtering and access control**—Amazon Kendra
  crawls the access control list (ACL) for your documents,
  if you have an ACL for your documents. The ACL
  information is used to filter search results based on the user or their
  group access to documents. For more information, see [User context
  filtering](user-context-filter.md#datasource-context-filter "user-context-filter.md#datasource-context-filter").
- **Field mappings**—Choose to map your Jira
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

## Learn more

To learn more about integrating Amazon Kendra with your Jira data
source, see:

- [Intelligently search your Jira projects with Amazon Kendra Jira Cloud
  connector](https://aws.amazon.com/blogs/machine-learning/intelligently-search-your-jira-projects-with-amazon-kendra-jira-cloud-connector/ "https://aws.amazon.com/blogs/machine-learning/intelligently-search-your-jira-projects-with-amazon-kendra-jira-cloud-connector/")
