# How configurable AD sync works

IAM Identity Center refreshes the AD-based identity data in the identity store by using the following
process. To learn more about the prerequisites, see [Prerequisites and considerations](provision-users-from-ad-configurable-ADsync.md#prerequisites-configurable-ADsync "provision-users-from-ad-configurable-ADsync.md#prerequisites-configurable-ADsync").

## Creation

After you connect your self-managed directory in Active Directory or your AWS Managed Microsoft AD
directory that is managed by AWS Directory Service to IAM Identity Center, you can explicitly configure the Active
Directory users and groups that you want to sync into the IAM Identity Center identity store. The
identities that you choose will be synchronized every three hours or so into the IAM Identity Center
identity store. Depending on the size of your directory, the sync process might take
longer.

Groups that are members of other groups (called _nested groups_ or
_child groups_) are also written to the identity store.

You can only assign access to new users or groups after they are synchronized into the
IAM Identity Center identity store.

## Update

The identity data in the IAM Identity Center identity store stays fresh by periodically reading data
from the source directory in Active Directory. IAM Identity Center syncs data from your Active Directory
every hour in a sync cycle by default. It may take 30 minutes to 2 hours for the data to
sync into IAM Identity Center, based on the size of your Active Directory.

User and group objects that are in the sync scope and their memberships are created or
updated in IAM Identity Center to map to the corresponding objects in the source directory in Active
Directory. For user attributes, only the subset of attributes listed in the
**Attributes for access control** section of the IAM Identity Center console are
updated in IAM Identity Center. It may take one sync cycle for any attribute updates you make in Active
Directory to reflect in IAM Identity Center.

You can also update the subset of users and groups that you synchronize into the IAM Identity Center
identity store. You can choose to add new users or groups to this subset, or remove them.
Any identities that you add are synchronized at the next scheduled sync. Identities that
you remove from the subset will stop being updated in the IAM Identity Center identity store. Any user
who isn't synchronized for more than 28 days will be disabled in the IAM Identity Center identity store.
The corresponding user objects will be automatically disabled in the IAM Identity Center identity store
during the next sync cycle, unless they are part of another group that is still part of
the sync scope.

## Deletion

Users and groups are deleted from the IAM Identity Center identity store when the corresponding user
or group objects are deleted from the source directory in Active Directory. Alternatively,
you can explicitly delete user objects from the IAM Identity Center identity store by using the IAM Identity Center
console. If you use the IAM Identity Center console, you must also remove the users from the sync scope
to ensure that they aren't re-synced back into IAM Identity Center during the next sync cycle.

You can also pause and restart synchronization at any time. If you pause
synchronization for more than 28 days, all your users will be disabled.
