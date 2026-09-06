

# Sign in through the AWS Command Line Interface
<a name="command-line-sign-in"></a>

 You must establish how the AWS CLI authenticates with AWS. Choose the method that best fits your workflow and security requirements.
+ [Login with console credentials (Recommended)](#command-line-sign-in-local-development) if you use root, IAM users or federation with IAM for AWS account access.
+ [Login with IAM Identity Center credentials](#command-line-sign-in-sso) if you use Identity Center for AWS account access.

If you're using our new AWS experience, you have access to connect your AI coding tool to your project. This lets you sign in using the command line. For more information, see [Connect an AI coding tool](https://docs.aws.amazon.com/accounts/latest/reference/connect-ai-coding-tool.html) in the *AWS Account Management Reference Guide*.

## Login with console credentials (Recommended)
<a name="command-line-sign-in-local-development"></a>

This authentication method lets you use your console credentials with the AWS CLI, making it easy to get started with AWS programmatically within minutes of account set up. You can get temporary credentials that work seamlessly across local development tools like the AWS CLI, AWS SDKs and AWS Tools for PowerShell.

### Prerequisites
<a name="command-line-sign-in-local-development-prereqs"></a>
+ Install the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). A minimum version of 2.32.0 is required to use the `aws login` command. 
+ Access to sign into the AWS Management Console as a root user, IAM user, or through federation with IAM. If you use IAM Identity Center, go to [Login with IAM Identity Center credentials](#command-line-sign-in-sso) instead.
+ Ensure the IAM identity has the appropriate permissions. Attach the [SignInLocalDevelopmentAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SignInLocalDevelopmentAccess.html) managed policy to your IAM user, role, or group. If you sign in as a root user, no additional permissions are required.

**To login with console credentials**

1. Run the following command to start the browser-based authentication process:

   ```
   $ aws login
   ```

   The `aws login` command supports several optional parameters:
   + `aws login --remote` - For cross-device authentication when your device doesn't support a browser
**Note**  
You can control access to same-device (`aws login`) and cross-device (`aws login --remote`) authentication. Use the following resource ARNs in any relevant IAM policy.  
`arn:aws:signin:{{region}}:{{account-id}}:oauth2/public-client/localhost` — Use this ARN for same-device authentication with `aws login`.
`arn:aws:signin:{{region}}:{{account-id}}:oauth2/public-client/remote` — Use this ARN for cross-device authentication with `aws login --remote`.
   + `aws login --profile {{profile-name}}` - To authenticate with a specific profile
   + `aws login --region {{region}}` - To authenticate in a specific region

1. Follow the prompts in your terminal. The command will automatically open your default browser and guide you through the authentication process. After successful authentication, your AWS CLI session will be valid for up to 12 hours.

1. To end your session, use:

   ```
   $ aws logout
   ```

If you are accessing AWS services programmatically by using AWS Tools for PowerShell, please see [Authenticating the AWS Tools for PowerShell with AWS](https://docs.aws.amazon.com/powershell/v5/userguide/creds-idc.html). If you are using AWS SDKs, please see [Authentication and access using AWS SDKs and tools](https://docs.aws.amazon.com/sdkref/latest/guide/access.html).

## Login with IAM Identity Center credentials
<a name="command-line-sign-in-sso"></a>

The AWS access portal makes it easy for IAM Identity Center users to select an AWS account and get temporary security credentials for the AWS CLI. For more information about how to get these credentials, see [Region availability for AWS Builder ID](https://docs.aws.amazon.com/signin/latest/userguide/sign-in-aws_builder_id.html#regions-aws_builder_id). You can also configure the AWS CLI directly to authenticate users with IAM Identity Center.

**To login with IAM Identity Center credentials**

1. Check that you've completed the [Prerequisites](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-prereqs).

1. If you're signing in for the first time, [configure your profile with the `aws configure sso` wizard](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso).

1. After you configure your profile, run the following command, then follow the prompts in your terminal:

   ```
   $ aws sso login --profile {{my-profile}}
   ```

## Additional information
<a name="command-line-sign-in-more-info"></a>

If you want more information about signing-in using the command line, refer to the following resources.
+ For more information on using your console credentials to login for AWS local development, see [Authentication and access credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html).
+ For more information on the AWS CLI sign-in process, see [Authenticating with short-term credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html).
+ For details on IAM Identity Center configuration, see [Configuring the AWS CLI to use IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).