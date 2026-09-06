

# Configuring Your Account
<a name="configure-account"></a>

The steps in this section describe how to sign in and create an account alias and access keys.

**To sign in to the AWS GovCloud (US) console:**

1. Open the [AWS GovCloud (US) console](https://console.amazonaws-us-gov.com).

1. Sign in using your account number and IAM administrator user credentials. For your user name, type `Administrator`.
**Note**  
If you did not save your AWS GovCloud (US) sign-in link, which includes your account number, you can retrieve your account number by signing in to the standard AWS Management Console with your root user credentials and choosing **Account**. On the **Account Settings** page, your 12-digit AWS GovCloud (US) account number appears under **Linked AWS GovCloud (US) account**.

**To create an account alias**  
Creating an account alias is optional, but strongly recommended. If you do not create an account alias, be sure to save your AWS GovCloud (US) sign-in link because your AWS GovCloud (US) account number is different from your AWS account number.

1. Sign in to the AWS GovCloud (US) console and open the IAM console at https://console.amazonaws-us-gov.com/iam.

1. Next to the IAM users sign-in link, choose **Customize**.

1. Type an alias for your account.

    IAM users can now use either the account alias or account number when signing in to the AWS GovCloud (US) console.

**To create and download access keys**  
The password for your AWS GovCloud (US) administrator IAM user cannot be reset by the linked standard AWS account root user. Creating access keys for your AWS GovCloud (US) administrator user is helpful because they can be used to reset your administrator password from the command line.

1. Sign in to the AWS GovCloud (US) console and open the IAM console at https://console.amazonaws-us-gov.com/iam.

1. In the navigation pane, choose **Users**, and select the IAM user account for which you would like to generate access keys.

1. On the **My Security Credentials** tab, choose **Create Access Key**.

1. To download the access key, choose **Download Credentials** and save them locally.

**Important**  
If you configure an IAM password expiration policy that requires administrator reset, and your Administrator password expires, access keys with appropriate privileges can be used to reset your administrator password from the command line. If you do not have additional administrator users created or access keys for your Administrator account, you will need to contact support to regain access to your account.