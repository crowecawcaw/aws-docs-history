

# User lifecycle and data handling in Amazon Quick
<a name="user-lifecycle-data-handling"></a>

What happens to a user's data and assets in Amazon Quick depends on how the user is removed. This page describes the three removal paths and their effect on a user's assets. It also covers the cleanup steps you must complete as an administrator.

**Topics**
+ [How users are removed](#user-removal-paths)
+ [What is deleted immediately](#user-removal-metadata-deletion)
+ [Assets with multiple owners](#user-removal-shared-assets)
+ [Orphaned assets](#user-removal-orphaned-assets)
+ [Deactivation compared with deletion](#user-deactivation-vs-deletion)
+ [Account termination](#user-removal-account-termination)
+ [Conversations and Amazon Q data](#user-conversations-q-data)
+ [When access ends](#user-removal-access-timing)

## How users are removed
<a name="user-removal-paths"></a>

How a user is removed determines what happens to the assets they owned. The following table describes the three removal paths.


| Removal path | Access | What happens to the user's assets | 
| --- | --- | --- | 
| Console deletion by an administrator | Ends when the user is deleted. | The administrator chooses whether to transfer the user's assets to another user or delete them. If no transfer user is chosen, assets owned solely by the deleted user are deleted, and assets that have other owners remain available to those owners with the deleted user removed from their permissions. | 
| DeleteUser API operation | Ends when the user is deleted. | No asset cleanup runs. The user's assets are neither transferred nor deleted; they remain in the account without an owner until an administrator transfers them. | 
| Removal from a directory group (IAM Identity Center or Active Directory) | The user can no longer sign in. | No asset cleanup runs automatically. Amazon Quick detects the removal and lists the user in the Inactive users list on the Manage users page, where an administrator can review them and apply the same transfer-or-delete choice as console deletion. Until an administrator acts, the user's assets remain in the account. This detection applies only to IAM Identity Center and Active Directory. | 

To complete cleanup, administrators use the asset management console to transfer assets owned by a departed user, and review users removed from IAM Identity Center or Active Directory on the **Manage users** page, where those users appear in the **Inactive users** list. For the console deletion procedure, see [Deleting a Amazon Quick user account](managing-user-access-qs-iam.md#delete-a-user-account). To transfer assets that no longer have an owner, see [Amazon Quick asset management](manage-qs-assets.md). For users removed from IAM Identity Center or Active Directory, see [Deleting Enterprise accounts](managing-user-access-idc.md#delete-a-user-account-enterprise).

**The Inactive users list applies to directory-federated users only**  
Amazon Quick detects removed users and populates the **Inactive users** list only for accounts that federate through IAM Identity Center or Active Directory. Users that you create directly in Amazon Quick, including IAM federation users, are managed at the user level, so Amazon Quick does not detect their removal from an external identity provider. Remove these users with console deletion or the `DeleteUser` API operation, and transfer or delete their assets as part of that removal.

If your knowledge bases use document-level access control lists (ACLs), also update the ACL configuration to remove the departing user, and refresh the affected knowledge bases. User removal does not update knowledge base ACLs. For more information, see [Best practices for managing ACLs in knowledge bases](acl-best-practices-kb.md).

## What is deleted immediately
<a name="user-removal-metadata-deletion"></a>

When you delete a user through any path, Amazon Quick permanently deletes the user's metadata, including their profile and role membership.

## Assets with multiple owners
<a name="user-removal-shared-assets"></a>

Amazon Quick never deletes an asset that has more than one owner when a user is removed. Amazon Quick removes the departed user from the asset's permissions, and the asset remains available to its other owners.

## Orphaned assets
<a name="user-removal-orphaned-assets"></a>

No user can access assets that remain in the account without an owner – for example, after deletion with the `DeleteUser` API operation, or after identity-provider removal that is pending administrator review – until you transfer them. Use the asset management console to find and transfer assets that a departed user owned. For more information, see [Amazon Quick asset management](manage-qs-assets.md).

## Deactivation compared with deletion
<a name="user-deactivation-vs-deletion"></a>

Deactivating a user revokes the user's access but leaves the user's assets associated with them. Deactivation occurs, for example, when you remove the user from the IAM Identity Center or Active Directory group that grants Amazon Quick access. Reactivating the user restores their access to those assets. Deletion is permanent.

A user who is removed from IAM Identity Center or Active Directory appears in the **Inactive users** list on the **Manage users** page until the first day of the following month. After that date, Amazon Quick removes them from the list.

A user who is deleted but not deactivated can sign in again as a new user, without access to their previous assets.

For more information, see [Deactivating user accounts](managing-user-access-idc.md#deactivate-user-groups-enterprise).

## Account termination
<a name="user-removal-account-termination"></a>

Unsubscribing from Amazon Quick permanently deletes all of your Amazon Quick data, including all metadata, any data in SPICE, and Amazon Q data. For more information about account settings, see [Account details in Amazon Quick](manage-qs-account-settings.md). For how unsubscribing affects the Amazon Q data key, see [Amazon Q data key](customer-managed-keys.md#customer-managed-keys-q-data-key).

## Conversations and Amazon Q data
<a name="user-conversations-q-data"></a>

A user's chat conversations are private to that user. When you delete or deprovision a user, Amazon Quick does not transfer their conversation history to any other user, and you can't access it through the application.

Deleting a user does not immediately delete the user's conversation history. Amazon Quick retains conversations, messages, and chat file attachments on a rolling 30-day window measured from activity, and then permanently deletes them. Users can delete their own conversations at any time. When you unsubscribe from Amazon Quick, Amazon Quick permanently deletes all Amazon Q data, including conversation history.

Amazon Quick does not delete feedback that a user submitted when that user is deleted. Amazon Quick retains analytics data according to your instance's data retention policies.

## When access ends
<a name="user-removal-access-timing"></a>

Removing or deleting a user prevents new sign-ins to Amazon Quick. Amazon Quick also denies requests from the user's existing sessions after the change takes effect, which can take up to five minutes.