# GitLab connector for Amazon AppFlow

GitLab is an open source code repository and software development platform. If
you're a GitLab user, your account contains data about your projects and repositories.
You can use Amazon AppFlow to transfer data from
GitLab to certain AWS services or other supported applications.

## Amazon AppFlow support for GitLab

Amazon AppFlow supports GitLab as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from GitLab.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to GitLab.

**Supported API version**

Amazon AppFlow retrieves your data by sending requests to the GitLab v4 REST API.

## Before you begin

To use Amazon AppFlow to transfer data from GitLab to supported destinations, you must meet these
requirements:

- You have a GitLab account and one or more projects that contain the data that
  you want to transfer. For more information about the GitLab data objects that
  Amazon AppFlow supports, see [Supported objects](#gitlab-objects "#gitlab-objects").
- In the settings of your account, you've created either of the following resources for
  Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data securely when
  it makes authenticated calls to your account.

  - An application, which provides OAuth 2.0 authentication. For the steps to create an
    application, see [User owned applications](https://docs.gitlab.com/ee/integration/oauth_provider.html#user-owned-applications "https://docs.gitlab.com/ee/integration/oauth_provider.html#user-owned-applications") in the GitLab Docs.
  - A personal access token. For the steps to create one, see [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token "https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token") in the GitLab Docs.

  Your personal access token must permit the `api` scope.

- If you created an application, you've configured it with the following settings:

  - You've specified a redirect URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from GitLab. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._
  - You've permitted the scopes that provide access to the data objects that you want to
    transfer. For information about GitLab OAuth 2.0 scopes, see [Authorized applications](https://docs.gitlab.com/ee/integration/oauth_provider.html#authorized-applications "https://docs.gitlab.com/ee/integration/oauth_provider.html#authorized-applications") in the GitLab Docs.

If you created an application, note the application ID and secret. If you created a personal
access token, note the token value. You provide these values to Amazon AppFlow when you connect to your
GitLab account.

## Connecting Amazon AppFlow to your GitLab account

To connect Amazon AppFlow to your GitLab account, provide the credentials from your
application, or provide a personal access token. If you haven't yet configured your
GitLab account for Amazon AppFlow integration, see [Before you begin](#gitlab-prereqs "#gitlab-prereqs").

###### To connect to GitLab

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **GitLab**.
4. Choose **Create connection**.
5. In the **Connect to GitLab** window, for **Select
   authentication type**, choose how to authenticate Amazon AppFlow with your GitLab
   account when it requests to access your data:

   - Choose **OAuth2** to authenticate Amazon AppFlow with the credentials from an
     application. Then, enter the following values:

     - **Client ID** – The application ID.
     - **Client secret** – The secret.

   - Choose **PersonalAccessToken** to authenticate Amazon AppFlow with a personal
     access token. Then, enter the token value for **Personal access
     token**.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Depending on the authentication type that you chose, do one of the following:

    * If you chose **OAuth2**, choose **Continue**. Then, in
     the window that appears, sign in to your GitLab account, and grant access to
     Amazon AppFlow.
    * If you chose **PersonalAccessToken**, choose
     **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses GitLab as the data source, you can select this connection.

## Transferring data from GitLab with a flow

To transfer data from GitLab, create an Amazon AppFlow flow, and choose GitLab as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for GitLab, see [Supported objects](#gitlab-objects "#gitlab-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#gitlab-destinations "#gitlab-destinations").

## Supported destinations

When you create a flow that uses GitLab as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")

## Supported objects

When you create a flow that uses GitLab as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                                               | **Field**             | **Data type**                | **Supported filters** |
| -------------------------------------------------------- | --------------------- | ---------------------------- | --------------------- |
| Branch                                                   | can\_push             | Boolean                      |                       |
| commit                                                   | Struct                |                              |
| default                                                  | Boolean               |                              |
| developers\_can\_merge                                   | Boolean               |                              |
| developers\_can\_push                                    | Boolean               |                              |
| merged                                                   | Boolean               |                              |
| name                                                     | String                |                              |
| protected                                                | Boolean               |                              |
| search                                                   | String                | EQUAL\_TO                    |
| web\_url                                                 | String                |                              |
| Commit                                                   | all                   | Boolean                      | EQUAL\_TO             |
| author\_email                                            | String                |                              |
| author\_name                                             | String                |                              |
| authored\_date                                           | DateTime              |                              |
| committed\_date                                          | DateTime              |                              |
| committer\_email                                         | String                |                              |
| committer\_name                                          | String                |                              |
| created\_at                                              | DateTime              |                              |
| first\_parent                                            | Boolean               | EQUAL\_TO                    |
| id                                                       | String                |                              |
| message                                                  | String                |                              |
| order                                                    | String                | EQUAL\_TO                    |
| parent\_ids                                              | List                  |                              |
| path                                                     | String                | EQUAL\_TO                    |
| ref\_name                                                | String                | EQUAL\_TO                    |
| short\_id                                                | String                |                              |
| since                                                    | DateTime              | GREATER\_THAN\_OR\_EQUAL\_TO |
| since\_until                                             | DateTime              | BETWEEN                      |
| title                                                    | String                |                              |
| trailers                                                 | Boolean               | EQUAL\_TO                    |
| until                                                    | DateTime              | LESS\_THAN\_OR\_EQUAL\_TO    |
| web\_url                                                 | String                |                              |
| with\_stats                                              | Boolean               | EQUAL\_TO                    |
| Group                                                    | auto\_devops\_enabled | String                       |                       |
| avatar\_url                                              | String                |                              |
| created\_at                                              | DateTime              |                              |
| default\_branch\_protection                              | Integer               |                              |
| description                                              | String                |                              |
| emails\_disabled                                         | String                |                              |
| file\_template\_project\_id                              | Integer               |                              |
| full\_name                                               | String                |                              |
| full\_path                                               | String                |                              |
| id                                                       | Integer               |                              |
| ip\_restriction\_ranges                                  | String                |                              |
| ldap\_access                                             | String                |                              |
| ldap\_cn                                                 | String                |                              |
| lfs\_enabled                                             | Boolean               |                              |
| mentions\_disabled                                       | String                |                              |
| min\_access\_level                                       | Integer               | EQUAL\_TO                    |
| name                                                     | String                |                              |
| order\_by                                                | String                | EQUAL\_TO                    |
| owned                                                    | Boolean               | EQUAL\_TO                    |
| parent\_id                                               | String                |                              |
| path                                                     | String                |                              |
| project\_creation\_level                                 | String                |                              |
| request\_access\_enabled                                 | Boolean               |                              |
| require\_two\_factor\_authentication                     | Boolean               |                              |
| search                                                   | String                | EQUAL\_TO                    |
| share\_with\_group\_lock                                 | Boolean               |                              |
| skip\_groups                                             | Integer               | EQUAL\_TO                    |
| sort                                                     | String                | EQUAL\_TO                    |
| statistics                                               | Boolean               | EQUAL\_TO                    |
| subgroup\_creation\_level                                | String                |                              |
| top\_level\_only                                         | Boolean               | EQUAL\_TO                    |
| two\_factor\_grace\_period                               | Integer               |                              |
| visibility                                               | String                |                              |
| web\_url                                                 | String                |                              |
| with\_custom\_attributes                                 | Boolean               | EQUAL\_TO                    |
| Group Member                                             | access\_level         | Integer                      |                       |
| avatar\_url                                              | String                |                              |
| created\_at                                              | DateTime              |                              |
| created\_by                                              | Struct                |                              |
| email                                                    | String                |                              |
| expires\_at                                              | DateTime              |                              |
| group\_saml\_identity                                    | Struct                |                              |
| id                                                       | Integer               |                              |
| is\_using\_seat                                          | String                |                              |
| membership\_state                                        | String                |                              |
| name                                                     | String                |                              |
| query                                                    | String                | EQUAL\_TO                    |
| show\_seat\_info                                         | Boolean               | EQUAL\_TO                    |
| skip\_users                                              | Integer               | EQUAL\_TO                    |
| state                                                    | String                |                              |
| user\_ids                                                | Integer               | EQUAL\_TO                    |
| username                                                 | String                |                              |
| web\_url                                                 | String                |                              |
| Group label                                              | closed\_issues\_count | Integer                      |                       |
| color                                                    | String                |                              |
| description                                              | String                |                              |
| description\_html                                        | String                |                              |
| id                                                       | Integer               |                              |
| include\_ancestor\_groups                                | Boolean               | EQUAL\_TO                    |
| include\_descendant\_groups                              | Boolean               | EQUAL\_TO                    |
| name                                                     | String                |                              |
| only\_group\_labels                                      | Boolean               | EQUAL\_TO                    |
| open\_issues\_count                                      | Integer               |                              |
| open\_merge\_requests\_count                             | Integer               |                              |
| search                                                   | String                | EQUAL\_TO                    |
| subscribed                                               | Boolean               |                              |
| text\_color                                              | String                |                              |
| with\_counts                                             | Boolean               | EQUAL\_TO                    |
| Group milestone                                          | created\_at           | DateTime                     |                       |
| description                                              | String                |                              |
| due\_date                                                | Date                  |                              |
| expired                                                  | Boolean               |                              |
| group\_id                                                | Integer               |                              |
| id                                                       | Integer               |                              |
| iid                                                      | Integer               |                              |
| iids                                                     | Integer               | EQUAL\_TO                    |
| include\_parent\_milestones                              | Boolean               | EQUAL\_TO                    |
| search                                                   | String                | EQUAL\_TO                    |
| start\_date                                              | Date                  |                              |
| state                                                    | String                | EQUAL\_TO                    |
| title                                                    | String                | EQUAL\_TO                    |
| updated\_at                                              | DateTime              |                              |
| web\_url                                                 | String                |                              |
| Issue                                                    | \_links               | Struct                       |                       |
| assignee                                                 | Struct                |                              |
| assignee\_id                                             | Integer               | EQUAL\_TO                    |
| assignee\_username                                       | String                | EQUAL\_TO                    |
| assignees                                                | List                  |                              |
| author                                                   | Struct                |                              |
| author\_id                                               | String                | EQUAL\_TO                    |
| author\_username                                         | String                | EQUAL\_TO                    |
| blocking\_issues\_count                                  | Integer               |                              |
| closed\_at                                               | DateTime              |                              |
| closed\_by                                               | String                |                              |
| confidential                                             | Boolean               | EQUAL\_TO                    |
| created\_after                                           | DateTime              | GREATER\_THAN\_OR\_EQUAL\_TO |
| created\_at                                              | DateTime              |                              |
| created\_before                                          | DateTime              | LESS\_THAN\_OR\_EQUAL\_TO    |
| created\_before\_after                                   | DateTime              | BETWEEN                      |
| description                                              | String                |                              |
| discussion\_locked                                       | Boolean               |                              |
| downvotes                                                | Integer               |                              |
| due\_date                                                | String                | EQUAL\_TO                    |
| has\_tasks                                               | Boolean               |                              |
| id                                                       | Integer               |                              |
| iid                                                      | Integer               |                              |
| iids                                                     | Integer               | EQUAL\_TO                    |
| issue\_type                                              | String                | EQUAL\_TO                    |
| labels                                                   | List                  |                              |
| merge\_requests\_count                                   | Integer               |                              |
| milestone                                                | Struct                |                              |
| milestone\_id                                            | String                | EQUAL\_TO                    |
| moved\_to\_id                                            | String                |                              |
| my\_reaction\_emoji                                      | String                | EQUAL\_TO                    |
| non\_archived                                            | Boolean               | EQUAL\_TO                    |
| order\_by                                                | String                | EQUAL\_TO                    |
| project\_id                                              | Integer               |                              |
| references                                               | Struct                |                              |
| scope                                                    | String                | EQUAL\_TO                    |
| search                                                   | String                | EQUAL\_TO                    |
| service\_desk\_reply\_to                                 | String                |                              |
| severity                                                 | String                |                              |
| sort                                                     | String                | EQUAL\_TO                    |
| state                                                    | String                | EQUAL\_TO                    |
| task\_completion\_status                                 | Struct                |                              |
| task\_status                                             | String                |                              |
| time\_stats                                              | Struct                |                              |
| title                                                    | String                |                              |
| type                                                     | String                |                              |
| updated\_after                                           | DateTime              | GREATER\_THAN\_OR\_EQUAL\_TO |
| updated\_at                                              | DateTime              |                              |
| updated\_before                                          | DateTime              | LESS\_THAN\_OR\_EQUAL\_TO    |
| updated\_before\_after                                   | DateTime              | BETWEEN                      |
| upvotes                                                  | Integer               |                              |
| user\_notes\_count                                       | Integer               |                              |
| web\_url                                                 | String                |                              |
| with\_labels\_details                                    | Boolean               | EQUAL\_TO                    |
| Job                                                      | allow\_failure        | Boolean                      |                       |
| artifacts                                                | List                  |                              |
| artifacts\_expire\_at                                    | DateTime              |                              |
| artifacts\_file                                          | Struct                |                              |
| commit                                                   | Struct                |                              |
| coverage                                                 | String                |                              |
| created\_at                                              | DateTime              |                              |
| duration                                                 | Integer               |                              |
| failure\_reason                                          | String                |                              |
| finished\_at                                             | DateTime              |                              |
| id                                                       | Integer               |                              |
| name                                                     | String                |                              |
| pipeline                                                 | Struct                |                              |
| project                                                  | Struct                |                              |
| queued\_duration                                         | Integer               |                              |
| ref                                                      | String                |                              |
| runner                                                   | String                |                              |
| scope                                                    | String                | EQUAL\_TO                    |
| stage                                                    | String                |                              |
| started\_at                                              | DateTime              |                              |
| status                                                   | String                |                              |
| tag                                                      | Boolean               |                              |
| tag\_list                                                | List                  |                              |
| user                                                     | Struct                |                              |
| web\_url                                                 | String                |                              |
| Pipeline                                                 | created\_at           | DateTime                     |                       |
| id                                                       | Integer               |                              |
| iid                                                      | Integer               |                              |
| order\_by                                                | String                | EQUAL\_TO                    |
| project\_id                                              | Integer               |                              |
| ref                                                      | String                | EQUAL\_TO                    |
| scope                                                    | String                | EQUAL\_TO                    |
| sha                                                      | String                | EQUAL\_TO                    |
| sort                                                     | String                | EQUAL\_TO                    |
| source                                                   | String                | EQUAL\_TO                    |
| status                                                   | String                | EQUAL\_TO                    |
| updated\_after                                           | DateTime              | GREATER\_THAN\_OR\_EQUAL\_TO |
| updated\_at                                              | DateTime              |                              |
| updated\_before                                          | DateTime              | LESS\_THAN\_OR\_EQUAL\_TO    |
| updated\_before\_after                                   | DateTime              | BETWEEN                      |
| username                                                 | String                | EQUAL\_TO                    |
| web\_url                                                 | String                |                              |
| yaml\_errors                                             | Boolean               | EQUAL\_TO                    |
| Project                                                  | \_links               | Struct                       |                       |
| allow\_merge\_on\_skipped\_pipeline                      | String                |                              |
| analytics\_access\_level                                 | String                |                              |
| archived                                                 | Boolean               | EQUAL\_TO                    |
| auto\_cancel\_pending\_pipelines                         | String                |                              |
| auto\_devops\_deploy\_strategy                           | String                |                              |
| auto\_devops\_enabled                                    | Boolean               |                              |
| autoclose\_referenced\_issues                            | Boolean               |                              |
| avatar\_url                                              | String                |                              |
| build\_timeout                                           | Integer               |                              |
| builds\_access\_level                                    | String                |                              |
| can\_create\_merge\_request\_in                          | Boolean               |                              |
| ci\_allow\_fork\_pipelines\_to\_run\_in\_parent\_project | Boolean               |                              |
| ci\_config\_path                                         | String                |                              |
| ci\_default\_git\_depth                                  | Integer               |                              |
| ci\_forward\_deployment\_enabled                         | Boolean               |                              |
| ci\_job\_token\_scope\_enabled                           | Boolean               |                              |
| ci\_separated\_caches                                    | Boolean               |                              |
| compliance\_frameworks                                   | List                  |                              |
| container\_expiration\_policy                            | Struct                |                              |
| container\_registry\_access\_level                       | String                |                              |
| container\_registry\_enabled                             | Boolean               |                              |
| container\_registry\_image\_prefix                       | String                |                              |
| created\_at                                              | DateTime              |                              |
| creator\_id                                              | Integer               |                              |
| default\_branch                                          | String                |                              |
| description                                              | String                |                              |
| emails\_disabled                                         | String                |                              |
| empty\_Repo                                              | Boolean               |                              |
| enforce\_auth\_checks\_on\_uploads                       | Boolean               |                              |
| external\_authorization\_classification\_label           | String                |                              |
| forking\_access\_level                                   | String                |                              |
| forks\_count                                             | Integer               |                              |
| http\_url\_to\_repo                                      | String                |                              |
| id                                                       | Integer               |                              |
| id\_after                                                | Integer               | EQUAL\_TO                    |
| id\_before                                               | Integer               | EQUAL\_TO                    |
| import\_status                                           | String                |                              |
| imported                                                 | Boolean               | EQUAL\_TO                    |
| issues\_access\_level                                    | String                |                              |
| issues\_enabled                                          | Boolean               |                              |
| jobs\_enabled                                            | Boolean               |                              |
| keep\_latest\_artifact                                   | Boolean               |                              |
| last\_activity\_after                                    | DateTime              | GREATER\_THAN\_OR\_EQUAL\_TO |
| last\_activity\_at                                       | DateTime              |                              |
| last\_activity\_before                                   | DateTime              | LESS\_THAN\_OR\_EQUAL\_TO    |
| last\_activity\_before\_after                            | DateTime              | BETWEEN                      |
| lfs\_enabled                                             | Boolean               |                              |
| membership                                               | Boolean               | EQUAL\_TO                    |
| merge\_commit\_template                                  | String                |                              |
| merge\_method                                            | String                |                              |
| merge\_requests\_access\_level                           | String                |                              |
| merge\_requests\_enabled                                 | Boolean               |                              |
| min\_access\_level                                       | Integer               | EQUAL\_TO                    |
| name                                                     | String                |                              |
| name\_with\_namespace                                    | String                |                              |
| namespace                                                | Struct                |                              |
| only\_allow\_merge\_if\_all\_discussions\_are\_resolved  | Boolean               |                              |
| only\_allow\_merge\_if\_pipeline\_succeeds               | Boolean               |                              |
| open\_issues\_count                                      | Integer               |                              |
| operations\_access\_level                                | String                |                              |
| order\_by                                                | String                | EQUAL\_TO                    |
| owned                                                    | Boolean               | EQUAL\_TO                    |
| packages\_enabled                                        | Boolean               |                              |
| pages\_access\_level                                     | String                |                              |
| path                                                     | String                |                              |
| path\_with\_namespace                                    | String                |                              |
| permissions                                              | Struct                |                              |
| printing\_merge\_request\_link\_enabled                  | Boolean               |                              |
| public\_jobs                                             | Boolean               |                              |
| readme\_url                                              | String                |                              |
| remove\_source\_branch\_after\_merge                     | Boolean               |                              |
| repository\_access\_level                                | String                |                              |
| repository\_storage                                      | String                | EQUAL\_TO                    |
| request\_access\_enabled                                 | Boolean               |                              |
| requirements\_access\_level                              | String                |                              |
| requirements\_enabled                                    | Boolean               |                              |
| resolve\_outdated\_diff\_discussions                     | Boolean               |                              |
| restrict\_user\_defined\_variables                       | Boolean               |                              |
| runner\_token\_expiration\_interval                      | String                |                              |
| search                                                   | String                | EQUAL\_TO                    |
| search\_namespaces                                       | Boolean               | EQUAL\_TO                    |
| security\_and\_compliance\_access\_level                 | String                |                              |
| security\_and\_compliance\_enabled                       | Boolean               |                              |
| service\_desk\_enabled                                   | Boolean               |                              |
| shared\_runners\_enabled                                 | Boolean               |                              |
| shared\_with\_groups                                     | List                  |                              |
| simple                                                   | Boolean               | EQUAL\_TO                    |
| snippets\_access\_level                                  | String                |                              |
| snippets\_enabled                                        | Boolean               |                              |
| sort                                                     | String                | EQUAL\_TO                    |
| squash\_commit\_template                                 | String                |                              |
| squash\_option                                           | String                |                              |
| ssh\_url\_to\_repo                                       | String                |                              |
| star\_count                                              | Integer               |                              |
| starred                                                  | Boolean               | EQUAL\_TO                    |
| statistics                                               | Boolean               | EQUAL\_TO                    |
| suggestion\_commit\_message                              | String                |                              |
| tag\_list                                                | List                  |                              |
| topic                                                    | String                | EQUAL\_TO                    |
| topic\_id                                                | Integer               | EQUAL\_TO                    |
| topics                                                   | List                  |                              |
| visibility                                               | String                | EQUAL\_TO                    |
| web\_url                                                 | String                |                              |
| wiki\_access\_level                                      | String                |                              |
| wiki\_enabled                                            | Boolean               |                              |
| with\_custom\_attributes                                 | Boolean               | EQUAL\_TO                    |
| with\_issues\_enabled                                    | Boolean               | EQUAL\_TO                    |
| with\_merge\_requests\_enabled                           | Boolean               | EQUAL\_TO                    |
| with\_programming\_language                              | Boolean               | EQUAL\_TO                    |
| Project Label                                            | closed\_issues\_count | Integer                      |                       |
| color                                                    | String                |                              |
| description                                              | String                |                              |
| description\_html                                        | String                |                              |
| id                                                       | Integer               |                              |
| include\_ancestor\_groups                                | Boolean               | EQUAL\_TO                    |
| is\_project\_label                                       | Boolean               |                              |
| name                                                     | String                |                              |
| open\_issues\_count                                      | Integer               |                              |
| open\_merge\_requests\_count                             | Integer               |                              |
| priority                                                 | Integer               |                              |
| search                                                   | String                | EQUAL\_TO                    |
| subscribed                                               | Boolean               |                              |
| text\_color                                              | String                |                              |
| with\_counts                                             | Boolean               | EQUAL\_TO                    |
| Project Member                                           | access\_level         | Integer                      |                       |
| avatar\_url                                              | String                |                              |
| created\_at                                              | DateTime              |                              |
| created\_by                                              | Struct                |                              |
| email                                                    | String                |                              |
| expires\_at                                              | DateTime              |                              |
| group\_saml\_identity                                    | Struct                |                              |
| id                                                       | Integer               |                              |
| is\_using\_seat                                          | String                |                              |
| membership\_state                                        | String                |                              |
| name                                                     | String                |                              |
| query                                                    | String                | EQUAL\_TO                    |
| show\_seat\_info                                         | Boolean               | EQUAL\_TO                    |
| skip\_users                                              | Integer               | EQUAL\_TO                    |
| state                                                    | String                |                              |
| user\_ids                                                | Integer               | EQUAL\_TO                    |
| username                                                 | String                |                              |
| web\_url                                                 | String                |                              |
| Project Merge Request                                    | allow\_collaboration  | Boolean                      |                       |
| allow\_maintainer\_to\_push                              | Boolean               |                              |
| approvals\_before\_merge                                 | String                |                              |
| assignee                                                 | Struct                |                              |
| assignee\_id                                             | Integer               | EQUAL\_TO                    |
| assignees                                                | List                  |                              |
| author                                                   | Struct                |                              |
| author\_id                                               | Integer               | EQUAL\_TO                    |
| author\_username                                         | Integer               | EQUAL\_TO                    |
| blocking\_discussions\_resolved                          | Boolean               |                              |
| closed\_at                                               | DateTime              |                              |
| closed\_by                                               | String                |                              |
| created\_after                                           | DateTime              | GREATER\_THAN\_OR\_EQUAL\_TO |
| created\_at                                              | DateTime              |                              |
| created\_before                                          | DateTime              | LESS\_THAN\_OR\_EQUAL\_TO    |
| created\_before\_after                                   | DateTime              | BETWEEN                      |
| deployed\_after                                          | DateTime              | GREATER\_THAN\_OR\_EQUAL\_TO |
| deployed\_before                                         | DateTime              | LESS\_THAN\_OR\_EQUAL\_TO    |
| deployed\_before\_after                                  | DateTime              | BETWEEN                      |
| description                                              | String                |                              |
| discussion\_locked                                       | String                |                              |
| downvotes                                                | Integer               |                              |
| draft                                                    | Boolean               |                              |
| environment                                              | String                | EQUAL\_TO                    |
| force\_remove\_source\_branch                            | Boolean               |                              |
| has\_conflicts                                           | Boolean               |                              |
| id                                                       | Integer               |                              |
| iid                                                      | Integer               |                              |
| labels                                                   | List                  |                              |
| merge\_commit\_sha                                       | String                |                              |
| merge\_status                                            | String                |                              |
| merge\_user                                              | Struct                |                              |
| merge\_when\_pipeline\_succeeds                          | Boolean               |                              |
| merged\_at                                               | DateTime              |                              |
| merged\_by                                               | Struct                |                              |
| milestone                                                | Struct                |                              |
| my\_reaction\_emoji                                      | String                | EQUAL\_TO                    |
| order\_by                                                | String                | EQUAL\_TO                    |
| project\_id                                              | Integer               |                              |
| references                                               | Struct                |                              |
| reviewer\_id                                             | Integer               | EQUAL\_TO                    |
| reviewer\_username                                       | String                | EQUAL\_TO                    |
| reviewers                                                | List                  |                              |
| scope                                                    | String                | EQUAL\_TO                    |
| search                                                   | String                | EQUAL\_TO                    |
| sha                                                      | String                |                              |
| should\_remove\_source\_branch                           | Boolean               |                              |
| sort                                                     | String                | EQUAL\_TO                    |
| source\_branch                                           | String                | EQUAL\_TO                    |
| source\_project\_id                                      | Integer               |                              |
| squash                                                   | Boolean               |                              |
| squash\_commit\_sha                                      | String                |                              |
| state                                                    | String                | EQUAL\_TO                    |
| target\_branch                                           | String                | EQUAL\_TO                    |
| target\_project\_id                                      | Integer               |                              |
| task\_completion\_status                                 | Struct                |                              |
| time\_stats                                              | Struct                |                              |
| title                                                    | String                |                              |
| updated\_after                                           | DateTime              | GREATER\_THAN\_OR\_EQUAL\_TO |
| updated\_at                                              | DateTime              |                              |
| updated\_before                                          | DateTime              | LESS\_THAN\_OR\_EQUAL\_TO    |
| updated\_before\_after                                   | DateTime              | BETWEEN                      |
| upvotes                                                  | Integer               |                              |
| user\_notes\_count                                       | Integer               |                              |
| view                                                     | String                | EQUAL\_TO                    |
| web\_url                                                 | String                |                              |
| wip                                                      | String                | EQUAL\_TO                    |
| with\_labels\_details                                    | Boolean               | EQUAL\_TO                    |
| with\_merge\_status\_recheck                             | Boolean               | EQUAL\_TO                    |
| work\_in\_progress                                       | Boolean               |                              |
| Project milestone                                        | created\_at           | DateTime                     |                       |
| description                                              | String                |                              |
| due\_date                                                | Date                  |                              |
| expired                                                  | Boolean               |                              |
| id                                                       | Integer               |                              |
| iid                                                      | Integer               |                              |
| iids                                                     | Integer               | EQUAL\_TO                    |
| include\_parent\_milestones                              | Boolean               | EQUAL\_TO                    |
| project\_id                                              | Integer               |                              |
| search                                                   | String                | EQUAL\_TO                    |
| start\_date                                              | Date                  |                              |
| state                                                    | String                | EQUAL\_TO                    |
| title                                                    | String                | EQUAL\_TO                    |
| updated\_at                                              | DateTime              |                              |
| web\_url                                                 | String                |                              |
| Release                                                  | \_links               | Struct                       |                       |
| assets                                                   | Struct                |                              |
| author                                                   | Struct                |                              |
| commit                                                   | Struct                |                              |
| commit\_path                                             | String                |                              |
| created\_at                                              | DateTime              |                              |
| description                                              | String                |                              |
| evidences                                                | List                  |                              |
| include\_html\_description                               | Boolean               | EQUAL\_TO                    |
| milestones                                               | List                  |                              |
| name                                                     | String                |                              |
| order\_by                                                | String                | EQUAL\_TO                    |
| released\_at                                             | DateTime              |                              |
| sort                                                     | String                | EQUAL\_TO                    |
| tag\_name                                                | String                |                              |
| tag\_path                                                | String                |                              |
| upcoming\_release                                        | Boolean               |                              |
| Tag                                                      | commit                | Struct                       |                       |
| message                                                  | String                |                              |
| name                                                     | String                |                              |
| order\_by                                                | String                | EQUAL\_TO                    |
| protected                                                | Boolean               |                              |
| release                                                  | Struct                |                              |
| search                                                   | String                | EQUAL\_TO                    |
| sort                                                     | String                | EQUAL\_TO                    |
| target                                                   | String                |                              |
