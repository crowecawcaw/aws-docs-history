# Manage user and group access to

Amazon Managed Grafana workspaces

You access Amazon Managed Grafana workspaces with users that are set up in your Identity provider
(IdP) or AWS IAM Identity Center. You must give those users (or groups that they belong to)
permissions to the workspace. You can give them `User`, `Editor`,
or `Admin` permissions.

## Grant permissions to a user or

group

**Prerequisites**

- To grant a user or a user group access to Amazon Managed Grafana workspaces, the user
  or group must first be provisioned in an Identity provider (IdP) or in
  AWS IAM Identity Center. For more information, see [Authenticate users in Amazon Managed Grafana
  workspaces](authentication-in-AMG.md "authentication-in-AMG.md").
- To manage user and group access, you must be signed in as a user that has
  the AWS Identity and Access Management (IAM) policy
  **AWSGrafanaWorkspacePermissionManagementV2**, or
  equivalent permissions. If you are managing users with IAM Identity Center, you must also
  have the **AWSSSOMemberAccountAdministrator** and
  **AWSSSODirectoryReadOnly** IAM policies, or
  equivalent permissions. For more information, see [Assign
  and unassign users access to Amazon Managed Grafana](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-assign-users "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-assign-users").

###### To manage user access to a Grafana workspace using the Amazon Managed Grafana

console

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. In the left navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the name of the workspace that you want to manage.
5. Choose the **Authentication** tab.
6. If you are using IAM Identity Center in this workspace, choose **Configure users
   and user groups** and do one or more of the following:
   - To give a user access to the Amazon Managed Grafana workspace, select the check
     box next to the user, and choose **Assign
     user**.
   - To make a user an `Admin` of the workspace, choose
     **Make admin**.
   - To remove workspace access for a user, choose **Unassign
     user**.
   - To add groups of users such as an LDAP group, choose the
     **Assigned user groups** tab. Then, do one of
     the following:
     - To give all members of a group access to the Amazon Managed Grafana
       workspace, select the check box next to the group, and
       choose **Assign group**.
     - To give all members of a group the `Admin` role
       in the workspace, choose **Make
       admin**.
     - To remove workspace access for all members of a group,
       choose **Unassign group**.

###### Note

If you are using IAM Identity Center to manage users, use the IAM Identity Center console only to
provision new users and groups. Use the Amazon Managed Grafana console or APIs to
give or remove access to your Grafana workspaces.

