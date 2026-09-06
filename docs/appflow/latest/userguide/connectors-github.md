

# GitHub connector for Amazon AppFlow
<a name="connectors-github"></a>

GitHub is a service that hosts code repositories for software developers, and it provides version control with Git. If you're a GitHub user, your account contains data about your repositories, such as branches, commits, and pull requests. You can use Amazon AppFlow to transfer data from GitHub to certain AWS services or other supported applications.

## Amazon AppFlow support for GitHub
<a name="github-support"></a>

Amazon AppFlow supports GitHub as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from GitHub.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to GitHub.

## Before you begin
<a name="github-prereqs"></a>

To use Amazon AppFlow to transfer data from GitHub to supported destinations, you must meet these requirements:
+ You have an account with GitHub that contains the data that you want to transfer. For more information about the GitHub data objects that Amazon AppFlow supports, see [Supported objects](#github-objects).
+ In the developer settings of your account, you've created either of the following resources for Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account.
  + An OAuth app. For the steps to create one, see [Creating an OAuth App](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app) in the GitHub Docs.
  + A personal access token. For the steps to create one, see [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) in the GitHub Docs.
+ If you created an OAuth app, you've configured it with the following settings:
  + You've set the homepage URL to `https://console.aws.amazon.com/appflow/home`.
  + You've specified a callback URL for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from GitHub. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
  + You've generated a client secret.
+ If you created a personal access token, it permits the following recommended scopes. If you want to allow fewer scopes, you can omit any that apply to objects that you don't want to transfer.
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

  For more information about these scopes, see [Available scopes](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes) in the GitHub Docs.

If you created an OAuth app, note the client ID and client secret. If you created a personal access token, note the token value. You provide these values to Amazon AppFlow when you connect to your GitHub account.

## Connecting Amazon AppFlow to your GitHub account
<a name="github-connecting"></a>

To connect Amazon AppFlow to your GitHub account, provide the client credentials from your OAuth app, or provide a personal access token. If you haven't yet configured your GitHub account for Amazon AppFlow integration, see [Before you begin](#github-prereqs).

**To connect to GitHub**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **GitHub**.

1. Choose **Create connection**.

1. In the **Connect to GitHub** window, for **Select authentication type**, choose how to authenticate Amazon AppFlow with your GitHub account when it requests to access your data:
   + Choose **OAuth2** to authenticate Amazon AppFlow with the client ID and client secret from an OAuth app. Then, enter values for **Client ID** and **Client secret**.
   + Choose **BasicAuthPersonalAccessToken** to authenticate Amazon AppFlow with a personal access token. Then, enter values for **User name** and **Personal Access Token**.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**. A window appears that asks if you want to allow Amazon AppFlow to access your GitHub account.

1. Choose **Authorize**.

1. Confirm the access request with GitHub. You can choose **Send SMS** to use a two-factor authentication code, or you can choose **Use your password** to enter your password.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses GitHub as the data source, you can select this connection.

## Transferring data from GitHub with a flow
<a name="github-transfer-data"></a>

To transfer data from GitHub, create an Amazon AppFlow flow, and choose GitHub as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for GitHub, see [Supported objects](#github-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#github-destinations).

## Supported destinations
<a name="github-destinations"></a>

When you create a flow that uses GitHub as the data source, you can set the destination to any of the following connectors: 
+ [Amazon Lookout for Metrics](lookout.md)
+ [Amazon Redshift](redshift.md)
+ [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md)
+ [Amazon S3](s3.md)
+ [HubSpot](connectors-hubspot.md)
+ [Marketo](marketo.md)
+ [Salesforce](salesforce.md)
+ [SAP OData](sapodata.md)
+ [Snowflake](snowflake.md)
+ [Upsolver](upsolver.md)
+ [Zendesk](zendesk.md)
+ [Zoho CRM](connectors-zoho-crm.md)

## Supported objects
<a name="github-objects"></a>

When you create a flow that uses GitHub as the data source, you can transfer any of the following data objects to supported destinations:



- ** Branch**
  - **** Field**:** Commit / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Protected / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Protection / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Protection URL / **** Data type**:** String / **** Supported filters**:** 

- ** Card (aka Project Card)**
  - **** Field**:** Archived / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Archived State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Column URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Content URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creator / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Project URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Long / **** Supported filters**:** 

- ** Commit**
  - **** Field**:** Author / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commit / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Commit Author Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Committer / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parents / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** SHA / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** Commit Comment**
  - **** Field**:** Author Association / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commit ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Line / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Position / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Reactions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Long / **** Supported filters**:** 

- ** Commit Pull Request**
  - **** Field**:** Active Lock Reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Assignee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Assignees / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Author Association / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Auto Merge / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Base / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Closed at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commits URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Diff URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Draft / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Head / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Issue URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Labels / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Locked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Merge Commit SHA / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Merged at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Milestone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Patch URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Requested Reviewers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Requested Teams / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Review Comment URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Review Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Statuses URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** \_links / **** Data type**:** Struct / **** Supported filters**:** 

- ** Deployment**
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creator / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Environment / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Original Environment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Payload / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Performed via GitHub app / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Production Environment / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Repository URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SHA / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Statuses URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Task / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Transient Environment / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ref / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Deployment Status**
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creator / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Deployment URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Environment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Environment URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Log URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Performed via GitHub app / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Repository URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Target URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Fork**
  - **** Field**:** Allow Forking / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Archive URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Archived / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Assignees URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Blobs URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Branches URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Clone URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Collaborators URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commits URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Compare URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contents URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contributors URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Default Branch / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Deployments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Disabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Downloads URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fork / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Forks / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Forks Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Forks URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Full Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Git Commits URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Git Refs URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Git Tags URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Git URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Has Downloads / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Issues / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Pages / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Projects / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Wiki / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Homepage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Hooks URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Is Template / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Issue Comment URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Issue Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Issues URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Keys URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Labels URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Language / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Languages URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** License / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Merges URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Milestones URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mirror URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Notifications URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Open Issues / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Open Issues Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Permissions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Private / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Pulls URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pushed at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Releases URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SSH URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SVN URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Size / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Stargazers Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Stargazers URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Statuses URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscribers URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscription URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tags URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Teams URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Topics / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Trees URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Visibility / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Watchers / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Watchers Count / **** Data type**:** Long / **** Supported filters**:** 

- ** Issue**
  - **** Field**:** Active Lock Reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Assignee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Assignees / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Author Association / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Closed at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Closed by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Comments / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Filter / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Issue Labels Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Labels / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Labels URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Locked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Milestone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Performed via GitHub App / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Reactions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Repository URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Timeline URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** User / **** Data type**:** Struct / **** Supported filters**:** 

- ** Issue Assignee**
  - **** Field**:** Avatar URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Followers URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Following URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gists URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gravatar ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Login / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Organizations URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Received Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Repos URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Site Admin / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Starred URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscriptions URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

- ** Issue Comment**
  - **** Field**:** Author Association / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Issue URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Performed via GitHub app / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Reactions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** User / **** Data type**:** Struct / **** Supported filters**:** 

- ** Issue Event**
  - **** Field**:** Actor / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Assignee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Assigner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Commit ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commit URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Event / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Performed via GitHub app / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

- ** Label**
  - **** Field**:** Color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

- ** Milestone**
  - **** Field**:** Closed Issues / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Closed at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creator / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Due on / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Labels URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Open Issues / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Organization**
  - **** Field**:** Avatar URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Hooks URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Issues URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Login / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Members URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Public Members URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Repos URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

- ** Project**
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creator / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Organization Permission / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Private / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Project Column**
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Pull Request**
  - **** Field**:** Active Lock Reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Assignee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Assignees / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Author Association / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Auto Merge / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Base / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Closed at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commits URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Diff URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Draft / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Head / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Issue URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Labels / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Locked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Merge Commit SHA / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Merged at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Milestone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Patch URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pull Request Base / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Pull Request Head Label / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Requested Reviewers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Requested Teams / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Review Comment URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Review Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Statuses URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** \_links / **** Data type**:** Struct / **** Supported filters**:** 

- ** Pull Request Commit**
  - **** Field**:** Author / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commit / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Committer / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parents / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** SHA / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

- ** Pull Request Review**
  - **** Field**:** Author Association / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commit ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pull Request URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Submitted at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** \_links / **** Data type**:** Struct / **** Supported filters**:** 

- ** Release**
  - **** Field**:** Assets / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Assets URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Author / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Draft / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Prerelease / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Published at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Tag Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tarball URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Target Commitish / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Upload URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Zipball URL / **** Data type**:** String / **** Supported filters**:** 

- ** Repository**
  - **** Field**:** Allow Auto Merge / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Allow Forking / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Allow Merge Commit / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Allow Rebase Merge / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Allow Squash Merge / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Allow Update Branch / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Archive URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Archived / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Assignees URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Blobs URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Branches URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Clone URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Collaborators URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Commits URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Compare URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contents URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contributors URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Default Branch / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Delete Branch on Merge / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Deployments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Disabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Downloads URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fork / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Forks / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Forks Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Forks URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Full Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Git Commits URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Git Refs URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Git Tags URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Git URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Has Downloads / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Issues / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Pages / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Projects / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Wiki / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Homepage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Hooks URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Is Template / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Issue Comment URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Issue Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Issues URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Keys URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Labels URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Language / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Languages URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** License / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Merges URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Milestones URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mirror URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Network Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Notifications URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Open Issues / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Open Issues Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Permissions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Private / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Pulls URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pushed at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Releases URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SSH URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SVN URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Size / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Stargazers Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Stargazers URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Statuses URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscribers Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Subscribers URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscription URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tags URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Teams URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Temp Clone Token / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Topics / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Trees URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Visibility / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Watchers / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Watchers Count / **** Data type**:** Long / **** Supported filters**:** 

- ** Repository Issue**
  - **** Field**:** Active Lock Reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Assignee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Assignees / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Author Association / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Closed at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Closed by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Comments / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Comments URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creator / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Labels / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Labels URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Locked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Mentioned / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Milestone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Performed via GitHub App / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Reactions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Repository Issue Assignee Login / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Repository Issue Labels Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Repository Issue Milestone Number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Repository URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Timeline URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** User / **** Data type**:** Struct / **** Supported filters**:** 

- ** Repository Project**
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creator / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Organization Permission / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Private / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Review Comment**
  - **** Field**:** Author Association / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Commit ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Diff Hunk / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** In Reply to ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Node id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Original Commit ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Original Position / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Position / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Pull Request Review ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Pull Request URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** \_links / **** Data type**:** Struct / **** Supported filters**:** 

- ** Stargazer**
  - **** Field**:** Avatar URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Followers URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Following URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gists URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gravatar ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Login / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Organizations URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Received Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Repos URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Site Admin / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Starred URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscriptions URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

- ** Team**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Members URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parent / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Permission / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Privacy / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Repositories URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

- ** Team Member**
  - **** Field**:** Avatar URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Followers URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Following URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gists URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gravatar ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Login / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Organizations URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Received Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Repos URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Site Admin / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Starred URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscriptions URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

- ** Watcher**
  - **** Field**:** Avatar URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Followers URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Following URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gists URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gravatar ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HTML URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Login / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Node ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Organizations URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Received Events URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Repos URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Site Admin / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Starred URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscriptions URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 

