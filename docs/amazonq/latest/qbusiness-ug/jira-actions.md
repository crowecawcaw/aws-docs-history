# Configuring a Jira Cloud plugin for

Amazon Q Business

Jira Cloud is a project management tool that creates issues (tickets) for software
development, product management, and bug tracking. If you’re a Jira Cloud user, you
can create an Amazon Q Business plugin to allow your end users to perform the
following actions from within their web experience chat:

- Read issues
- Create issues
- Search issues
- Change issue status
- Delete issue
- Read sprint
- Move issue to sprint
- Create sprint
- Delete sprint
  To create a Jira Cloud plugin, you need configuration information from your
  Jira Cloud instance to set up a connection between Amazon Q and
  Jira Cloud and allow Amazon Q to perform actions in
  Jira Cloud.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#jira-plugin-prereqs "#jira-plugin-prereqs")
- [Service access roles](#jira-plugin-iam "#jira-plugin-iam")
- [Creating a plugin](#jira-plugin-create "#jira-plugin-create")

## Prerequisites

Before you configure your Amazon Q Jira Cloud plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 Jira Cloud app in the
  Jira Cloud developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [OAuth 2.0 (3LO) apps](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/ "https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/") in Jira Cloud Developer
  Documentation.
- Make sure sharing is enabled and the following required scopes are
  added:
  - `read:jira-work`
  - `write:jira-work`
  - `manage:jira-project`
  - `read:sprint:jira-software`
  - `write:sprint:jira-software`
  - `delete:sprint:jira-software`
  - `read:board-scope:jira-software`
  - `read:project:jira`

- Note the domain URL of your Jira Cloud instance. For example:
  `https://api.atlassian.com/ex/jira/`yourInstanceId``.
  To learn how to retrieve your instance ID (Cloud Site ID), go to [How to retrieve Cloud Site Id](https://confluence.atlassian.com/cloudkb/retrieve-my-atlassian-site-s-cloud-id-1272283178.html "https://confluence.atlassian.com/cloudkb/retrieve-my-atlassian-site-s-cloud-id-1272283178.html") in Jira Software
  Support.
- Note your:

      + **Access token URL** – For
       Jira Cloud OAuth applications, this is
       `https://auth.atlassian.com/oauth/token`.
      + **Authorization URL** – For
       Jira Cloud OAuth applications, this is
       `https://auth.atlassian.com/authorize`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The client ID
       generated when you create your OAuth 2.0 application in
       Jira Cloud.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       Jira Cloud.

  You will need this authentication information during the plugin configuration
  process.

## Service access roles

To successfully connect Amazon Q to Jira Cloud, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your Jira Cloud
credentials. Amazon Q assumes this role to access
your Jira Cloud credentials.

The following is the service access IAM role required:

```
{
    "Version": "2012-10-17",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:{{your-region}}:{{your-account-id}}:secret:[[secret-id]]"
            ]
        }
    ]
}
```

To allow Amazon Q to assume a role, use the following trust policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "QBusinessApplicationTrustPolicy",
      "Effect": "Allow",
      "Principal": {
        "Service": "qbusiness.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{source_account}}"
        },
        "ArnLike": {
          "aws:SourceArn":"arn:aws:qbusiness:{{your-region}}:{{source_account}}:application/{{application_id}}"
        }
      }
    }
  ]
}

```

If you use the console and choose to create a new IAM role,
Amazon Q creates the role for you. If you use the console and choose
to use an existing secret, or you use the API, make sure your IAM role contains these
permissions.

## Creating a plugin

To create a Jira Cloud plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a Jira Cloud plugin using the
console and code examples for the AWS CLI.

Console
**To create a Jira Cloud plugin**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the Amazon Q console, in
   **Applications**, select the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. For **Plugins**, choose **Add
   plugin**.
5. For **Add plugins**, choose
   **Jira Cloud**.
6. For **Jira Cloud**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      Jira Cloud domain URL. For example,
      `https://api.atlassian.com/ex/jira/`yourInstanceId``.
   3. **OAuth 2.0 authentication** – do
      the following:
      1. For **AWS Secrets Manager secret** –
         Choose **Create and add a new
         secret** or **Use an existing
         one**. Your secret must contain the
         following information:
         - **Secret name** – A
           name for your Secrets Manager secret.
         - **Client ID**
           – The client ID generated when you create
           your OAuth 2.0 application in
           Jira Cloud.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in Jira Cloud.
         - For **Redirect
           URL** – The URL to which user
           needs to be redirected after authentication. If
           your deployed web url is
           `<q-endpoint>`, use
           `<q-endpoint>/oauth/callback` .
           Amazon Q Business will handle OAuth tokens
           in this URL. This callback URL needs to be
           allowlisted in your third-party
           application.

      2. For **Access token
         URL** – For Jira Cloud
         OAuth applications, this is
         `https://auth.atlassian.com/oauth/token`.
      3. For **Authorization
         URL** – For Jira Cloud
         OAuth applications, this is
         `https://auth.atlassian.com/authorize`.

   4. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Choose **Save**.

AWS CLI
**To create a Jira Cloud
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `JIRA_CLOUD` \
--server-url  `https://api.atlassian.com/ex/jira/`yourInstanceId`` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
