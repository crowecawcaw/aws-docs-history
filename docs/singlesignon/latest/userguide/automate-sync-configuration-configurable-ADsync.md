# Automate your sync

configuration for configurable AD sync

To ensure that your automated workflow works as expected with configurable AD sync, we
recommend that you perform the following steps to automate your sync configuration.

###### To automate your sync configuration for configurable AD sync

1. In Active Directory, create a _parent sync group_ to contain all
   users and groups that you want to sync into IAM Identity Center. For example, you can name the group
   _IAMIdentityCenterAllUsersAndGroups_.
2. In IAM Identity Center, add the parent sync group to your configurable sync list. IAM Identity Center will
   synchronize all users, groups, sub-groups, and members of all groups contained within
   the parent sync group.
3. Use the Active Directory user and group management API actions provided by Microsoft
   to add or remove users and groups from the parent sync group.
