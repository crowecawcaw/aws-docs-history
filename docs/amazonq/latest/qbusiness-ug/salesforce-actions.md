# Configuring a Salesforce plugin for Amazon Q Business

Salesforce is a customer relationship management (CRM) tool for managing customer
interactions. If you’re a Salesforce user, you can create an Amazon Q Business
plugin to allow your end users to perform the following actions from within their web
experience chat:

- Managing cases (create, delete, update, get)
- Retrieving account lists
- Handling opportunities (create, update, delete, get, fetch specific)
- Fetching specific contacts

###### Note

The Salesforce plugin returns a maximum of 5 items per query to manage response size and performance.

To set up this plugin, you'll need configuration details from your Salesforce instance to
connect Amazon Q Business with Salesforce.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#salesforce-plugin-prereqs "#salesforce-plugin-prereqs")
- [Service access roles](#salesforce-plugin-iam "#salesforce-plugin-iam")
- [Creating a plugin](#salesforce-plugin-create "#salesforce-plugin-create")

## Prerequisites

Before you configure your Amazon Q Salesforce plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 Salesforce app in the
  Salesforce developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [Create a Connected App in Salesforce for OAuth](https://help.salesforce.com/s/articleView?id=platform.ev_relay_create_connected_app.htm&type=5 "https://help.salesforce.com/s/articleView?id=platform.ev_relay_create_connected_app.htm&type=5") in
  Salesforce Developer Documentation.
- Make sure to select **Yes** for **Enable
  Authorization Code and Credential Flow**, **Require Secret
  for Web Server Flow**, **Require Secret for Refresh Token
  Flow**, **Enable Token Exchange Flow**, and
  **Require Secret for Token Exchange Flow**.
- Make sure that the following required scopes are added:
  - `visualforce`
  - `address`
  - `custom_permissions`
  - `open_id`
  - `profile`
  - `refresh_token`
  - `wave_api`
  - `web`
  - `phome`
  - `offline_access`
  - `chatter_api`
  - `id`
  - `api`
  - `eclair_api`
  - `email`
  - `pardot_api`
  - `full`

- Note the domain URL of your Salesforce instance. For example:
  `https://`yourInstance`.my.salesforce.com/services/data/v60.0`.
- Note your:

      + **Access token URL** – For
       Salesforce OAuth applications, this is
       `https://login.salesforce.com/services/oauth2/token`.
      + **Authorization URL** – For
       Salesforce OAuth applications, this is
       `https://login.salesforce.com/services/oauth2/authorize`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The client ID
       generated when you create your OAuth 2.0 application in
       Salesforce.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       Salesforce.

  You will need this authentication information during the plugin configuration
  process.

###### Note

The Require Proof Key for Code Exchange (PKCE) extension option is not supported and it must be disabled in the Salesforce Connector application.

## Service access roles

To successfully connect Amazon Q to Salesforce, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your Salesforce
credentials. Amazon Q assumes this role to access
your Salesforce credentials.

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

To create a Salesforce plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a Salesforce plugin using the
console and code examples for the AWS CLI.

Console
**To create a Salesforce plugin**

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
   **Salesforce**.
6. For **Salesforce**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      Salesforce domain URL. For example,
      `https://`yourInstance`.my.salesforce.com/services/data/v60.0`.
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
           Salesforce.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in Salesforce.
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
         URL** – For Salesforce
         OAuth applications, this is
         `https://login.salesforce.com/services/oauth2/token`.
      3. For **Authorization
         URL** – For Salesforce
         OAuth applications, this is
         `https://login.salesforce.com/services/oauth2/authorize`.

   4. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Choose **Save**.

AWS CLI
**To create a Salesforce
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `SALESFORCE_CRM` \
--server-url `https://`yourInstance`.my.salesforce.com/services/data/v60.0` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
