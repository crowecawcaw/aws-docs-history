# Configuring a Jira plugin for Amazon Q Business

Jira is a project management tool that creates issues (tickets) for software
development, product management, and bug tracking. If you’re a Jira user, you
can create an Amazon Q Business plugin to allow your end users to create
Jira issues from within their web experience chat.

To create a Jira plugin, you need configuration information from your
Jira instance to set up a connection between Amazon Q and
Jira and allow Amazon Q to perform actions in
Jira.

For more information on how to use plugins during your web experience chat, see [Using
plugins](using-plugins.md "using-plugins.md").

###### Topics

- [Prerequisites for creating an Amazon Q Business Jira plugin](#jira-plugin-prereqs "#jira-plugin-prereqs")
- [Service access roles](#jira-plugin-iam "#jira-plugin-iam")
- [Creating a plugin](#jira-plugin-create "#jira-plugin-create")

## Prerequisites for creating an Amazon Q Business Jira plugin

Before you configure your Amazon Q Jira plugin, you must do
the following:

- Set up a new user in your Jira instance with scoped permissions
  for performing actions in Amazon Q.
- (Optional) [Create an API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/ "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/") for the new user that you created.
- Note this user’s Jira username and Jira account
  password (and optionally, their API token). You will need this basic
  authentication information for creating an AWS Secrets Manager secret during
  the plugin configuration process.
- Note the base URL of your Jira Cloud instance hosted by
  Atlassian. For example: `https://yourcompany.atlassian.net`.

## Service access roles

To successfully connect Amazon Q to Jira, you need to give Amazon Q
the following permission to access your Secrets Manager secret to get your Jira
credentials. Amazon Q assumes this role to access
your Jira credentials.

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

To create a Jira plugin for your web experience chat, you can use the
AWS Management Console or the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation. The
following tabs provide a procedure to create a Jira plugin using the
console and code examples for the AWS CLI.

Console
**To create a Jira plugin**

1.  Sign in to the AWS Management Console and open the Amazon Q console
    at [https://console.aws.amazon.com/amazonq/business/](https://console.aws.amazon.com/amazonq/business/?region=us-east-1 "https://console.aws.amazon.com/amazonq/business/?region=us-east-1").
2.  In **Applications**, select the name of your
    application from the list of applications.
3.  From the left navigation menu, choose
    **Actions**, and then choose
    **Plugins**.
4.  For **Plugins**, choose **Add
    plugin**.
5.  For **Add plugins**, choose
    **Jira**.
6.  For **Jira**, enter the following
    information:
    1. **Name**, **Plugin
       name** – A name for your Amazon Q plugin. The name can include hyphens (-),
       but not spaces, and can have a maximum of 1,000 alphanumeric
       characters.
    2. **Service access** – Choose
       **Create and add a new service role**
       or **Use an existing service role**. Make
       sure that your service role has the necessary
       permissions.
    3. **URL** – The base URL of your
       Jira Cloud instance hosted by Atlassian. For
       example:
       `https://yourcompany.atlassian.net`.
    4. **Authentication** – Choose to
       **Create and add a new secret** or
       **Use an existing one**.

    If you choose to create a new secret, a Secrets Manager
    secret window opens requesting the following
    information:

        1. **Secret name** – A name
         for your Secrets Manager secret.
        2. **Jira username**
         – The username for your Jira
         user.
        3. **Jira password/API
         token** – The password/API token
         for your Jira user.

7.  **Tags – _optional_**
    – Add an optional tag to track your plugin.
8.  Choose **Save**.

AWS CLI
**To create a Jira
plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `JIRA` \
--server-url `https://example.atlassian.net` \
--auth-configuration basicAuthConfiguration="{secretArn=`<secret-arn>`,roleArn=`<role-arn>}`"
```
