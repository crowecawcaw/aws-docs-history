# Getting IAM Identity Center user credentials for the AWS CLI or AWS

SDKs

You can access AWS services programmatically by using the AWS Command Line Interface or AWS Software
Development Kits (SDKs) with user credentials from IAM Identity Center. This topic describes how to get
temporary credentials for a user in IAM Identity Center.

The AWS access portal provides IAM Identity Center users with single-sign on access to their AWS accounts
and cloud applications. After you sign in to the AWS access portal as an IAM Identity Center user, you can get
temporary credentials. You can then use the credentials, also referred to as IAM Identity Center user
credentials, in the AWS CLI or AWS SDKs to access resources in an AWS account.

If you’re using the AWS CLI to access AWS services programmatically, you can use the
procedures in this topic to initiate access to the AWS CLI. For information about the AWS CLI, see
the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/gcli-chap-welcome.md "../../../cli/latest/userguide/gcli-chap-welcome.md").

If you’re using the AWS SDKs to access AWS services programmatically, following the
procedures in this topic also directly establishes authentication for the AWS SDKs. For
information about the AWS SDKs, see the [AWS SDKs and Tools
Reference Guide](../../../sdkref/latest/guide/overview.md "../../../sdkref/latest/guide/overview.md").

###### Note

Users in IAM Identity Center are different than [IAM users](../../../cli/latest/userguide/id_users.md "../../../cli/latest/userguide/id_users.md").
IAM users are granted long-term credentials to AWS resources. Users in IAM Identity Center are granted
temporary credentials. We recommend that you use temporary credentials as a security best
practice for accessing your AWS accounts because these credentials are generated every
time you sign in.

## Prerequisites

To get temporary credentials for your IAM Identity Center user, you'll need the following:

- **An IAM Identity Center user** – You'll sign in to the
  AWS access portal as this user. You or your administrator might create this user. For
  information about how to enable IAM Identity Center and create an IAM Identity Center user, see [Getting started with IAM Identity Center](getting-started.md "getting-started.md").
- **User access to an AWS account** – To grant
  an IAM Identity Center user permission to retrieve their temporary credentials, you or an
  administrator must assign the IAM Identity Center user to a [permission set](permissionsetsconcept.md "permissionsetsconcept.md"). Permission sets are stored in IAM Identity Center and define the level of
  access that an IAM Identity Center user has to an AWS account. If your administrator
  created the IAM Identity Center user for you, ask them to add this access for you. For more
  information, see [Assign user or group access to AWS accounts](assignusers.md "assignusers.md").
- **AWS CLI installed** – To use the temporary
  credentials, you must install the AWS CLI. For instructions, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS CLI
  User Guide_.

## Considerations

Before you complete the steps to get temporary credentials for your IAM Identity Center user, keep the
following considerations in mind:

