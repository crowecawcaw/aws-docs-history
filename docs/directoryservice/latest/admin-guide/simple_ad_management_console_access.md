# Enabling access to the AWS Management Console with

Simple AD credentials

Directory Service allows you to grant members of your directory access to the AWS Management Console. By default,
your directory members do not have access to any AWS resources. You assign IAM roles to
your directory members to give them access to the various AWS services and resources. The
IAM role defines the services, resources, and level of access that your directory members
have.

Before you can grant console access to your directory members, your directory must have an
access URL. For more information about how to view directory details and get your access URL,
see [Viewing AWS Managed Microsoft AD directory
information](ms_ad_view_directory_info.md "ms_ad_view_directory_info.md"). For more
information about how to create an access URL, see [Creating an access URL for AWS Managed Microsoft AD](ms_ad_create_access_url.md "ms_ad_create_access_url.md").

For more information about how to create and assign IAM roles to your directory members,
see [Granting AWS Managed Microsoft AD users and groups access to AWS
resources with IAM roles](ms_ad_manage_roles.md "ms_ad_manage_roles.md").

###### Topics

- [Enabling AWS Management Console access](#simple_ad_console_enable "#simple_ad_console_enable")
- [Disabling AWS Management Console access](#simple_ad_console_disable "#simple_ad_console_disable")
- [Setting login session length](#simple_ad_console_session "#simple_ad_console_session")
  **Related AWS Security Blog Article**

- [How to Access the AWS Management Console Using AWS Managed Microsoft AD and Your On-Premises Credentials](https://aws.amazon.com/blogs/security/how-to-access-the-aws-management-console-using-aws-microsoft-ad-and-your-on-premises-credentials/ "https://aws.amazon.com/blogs/security/how-to-access-the-aws-management-console-using-aws-microsoft-ad-and-your-on-premises-credentials/")
  **Related AWS re:Post Article**

- [How can I grant access to the AWS Management Console for an on-premises Active Directory users?](https://repost.aws/knowledge-center/enable-active-directory-console-access "https://repost.aws/knowledge-center/enable-active-directory-console-access")

## Enabling AWS Management Console access

By default, console access is not enabled for any directory. To enable console access
for your directory users and groups, perform the following steps:

###### To enable console access

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, select the
   **Application management** tab.
4. Under the **AWS Management Console** section, choose
   **Enable**. Console access is now enabled for your
   directory.

###### Important

Before users can sign-in to the console with your access URL, you must
first add your users to the IAM role. For general information about assigning
users to IAM roles, see [Assigning users or groups to an existing IAM
role](assign_role.md "assign_role.md"). After the IAM roles have been assigned,
users can then access the console using your access URL. For example, if
your directory access URL is example-corp.awsapps.com, the URL to access the
console is https://example-corp.awsapps.com/console/.

## Disabling AWS Management Console access

To disable console access for your directory users and groups, perform the following
steps:

###### To disable console access

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, select the
   **Application management** tab.
4. Under the **AWS Management Console** section, choose
   **Disable**. Console access is now disabled for your
   directory.
5. If any IAM roles have been assigned to users or groups in the directory, the
   **Disable** button may be unavailable. In this case, you
   must remove all IAM role assignments for the directory before proceeding,
   including assignments for users or groups in your directory that have been
   deleted, which will show as **Deleted User** or
   **Deleted Group**.

After all IAM role assignments have been removed, repeat the steps
above.

## Setting login session length

By default, users have 1 hour to use their session after successfully signing in to
the console before they are logged out. After that, users must sign in again to start
the next 1 hour session before being logged off again. You can use the following
procedure to change the length of time to up to 12 hours per session.

###### To set login session length

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, choose
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, select the
   **Application management** tab.
4. Under the **AWS apps & services** section, choose
   **AWS Management Console**.
5. In the **Manage Access to AWS Resource** dialog box, choose
   **Continue**.
6. In the **Assign users and groups to IAM roles** page, under
   **Set login session length**, edit the numbered value, and
   then choose **Save**.
