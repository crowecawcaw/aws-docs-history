# Sign in through the AWS Command Line Interface

You must establish how the AWS CLI authenticates with AWS. Choose the method that best fits your workflow and security
requirements.

- [Login with console credentials (Recommended)](#command-line-sign-in-local-development "#command-line-sign-in-local-development") if you use root,
  IAM users or federation with IAM for AWS account access.
- [Login with IAM Identity Center credentials](#command-line-sign-in-sso "#command-line-sign-in-sso") if you use Identity Center for AWS account access.

## Login with console credentials (Recommended)

This authentication method lets you use your console credentials with the AWS CLI,
making it easy to get started with AWS programmatically within minutes of account set up.
You can get temporary credentials that work seamlessly across local development tools like the AWS CLI, AWS SDKs and AWS Tools for PowerShell.

### Prerequisites

- Install the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
  A minimum version of 2.32.0 is required to use the `aws login` command.
- Access to sign into the AWS Management Console as a root user, IAM user, or through federation with IAM.
  If you use IAM Identity Center, go to [Login with IAM Identity Center credentials](#command-line-sign-in-sso "#command-line-sign-in-sso") instead.
- Ensure the IAM identity has the appropriate permissions. Attach the [SignInLocalDevelopmentAccess](../../../aws-managed-policy/latest/reference/SignInLocalDevelopmentAccess.md "../../../aws-managed-policy/latest/reference/SignInLocalDevelopmentAccess.md") managed policy to your IAM
  user, role, or group. If you sign in as a root user, no additional permissions are required.

###### To login with console credentials

1. Run the following command to start the browser-based authentication
   process:

```
`$` `aws login`
```

The `aws login` command supports several optional
parameters:

    * `aws login --remote` - For cross-device authentication
     when your device doesn't support a browser


    ###### Note

    You can control access to same-device (`aws login`) and cross-device (`aws login --remote`) authentication. Use the following resource ARNs in any relevant IAM policy.



    	+ `arn:aws:signin:`region`:`account-id`:oauth2/public-client/localhost`
    	 — Use this ARN for same-device authentication with `aws login`.
    	+ `arn:aws:signin:`region`:`account-id`:oauth2/public-client/remote`
    	 — Use this ARN for cross-device authentication with `aws login --remote`.
    * `aws login --profile
     `profile-name`` - To authenticate
     with a specific profile
    * `aws login --region `region`` - To
     authenticate in a specific region

2. Follow the prompts in your terminal. The command will automatically open your
   default browser and guide you through the authentication process. After successful authentication, your AWS CLI session will be valid for up to 12
   hours.
3. To end your session, use:

```
`$` `aws logout`
```

If you are accessing AWS services programmatically by using AWS Tools for PowerShell, please see [Authenticating the AWS Tools for PowerShell with AWS](../../../powershell/v5/userguide/creds-idc.md "../../../powershell/v5/userguide/creds-idc.md").
If you are using AWS SDKs, please see [Authentication and access using AWS SDKs and tools](../../../sdkref/latest/guide/access.md "../../../sdkref/latest/guide/access.md").

## Login with IAM Identity Center credentials

The AWS access portal makes it easy for IAM Identity Center users to select an AWS account and
get temporary security credentials for the AWS CLI. For more information about how to get
these credentials, see [Region availability for AWS Builder ID](sign-in-builder-id.md#regions-aws_builder_id "sign-in-builder-id.md#regions-aws_builder_id"). You can also configure the AWS CLI directly
to authenticate users with IAM Identity Center.

###### To login with IAM Identity Center credentials

1. Check that you've completed the [Prerequisites](../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-prereqs "../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-prereqs").
2. If you're signing in for the first time, [configure your profile with the `aws configure sso`
   wizard](../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-token-auto-sso "../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-token-auto-sso").
3. After you configure your profile, run the following command, then follow the
   prompts in your terminal:

```
`$` `aws sso login --profile` `my-profile`
```

## Additional information

If you want more information about signing-in using the command line, refer to the
following resources.

- For more information on using your console credentials to login for AWS local development,
  see [Authentication and access credentials for the AWS CLI](../../../cli/latest/userguide/cli-chap-authentication.md "../../../cli/latest/userguide/cli-chap-authentication.md").
- For more information on the AWS CLI sign-in process, see [Authenticating with short-term credentials for the AWS CLI](../../../cli/latest/userguide/cli-chap-authentication.md "../../../cli/latest/userguide/cli-chap-authentication.md").
- For details on IAM Identity Center configuration, see [Configuring the AWS CLI to use IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md").
