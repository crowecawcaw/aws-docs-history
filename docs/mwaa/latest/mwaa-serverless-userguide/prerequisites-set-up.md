

# Prerequisites for using Amazon MWAA Serverless
<a name="prerequisites-set-up"></a>

Learn about the prerequisites you need before using Amazon MWAA Serverless. These include account setup and permissions management. You must have an AWS account before completing these tasks.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Grant IAM permissions](#set-up-iam)
+ [Install and configure the AWS CLI](#set-up-cli)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Grant IAM permissions
<a name="set-up-iam"></a>

We recommend that you use finer-grained policies. For policy setup, refer to [How Amazon MWAA Serverless works with IAM](security_iam_service-with-iam.md). To learn more about access management, refer to [Access management for AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the IAM User Guide. For example, you can use policy similar to following.

------
#### [ JSON ]

```
{
  "Version":"2012-10-17", 		 	 	                    
  "Statement": [
    {
      "Sid": "MWAAServerlessFullAccess",
      "Effect": "Allow",
      "Action": [
        "airflow-serverless:*"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "MWAAServerlessSLRCreation",
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "MWAAServerlessServicePassroleAccess",
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "MWAAServerlessServiceS3ReadAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        's3:GetObjectVersion'
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "MWAAServerlessServiceCWLogsAccess",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:DescribeLogGroups"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "MWAAServerlessServiceKMSAccess",
      "Effect": "Allow",
      "Action": [
        "kms:Encrypt", 
        "kms:Decrypt", 
        "kms:GenerateDataKey", 
        "kms:DescribeKey"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

------

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

### Grant programmatic access
<a name="set-up-access"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.



| Which user needs programmatic access? | To | By | 
| --- | --- | --- | 
| IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Login for AWS local development](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, see [Login for AWS local development](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html) in the *AWS SDKs and Tools Reference Guide*.  | 
| Workforce identity<br />(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*.  | 
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. | 
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*. <br />+  For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.  | 

## Install and configure the AWS CLI
<a name="set-up-cli"></a>

If you want to use Amazon MWAA Serverless APIs with the AWS Command Line Interface (AWS CLI), use the following instructions to install the latest version.

**Tip**  
If you prefer to use Amazon MWAA Serverless with SDKs, you can access AWS builder tools in the [Builder Center](https://builder.aws.com/build/tools). Tools are listed by programming language.

**To set up the AWS CLI**

1. To install the latest version of the AWS CLI for macOS, Linux, or Windows, refer to [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. To configure the AWS CLI and secure setup of your access to AWS services, including Amazon MWAA Serverless, refer to [Quick configuration with `aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config).

1. To verify the setup, enter the following command at the command prompt.

------
#### [ CLI ]

   ```
   aws mwaa-serverless help
   ```

------

   AWS CLI commands use the default AWS Region from your configuration, unless you set it with a parameter or a profile. To set your AWS Region with a parameter, you can add the `--region` parameter to each command.

   To set your AWS Region with a profile, first add a named profile in the `~/.aws/config` file or the `%UserProfile%/.aws/config` file (for Microsoft Windows). Follow the steps in [Named profiles for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html). Next, set your AWS Region and other settings with a command similar to the one in the following example.

------
#### [ CLI ]

   ```
   [profile mwaa-serverless]
   aws_access_key_id = {{ACCESS-KEY-ID-OF-IAM-USER}}
   aws_secret_access_key = {{SECRET-ACCESS-KEY-ID-OF-IAM-USER}}
   region = us-east-1
   output = text
   ```

------