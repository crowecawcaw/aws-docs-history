

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Configuring a Zendesk plugin for Amazon Q Business
<a name="zendesk-plugin"></a>

Zendesk is a customer relationship management system that helps businesses automate and enhance customer support interactions by creating tickets to track work. If you’re a Zendesk user, you can create an Amazon Q Business plugin to allow your end users to create Zendesk cases from within their web experience chat.

To create a Zendesk plugin, you need configuration information from your Zendesk instance to set up a connection between Amazon Q and Zendesk and allow Amazon Q to perform actions in Zendesk. 

For more information on how to use plugins during your web experience chat, see [Using plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-plugins.html).

**Topics**
+ [Prerequisites](#zendesk-plugin-prereqs)
+ [Service access roles](#zendesk-plugin-iam)
+ [Creating a plugin](#zendesk-plugin-create)

## Prerequisites
<a name="zendesk-plugin-prereqs"></a>

Before you configure your Amazon Q Zendesk plugin, you must do the following:
+ As an admin, set up a new user in your Zendesk instance with scoped permissions for performing actions in Amazon Q.
+ (Optional) [Create an API token](https://support.zendesk.com/hc/en-us/articles/4408831452954-How-can-I-authenticate-API-requests-) for that new user.
+ Note your Zendesk username and Zendesk password/API token. You will need this basic authentication information for creating an AWS Secrets Manager secret during the plugin configuration process. 
+ Note the base URL of your Zendesk instance. For example: `https://yoursubdomain.zendesk.com`.

## Service access roles
<a name="zendesk-plugin-iam"></a>

To successfully connect Amazon Q to Zendesk, you need to give Amazon Q the following permission to access your Secrets Manager secret to get your Zendesk credentials. Amazon Q assumes this role to access your Zendesk credentials.

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

If you use the console and choose to create a new IAM role, Amazon Q creates the role for you. If you use the console and choose to use an existing secret, or you use the API, make sure your IAM role contains these permissions. 

## Creating a plugin
<a name="zendesk-plugin-create"></a>

To create a Zendesk plugin for your web experience chat, you can use AWS Management Console or the [CreatePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreatePlugin.html) API operation. The following tabs provide a procedure for creating a Zendesk plugin using the console and code examples for the AWS CLI.

------
#### [ Console ]

**To create a Zendesk plugin** 

1. Sign in to the AWS Management Console and open the Amazon Q console at [https://console.aws.amazon.com/amazonq/business/](https://console.aws.amazon.com/amazonq/business/?region=us-east-1).

1. From the Amazon Q console, in **Applications**, select the name of your application from the list of applications.

1. From the left navigation menu, choose **Actions**, and then choose **Plugins**.

1. For **Plugins**, choose **Add plugin**.

1. For **Add plugins**, choose **Zendesk**.

1. For **Zendesk**, enter the following information:

   1. **Name**, **Plugin name** – A name for your Amazon Q plugin. The name can include hyphens (-), but not spaces, and can have a maximum of 1,000 alphanumeric characters.

   1. For **Service access** – Choose **Create and add a new service role** or **Use an existing service role**. Make sure that your service role has the necessary permissions.

   1. **URL** – The base URL of your Zendesk instance. For example: `https://yoursubdomain.zendesk.com`

   1. **Authentication** – Choose **Create and add a new secret** or **Use an existing one**. Your secret must contain the following information:

      1. **Secret name** – A name for your Secrets Manager secret.

      1. **Zendesk username** – The username for your Zendesk user.

      1. **Zendesk password/API token** – The password/API token for your Zendesk user.

1. **Tags – *optional*** – An optional tag to track your plugin.

1. Choose **Save**. 

------
#### [ AWS CLI ]

**To create a Zendesk plugin**

```
aws qbusiness create-plugin \
--application-id {{application-id}} \
--display-name {{display-name}} \
--type ZENDESK \
--server-url {{//example.zendesk.com}} \
--auth-configuration basicAuthConfiguration="{secretArn={{<secret-arn>}},roleArn={{<role-arn>}}}"
```

------