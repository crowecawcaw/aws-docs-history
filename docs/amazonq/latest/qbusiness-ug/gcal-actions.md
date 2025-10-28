# Configuring a Google Calendar plugin for

Amazon Q Business

Google Calendar is an online calendar service that helps users schedule meetings, set
up events, set reminders, and share their schedules. If you’re a Google Calendar user,
you can create an Amazon Q Business plugin to allow your end users to find and list
events from within their web experience chat.

To create a Google Calendar plugin, you need configuration information from your
Google Calendar instance to set up a connection between Amazon Q and
Google Calendar and allow Amazon Q to perform actions in Google Calendar.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#gcal-plugin-prereqs "#gcal-plugin-prereqs")
- [Service access roles](#gcal-plugin-iam "#gcal-plugin-iam")
- [Creating a plugin](#gcal-plugin-create "#gcal-plugin-create")

## Prerequisites

Before you configure your Amazon Q Google Calendar plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 Google Calendar app in the
  Google Calendar developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [Using OAuth
  2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2 "https://developers.google.com/identity/protocols/oauth2") in Google Calendar Developer
  Documentation.
- Make sure you've added following required scopes:
  `calendar.readonly`, `calendar.events`.
- Note the domain URL of your Google Calendar instance. For example:
  `https://www.googleapis.com/calendar/v3`.
- Note your:

      + **Access token URL** – For
       Google Calendar OAuth applications, this is
       `https://oauth2.googleapis.com/token`.
      + **Authorization URL** – For
       Google Calendar OAuth applications, this is
       `https://accounts.google.com/o/oauth2/v2/auth`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The client ID
       generated when you create your OAuth 2.0 application in
       Google Calendar.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       Google Calendar.

  You will need this authentication information during the plugin configuration
  process.

## Service access roles

To successfully connect Amazon Q to Google Calendar, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your Google Calendar
credentials. Amazon Q assumes this role to access
your Google Calendar credentials.

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

To create a Google Calendar plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a Google Calendar plugin using the
console and code examples for the AWS CLI.

Console
**To create a Google Calendar plugin**

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
   **Google Calendar**.
6. For **Google Calendar**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      Google Calendar domain URL. For example,
      `https://www.googleapis.com/calendar/v3`.
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
           Google Calendar.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in Google Calendar.
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
         URL** – For Google Calendar
         OAuth applications, this is
         `https://oauth2.googleapis.com/token`.
      3. For **Authorization
         URL** – For Google Calendar
         OAuth applications, this is
         `https://accounts.google.com/o/oauth2/v2/auth`.

   4. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Choose **Save**.

AWS CLI
**To create a Google Calendar
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `GOOGLE_CALENDAR` \
--server-url `https://www.googleapis.com/calendar/v3` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
