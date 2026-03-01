# Configuring a ServiceNow plugin for Amazon Q Business

ServiceNow provides a cloud-based service management system to create and manage
organization-level workflows, such as IT services, ticketing systems, and support.
ServiceNow uses incidents (tickets) to track issues. If you’re a ServiceNow
user, you can create an Amazon Q Business plugin to allow your end users to create
ServiceNow cases from within their web experience chat.

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

- As an admin, set up a new user in your ServiceNow instance with scoped
  permissions for performing actions in Amazon Q.
- Note your ServiceNow username and ServiceNow password. You
  will need this basic authentication information for creating an AWS Secrets Manager secret during the plugin configuration process.
- Note the base URL of your ServiceNow instance. For example:
  `https://yourinstance.service-now.com`.

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
   **ServiceNow**.
6. For **ServiceNow**, enter the following
   information:
   1. **Name**, for **Plugin
      name** – A name for your Amazon Q plugin. The name can include hyphens (-),
      but not spaces, and can have a maximum of 1,000 alphanumeric
      characters.
   2. **Service access** – Choose
      **Create and add a new service role**
      or **Use an existing service role**. Make
      sure tha your service role has the necessary
      permissions.
   3. **URL** – The base URL of your
      ServiceNow instance. For example:
      `https://yourinstance.service-now.com`
   4. **Authentication** – Choose
      **Create and add a new secret** or
      **Use an existing one**. Your secret
      must contain the following information:
      1. **Secret name** – A name
         for your Secrets Manager secret.
      2. **ServiceNow username**
         – The username for your ServiceNow
         user.
      3. **ServiceNow password**
         – The password for your ServiceNow
         user.

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
--type `SERVICE-NOW` \
--server-url `//example.service-now.com` \
--auth-configuration basicAuthConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>}`"
```
