# Configuring a ServiceNow plugin for

Amazon Q Business

ServiceNow provides a cloud-based service management system to create and manage
organization-level workflows, such as IT services, ticketing systems, and support.
ServiceNow uses incidents (tickets) to track issues. If you’re a ServiceNow
user, you can create an Amazon Q Business plugin to allow your end users to perform
the following actions from within their web experience chat:

- Create incident
- Read incident
- Update incident
- Delete incident
- Read change request
- Create change request
- Update change request
- Delete change request
  To create a ServiceNow plugin, you need configuration information from your
  ServiceNow instance to set up a connection between Amazon Q and
  ServiceNow and allow Amazon Q to perform actions in ServiceNow.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#servicenow-plugin-prereqs "#servicenow-plugin-prereqs")
- [Service access roles](#servicenow-plugin-iam "#servicenow-plugin-iam")
- [Creating a plugin](#servicenow-plugin-create "#servicenow-plugin-create")

## Prerequisites

Before you configure your Amazon Q ServiceNow plugin, you must do
the following:

- As an admin, create a new OAuth 2.0 ServiceNow app in the
  ServiceNow developer console with scoped permissions for performing
  actions in Amazon Q. To learn how to do this, see [Create an endpoint for clients to access the instance](https://docs.servicenow.com/bundle/xanadu-platform-security/page/administer/security/task/t_CreateEndpointforExternalClients.html "https://docs.servicenow.com/bundle/xanadu-platform-security/page/administer/security/task/t_CreateEndpointforExternalClients.html") in
  ServiceNow Developer Documentation.
- Make sure the OAuth plugin is active and the OAuth activation property is set
  to true. Required scopes:
  - `read`
  - `write`
  - `useraccount`

###### Note

We recommend choosing Classic OAuth Scopes.

- Make sure to create an authentication profile by following the steps outlined
  in [ServiceNow Documentation](https://www.servicenow.com/docs/bundle/xanadu-platform-security/page/integrate/authentication/task/create-authentication-profile.html "https://www.servicenow.com/docs/bundle/xanadu-platform-security/page/integrate/authentication/task/create-authentication-profile.html"). For **Type**,
  select **OAuth**. For authentication policy, select
  **Allow Access Policy**.

Then, add the authentication profile you created to the REST API access
policies for **Table API** and **Change
Management** by following steps outlined in [Create REST API access policy](https://www.servicenow.com/docs/bundle/xanadu-platform-security/page/integrate/authentication/task/create-api-access-policy.html "https://www.servicenow.com/docs/bundle/xanadu-platform-security/page/integrate/authentication/task/create-api-access-policy.html") in ServiceNow
Documentation.

- Note the domain URL of your ServiceNow instance. For example:
  `https://`yourInstanceId`.service-now.com`.
- Note your:

      + **Access token URL** – For
       ServiceNow OAuth applications, this is
       `https://`yourInstanceId`.service-now.com/oauth_token.do`.
      + **Authorization URL** – For
       ServiceNow OAuth applications, this is
       `https://`yourInstanceId`.service-now.com/oauth_auth.do`.
      + **Redirect URL** – The URL to
       which user needs to be redirected after authentication. If your deployed
       web url is `<q-endpoint>`, use
       `<q-endpoint>/oauth/callback` . Amazon Q Business will handle OAuth tokens in this URL. This callback
       URL needs to be allowlisted in your third-party application.
      + **Client ID** – The client ID
       generated when you create your OAuth 2.0 application in
       ServiceNow.
      + **Client secret** – The client
       secret generated when you create your OAuth 2.0 application in
       ServiceNow.

  You will need this authentication information during the plugin configuration
  process.

## Service access roles

To successfully connect Amazon Q to ServiceNow, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your ServiceNow
credentials. Amazon Q assumes this role to access
your ServiceNow credentials.

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

To create a ServiceNow plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure for creating a ServiceNow plugin using the
console and code examples for the AWS CLI.

Console
**To create a ServiceNow plugin**

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
   **ServiceNow**.
6. For **ServiceNow**, enter the following
   information:
   1. In **Plugin name**, for
      **Name** – A name for your
      Amazon Q plugin. The name can include hyphens
      (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters.
   2. In **Domain URL**, for
      **URL** – Enter your
      ServiceNow domain URL. For example,
      `https://`yourInstanceId`.service-now.com`.
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
           ServiceNow.
         - **Client
           secret** – The client secret
           generated when you create your OAuth 2.0
           application in ServiceNow.
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
         URL** – For ServiceNow
         OAuth applications, this is
         `https://`yourInstanceId`.service-now.com/oauth_token.do`.
      3. For **Authorization
         URL** – For ServiceNow
         OAuth applications, this is
         `https://`yourInstanceId`.service-now.com/oauth_auth.do`.

   4. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Choose **Save**.

AWS CLI
**To create a ServiceNow
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `SERVICENOW_NOW_PLATFORM` \
--server-url `https://`yourInstanceId`.service-now.com` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>`,authorizationUrl=`<auth-url>`,tokenUrl=`<token-url>`}"
```