If IAM Identity Center and Amazon Managed Grafana get out of sync, you are presented with an
option to **Resolve** any conflicts. For more
information, see [Permission mismatch errors
when configuring users and groups](#AMG-manage-users-and-groups-mismatch "#AMG-manage-users-and-groups-mismatch"),
below. 7. If you are using SAML in this workspace, choose **SAML
configuration** and do one or more of the following:

    * For **Import method**, do one of the
     following:




    	+ Choose **URL** and enter the URL of the
    	 IdP metadata.
    	+ Choose **Upload or copy/paste**. If you
    	 are uploading the metadata, choose **Choose
    	 file** and select the metadata file. Or, if you
    	 are using copy and paste, copy the metadata into
    	 **Import the metadata**.
    * For **Assertion attribute role**, enter the name
     of the SAML assertion attribute from which to extract role
     information.
    * For **Admin role values**, either enter the user
     roles from your IdP who should all be granted the `Admin`
     role in the Amazon Managed Grafana workspace, or select **I want to
     opt-out of assigning admins to my workspace.**


    ###### Note

    If you choose **I want to opt-out of assigning admins
     to my workspace.**, you won't be able to use the
     Amazon Managed Grafana console to administer the workspace, including tasks
     such as managing data sources, users, and dashboard permissions.
     You can make administrative changes to the workspace only by
     using Amazon Managed Grafana APIs.
    * (Optional) To enter additional SAML settings, choose
     **Additional settings** and do one or more the
     following, and then choose **Save SAML
     configuration**. All of these fields are
     optional.




    	+ For **Assertion attribute name**, specify
    	 the name of the attribute within the SAML assertion to use
    	 for the user full "friendly" names for SAML users.
    	+ For **Assertion attribute login**,
    	 specify the name of the attribute within the SAML assertion
    	 to use for the user sign-in names for SAML users.
    	+ For **Assertion attribute email**,
    	 specify the name of the attribute within the SAML assertion
    	 to use for the user email names for SAML users.
    	+ For **Login validity duration (in
    	 minutes)**, specify how long a SAML user's
    	 sign-in is valid before the user must sign in again.
    	+ For **Assertion attribute organization**,
    	 specify the name of the attribute within the SAML assertion
    	 to use for the "friendly" name for user
    	 organizations.
    	+ For **Assertion attribute groups**,
    	 specify the name of the attribute within the SAML assertion
    	 to use for the "friendly" name for user groups.
    	+ For **Allowed organizations**, you can
    	 limit user access to only the users who are members of
    	 certain organizations in the IdP. Enter one or more
    	 organizations to allow, separating them with commas.
    	+ For **Editor role values**, enter the
    	 user roles from your IdP who should all be granted the
    	 `Editor` role in the Amazon Managed Grafana workspace.
    	 Enter one or more roles, separated by commas.

8. Alternatively, to add groups of users such as an LDAP group, choose the
   **User Group** tab. Then, do one of the following:
   - To give all members of a group access to the Amazon Managed Grafana workspace,
     select the check box next to the group, and choose **Assign
     group**.
   - To give all members of a group the `Admin` role in the
     workspace, choose **Make admin**.
   - To remove workspace access for all members of a group, choose
     **Unassign group**.

## Permission mismatch errors

when configuring users and groups

You might run into mismatch errors when configuring users and groups in the
Amazon Managed Grafana console. This indicates that Amazon Managed Grafana and IAM Identity Center are out of sync. In this
case, Amazon Managed Grafana displays a warning and a choice to **Resolve** the
mismatch. If you choose **Resolve**, Amazon Managed Grafana displays a dialog
with a list of users that have permissions that are out of sync.

Users that have been removed from IAM Identity Center show up as `Unknown user`, with
a numeric ID in the dialog. For these users, the only way to fix the mismatch is to
choose **Resolve**, and remove their permissions.

Users that are still in IAM Identity Center, but no longer belong to a group with the access
rights that they previously had, show up with their user name in the
**Resolve** list. There are two ways to fix this issue. You can
use the **Resolve** dialog to remove or reduce their access, or you
can give them access by following the instructions in the previous section.

## Frequently asked

questions about permissions mismatches

###### Why am I seeing an error stating mismatch in permissions in the

**Configure Users and Groups** section of the Amazon Managed Grafana
console?

You are seeing this message because a mismatch has been identified in users
and group associations in IAM Identity Center and permissions in Amazon Managed Grafana for your workspace.
You can add or remove users to your Grafana workspace from the Amazon Managed Grafana console
(in the **Configure Users and Groups** tab), or from the IAM Identity Center
console (**Application assignments** page). However, the
Grafana user permissions can only be defined from Amazon Managed Grafana (using the Amazon Managed Grafana
console or APIs), by assigning **Viewer**,
**Editor**, or **Admin** permissions to
the user or group. A user can belong to multiple groups with varying
permissions, in which case their permission is based on the highest access level
across all groups and permissions the user belongs to.

Mismatched records can result from:

- A user or group is deleted from IAM Identity Center, but not in Amazon Managed Grafana. These records
  show as **Unknown users** in the Amazon Managed Grafana console.
- A user or group's association with Grafana is deleted in IAM Identity Center (under
  **Application assignments**), but not in
  Amazon Managed Grafana.
- User permissions were previously updated from the Grafana workspace
  directly. Updates from the Grafana workspace are not supported in
  Amazon Managed Grafana.

To avoid these mismatches, use the Amazon Managed Grafana console or Amazon Managed Grafana APIs to manage
user and group permissions for your workspace.

###### I have previously updated the access levels for some of my team members from

the Grafana workspace. Now I see that their access levels are reverted back to
their older access level. Why am I seeing this and how do I resolve
this?

This is most likely due to a mismatch that was identified between the user and
group association in IAM Identity Center and the permission records Amazon Managed Grafana for your
workspace. If your team members are experiencing different access levels, you or
an admin for your Amazon Managed Grafana might have resolved the mismatch from the Amazon Managed Grafana
console, removing the mismatched records. You can re-assign the required access
levels from the Amazon Managed Grafana console or APIs to restore the desired
permissions.

###### Note

User access management is not supported from the Grafana workspace. Use the
Amazon Managed Grafana console or APIs to assign user or group permissions.

###### Why am I noticing changes in my access levels? For example, I previously had

admin access, but now only have editor permissions.

An admin for your workspace might have changed your permissions. This can
happen inadvertently in the case of a mismatch between your user and group
associations in IAM Identity Center and your permissions in Amazon Managed Grafana. In this case, resolving
the mismatch might have removed your higher access permissions. You can request
an admin to re-assign the required access level from the Amazon Managed Grafana
console.
