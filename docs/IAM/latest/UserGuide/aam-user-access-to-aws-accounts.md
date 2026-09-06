

# User access to AWS accounts
<a name="aam-user-access-to-aws-accounts"></a>

This topic describes how users access the AWS accounts assigned to them with account access manager.

## Getting your portal URL
<a name="aam-get-your-portal-url"></a>

You can access your assigned AWS accounts in several ways:

1. Your administrator might provide you with an account access portal URL (for example, `https://aa-gyxmap389.account-access.us-east-2.app.aws` or a vanity URL).

1. Your administrator might provide you with the URL for the main AWS access portal which displays all AWS applications assigned to you, including the account access portal.

1. Your organization might have enabled you to launch the account access portal from an external identity provider portal or another portal outside AWS.

## Access AWS accounts with a web browser
<a name="aam-access-accounts-in-web-browser"></a>

The account access portal displays the AWS accounts you have access to, and the IAM roles you can assume in each account.

**To access an account in a browser**

1. Navigate to the account access portal URL and when prompted, sign in using your credentials as instructed by your administrator.
**Note**  
To launch the account access portal from the AWS access portal instead, navigate to the **Applications** tab.

1. The browser page displays the AWS accounts you are assigned to. You can search accounts by account name or ID.

1. Expand the account of interest to see all the roles you can assume in the account.

1. Choose the IAM role to sign in with (for example, Developer). A new browser tab opens where you are signed into the account with the chosen role.

## Access AWS accounts with the AWS CLI or AWS SDKs
<a name="aam-access-accounts-cli-sdk"></a>

You can access AWS services programmatically by using the AWS Command Line Interface or AWS Software Development Kits (SDKs) with user credentials from IAM Identity Center.

The account access portal provides users with single sign-on access to their AWS accounts for account assignments managed in account access manager. After you sign in to the account access portal, you can get temporary credentials. You can then use the credentials in the AWS CLI or AWS SDKs to access resources in an AWS account.

If you're using the AWS CLI to access AWS services programmatically, you can use the procedures in this topic to initiate access to the AWS CLI. For information about the AWS CLI, see the *AWS Command Line Interface User Guide*.

If you're using the AWS SDKs to access AWS services programmatically, following the procedures in this topic also directly establishes authentication for the AWS SDKs. For information about the AWS SDKs, see the *AWS SDKs and Tools Reference Guide*.

### AWS account access with **aws login** (recommended)
<a name="aam-access-accounts-console-credentials"></a>

You can use the **aws login** command to gain access to AWS accounts you are assigned to in account access manager. First, install the latest AWS CLI. Then, follow this procedure:

**To access an account with AWS CLI**

1. In your default browser, sign in to your account access portal, and from there to the target AWS account using one of the assigned IAM roles for the account. Follow the procedure earlier in this topic.

1. On the command line, run the **aws login** command.

1. If you have not set a default Region, the AWS CLI prompts you to specify the AWS Region of your choice (for example, us-east-2). The AWS CLI will remember your choice for future use.

1. The AWS CLI opens a web page in your default browser and prompts you to continue with the active session you just initiated or sign in to a new session.

1. On the web page, choose the tile with the session you initiated earlier in the browser.

1. The browser page confirms that your credentials have been shared successfully and can be used until your session expires. You can now close the tab with the web page and continue working with the AWS CLI using this session.

**Note**  
IAM Identity Center-specific AWS CLI commands such as **aws sso configure** and **aws sso login** don't work with account assignments in account access manager.

### AWS account access with access keys
<a name="aam-access-accounts-access-keys"></a>

You can use the manual credential refresh method to get temporary credentials for an IAM role assigned to you in a specific AWS account. To do so, you copy and paste the required commands for the temporary credentials. With this method, you must refresh the temporary credentials manually.

You can run AWS CLI commands until your temporary credentials expire.

**To get credentials that you manually refresh**

1. Sign in to the account access portal as explained in [Access AWS accounts with a web browser](#aam-access-accounts-in-web-browser).

1. Locate the AWS account from which you want to retrieve access credentials and expand it to show the IAM role name (for example Developer).

1. Choose **Generate access key** next to the desired role.
**Note**  
If you do not see any AWS account assignments, it is likely that you've not yet been assigned to any account. In this case, contact your administrator and ask them to assign access to you.

1. In the **Get credentials** dialog box, choose the **MacOS and Linux**, **Windows**, or **PowerShell** tab depending on the operating system on which you installed the AWS CLI.

1. Choose any of the following options:
   + **Option 1: Set AWS environment variables**

     Choose this option to override all credential settings, including any settings in the credentials files and config files. For more information, see [Environment variables to configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html) in the *AWS Command Line Interface User Guide*.

     To use this option, copy the commands to your clipboard, paste the commands into your AWS CLI terminal window, and then press Enter to set the required environment variables.
   + **Option 2: Use individual values in your AWS service client**

     Choose this option to access AWS resources from an AWS service client. For more information, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/).

     To use this option, copy the values to your clipboard, paste the values into your code, and assign them to the appropriate variables for your SDK. For more information, see the documentation for your specific SDK API.

## Creating shortcut links to AWS Management Console destinations
<a name="aam-shortcut-links"></a>

The account access portal offers an option to create a shareable deep link.

**To create a shortcut link**

1. While signed into the account access portal, choose the **Create shortcut link** button.

1. In the dialog box:

   1. Choose an AWS account using the account ID or account name. As you type, a drop-down menu displays matching account IDs and names that you can access. You can choose only an account to which you have access.

   1. (Optional) Choose an IAM role from the drop-down list. These are the IAM roles assigned to you for the selected account. If you omit choosing the role, users are prompted to select one assigned to them for the chosen account when using the shortcut link.
**Note**  
You cannot grant new access with shortcut links. Shortcut links work only with the accounts and roles already assigned to the user.

### Constructing secure AWS Management Console shortcut links with URL encoding
<a name="aam-construct-shortcut-links-url-encoding"></a>

All parameter values of the URL, including the account ID, IAM role name, and destination URL, must be URL-encoded.

Shortcut links extend the account access portal URL with the following path:

```
/#/console?account_id=[account_ID]&role_name=[role_name]&destination=[destination_URL]
```

The full URL in a commercial AWS Region follows this pattern:

```
https://[Tenant-ID].account-access.[Region].app.aws/#/console?account_id=[account_ID]&role_name=[role_name]&destination=[destination_URL]
```

Here's an example shortcut link that signs a user into account 123456789012 with the S3FullAccess IAM role name, and takes them to the S3 console home page:

```
https://aa-gyxmap389.account-access.us-east-2.app.aws/#/console?account_id=123456789012&role_name=S3FullAccess&destination=https%3A%2F%2Fconsole.aws.amazon.com%2Fs3%2Fhome
```

### Considerations
<a name="aam-shortcut-links-considerations"></a>

The following considerations apply to the use of shortcut links:
+ If you share shortcut links with coworkers, they need to have the same account assignments to be able to use the links in the same way.
+ Shortcut links are Regional links. If the referenced Region is experiencing a disruption, the link might not work.
+ Shortcut links contain the account ID and role name in plain text. Consider whether your organization's policies restrict where this metadata is stored.