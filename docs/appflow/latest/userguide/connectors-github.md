# GitHub connector for Amazon AppFlow

GitHub is a service that hosts code repositories for software developers, and it
provides version control with Git. If you're a GitHub user, your account contains data
about your repositories, such as branches, commits, and pull requests.
You can use Amazon AppFlow to transfer data from
GitHub to certain AWS services or other supported applications.

## Amazon AppFlow support for GitHub

Amazon AppFlow supports GitHub as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from GitHub.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to GitHub.

## Before you begin

To use Amazon AppFlow to transfer data from GitHub to supported destinations, you must meet these
requirements:

- You have an account with GitHub that contains the data that you want to transfer. For more
  information about the GitHub data objects that Amazon AppFlow supports, see [Supported objects](#github-objects "#github-objects").
- In the developer settings of your account, you've created either of the following
  resources for Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data
  securely when it makes authenticated calls to your account.
  - An OAuth app. For the steps to create one, see [Creating an OAuth App](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app "https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app") in the GitHub Docs.
  - A personal access token. For the steps to create one, see [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token") in the GitHub Docs.

- If you created an OAuth app, you've configured it with the following settings:
  - You've set the homepage URL to
    `https://console.aws.amazon.com/appflow/home`.
  - You've specified a callback URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from GitHub. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._
  - You've generated a client secret.

- If you created a personal access token, it permits the following recommended scopes. If
  you want to allow fewer scopes, you can omit any that apply to objects that you don't want to
  transfer.

      + `repo:status`
      + `repo_deployment`
      + `public_repo`
      + `security_events`
      + `admin:repo_hook`
      + `read:repo_hook`
      + `read:org`
      + `read:public_key`
      + `notifications`
      + `read:user`
      + `user:email`
      + `read:discussion`

  For more information about these scopes, see [Available scopes](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes "https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes") in the GitHub Docs.

If you created an OAuth app, note the client ID and client secret. If you created a personal
access token, note the token value. You provide these values to Amazon AppFlow when you connect to your
GitHub account.

## Connecting Amazon AppFlow to your GitHub

account

To connect Amazon AppFlow to your GitHub account, provide the client credentials from
your OAuth app, or provide a personal access token. If you haven't yet configured your
GitHub account for Amazon AppFlow integration, see [Before you begin](#github-prereqs "#github-prereqs").

###### To connect to GitHub

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **GitHub**.
4. Choose **Create connection**.
5. In the **Connect to GitHub** window, for **Select
   authentication type**, choose how to authenticate Amazon AppFlow with your GitHub
   account when it requests to access your data:
   - Choose **OAuth2** to authenticate Amazon AppFlow with the client ID and client
     secret from an OAuth app. Then, enter values for **Client ID** and
     **Client secret**.
   - Choose **BasicAuthPersonalAccessToken** to authenticate Amazon AppFlow with a
     personal access token. Then, enter values for **User name** and
     **Personal Access Token**.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. A window appears that asks if you want to allow
Amazon AppFlow to access your GitHub account. 9. Choose **Authorize**. 10. Confirm the access request with GitHub. You can choose **Send
SMS** to use a two-factor authentication code, or you can choose **Use your
password** to enter your password.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses GitHub as the data source, you can select this connection.

## Transferring data from GitHub with a flow

To transfer data from GitHub, create an Amazon AppFlow flow, and choose GitHub as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for GitHub, see [Supported objects](#github-objects "#github-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#github-destinations "#github-destinations").

## Supported destinations

When you create a flow that uses GitHub as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses GitHub as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                        | **Field**          | **Data type** | **Supported filters** |
| --------------------------------- | ------------------ | ------------- | --------------------- | ---------------------------- | -------- | -------- |
| Branch                            | Commit             | Struct        |                       |
| Name                              | String             |               |                       | Protected                    | Boolean  | EQUAL_TO |
| Protection                        | Struct             |               |                       | Protection URL               | String   |          |
| Card (aka Project Card)           | Archived           | Boolean       |                       |
| Archived State                    | String             | EQUAL_TO      |                       | Column URL                   | String   |          |
| Content URL                       | String             |               |                       | Created at                   | DateTime |          |
| Creator                           | Struct             |               |                       | Node ID                      | String   |          |
| Note                              | String             |               |                       | Project URL                  | String   |          |
| URL                               | String             |               |                       | Updated at                   | DateTime |          |
| id                                | Long               |               |
| Commit                            | Author             | Struct        |                       |
| Comments URL                      | String             |               |                       | Commit                       | Struct   |          |
| Commit Author Name                | String             | EQUAL_TO      |                       | Committer                    | Struct   |          |
| HTML URL                          | String             |               |                       | Node ID                      | String   |          |
| Parents                           | List               |               |                       | SHA                          | String   | EQUAL_TO |
| URL                               | String             |               |                       | Updated since                | DateTime | EQUAL_TO |
| Commit Comment                    | Author Association | String        |                       |
| Body                              | String             |               |                       | Commit ID                    | String   |          |
| Created at                        | DateTime           |               |                       | HTML URL                     | String   |          |
| Line                              | Long               |               |                       | Node ID                      | String   |          |
| Path                              | String             |               |                       | Position                     | Long     |          |
| Reactions                         | Struct             |               |                       | URL                          | String   |          |
| Updated at                        | DateTime           |               |                       | User                         | Struct   |          |
| id                                | Long               |               |
| Commit Pull Request               | Active Lock Reason | String        |                       |
| Assignee                          | Struct             |               |                       | Assignees                    | List     |          |
| Author Association                | String             |               |                       | Auto Merge                   | Struct   |          |
| Base                              | Struct             |               |                       | Body                         | String   |          |
| Closed at                         | DateTime           |               |                       | Comments URL                 | String   |          |
| Commits URL                       | String             |               |                       | Created at                   | DateTime |          |
| Diff URL                          | String             |               |                       | Draft                        | Boolean  |          |
| HTML URL                          | String             |               |                       | Head                         | Struct   |          |
| ID                                | Long               |               |                       | Issue URL                    | String   |          |
| Labels                            | List               |               |                       | Locked                       | Boolean  |          |
| Merge Commit SHA                  | String             |               |                       | Merged at                    | DateTime |          |
| Milestone                         | Struct             |               |                       | Node ID                      | String   |          |
| Number                            | Long               |               |                       | Patch URL                    | String   |          |
| Requested Reviewers               | List               |               |                       | Requested Teams              | List     |          |
| Review Comment URL                | String             |               |                       | Review Comments URL          | String   |          |
| State                             | String             |               |                       | Statuses URL                 | String   |          |
| Title                             | String             |               |                       | URL                          | String   |          |
| Updated at                        | DateTime           |               |                       | User                         | Struct   |          |
| \_links                           | Struct             |               |
| Deployment                        | Created at         | DateTime      |                       |
| Creator                           | Struct             |               |                       | Description                  | String   |          |
| Environment                       | String             | EQUAL_TO      |                       | ID                           | Long     |          |
| Node ID                           | String             |               |                       | Original Environment         | String   |          |
| Payload                           | Struct             |               |                       | Performed via GitHub app     | Struct   |          |
| Production Environment            | Boolean            |               |                       | Repository URL               | String   |          |
| SHA                               | String             | EQUAL_TO      |                       | Statuses URL                 | String   |          |
| Task                              | String             | EQUAL_TO      |                       | Transient Environment        | Boolean  |          |
| URL                               | String             |               |                       | Updated at                   | DateTime |          |
| ref                               | String             | EQUAL_TO      |
| Deployment Status                 | Created at         | DateTime      |                       |
| Creator                           | Struct             |               |                       | Deployment URL               | String   |          |
| Description                       | String             |               |                       | Environment                  | String   |          |
| Environment URL                   | String             |               |                       | ID                           | Long     |          |
| Log URL                           | String             |               |                       | Node ID                      | String   |          |
| Performed via GitHub app          | Struct             |               |                       | Repository URL               | String   |          |
| State                             | String             |               |                       | Target URL                   | String   |          |
| URL                               | String             |               |                       | Updated at                   | DateTime |          |
| Fork                              | Allow Forking      | Boolean       |                       |
| Archive URL                       | String             |               |                       | Archived                     | Boolean  |          |
| Assignees URL                     | String             |               |                       | Blobs URL                    | String   |          |
| Branches URL                      | String             |               |                       | Clone URL                    | String   |          |
| Collaborators URL                 | String             |               |                       | Comments URL                 | String   |          |
| Commits URL                       | String             |               |                       | Compare URL                  | String   |          |
| Contents URL                      | String             |               |                       | Contributors URL             | String   |          |
| Created at                        | DateTime           |               |                       | Default Branch               | String   |          |
| Deployments URL                   | String             |               |                       | Description                  | String   |          |
| Disabled                          | Boolean            |               |                       | Downloads URL                | String   |          |
| Events URL                        | String             |               |                       | Fork                         | Boolean  |          |
| Forks                             | Long               |               |                       | Forks Count                  | Long     |          |
| Forks URL                         | String             |               |                       | Full Name                    | String   |          |
| Git Commits URL                   | String             |               |                       | Git Refs URL                 | String   |          |
| Git Tags URL                      | String             |               |                       | Git URL                      | String   |          |
| HTML URL                          | String             |               |                       | Has Downloads                | Boolean  |          |
| Has Issues                        | Boolean            |               |                       | Has Pages                    | Boolean  |          |
| Has Projects                      | Boolean            |               |                       | Has Wiki                     | Boolean  |          |
| Homepage                          | String             |               |                       | Hooks URL                    | String   |          |
| ID                                | Long               |               |                       | Is Template                  | Boolean  |          |
| Issue Comment URL                 | String             |               |                       | Issue Events URL             | String   |          |
| Issues URL                        | String             |               |                       | Keys URL                     | String   |          |
| Labels URL                        | String             |               |                       | Language                     | String   |          |
| Languages URL                     | String             |               |                       | License                      | Struct   |          |
| Merges URL                        | String             |               |                       | Milestones URL               | String   |          |
| Mirror URL                        | String             |               |                       | Name                         | String   |          |
| Node ID                           | String             |               |                       | Notifications URL            | String   |          |
| Open Issues                       | Long               |               |                       | Open Issues Count            | Long     |          |
| Owner                             | Struct             |               |                       | Permissions                  | Struct   |          |
| Private                           | Boolean            |               |                       | Pulls URL                    | String   |          |
| Pushed at                         | DateTime           |               |                       | Releases URL                 | String   |          |
| SSH URL                           | String             |               |                       | SVN URL                      | String   |          |
| Size                              | Long               |               |                       | Stargazers Count             | Long     |          |
| Stargazers URL                    | String             |               |                       | Statuses URL                 | String   |          |
| Subscribers URL                   | String             |               |                       | Subscription URL             | String   |          |
| Tags URL                          | String             |               |                       | Teams URL                    | String   |          |
| Topics                            | List               |               |                       | Trees URL                    | String   |          |
| URL                               | String             |               |                       | Updated at                   | DateTime |          |
| Visibility                        | String             |               |                       | Watchers                     | Long     |          |
| Watchers Count                    | Long               |               |
| Issue                             | Active Lock Reason | String        |                       |
| Assignee                          | Struct             |               |                       | Assignees                    | List     |          |
| Author Association                | String             |               |                       | Body                         | String   |          |
| Closed at                         | DateTime           |               |                       | Closed by                    | Struct   |          |
| Comments                          | Long               |               |                       | Comments URL                 | String   |          |
| Created at                        | DateTime           |               |                       | Events URL                   | String   |          |
| Filter                            | String             | EQUAL_TO      |                       | HTML URL                     | String   |          |
| ID                                | Long               |               |                       | Issue Labels Name            | String   | EQUAL_TO |
| Labels                            | List               |               |                       | Labels URL                   | String   |          |
| Locked                            | Boolean            |               |                       | Milestone                    | Struct   |          |
| Node ID                           | String             |               |                       | Number                       | Long     |          |
| Performed via GitHub App          | Struct             |               |                       | Reactions                    | Struct   |          |
| Repository URL                    | String             |               |                       | State                        | String   | EQUAL_TO |
| Timeline URL                      | String             |               |                       | Title                        | String   |          |
| URL                               | String             |               |                       | Updated at                   | DateTime | EQUAL_TO |
| User                              | Struct             |               |
| Issue Assignee                    | Avatar URL         | String        |                       |
| Events URL                        | String             |               |                       | Followers URL                | String   |          |
| Following URL                     | String             |               |                       | Gists URL                    | String   |          |
| Gravatar ID                       | String             |               |                       | HTML URL                     | String   |          |
| ID                                | Long               |               |                       | Login                        | String   |          |
| Node ID                           | String             |               |                       | Organizations URL            | String   |          |
| Received Events URL               | String             |               |                       | Repos URL                    | String   |          |
| Site Admin                        | Boolean            |               |                       | Starred URL                  | String   |          |
| Subscriptions URL                 | String             |               |                       | Type                         | String   |          |
| URL                               | String             |               |
| Issue Comment                     | Author Association | String        |                       |
| Body                              | String             |               |                       | Created at                   | DateTime |          |
| HTML URL                          | String             |               |                       | ID                           | Long     |          |
| Issue URL                         | String             |               |                       | Node ID                      | String   |          |
| Performed via GitHub app          | Struct             |               |                       | Reactions                    | Struct   |          |
| URL                               | String             |               |                       | Updated at                   | DateTime | EQUAL_TO |
| User                              | Struct             |               |
| Issue Event                       | Actor              | Struct        |                       |
| Assignee                          | Struct             |               |                       | Assigner                     | Struct   |          |
| Commit ID                         | String             |               |                       | Commit URL                   | String   |          |
| Created at                        | DateTime           |               |                       | Event                        | String   |          |
| ID                                | Long               |               |                       | Node ID                      | String   |          |
| Performed via GitHub app          | Struct             |               |                       | URL                          | String   |          |
| Label                             | Color              | String        |                       |
| Default                           | Boolean            |               |                       | Description                  | String   |          |
| ID                                | Long               |               |                       | Name                         | String   |          |
| Node ID                           | String             |               |                       | URL                          | String   |          |
| Milestone                         | Closed Issues      | Long          |                       |
| Closed at                         | DateTime           |               |                       | Created at                   | DateTime |          |
| Creator                           | Struct             |               |                       | Description                  | String   |          |
| Due on                            | DateTime           |               |                       | HTML URL                     | String   |          |
| ID                                | Long               |               |                       | Labels URL                   | String   |          |
| Node ID                           | String             |               |                       | Number                       | Long     |          |
| Open Issues                       | Long               |               |                       | State                        | String   | EQUAL_TO |
| Title                             | String             |               |                       | URL                          | String   |          |
| Updated at                        | DateTime           |               |
| Organization                      | Avatar URL         | String        |                       |
| Description                       | String             |               |                       | Events URL                   | String   |          |
| Hooks URL                         | String             |               |                       | ID                           | Long     |          |
| Issues URL                        | String             |               |                       | Login                        | String   |          |
| Members URL                       | String             |               |                       | Node ID                      | String   |          |
| Public Members URL                | String             |               |                       | Repos URL                    | String   |          |
| URL                               | String             |               |
| Project                           | Body               | String        |                       |
| Created at                        | DateTime           |               |                       | Creator                      | Struct   |          |
| ID                                | Long               |               |                       | Name                         | String   |          |
| Node ID                           | String             |               |                       | Number                       | Long     |          |
| Organization Permission           | String             |               |                       | Private                      | Boolean  |          |
| State                             | String             | EQUAL_TO      |                       | Updated at                   | DateTime |          |
| Project Column                    | Created at         | DateTime      |                       |
| ID                                | Long               |               |                       | Name                         | String   |          |
| Node ID                           | String             |               |                       | Updated at                   | DateTime |          |
| Pull Request                      | Active Lock Reason | String        |                       |
| Assignee                          | Struct             |               |                       | Assignees                    | List     |          |
| Author Association                | String             |               |                       | Auto Merge                   | Struct   |          |
| Base                              | Struct             |               |                       | Body                         | String   |          |
| Closed at                         | DateTime           |               |                       | Comments URL                 | String   |          |
| Commits URL                       | String             |               |                       | Created at                   | DateTime |          |
| Diff URL                          | String             |               |                       | Draft                        | Boolean  |          |
| HTML URL                          | String             |               |                       | Head                         | Struct   |          |
| ID                                | Long               |               |                       | Issue URL                    | String   |          |
| Labels                            | List               |               |                       | Locked                       | Boolean  |          |
| Merge Commit SHA                  | String             |               |                       | Merged at                    | DateTime |          |
| Milestone                         | Struct             |               |                       | Node ID                      | String   |          |
| Number                            | Long               |               |                       | Patch URL                    | String   |          |
| Pull Request Base                 | String             | EQUAL_TO      |                       | Pull Request Head Label      | String   | EQUAL_TO |
| Requested Reviewers               | List               |               |                       | Requested Teams              | List     |          |
| Review Comment URL                | String             |               |                       | Review Comments URL          | String   |          |
| State                             | String             | EQUAL_TO      |                       | Statuses URL                 | String   |          |
| Title                             | String             |               |                       | URL                          | String   |          |
| Updated at                        | DateTime           |               |                       | User                         | Struct   |          |
| \_links                           | Struct             |               |
| Pull Request Commit               | Author             | Struct        |                       |
| Comments URL                      | String             |               |                       | Commit                       | Struct   |          |
| Committer                         | Struct             |               |                       | HTML URL                     | String   |          |
| Node ID                           | String             |               |                       | Parents                      | List     |          |
| SHA                               | String             |               |                       | URL                          | String   |          |
| Pull Request Review               | Author Association | String        |                       |
| Body                              | String             |               |                       | Commit ID                    | String   |          |
| HTML URL                          | String             |               |                       | ID                           | Long     |          |
| Node ID                           | String             |               |                       | Pull Request URL             | String   |          |
| State                             | String             |               |                       | Submitted at                 | DateTime |          |
| User                              | Struct             |               |                       | \_links                      | Struct   |          |
| Release                           | Assets             | List          |                       |
| Assets URL                        | String             |               |                       | Author                       | Struct   |          |
| Body                              | String             |               |                       | Created at                   | DateTime |          |
| Draft                             | Boolean            |               |                       | HTML URL                     | String   |          |
| ID                                | Long               |               |                       | Name                         | String   |          |
| Node ID                           | String             |               |                       | Prerelease                   | Boolean  |          |
| Published at                      | DateTime           |               |                       | Tag Name                     | String   |          |
| Tarball URL                       | String             |               |                       | Target Commitish             | String   |          |
| URL                               | String             |               |                       | Upload URL                   | String   |          |
| Zipball URL                       | String             |               |
| Repository                        | Allow Auto Merge   | Boolean       |                       |
| Allow Forking                     | Boolean            |               |                       | Allow Merge Commit           | Boolean  |          |
| Allow Rebase Merge                | Boolean            |               |                       | Allow Squash Merge           | Boolean  |          |
| Allow Update Branch               | Boolean            |               |                       | Archive URL                  | String   |          |
| Archived                          | Boolean            |               |                       | Assignees URL                | String   |          |
| Blobs URL                         | String             |               |                       | Branches URL                 | String   |          |
| Clone URL                         | String             |               |                       | Collaborators URL            | String   |          |
| Comments URL                      | String             |               |                       | Commits URL                  | String   |          |
| Compare URL                       | String             |               |                       | Contents URL                 | String   |          |
| Contributors URL                  | String             |               |                       | Created at                   | DateTime |          |
| Default Branch                    | String             |               |                       | Delete Branch on Merge       | Boolean  |          |
| Deployments URL                   | String             |               |                       | Description                  | String   |          |
| Disabled                          | Boolean            |               |                       | Downloads URL                | String   |          |
| Events URL                        | String             |               |                       | Fork                         | Boolean  |          |
| Forks                             | Long               |               |                       | Forks Count                  | Long     |          |
| Forks URL                         | String             |               |                       | Full Name                    | String   |          |
| Git Commits URL                   | String             |               |                       | Git Refs URL                 | String   |          |
| Git Tags URL                      | String             |               |                       | Git URL                      | String   |          |
| HTML URL                          | String             |               |                       | Has Downloads                | Boolean  |          |
| Has Issues                        | Boolean            |               |                       | Has Pages                    | Boolean  |          |
| Has Projects                      | Boolean            |               |                       | Has Wiki                     | Boolean  |          |
| Homepage                          | String             |               |                       | Hooks URL                    | String   |          |
| ID                                | Long               |               |                       | Is Template                  | Boolean  |          |
| Issue Comment URL                 | String             |               |                       | Issue Events URL             | String   |          |
| Issues URL                        | String             |               |                       | Keys URL                     | String   |          |
| Labels URL                        | String             |               |                       | Language                     | String   |          |
| Languages URL                     | String             |               |                       | License                      | Struct   |          |
| Merges URL                        | String             |               |                       | Milestones URL               | String   |          |
| Mirror URL                        | String             |               |                       | Name                         | String   |          |
| Network Count                     | Long               |               |                       | Node ID                      | String   |          |
| Notifications URL                 | String             |               |                       | Open Issues                  | Long     |          |
| Open Issues Count                 | Long               |               |                       | Owner                        | Struct   |          |
| Permissions                       | Struct             |               |                       | Private                      | Boolean  |          |
| Pulls URL                         | String             |               |                       | Pushed at                    | DateTime |          |
| Releases URL                      | String             |               |                       | SSH URL                      | String   |          |
| SVN URL                           | String             |               |                       | Size                         | Long     |          |
| Stargazers Count                  | Long               |               |                       | Stargazers URL               | String   |          |
| Statuses URL                      | String             |               |                       | Subscribers Count            | Long     |          |
| Subscribers URL                   | String             |               |                       | Subscription URL             | String   |          |
| Tags URL                          | String             |               |                       | Teams URL                    | String   |          |
| Temp Clone Token                  | String             |               |                       | Topics                       | List     |          |
| Trees URL                         | String             |               |                       | Type                         | String   | EQUAL_TO |
| URL                               | String             |               |                       | Updated at                   | DateTime |          |
| Visibility                        | String             |               |                       | Watchers                     | Long     |          |
| Watchers Count                    | Long               |               |
| Repository Issue                  | Active Lock Reason | String        |                       |
| Assignee                          | Struct             |               |                       | Assignees                    | List     |          |
| Author Association                | String             |               |                       | Body                         | String   |          |
| Closed at                         | DateTime           |               |                       | Closed by                    | Struct   |          |
| Comments                          | Long               |               |                       | Comments URL                 | String   |          |
| Created at                        | DateTime           |               |                       | Creator                      | String   | EQUAL_TO |
| Events URL                        | String             |               |                       | HTML URL                     | String   |          |
| ID                                | Long               |               |                       | Labels                       | List     |          |
| Labels URL                        | String             |               |                       | Locked                       | Boolean  |          |
| Mentioned                         | String             | EQUAL_TO      |                       | Milestone                    | Struct   |          |
| Node ID                           | String             |               |                       | Number                       | Long     |          |
| Performed via GitHub App          | Struct             |               |                       | Reactions                    | Struct   |          |
| Repository Issue Assignee Login   | String             | EQUAL_TO      |                       | Repository Issue Labels Name | String   | EQUAL_TO |
| Repository Issue Milestone Number | String             | EQUAL_TO      |                       | Repository URL               | String   |          |
| State                             | String             | EQUAL_TO      |                       | Timeline URL                 | String   |          |
| Title                             | String             |               |                       | URL                          | String   |          |
| Updated at                        | DateTime           | EQUAL_TO      |                       | User                         | Struct   |          |
| Repository Project                | Body               | String        |                       |
| Created at                        | DateTime           |               |                       | Creator                      | Struct   |          |
| ID                                | Long               |               |                       | Name                         | String   |          |
| Node ID                           | String             |               |                       | Number                       | Long     |          |
| Organization Permission           | String             |               |                       | Private                      | Boolean  |          |
| State                             | String             | EQUAL_TO      |                       | Updated at                   | DateTime |          |
| Review Comment                    | Author Association | String        |                       |
| Body                              | Struct             |               |                       | Commit ID                    | String   |          |
| Created at                        | DateTime           |               |                       | Diff Hunk                    | String   |          |
| HTML URL                          | String             |               |                       | ID                           | Long     |          |
| In Reply to ID                    | Long               |               |                       | Node id                      | String   |          |
| Original Commit ID                | String             |               |                       | Original Position            | Long     |          |
| Path                              | String             |               |                       | Position                     | Long     |          |
| Pull Request Review ID            | Long               |               |                       | Pull Request URL             | String   |          |
| URL                               | String             |               |                       | Updated at                   | DateTime | EQUAL_TO |
| User                              | Struct             |               |                       | \_links                      | Struct   |          |
| Stargazer                         | Avatar URL         | String        |                       |
| Events URL                        | String             |               |                       | Followers URL                | String   |          |
| Following URL                     | String             |               |                       | Gists URL                    | String   |          |
| Gravatar ID                       | String             |               |                       | HTML URL                     | String   |          |
| ID                                | Long               |               |                       | Login                        | String   |          |
| Node ID                           | String             |               |                       | Organizations URL            | String   |          |
| Received Events URL               | String             |               |                       | Repos URL                    | String   |          |
| Site Admin                        | String             |               |                       | Starred URL                  | String   |          |
| Subscriptions URL                 | String             |               |                       | Type                         | String   |          |
| URL                               | String             |               |
| Team                              | Description        | String        |                       |
| HTML URL                          | String             |               |                       | ID                           | Long     |          |
| Members URL                       | String             |               |                       | Name                         | String   |          |
| Node ID                           | String             |               |                       | Parent                       | Struct   |          |
| Permission                        | String             |               |                       | Privacy                      | String   |          |
| Repositories URL                  | String             |               |                       | Slug                         | String   |          |
| URL                               | String             |               |
| Team Member                       | Avatar URL         | String        |                       |
| Events URL                        | String             |               |                       | Followers URL                | String   |          |
| Following URL                     | String             |               |                       | Gists URL                    | String   |          |
| Gravatar ID                       | String             |               |                       | HTML URL                     | String   |          |
| ID                                | Long               |               |                       | Login                        | String   |          |
| Node ID                           | String             |               |                       | Organizations URL            | String   |          |
| Received Events URL               | String             |               |                       | Repos URL                    | String   |          |
| Site Admin                        | Boolean            |               |                       | Starred URL                  | String   |          |
| Subscriptions URL                 | String             |               |                       | Type                         | String   |          |
| URL                               | String             |               |
| Watcher                           | Avatar URL         | String        |                       |
| Events URL                        | String             |               |                       | Followers URL                | String   |          |
| Following URL                     | String             |               |                       | Gists URL                    | String   |          |
| Gravatar ID                       | String             |               |                       | HTML URL                     | String   |          |
| ID                                | Long               |               |                       | Login                        | String   |          |
| Node ID                           | String             |               |                       | Organizations URL            | String   |          |
| Received Events URL               | String             |               |                       | Repos URL                    | String   |          |
| Site Admin                        | Boolean            |               |                       | Starred URL                  | String   |          |
| Subscriptions URL                 | String             |               |                       | Type                         | String   |          |
| URL                               | String             |               |
