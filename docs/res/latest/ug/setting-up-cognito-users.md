

# Setting up Amazon Cognito users
<a name="setting-up-cognito-users"></a>

Research and Engineering Studio (RES) allows you to set up Amazon Cognito as a native user directory. This allows users to log in to the web portal and Linux-based VDIs with Amazon Cognito user identities. Administrators can import multiple users into the user pool using a csv file from the AWS Console. For more details on bulk user import, see [Importing users into user pools from a CSV file](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html) in the *Amazon Cognito Developer Guide*. RES supports using a Amazon Cognito-based native user directory and SSO together. 

## Administrative setup
<a name="setting-up-cognito-users-admin"></a>

As a RES Administrator, to configure the RES environment to use Amazon Cognito as a user directory, toggle the **Use Amazon Cognito as user directory** button on the **Identities management** page which is accessible from the **Environment Management** page. To allow users to self register, toggle the **User self registration** button on that same page.

![Identities management page showing cognito directory settings](http://docs.aws.amazon.com/res/latest/ug/images/id-management-cognito-directory.png)


## User sign up/sign in flow
<a name="setting-up-cognito-users-user-signin"></a>

If **User self registration** is enabled, you can give your users the URL of your web application. There, users will find an option that says **Not a user yet? Sign up here**.

![User sign-in page with option to self-register](http://docs.aws.amazon.com/res/latest/ug/images/user-sign-up.png)


## Sign up flow
<a name="setting-up-cognito-users-signup"></a>

Users that choose **Not a user yet? Sign up here** will be asked to enter their email and password to create an account.

![Create account page for user self-registration](http://docs.aws.amazon.com/res/latest/ug/images/create-account.png)


As part of the sign up flow, users will be asked to enter the verification code received in their email to complete the sign up process.

![Verification code entry page](http://docs.aws.amazon.com/res/latest/ug/images/verify-email.png)


If self-sign up is disabled, users will not see the sign up link. Administrators must configure the users in Amazon Cognito outside of RES. (See [Creating user accounts as administrator](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-create-user-accounts.html) in the *Amazon Cognito Developer Guide*.)

![Verification code entry page](http://docs.aws.amazon.com/res/latest/ug/images/user-sign-in.png)


## Login page options
<a name="setting-up-cognito-users-login"></a>

If both SSO and Amazon Cognito are enabled, an option to **Sign in with organization SSO** will appear. When users click that option it will reroute them to their SSO login page. By default, users will authenticate with Amazon Cognito if it is enabled.

![User sign-in page with options to sign up, verify account, or sign-in with organization SSO](http://docs.aws.amazon.com/res/latest/ug/images/org-sso-sign-in.png)


## Constraints
<a name="setting-up-cognito-users-constraints"></a>
+ Your Amazon Cognito **Group name** can have a maximum of six letters; only lower case letters are accepted.
+ Amazon Cognito signup will not allow two email addresses with the same user name but a different domain address.
+ If both Active Directory and Amazon Cognito are enabled, and the system detects a duplicate user name, only Active Directory users will be allowed to authenticate. Administrators should take steps to not configure duplicate user names between Amazon Cognito and their Active Directory.
+ Cognito users will not be allowed to launch Windows-based VDIs since RES does not support Amazon Cognito-based authentication for Windows instances.

## Administrator group for Amazon Cognito users
<a name="admin-group-cognito-users-sync"></a>

By default, RES grants Cognito users within the `admins` group administrator privilege. To add users to the Cognito `admins` group:

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home), and choose the existing user pool used for RES.

1. Navigate to **Groups** under **User Management**, and then choose **Create a group.**

1. On the **Create a group** page, in **Group name,** enter `admins`.

1. Select the `admins` group you created, and choose **Add user to group** to add Cognito users.

1. Initiate Cognito synchronization manually by following [Synchronization](#setting-up-cognito-users-sync). 

After a successful Amazon Cognito synchronization, users added to the `admins` group will receive administrator privileges.

## Synchronization
<a name="setting-up-cognito-users-sync"></a>

RES synchronizes its database with user and group information from Amazon Cognito every hour. Any users that belong to the group "admins" will be given sudo privilege in their VDIs.

You can also initiate the sync manually from the Lambda console. 

**Initiate the sync process manually:**

1. Open the [Lambda console](https://console.aws.amazon.com/lambda).

1. Search for the Cognito sync Lambda. This Lambda follows this naming convention: `{{{RES_ENVIRONMENT_NAME}}}_cognito-sync-lambda`.

1. Select **Test**.

1. In the **Test event** section, choose the **Test** button at the top right. The event body format does not matter.

## Security considerations for Cognito
<a name="setting-up-cognito-users-security"></a>

Prior to the 2024.12 release, [user activity logging](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html), which is part of the Amazon Cognito Plus plan feature was enabled by default. This feature was removed from the baseline deployment to save costs for customers who want to try RES. You may re-enable this feature as needed to align with your organization's cloud security settings.