# Use Active Directory to authenticate

users

To use your corporate Active Directory or AWS Managed Microsoft AD for user authenticated
access to your SMB file share, edit the SMB settings for your gateway with your
Microsoft AD domain credentials. Doing this allows your gateway to join your Active
Directory domain and allows members of the domain to access the SMB file
share.

###### Note

Using Directory Service, you can create a hosted Active Directory domain service in the
AWS Cloud.

To use AWS Managed Microsoft AD with an Amazon EC2 gateway, you must create the Amazon EC2 instance
in the same VPC as the AWS Managed Microsoft AD, add the \_workspaceMembers security group to
the Amazon EC2 instance, and join the AD domain using the Admin credentials from the
AWS Managed Microsoft AD.

For more information about AWS Managed Microsoft AD, see the [_AWS Directory Service Administration
Guide_](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md").

For more information about Amazon EC2, see the [_Amazon Elastic Compute Cloud Documentation_](../../../ec2.md "../../../ec2.md").

You can also activate access control lists (ACLs) on your SMB file share. For
information about how to activate ACLs, see [Using Windows ACLs to limit SMB file share access](smb-acl.md "smb-acl.md").

###### To turn on Active Directory authentication

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Gateways**, then choose the gateway for which
   you want to edit SMB settings.
3. From the **Actions** drop-down menu, choose
   **Edit SMB settings**, then choose **Active
   Directory settings**.
4. For **Domain name**, enter the name of the Active
   Directory domain you want your gateway to join.

###### Note

**Active Directory status** shows
**Detached** when a gateway has never joined a
domain.

Your Active Directory service account must have the requisite
permissions. For more information, see [Active Directory service account permission
requirements](ad-serviceaccount-permissions.md "ad-serviceaccount-permissions.md").

Joining a domain creates an Active Directory computer account in the
default computers container (which is not an OU), using the gateway's
**Gateway ID** as the account name (for example,
SGW-1234ADE). It is not possible to customize the name of this
account.

If your Active Directory environment requires that you pre-stage
accounts to facilitate the join domain process, you will need to create
this account ahead of time.

If your Active Directory environment has a designated OU for new
computer objects, you must specify that OU when joining the
domain.

If your gateway can't join an Active Directory directory, try
joining with the directory's IP address by using the [JoinDomain](../../../storagegateway/latest/APIReference/API_JoinDomain.md "../../../storagegateway/latest/APIReference/API_JoinDomain.md") API operation. 5. For **Domain user** and **Domain
password**, enter the credentials for the Active Directory
service account that the gateway will use to join the domain. 6. (Optional) For **Organization unit (OU)**, enter the
designated OU that your Active Directory uses for new computer
objects. 7. (Optional) For **Domain controller(s) (DC)**, enter the
name of one or more DCs through which your gateway will connect to Active
Directory. You can enter multiple DCs as a comma-separated list. You can
leave this field blank to allow DNS to automatically select a DC. 8. Choose **Save changes**.

###### To limit file share access to specific AD users and groups

1. In the Storage Gateway console, choose the file share that you want to limit
   access to.
2. From the **Actions** drop-down menu, choose
   **Edit file share access settings**.
3. In the **User and group file share access** section,
   choose your settings.

For **Allowed users and groups**, choose **Add
allowed user** or **Add allowed group** and
enter an AD user or group that you want to allow file share access. Repeat
this process to allow as many users and groups as necessary.

For **Denied users and groups**, choose **Add
denied user** or **Add denied group** and
enter an AD user or group that you want to deny file share access. Repeat
this process to deny as many users and groups as necessary.

###### Note

The **User and group file share access** section
appears only if **Active Directory** is
selected.

Groups must be prefixed with the `@` character. Acceptable
formats include: `DOMAIN\User1`, `user1`,
`@group1`, and `@DOMAIN\group1`.

If you configure **Allowed and Denied Users and
Groups** lists, then Windows ACLs will not grant any access
that overrides those lists.

The **Allowed and Denied Users and Groups** lists are
evaluated before ACLs, and control which users can mount or access the
file share. If any users or groups are placed on the
**Allowed** list, the list is considered active,
and only those users can mount the file share.

After a user has mounted a file share, ACLs then provide more granular
protection that controls which specific files or folders the user can
access. For more information, see
[Activating Windows ACLs on a new SMB file share](smb-acl.md#enable-acl-new-fileshare "smb-acl.md#enable-acl-new-fileshare"). 4. When you finish adding your entries, choose
**Save**.
