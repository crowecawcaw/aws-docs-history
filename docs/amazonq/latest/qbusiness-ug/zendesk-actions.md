# Configuring a Zendesk Suite plugin for Amazon Q Business

Zendesk Suite is a customer relationship management system that helps businesses
automate and enhance customer support interactions by creating tickets to track work. If
you’re a Zendesk Suite user, you can create an Amazon Q Business plugin to allow
your end users to create, update, search for, and get ticket details from within their web
experience chat.

To create a Zendesk Suite plugin, you need configuration information from your
Zendesk Suite instance to set up a connection between Amazon Q and
Zendesk Suite and allow Amazon Q to perform actions in Zendesk Suite.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#zendesk-plugin-prereqs "#zendesk-plugin-prereqs")
- [Service access roles](#zendesk-plugin-iam "#zendesk-plugin-iam")
- [Creating a plugin](#zendesk-plugin-create "#zendesk-plugin-create")

## Prerequisites

Before you configure your Amazon Q Zendesk Suite plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 Zendesk Suite app in the
  Zendesk Suite developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [Using OAuth authentication with your application](https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application "https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application") in
  Zendesk Suite Developer Documentation.
- Make sure the following required scopes are added:
  - `tickets:read`
  - `tickets:write, read`

- Note the domain URL of your Zendesk Suite instance. For example:
  `https://`yourInstanceId`.zendesk.com`.
- Note your:

      + **Access token URL** – For
       Zendesk Suite OAuth applications, this is
       `https://`yourInstanceId`.zendesk.com/oauth/tokens`.
      + **Authorization URL** – For
       Zendesk Suite OAuth applications, this is
       `https://`yourInstanceId`.zendesk.com/oauth/authorizations/new`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The unique
       identifier generated when you create your OAuth 2.0 application in
       Zendesk Suite.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       Zendesk Suite.

  You will need this authentication information during the plugin configuration
  process.

## Service access roles

To successfully connect Amazon Q to Zendesk Suite, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your Zendesk Suite
credentials. Amazon Q assumes this role to access
your Zendesk Suite credentials.

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

To create a Zendesk Suite plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a Zendesk Suite plugin using the
console and code examples for the AWS CLI.

Console
**To create a Zendesk Suite plugin**

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
   **Zendesk Suite**.
6. For **Zendesk Suite**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      Zendesk Suite domain URL. For example,
      `https://`yourInstanceId`.zendesk.com`.
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
           Zendesk Suite.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in Zendesk Suite.
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
         URL** – For Zendesk Suite
         OAuth applications, this is
         `https://`yourInstanceId`.zendesk.com/oauth/tokens`.
      3. For **Authorization
         URL** – For Zendesk Suite
         OAuth applications, this is
         `https://`yourInstanceId`.zendesk.com/oauth/authorizations/new`.

   4. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Choose **Save**.

AWS CLI
**To create a Zendesk Suite
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `ZENDESK_SUITE` \
--server-url `https://`yourInstanceId`.zendesk.com` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
