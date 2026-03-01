# Configuring a Salesforce plugin for Amazon Q Business

Salesforce is a customer relationship management (CRM) tool for managing support,
sales, and marketing teams that you can use to create cases (tickets) to track issues. If
you’re a Salesforce user, you can create an Amazon Q Business plugin to allow
your end users to create Salesforce cases from within their web experience
chat.

To create a Salesforce plugin, you need configuration information from your
Salesforce instance to set up a connection between Amazon Q and
Salesforce and allow Amazon Q to perform actions in Salesforce.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites](#salesforce-plugin-prereqs "#salesforce-plugin-prereqs")
- [Service access roles](#salesforce-plugin-iam "#salesforce-plugin-iam")
- [Creating a plugin](#salesforce-plugin-create "#salesforce-plugin-create")

## Prerequisites

Before you configure your Amazon Q Salesforce plugin, you must do
the following:

- Set up a Connected App using the admin role in your Salesforce
  instance with Client Credentials Flow enabled.
- As an admin, configure an execution user with scoped permissions for
  performing actions in Amazon Q. For instructions, see [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5")
  in the Salesforce documentation.
- Note your Salesforce Connected App’s consumer key
  (`client_id`) and your Salesforce Connected App Consumer
  secret (`client_secret`). You will need this Oauth 2.0 authentication
  information for creating an AWS Secrets Manager secret during the plugin
  configuration process.
- Note the Salesforce My Domain URL of your Salesforce
  organization. For example:
  `https://yourdomain.my.salesforce.com`.

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

1. Sign in to the AWS Management Console and open the Amazon Q console
   at [https://console.aws.amazon.com/amazonq/business/](https://console.aws.amazon.com/amazonq/business/?region=us-east-1 "https://console.aws.amazon.com/amazonq/business/?region=us-east-1").
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
   1. **Name**, for **Plugin
      name** – A name for your Amazon Q plugin. The name can include hyphens (-),
      but not spaces, and can have a maximum of 1,000 alphanumeric
      characters.
   2. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure that your service role has the necessary
      permissions.
   3. **URL** – My Domain URL of your
      Salesforce organization. For example:
      `https://yourdomain.my.salesforce.com`
   4. **Authentication** – Choose
      **Create and add a new secret** or
      **Use an existing one**. Your secret
      must contain the following information:
      1. **Secret name** – A name
         for your Secrets Manager secret.
      2. **Connected app consumer key**
         – The consumer key for your Salesforce
         connected app.
      3. **Connected app consumer secret**
         – The consumer secret for your
         Salesforce connected app.

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
--type `SALESFORCE` \
--server-url `//example.my.salesforce.com` \
--auth-configuration oAuth2ClientCredentialConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>}`"
```
