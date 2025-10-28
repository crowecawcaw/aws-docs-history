# GitHub

GitHub is a web-based hosting service for software development providing code
storage and management services with version control. You can use Amazon Kendra to
index your GitHub Enterprise Cloud (SaaS) and GitHub Enterprise
Server (On Prem) repository files, issue and pull requests, issue and pull request comments,
and issue and pull request comment attachments. You can also choose to include or exclude
certain files.

###### Note

Amazon Kendra now supports an upgraded GitHub connector.

The console has been automatically upgraded for you. Any new connectors you create in
the console will use the upgraded architecture. If you use the API, you must now use the
[TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object instead of the
`GitHubConfiguration` object to configure your
connector.

Connectors configured using the older console and API architecture will continue to
function as configured. However, you won’t be able to edit or update them. If you want
to edit or update your connector configuration, you must create a new connector.

We recommended migrating your connector workflow to the upgraded version. Support for
connectors configured using the older architecture is scheduled to end by June 2024.

You can connect Amazon Kendra to your GitHub data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra GitHub data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-github "#supported-features-github")
- [Prerequisites](#prerequisites-github "#prerequisites-github")
- [Connection instructions](#data-source-procedure-github "#data-source-procedure-github")
- [Learn more](#github-learn-more "#github-learn-more")

## Supported features

Amazon Kendra GitHub data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your GitHub data source,
make these changes in your GitHub and AWS accounts.

**In GitHub, make sure you have:**

- Created a GitHub user with administrative permissions to the
  GitHub organization.
- Configured a personal access token in Git Hub to use as your authentication
  credentials. See [GitHub documentation on creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token").

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- **Recommended:**Configured an OAuth token for
  authentication credentials. Use OAuth token for better API throttle limits and
  connector performance. See [GitHub documentation on OAuth authorization](https://docs.github.com/en/rest/apps/oauth-applications?apiVersion=2022-11-28#about-oauth-apps-and-oauth-authorizations-of-github-apps "https://docs.github.com/en/rest/apps/oauth-applications?apiVersion=2022-11-28#about-oauth-apps-and-oauth-authorizations-of-github-apps").
- Noted the GitHub host URL for the type of GitHub
  service that you use. For example, the host URL for GitHub cloud
  could be `https://api.github.com` and the host URL for
  GitHub server could be
  `https://on-prem-host-url/api/v3/`.
- Noted the name of your organization for GitHub the GitHub
  Enterprise Cloud (SaaS) account or GitHub Enterprise Server
  (on-premises) account you want to connect to. You can find your organization
  name by logging into GitHub desktop and selecting **Your
  organizations** under your profile picture dropdown.
- **Optional (server only):** Generated a SSL
  certificate and copied the path to the certificate stored in an Amazon S3 bucket. You use this to connect to GitHub if you require a secure
  SSL connection. You can simply generate a self-signed X509 certificate on any
  computer using OpenSSL. For an example of using OpenSSL to create an X509
  certificate, see [Create and sign
  an X509 certificate](../../../elasticbeanstalk/latest/dg/configuring-https-ssl.md "../../../elasticbeanstalk/latest/dg/configuring-https-ssl.md").
- Added the following permissions:

**For GitHub Enterprise Cloud
(SaaS)**

    + `repo:status` – Grants read/write access to commit
     statuses in public and private repositories. This scope is only
     necessary to grant other users or services access to private repository
     commit statuses without granting access to the code.
    + `repo_deployment` – Grants access to deployment
     statuses for public and private repositories. This scope is only
     necessary to grant other users or services access to deployment
     statuses, without granting access to the code.
    + `public_repo` – Limits access to public
     repositories. That includes read/write access to code, commit statuses,
     repository projects, collaborators, and deployment statuses for public
     repositories and organizations. Also required for starring public
     repositories.
    + `repo:invite` – Grants accept/decline abilities for
     invitations to collaborate on a repository. This scope is only necessary
     to grant other users or services access to invites without granting
     access to the code.
    + `security_events` – Grants: read and write access to
     security events in the code scanning API. This scope is only necessary
     to grant other users or services access to security events without
     granting access to the code.
    + `read:org` – Read-only access to organization
     membership, organization projects, and team membership.
    + `user:email` – Grants read access to a user's email
     addresses. Required by Amazon Kendra to crawl ACLs.
    + `user:follow` – Grants access to follow or unfollow
     other users. Required by Amazon Kendra to crawl ACLs.
    + `read:user` – Grants access to read a user's profile
     data. Required by Amazon Kendra to crawl ACLs.
    + `workflow` – Grants the ability to add and update
     GitHub Actions workflow files. Workflow files can be committed without
     this scope if the same file (with both the same path and contents)
     exists on another branch in the same repository.

For more information, see [Scopes for OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps "https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps") in GitHub Docs.

**For GitHub Enterprise Server (On
Prem)**

    + `repo:status` – Grants read/write access to commit
     statuses in public and private repositories. This scope is only
     necessary to grant other users or services access to private repository
     commit statuses without granting access to the code.
    + `repo_deployment` – Grants access to deployment
     statuses for public and private repositories. This scope is only
     necessary to grant other users or services access to deployment
     statuses, without granting access to the code.
    + `public_repo` – Limits access to public
     repositories. That includes read/write access to code, commit statuses,
     repository projects, collaborators, and deployment statuses for public
     repositories and organizations. Also required for starring public
     repositories.
    + `repo:invite` – Grants accept/decline abilities for
     invitations to collaborate on a repository. This scope is only necessary
     to grant other users or services access to invites without granting
     access to the code.
    + `security_events` – Grants: read and write access to
     security events in the code scanning API. This scope is only necessary
     to grant other users or services access to security events without
     granting access to the code.
    + `read:user` – Grants access to read a user's profile
     data. Required by Amazon Q Business to crawl ACLs.
    + `user:email` – Grants read access to a user's email
     addresses. Required by Amazon Q Business to crawl ACLs.
    + `user:follow` – Grants access to follow or unfollow
     other users. Required by Amazon Q Business to crawl ACLs.
    + `site_admin` – Grants site administrators access to
     GitHub Enterprise Server Administration API endpoints.
    + `workflow` – Grants the ability to add and update
     GitHub Actions workflow files. Workflow files can be committed without
     this scope if the same file (with both the same path and contents)
     exists on another branch in the same repository.

For more information, see [Scopes for OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps "https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps") in GitHub Docs and [Understanding scopes for OAuth Apps](https://developer.github.com/enterprise/2.16/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/#available-scopes "https://developer.github.com/enterprise/2.16/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/#available-scopes") in GitHub
Developer.

- Checked each document is unique in GitHub and across other
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

- Stored your GitHub authentication credentials in an
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
connect your GitHub data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your GitHub data source, you must provide
the necessary details of your GitHub data source so that Amazon Kendra can access
your data. If you have not yet configured GitHub for Amazon Kendra,
see [Prerequisites](#prerequisites-github "#prerequisites-github").

Console
**To connect Amazon Kendra to
GitHub**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **GitHub connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **GitHub connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security** page,
    enter the following information:
    1. **GitHub
       source**—Choose between
       **GitHub Enterprise
       Cloud** and **GitHub
       Enterprise Server**.
    2. **GitHub host
       URL**—For example, the host URL for
       GitHub cloud could be
       `https://api.github.com`
       and the host URL for GitHub server could be
       `https://on-prem-host-url/api/v3/`.
    3. **GitHub organization
       name**—Enter your GitHub
       organization name. You can find your organization
       information in your GitHub account.

    ###### Note

    GitHub connector supports crawling a
    single organization per data source connector
    instance. 4. **Authorization**—Turn on or off access control list (ACL) information for your
    documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
    and groups can access. The ACL information is used to filter search results based on the user or
    their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources"). 5. **AWS Secrets Manager secret**—Choose an existing secret or create a new
    Secrets Manager secret to store your GitHub authentication
    credentials. If you choose to create a new secret an AWS Secrets Manager
    secret window opens.

        1. Enter following information in the
         **Create an AWS
         Secrets Manager secret
         window**:


        	1. **Secret name**—A
        	 name for your secret. The prefix
        	 ‘AmazonKendra-GitHub-’ is
        	 automatically added to your secret name.
        	2. For **GitHub
        	 token**—Enter the authentication
        	 credential value configured in
        	 GitHub.
        2. Save and add your secret.

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

7.  On the **Configure sync settings** page,
    enter the following information:
    1. **Select repositories**—Choose
       to crawl all repositories or select.

    If you choose to crawl select repositories, add the
    names for the repositories and, optionally, the name of
    any specific branches. 2. **Content types**—Choose the
    content types you want to crawl from files, issues, pull
    requests, and more. 3. **Regex patterns**—Add regular
    expression patterns to include or exclude certain
    files. 4. **Sync mode**—Choose how you
    want to update your index when your data source content
    changes. When you sync your data source with Amazon Kendra for the first time, all content is
    crawled and indexed by default. You must run a full sync
    of your data if your initial sync failed, even if you
    don't choose full sync as your sync mode option.

        * Full sync: Freshly index all content,
         replacing existing content each time your data
         source syncs with your index.
        * New, modified sync: Index only new and
         modified content each time your data source syncs
         with your index. Amazon Kendra can use your
         data source's mechanism for tracking content
         changes and index content that changed since the
         last sync.
        * New, modified, deleted sync: Index only new,
         modified, and deleted content each time your data
         source syncs with your index. Amazon Kendra
         can use your data source's mechanism for tracking
         content changes and index content that changed
         since the last sync.

    5. In **Sync run schedule** for
       **Frequency**—Choose how
       often to sync your data source content and update your
       index.
    6. Choose **Next**.

8.  On the **Set field mappings** page, enter the
    following information:
    1. **Default data source
       fields**—Select from the Amazon Kendra generated default data source fields you
       want to map to your index.
    2. **Add field**—To add custom data
       source fields to create an index field name to map to
       and the field data type.
    3. Choose **Next**.

9.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
GitHub**

You must specify a JSON of the [data source
schema](ds-schemas.md#ds-github-schema "ds-schemas.md#ds-github-schema") using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API. You must
provide the following information:

- **Data source**—Specify
  the data source type as `GITHUB` when
  you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call the
  [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **GitHub
  type**—Specify the type as either
  `SAAS` or `ON_PREMISE`.
- **Host URL**—Specify the
  GitHub host URL or API endpoint URL. For example, if you use
  GitHub SaaS/Enterprise Cloud, the host URL could be
  `https://api.github.com`, and for
  GitHub on-premises/Enterprise Server the host URL
  could be `https://on-prem-host-url/api/v3/`.
- **Organization
  name**—Specify the name of the organization of
  the GitHub account. You can find your organization name by
  logging into GitHub desktop and selecting **Your
  organizations** under your profile picture
  dropdown.
- **Sync mode**—Specify
  how Amazon Kendra should update your index when your data source
  content changes. When you sync your data source with Amazon Kendra
  for the first time, all content is crawled and indexed by default.
  You must run a full sync of your data if your initial sync failed,
  even if you don’t choose full sync as your sync mode option. You can
  choose between:
  - `FORCED_FULL_CRAWL` to freshly index all content,
    replacing existing content each time your data source syncs with
    your index.
  - `FULL_CRAWL` to index only new, modified, and deleted
    content each time your data source syncs with your index. Amazon Kendra
    can use your data source’s mechanism for tracking content changes and
    index content that changed since the last sync.
  - `CHANGE_LOG` to index only new and modified
    content each time your data source syncs with your index. Amazon Kendra
    can use your data source’s mechanism for tracking content changes and
    index content that changed since the last sync.

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
- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your GitHub account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "personalToken": "`token`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the GitHub connector and Amazon Kendra.
  For more information, see [IAM roles for GitHub
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").

###### Note

If you use GitHub server, you must use an
Amazon VPC to connect to your GitHub
server.

- **Repository filter**—Filter
  repositories by their name and branch names.
- **Document/content
  types**—Specify whether to crawl repository
  documents, issues, issue comments, issue comment attachments,
  pull requests, pull request comments, pull request comment
  attachments.
- **Inclusion and exclusion
  filters**—Specify whether to include or exclude
  certain files and folders.

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
- **Field mappings**—Choose to
  map your GitHub data source fields to your Amazon Kendra index fields. You can include fields of
  documents, commits, issues, issue attachments, issue comments,
  pull requests, pull request attachments, pull request comments.
  For more information, see [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent
for your documents is required in order for Amazon Kendra to
search your documents. You must map your document body field
name in your data source to the index field name
`_document_body`. All other fields are
optional.

For a list of other important JSON keys to configure, see [GitHub template
schema](ds-schemas.md#ds-github-schema "ds-schemas.md#ds-github-schema").

## Learn more

To learn more about integrating Amazon Kendra with your GitHub data
source, see:

- [Reimagine search on GitHub repositories with the power of the Amazon Kendra GitHub connector](https://aws.amazon.com/blogs/machine-learning/reimagine-search-on-github-repositories-with-the-power-of-the-amazon-kendra-github-connector/ "https://aws.amazon.com/blogs/machine-learning/reimagine-search-on-github-repositories-with-the-power-of-the-amazon-kendra-github-connector/")
