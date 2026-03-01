# Configuring a PagerDuty Advance plugin for Amazon Q Business

PagerDuty Operations Cloud is a software-as-a-service (SaaS) incident response management
platform that provides IT teams with knowledge about incidents as soon as they occur. If
you’re a PagerDuty Advance customer who has [PagerDuty Advance AI Assistant](https://support.pagerduty.com/main/docs/pagerduty-advance#manage-pagerduty-advance-account-settings "https://support.pagerduty.com/main/docs/pagerduty-advance#manage-pagerduty-advance-account-settings") functionality turned on, you can use the Amazon Q Business PagerDuty Advance plugin to allow your end users to perform the
following actions from within their web experience chat:

- Get incidents
- Similar incidents
- Root cause incident
- Find recent changes
- Who is on-call
- Status update on incident
- Customer impact
- Update incident
  To create a PagerDuty Advance plugin, you need configuration information from your
  PagerDuty Advance instance to set up a connection between Amazon Q and
  PagerDuty Advance and allow Amazon Q to perform actions in PagerDuty Advance.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#pagerduty-plugin-prereqs "#pagerduty-plugin-prereqs")
- [Service access roles](#pagerduty-plugin-iam "#pagerduty-plugin-iam")
- [Creating a plugin](#pagerduty-plugin-create "#pagerduty-plugin-create")

## Prerequisites

Before you configure your Amazon Q PagerDuty Advance plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 PagerDuty Advance app in the
  PagerDuty Advance developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [Register an App](https://developer.pagerduty.com/docs/dd91fbd09a1a1-register-an-app "https://developer.pagerduty.com/docs/dd91fbd09a1a1-register-an-app") in PagerDuty Advance Developer
  Documentation.
- Make sure you've added following required scopes:
  - `openid`
  - `write`

###### Note

We recommend choosing Classic OAuth Scopes.

- Note the domain URL of your PagerDuty Advance instance. For example:
  `https://api.pagerduty.com`.
- Note your:

      + **Access token URL** – For
       PagerDuty Advance OAuth applications, this is
       `https://identity.pagerduty.com/oauth/token`.
      + **Authorization URL** – For
       PagerDuty Advance OAuth applications, this is
       `https://identity.pagerduty.com/oauth/authorize`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The client ID
       generated when you create your OAuth 2.0 application in
       PagerDuty Advance.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       PagerDuty Advance.

  You will need this authentication information during the plugin configuration
  process.

## Service access roles

To successfully connect Amazon Q to PagerDuty Advance, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your PagerDuty Advance
credentials. Amazon Q assumes this role to access
your PagerDuty Advance credentials.

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

To create a PagerDuty Advance plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a PagerDuty Advance plugin using the
console and code examples for the AWS CLI.

Console
**To create a PagerDuty Advance plugin**

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
   **PagerDuty Advance**.
6. For **PagerDuty Advance**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      PagerDuty Advance domain URL. For example,
      `https://api.pagerduty.com`.
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
           PagerDuty Advance.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in PagerDuty Advance.
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
         URL** – For PagerDuty Advance
         OAuth applications, this is
         `https://identity.pagerduty.com/oauth/token`.
      3. For **Authorization
         URL** – For PagerDuty Advance
         OAuth applications, this is
         `https://identity.pagerduty.com/oauth/authorize`.

   4. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Choose **Save**.

AWS CLI
**To create a PagerDuty Advance
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `PAGERDUTY_ADVANCE` \
--server-url `https://api.pagerduty.com` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
