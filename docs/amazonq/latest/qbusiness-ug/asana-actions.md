# Configuring an Asana plugin for Amazon Q Business

Asana is a web-based work management platform that helps teams organize,
collaborate, and plan tasks. If you’re a Asana user, you can create an Amazon Q Business plugin to allow your end users to create and update tasks from within
their web experience chat.

To create a Asana plugin, you need configuration information from your
Asana instance to set up a connection between Amazon Q and
Asana and allow Amazon Q to perform actions in
Asana.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#asana-plugin-prereqs "#asana-plugin-prereqs")
- [Service access roles](#asana-plugin-iam "#asana-plugin-iam")
- [Creating a plugin](#asana-plugin-create "#asana-plugin-create")

## Prerequisites

Before you configure your Amazon Q Asana plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 Asana app in the
  Asana developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [OAuth](https://developers.asana.com/docs/oauth "https://developers.asana.com/docs/oauth") in
  Asana Developer Documentation.
- Make sure you've added following required scopes: `default`,
  `email`, `openid`, `profile`.
- Select the workspace you want this app to work with under **Choose
  distribution method**.
- Note the domain URL of your Asana instance. For example:
  `https://app.asana.com/api/1.0`.
- Note your:

      + **Access token URL** – For
       Asana OAuth applications, this is
       `https://app.asana.com/-/oauth_token`.
      + **Authorization URL** – For
       Asana OAuth applications, this is
       `https://app.asana.com/-/oauth_authorize`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The client ID
       generated when you create your OAuth 2.0 application in
       Asana.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       Asana.

  You will need this authentication information during the plugin configuration
  process.

## Service access roles

To successfully connect Amazon Q to Asana, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your Asana
credentials. Amazon Q assumes this role to access
your Asana credentials.

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

To create a Asana plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a Asana plugin using the
console and code examples for the AWS CLI.

Console
**To create a Asana plugin**

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
   **Asana**.
6. For **Asana**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      Asana domain URL. For example,
      `https://app.asana.com/api/1.0`.
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
           Asana.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in Asana.
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
         URL** – For Asana
         OAuth applications, this is
         `https://app.asana.com/-/oauth_token`.
      3. For **Authorization
         URL** – For Asana
         OAuth applications, this is
         `https://app.asana.com/-/oauth_authorize`
         or the authorization URL provided in the OAuth
         app.

   4. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Choose **Save**.

AWS CLI
**To create a Asana
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `ASANA` \
--server-url `https://app.asana.com/api/1.0` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