- **IAM Identity Center creates IAM roles** – When you assign
  a user in IAM Identity Center to a permission set, IAM Identity Center creates a corresponding IAM role from the
  permission set. IAM roles created by permission sets differ from IAM roles created
  in AWS Identity and Access Management in the following ways:

      + IAM Identity Center owns and secures the roles that are created by permission sets. Only IAM Identity Center
       can modify these roles.
      + Only users in IAM Identity Center can assume the roles that correspond to their assigned
       permission sets. You can’t assign permission set access to IAM users, IAM
       federated users, or service accounts.
      + You can’t modify a role trust policy on these roles to allow access to [principals](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal") outside of IAM Identity Center.

  For information about how to get temporary credentials for a role that you create in
  IAM, see [Using temporary security credentials with the AWS CLI](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md#using-temp-creds-sdk-cli "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md#using-temp-creds-sdk-cli") in the
  _AWS Identity and Access Management User Guide_.

- **You can set the session duration for permission
  sets** – After you sign in to the AWS access portal, the permission set to
  which your IAM Identity Center user is assigned appears as an available role. IAM Identity Center creates a separate
  session for this role. This session can be from one to 12 hours, depending the session
  duration configured for the permission set. The default session duration is one hour.
  For more information, see [Set session duration for
  AWS accounts](howtosessionduration.md "howtosessionduration.md").

## Getting and refreshing temporary credentials

You can get and refresh temporary credentials for your IAM Identity Center user automatically or
manually.

###### Topics

- [Automatic credential refresh
  (recommended)](#how-to-get-temp-credentials-automatic "#how-to-get-temp-credentials-automatic")
- [Manual credential refresh](#how-to-get-temp-credentials-manual "#how-to-get-temp-credentials-manual")

### Automatic credential refresh

(recommended)

Automatic credential refresh uses the Open ID Connect (OIDC) Device Code Authorization
standard. With this method, you initiate access directly by using the `aws configure
 sso` command in the AWS CLI. You can use this command to automatically access any
role that is associated with any permission set that you’re assigned to for any
AWS account.

To access the role created for your IAM Identity Center user, run the `aws configure sso`
command, and then authorize the AWS CLI from a browser window. As long as you have an active
AWS access portal session, the AWS CLI automatically retrieves temporary credentials and refreshes
the credentials automatically.

For more information, see [Configure your profile with the `aws configure sso wizard`](../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-token-auto-sso "../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-token-auto-sso") in the
_AWS Command Line Interface User Guide_.

###### To get temporary credentials that automatically refresh

1. Sign in to the AWS access portal by using the specific sign-in URL provided by your
   administrator. If you created the IAM Identity Center user, AWS sent an email invitation that
   includes your sign-in URL. For more information, see [Sign in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User
   Guide_.
2. In the **Accounts** tab, locate the AWS account from which you
   want to retrieve credentials. When you choose the account, the account name, account
   ID, and email address associated with the account appear.

###### Note

If you do not see any **AWS accounts** listed, it is likely
that you've not yet been assigned to a permission set for that account. In this
case, contact your administrator and ask them to add this access for you. For more
information, see [Assign user or group access to AWS accounts](assignusers.md "assignusers.md"). 3. Below the name of the account, the permission set to which your IAM Identity Center user is
assigned appears as an available role. For example, if your IAM Identity Center user is assigned to
the **PowerUserAccess** permission set for the account, the role
appears in the AWS access portal as **PowerUserAccess**. 4. Depending on your option next to the role name, either choose **Access
keys** or choose **Command line or programmatic
access**. 5. In the **Get credentials** dialog box, choose either
**macOS and Linux**, **Windows**, or
**PowerShell**, depending on the operating system on which you
installed the AWS CLI. 6. Under **AWS IAM Identity Center credentials (Recommended)**, your `SSO
 Start URL` and `SSO Region` are displayed. These values are
required to configure both an IAM Identity Center enabled profile and `sso-session` to
your AWS CLI. To complete this configuration, follow the instructions in [Configure your profile with the `aws configure sso wizard`](../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-token-auto-sso "../../../cli/latest/userguide/sso-configure-profile-token.md#sso-configure-profile-token-auto-sso") in
the _AWS Command Line Interface User Guide_.

Continue using the AWS CLI as necessary for your AWS account until the credentials
have expired.

### Manual credential refresh

You can use the manual credential refresh method to get temporary credentials for a
role that is associated with a specific permission set in a specific AWS account. To do
so, you copy and paste the required commands for the temporary credentials. With this
method, you must refresh the temporary credentials manually.

You can run AWS CLI commands until your temporary credentials expire.

###### To get credentials that you manually refresh

1. Sign in to the AWS access portal by using the specific sign-in URL provided by your
   administrator. If you created the IAM Identity Center user, AWS sent an email invitation that
   includes your sign-in URL. For more information, see [Sign in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User
   Guide_.
2. In the **Accounts** tab, locate the AWS account from which you
   want to retrieve access credentials and expand it to show the IAM role name (for
   example **Administrator**). Depending on your option next to the
   IAM role name, either choose **Access keys** or choose
   **Command line or programmatic access**.

###### Note

If you do not see any **AWS accounts** listed, it is likely
that you've not yet been assigned to a permission set for that account. In this
case, contact your administrator and ask them to add this access for you. For more
information, see [Assign user or group access to AWS accounts](assignusers.md "assignusers.md"). 3. In the **Get credentials** dialog box, choose **MacOS and
Linux**, **Windows**, or **PowerShell**,
depending on the operating system on which you installed the AWS CLI. 4. Choose any of the following options:

    * **Option 1: Set AWS environment variables**


    Choose this option to override all credential settings, including any settings
     in the `credentials` files and `config` files. For more
     information, see [Environment variables to configure the AWS CLI](../../../cli/latest/userguide/cli-configure-envvars.md "../../../cli/latest/userguide/cli-configure-envvars.md") in the *AWS CLI
     User Guide*.


    To use this option, copy the commands to your clipboard, paste the commands
     into your AWS CLI terminal window, and then press **Enter** to set
     the required environment variables.
    * **Option 2: Add a profile to your AWS credentials
     file**


    Choose this option to run commands with different sets of credentials.


    To use this option, copy the commands to your clipboard, and then paste the
     commands into your shared AWS `credentials` file to set up a new
     named profile. For more information, see [Shared
     config and credentials files](../../../sdkref/latest/guide/file-format.md "../../../sdkref/latest/guide/file-format.md") in the *AWS SDKs and Tools
     Reference Guide*. To use this credential, specify the
     `--profile` option in your AWS CLI command. This affects all
     environments that use the same credential file.
    * **Option 3: Use individual values in your AWS service
     client**


    Choose this option to access AWS resources from an AWS service client. For
     more information, see [Tools to Build on
     AWS](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").


    To use this option, copy the values to your clipboard, paste the values into
     your code, and assign them to the appropriate variables for your SDK. For more
     information, see the documentation for your specific SDK API.
