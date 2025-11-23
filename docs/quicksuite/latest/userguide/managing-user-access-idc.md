# Managing access for IAM Identity Center users

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                                                                   |
| --------------------------------------------------------------------------------- |
| Intended audience:<br>System administrators and Amazon Quick Suite administrators |

AWS administrators can use this topic to learn more about managing accounts that are
integrated with IAM Identity Center. The information in this section also applies to Quick Suite
accounts that use Active Directory.

To manage Quick Suite users, you must have administrative privileges in
Quick Suite and also the appropriate AWS permissions. For more information about
the necessary AWS permissions, see [IAM
policy examples for Quick Suite](../../../quicksight/latest/user/iam-policy-examples.md "../../../quicksight/latest/user/iam-policy-examples.md"). If you are using directory groups,
you need to be a network administrator.

Each Quick Suite Enterprise edition account can have an unlimited number of
users. User names that contain a semicolon ( `;` ) aren't supported.

Use the following topics to add, view, and deactivate Quick Suite users.

###### Important

You can't remap Amazon Quick Suite users or groups from one identity store to another.
For example, if you are migrating from an on-premises Active Directory to Directory Service, or
the other way around, you unsubscribe and resubscribe to Amazon Quick Suite. You do this
because even if the user's aliases remain the same, the underlying identity data
changes. To make the transition easier, request in advance that your users document
all their Amazon Quick Suite assets and settings before the migration.

###### Topics

- [Adding users](#add-user-accounts-enterprise "#add-user-accounts-enterprise")
- [Managing user access](#view-user-accounts-enterprise "#view-user-accounts-enterprise")
- [Deactivating user
  accounts](#deactivate-user-groups-enterprise "#deactivate-user-groups-enterprise")
- [Changing a user's
  role](#updating-user-accounts-enterprise "#updating-user-accounts-enterprise")
- [Deleting Enterprise
  accounts](#delete-a-user-account-enterprise "#delete-a-user-account-enterprise")

## Adding users

With IAM Identity Center, add users to Amazon Quick Suite by associating their IAM Identity Center group to an
Admin, Admin Pro, Author, Author Pro, Reader, or Reader Pro role in
Quick Suite. All users in the selected groups are authorized to sign in to
Quick Suite.

For more information about Pro roles in Quick Suite see [Get started with Generative BI](../../../quicksight/latest/user/generative-bi-get-started.md "../../../quicksight/latest/user/generative-bi-get-started.md").

To see which groups are integrated with your Quick Suite account, follow the
procedure in [Managing user access](../../../quicksight/latest/user/view-user-accounts-enterprise.md "../../../quicksight/latest/user/view-user-accounts-enterprise.md").

## Managing user access

Use the following procedure to view groups that are assigned to a role that grants
access to Quick Suite.

1. Open the [Quick Suite
   console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. Choose **Manage Quick Suite**, and then choose
   **Manage Users**.
3. Choose **Manage role groups**.
4. In the **Manage role groups** page, use the tables to add
   or remove groups in IAM Identity Center or Active Directory from the Admin, User, or
   Reader roles in Quick Suite.

## Deactivating user

accounts

Deactivating a Amazon Quick Suite group or user account removes that group or user's
access to Quick Suite resources, like analyses or data sets. IAM Identity Center or Active
Directory users that are removed from a group that grants them access to
Quick Suite lose access to Quick Suite. These users appear in the
**Inactive users** list in Quick Suite until the first
day of the following month. After that, the deactivated users are automatically
removed from the **Inactive users** list. Before you deactivate a
user, you can reassign their resources to another user with the asset management
console.

If you later need to reactivate a Quick Suite user's account, put the
user into a group with access to Quick Suite. Doing this restores their access
to Quick Suite and to any existing resources that are still associated with
that user.

###### Note

With IAM Identity Center integrated into your Amazon Quick Suite account or Active Directory
users, you can change a user's role type by moving them to a group that is
associated with a different Amazon Quick Suite role. If a user is in multiple groups
that are mapped to different Amazon Quick Suite role types, the user is able to access
Amazon Quick Suite with the role that offers the broadest level of access. Accounts
that use other identity types can't upgrade or downgrade a user by transferring
them between groups. For more information, see [Changing a user's role](../../../quicksight/latest/user/updating-user-accounts-enterprise.md "../../../quicksight/latest/user/updating-user-accounts-enterprise.md").

You can activate or deactivate multiple users at once by adding or removing one or
more IAM Identity Center or Active Directory groups that are associated with a role in
Amazon Quick Suite.

## Changing a user's

role

If you're using IAM Identity Center or Active Directory, you can change a user's role
by adding or removing them from a group that's mapped to the role that you want
to assign them in Quick Suite. You can also perform this task by adding a new
group to a role in Quick Suite. To do this, you need both administrative
privileges in Quick Suite and also appropriate AWS permissions.

With IAM Identity Center integrated users, you can change role types for a user by moving them
to a group that is associated with a different Quick Suite role. If a user
belongs to multiple groups that are mapped to different role types, the user is able
to access Quick Suite with the role that offers the broadest level of
access.

When you make changes to users or groups in Quick Suite, it can take up to
five minutes for the change to take effect. Examples of such changes are the
following:

- Deleting a user
- Changing a user from an admin to an author
- Adding or removing group members

The five-minute time period allows changes to propagate throughout the
system.

## Deleting Enterprise

accounts

If a user is deleted from IAM Identity Center or Active Directory or is removed from a group
that's associated with a role in Quick Suite, the user no longer exists
in Quick Suite. You do not need to delete the user in the Quick Suite
application. The deleted user will appear in the **Inactive users**
list in Quick Suite until the first day of the following month. After that
date passes, the user is automatically removed from the list.
