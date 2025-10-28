# Configuring a Microsoft Exchange plugin for

Amazon Q Business

Microsoft Exchange is an enterprise collaboration tool for messaging, meetings, and file
sharing. If you’re a Microsoft Exchange user, you can create an Amazon Q Business
plugin to allow your end users to get events from their calendars and get emails from within
their web experience chat.

To create a Microsoft Exchange plugin, you need configuration information from your
Microsoft Exchange instance to set up a connection between Amazon Q and
Microsoft Exchange and allow Amazon Q to perform actions in Microsoft Exchange.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#exchange-plugin-prereqs "#exchange-plugin-prereqs")
- [Service access roles](#exchange-plugin-iam "#exchange-plugin-iam")
- [Creating a plugin](#exchange-plugin-create "#exchange-plugin-create")

## Prerequisites

Before you configure your Amazon Q Microsoft Exchange plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 Microsoft Exchange app in the
  Microsoft Exchange developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate#register-an-application "https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate#register-an-application") in Microsoft Exchange Developer
  Documentation. Select **Accounts** in any organizational
  directly under **Supported Account Types**.
- Make sure you've added following required scopes: `mail.read`,
  `mail.send`, `calendars.readwrite`.
- Note the domain URL of your Microsoft Exchange instance. For example:
  `https://graph.microsoft.com/v1.0`.
- Note your:

      + **Access token URL** – For
       Microsoft Exchange OAuth applications, this is
       `https://login.microsoftonline.com/common/oauth2/v2.0/token`.
      + **Authorization URL** – For
       Microsoft Exchange OAuth applications, this is
       `https://login.microsoftonline.com/common/oauth2/v2.0/authorize`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The client ID
       generated when you create your OAuth 2.0 application in
       Microsoft Exchange.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       Microsoft Exchange.

  You will need this authentication information during the plugin configuration
  process.

## Service access roles

To successfully connect Amazon Q to Microsoft Exchange, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your Microsoft Exchange
credentials. Amazon Q assumes this role to access
your Microsoft Exchange credentials.

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

To create a Microsoft Exchange plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a Microsoft Exchange plugin using the
console and code examples for the AWS CLI.

Console
**To create a Microsoft Exchange plugin**

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
   **Microsoft Exchange**.
6. For **Microsoft Exchange**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      Microsoft Exchange domain URL. For example,
      `https://graph.microsoft.com/v1.0`.
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
           Microsoft Exchange.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in Microsoft Exchange.
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
         URL** – For Microsoft Exchange
         OAuth applications, this is
         `https://login.microsoftonline.com/common/oauth2/v2.0/token`.
      3. For **Authorization
         URL** – For Microsoft Exchange
         OAuth applications, this is
         `https://login.microsoftonline.com/common/oauth2/v2.0/authorize`.

   4. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Choose **Save**.

AWS CLI
**To create a Microsoft Exchange
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `MICROSOFT_EXCHANGE` \
--server-url `https://graph.microsoft.com/v1.0` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
