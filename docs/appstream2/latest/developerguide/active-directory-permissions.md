

# Granting Permissions to Create and Manage Active Directory Computer Objects
<a name="active-directory-permissions"></a>

To allow WorkSpaces Applications to perform Active Directory computer object operations, you need an account with sufficient permissions. As a best practice, use an account that has only the minimum privileges necessary. The minimum Active Directory organizational unit (OU) permissions are as follows:
+ Create Computer Object
+ Change Password
+ Reset Password
+ Write Description

Before setting up permissions, you'll need to do the following first:
+ Obtain access to a computer or an EC2 instance that is joined to your domain.
+ Install the Active Directory User and Computers MMC snap-in. For more information, see [Installing or Removing Remote Server Administration Tools for Windows 7](https://technet.microsoft.com/en-us/library/ee449483.aspx) in the Microsoft documentation.
+ Log in as a domain user with appropriate permissions to modify the OU security settings.
+ Create or identify the user, service account, or group for which to delegate permissions.

**To set up minimum permissions**

1. Open **Active Directory Users and Computers** in your domain or on your domain controller.

1. In the left navigation pane, select the first OU on which to provide domain join privileges, open the context (right-click) menu , and then choose **Delegate Control**.

1. On the **Delegation of Control Wizard** page, choose **Next**, **Add**.

1. For **Select Users, Computers, or Groups**, select the pre-created user, service account, or group, and then choose **OK**.

1. On the **Tasks to Delegate** page, choose **Create a custom task to delegate**, and then choose **Next**.

1. Choose **Only the following objects in the folder**, **Computer objects**.

1. Choose **Create selected objects in this folder**, **Next**.

1. For **Permissions**, choose **Read**, **Write**, **Change Password**, **Reset Password**, **Next**.

1. On the **Completing the Delegation of Control Wizard** page, verify the information and choose **Finish**.

1. Repeat steps 2-9 for any additional OUs that require these permissions.

If you delegated permissions to a group, create a user or service account with a strong password and add that account to the group. This account will then have sufficient privileges to connect your streaming instances to the directory. Use this account when creating your WorkSpaces Applications directory configuration.