# Assigning IAM Identity Center users and groups to Amazon WorkMail

application

When you enable IAM Identity Center in Amazon WorkMail, WorkMail creates an application in IAM Identity Center on your
behalf. By default, IAM Identity Center users must be assigned to this application or belong to a
group which is assigned to this application in order to access a mailbox in the Amazon WorkMail
organization. For more information, see [AWS
managed applications](../../../singlesignon/latest/userguide/awsapps.md "../../../singlesignon/latest/userguide/awsapps.md") in the AWS IAM Identity Center User Guide.

You can assign IAM Identity Center users and groups to Amazon WorkMail in the following ways:

- By IAM Identity Center users – You can assign IAM Identity Center users to Amazon WorkMail.
- By IAM Identity Center group – You can assign IAM Identity Center groups to Amazon WorkMail. By adding a
  group, all users under a group will have access to Amazon WorkMail.

For more information on adding users and groups, see [Users,
groups, and provisioning in IAM Identity Center](../../../singlesignon/latest/userguide/users-groups-provisioning.md "../../../singlesignon/latest/userguide/users-groups-provisioning.md") .

###### Note

If you are connecting your existing identity source with IAM Identity Center, review the
following before changing your directory source.

- Your authentication is being managed by IAM Identity Center.
- Amazon WorkMail will retain all Amazon WorkMail users and groups.
- IAM Identity Center will retain all IAM Identity Center users, groups, and assignments.
- You must manage Amazon WorkMail users and groups in Amazon WorkMail console.
- You must manage IAM Identity Center users and groups in IAM Identity Center.
- Users without an IAM Identity Center assignment or user association cannot access
  Amazon WorkMail.
- You must manage MFA policy controls in IAM Identity Center.
- When you change the IAM Identity Center source to and from Manage Active Directory in
  IAM Identity Center you must disable the existing IAM Identity Center configurations in Amazon WorkMail and
  reconfigure to associate your Amazon WorkMail users with IAM Identity Center.
  Users and groups synced with your IAM Identity Center directory are available to assign to your Amazon WorkMail
  application. For more information about IAM Identity Center user and group management, see [Get
  started with common tasks in IAM Identity Center.](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md").

###### To assign IAM Identity Center users and groups to Amazon WorkMail, follow these steps.

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the console
window, open the **Select a Region** list and
choose a Region. For more information, see [Region and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_Amazon Web Services General Reference_. 2. In the navigation pane, choose **Identity Center**.

The **IAM Identity Center Settings** page appears. 3. Choose **Assign users and groups**.

You can add and assign new users or assign existing users and groups.

    * Assign Users – You can assign individual IAM Identity Center users to the
     Amazon WorkMail. You can either create a new IAM Identity Center user or search for an existing
     user.
    * Assign Groups – You can also assign an IAM Identity Center group to Amazon WorkMail. All
     members of the group will then be assigned to Amazon WorkMail.

###### Note

All new IAM Identity Center users are enabled by default in IAM Identity Center. To grant access to Amazon WorkMail, you
must set their password in IAM Identity Center and assign them to Amazon WorkMail. For more information, see
[Add
users to your Identity Center directory](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md") .
