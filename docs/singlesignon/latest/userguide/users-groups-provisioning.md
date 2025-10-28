# Users, groups, and provisioning in IAM Identity Center

IAM Identity Center enables you to control who can sign in and what resources they can access. A user
must be provisioned to sign in. You can then assign access only to provisioned users or
groups. Learn about users, groups, and provisioning in IAM Identity Center.

## Username and email address uniqueness

IAM Identity Center requires each user have a unique username. The username is the user’s primary
identifier. The username does not have to match the user’s email address. IAM Identity Center requires
that all usernames and email addresses for your users are non-NULL and unique.

## Groups

Groups are a logical combination of users that you define. You can create groups and add
users to the groups. IAM Identity Center doesn't support nested groups (A group within a group). Groups
are useful when assigning access to AWS accounts and applications. Rather than assign each
user individually, you give permissions to a group. Later, as you add or remove users from a
group, the user dynamically gets or loses access to accounts and applications that you
assigned to the group.

## User and group provisioning

Provisioning is the process of making user and group information available for use by
IAM Identity Center and AWS managed applications or customer managed applications. You can create users
and groups directly in IAM Identity Center or connect your identity source to IAM Identity Center. With IAM Identity Center, you are
able to assign users and groups access to connected applications and AWS accounts.

Provisioning in IAM Identity Center varies based on the identity source that you use. For more
information, see [Manage your identity source](manage-your-identity-source.md "manage-your-identity-source.md").

## User and group deprovisioning

Deprovisioning is the process of removing users and group information from IAM Identity Center.

If you’re using Active Directory or an external identity provider with IAM Identity Center, you should
remove users and groups from these identity sources rather than IAM Identity Center. Deleting IAM Identity Center users
and groups will not completely remove them if your identity source is Active Directory or an
external identity provider.

If you need to deprovision IAM Identity Center users or groups, you should first [remove any assignments of permission sets](howtoremovepermissionset.md "howtoremovepermissionset.md") or
applications to the users or groups you want to deprovision. Otherwise, you’ll have
unassigned permission sets and application assignments in your IAM Identity Center.
