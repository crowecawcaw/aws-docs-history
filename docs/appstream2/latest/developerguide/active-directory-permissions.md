# Granting Permissions to Create and Manage

Active Directory Computer Objects

To allow AppStream 2.0 to perform Active Directory computer object operations, you need
an account with sufficient permissions. As a best practice, use an account that has
only the minimum privileges necessary. The minimum Active Directory organizational
unit (OU) permissions are as follows:

- Create Computer Object
- Change Password
- Reset Password
- Write Description

Before setting up permissions, you'll need to do the following first:

- Obtain access to a computer or an EC2 instance that is joined to your
  domain.
- Install the Active Directory User and Computers MMC snap-in. For more
  information, see [Installing or Removing Remote Server Administration Tools for Windows 7](https://technet.microsoft.com/en-us/library/ee449483.aspx "https://technet.microsoft.com/en-us/library/ee449483.aspx")
  in the Microsoft documentation.
- Log in as a domain user with appropriate permissions to modify the OU
  security settings.
- Create or identify the user, service account, or group for which to
  delegate permissions.

###### To set up minimum permissions

1. Open **Active Directory Users and Computers** in your
   domain or on your domain controller.
2. In the left navigation pane, select the first OU on which to provide
   domain join privileges, open the context (right-click) menu , and then
   choose **Delegate Control**.
3. On the **Delegation of Control Wizard** page,
   choose **Next**, **Add**.
4. For **Select Users, Computers, or Groups**, select the
   pre-created user, service account, or group, and then choose
   **OK**.
5. On the **Tasks to Delegate** page, choose
   **Create a custom task to delegate**, and then choose
   **Next**.
6. Choose **Only the following objects in the folder**,
   **Computer objects**.
7. Choose **Create selected objects in this
   folder**, **Next**.
8. For **Permissions**, choose **Read**, **Write**,
   **Change Password**, **Reset Password**, **Next**.
9. On the **Completing the Delegation of Control
   Wizard** page, verify the information and choose **Finish**.
10. Repeat steps 2-9 for any additional OUs that require these
    permissions.
    If you delegated permissions to a group, create a user or service account with a
    strong password and add that account to the group. This account will then have
    sufficient privileges to connect your streaming instances to the directory. Use this
    account when creating your AppStream 2.0 directory configuration.
