# Configuring an Atlassian Confluence plugin for Amazon Q Business

Atlassian Confluence is a collaborative work-management tool designed for sharing, storing,
and working on project planning, software development, and product management. If you’re a
Atlassian Confluence user, you can create an Amazon Q Business plugin to allow your end
users to search pages from within their web experience chat.

To create a Atlassian Confluence plugin, you need configuration information from your
Atlassian Confluence instance to set up a connection between Amazon Q and
Atlassian Confluence and allow Amazon Q to perform actions in Atlassian Confluence.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#confluence-plugin-prereqs "#confluence-plugin-prereqs")
- [Service access roles](#confluence-plugin-iam "#confluence-plugin-iam")
- [Creating a plugin](#confluence-plugin-create "#confluence-plugin-create")

## Prerequisites

Before you configure your Amazon Q Atlassian Confluence plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 Atlassian Confluence app in the
  Atlassian Confluence developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [OAuth 2.0 (3LO) apps](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/ "https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/") in Atlassian Confluence Developer Documentation.
  Make sure sharing is enabled. Required scopes:
  `search:confluence`.
- Note the domain URL of your Atlassian Confluence instance. For example:
  `https://api.atlassian.com/ex/confluence/`yourInstanceId``.
  To learn how to retrieve your instance ID (Cloud Site ID), go to [How to retrieve Cloud Site Id](https://confluence.atlassian.com/cloudkb/retrieve-my-atlassian-site-s-cloud-id-1272283178.html "https://confluence.atlassian.com/cloudkb/retrieve-my-atlassian-site-s-cloud-id-1272283178.html").
- Note your:

      + **Access token URL** – For
       Atlassian Confluence OAuth applications, this is
       `https://auth.atlassian.com/oauth/token`.
      + **Authorization URL** – For
       Atlassian Confluence OAuth applications, this is
       `https://auth.atlassian.com/authorize`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The client ID
       generated when you create your OAuth 2.0 application in
       Atlassian Confluence.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       Atlassian Confluence.

  You will need this authentication information during the plugin configuration
  process.

## Service access roles

To successfully connect Amazon Q to Atlassian Confluence, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your Atlassian Confluence
credentials. Amazon Q assumes this role to access
your Atlassian Confluence credentials.

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

To create a Atlassian Confluence plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a Atlassian Confluence plugin using the
console and code examples for the AWS CLI.

Console
**To create a Atlassian Confluence plugin**

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
   **Atlassian Confluence**.
6. For **Atlassian Confluence**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      Atlassian Confluence domain URL. For example,
      `https://api.atlassian.com/ex/confluence/`yourInstanceId``.
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
           Atlassian Confluence.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in Atlassian Confluence.
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
         URL** – For Atlassian Confluence
         OAuth applications, this is
         `https://auth.atlassian.com/oauth/token`.
      3. For **Authorization
         URL** – For Atlassian Confluence
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
**To create a Atlassian Confluence
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `ATLASSIAN_CONFLUENCE` \
--server-url `https://api.atlassian.com/ex/confluence/`yourInstanceId`` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
