# Manage users in the Amazon DataZone console

Your users can access the Amazon DataZone data portal by using either their AWS
credentials or single sign-on (SSO) credentials. To manage users in the Amazon DataZone
console for an Amazon DataZone domain, you must assume an IAM role in the account with
Amazon DataZone management console permissions. [Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") to obtain the minimum permissions necessary to
manage users in the Amazon DataZone console.

###### Topics

- [Manage IAM roles and users](#manage-IAM-users-roles "#manage-IAM-users-roles")
- [Manage SSO users](#manage-sso-users "#manage-sso-users")
- [Manage SSO groups](#manage-sso-groups "#manage-sso-groups")

## Manage IAM roles and users

IAM roles and users are created using AWS Identity and Access Management (IAM)
and gain access to your Amazon DataZone domains through permissions attached to them via
policies. For more information, see [Configure the IAM permissions required to use the
Amazon DataZone data portal](data-portal-permissions.md "data-portal-permissions.md"). In the current release of Amazon DataZone,
an administrator from an Amazon DataZone domain owner account, can create IAM user
profiles for users in their own account or for users in the associated accounts. An
administrator from an Amazon DataZone domain owner account can also set an existing
user's status to Assigned or Unassigned (as in assigned or unassigned to use
Amazon DataZone) or activate or deactivate any existing user.

1. Sign in to the AWS Management Console and open the DataZone console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Select **View domains** and choose the domain’s name from
   the list. The name is a hyperlink.
3. On the details page for the domain, choose **User
   management**.
4. To add a user IAM user in the Amazon DataZone domain owner account or in the
   associated account, choose **Add** and then choose
   **Add IAM users**.
5. On the **Add users** page, choose **Current
   account** or **Associated account**, use the
   **Find and add users or roles** field to find the users
   that you want to add, and then choose **Add users**.
6. To view an existing IAM user's status, on the **User
   management** page, choose **IAM Users** in the
   user type drop-down menu.
   - The **Name** column shows the ARN of the IAM user
     or role.
   - The **Status** column shows the current status of
     the IAM user or role in the domain.
     - Assigned means that the IAM user has been assigned to use
       Amazon DataZone.
     - Unassigned means that the IAM user has been unassigned to
       use Amazon DataZone.
     - Activated means that the IAM user or role has called an
       API, issued a command (via Command Line Interface), or
       accessed the Amazon DataZone portal for your domain.
     - Deactivated means that the IAM user or role can no longer
       use the Amazon DataZone Data Portal. To restrict
       programmatic access see [Restricting
       access to Amazon DataZone](user-management-portal-restricting-programmatic-access.md "user-management-portal-restricting-programmatic-access.md").

7. To deactivate an IAM user or role that is currently activated, check the
   box next to the user and select **Deactivate** from the
   **Actions** menu. This will result in the user no
   longer be able to use the Amazon DataZone Data Portal. To restrict programmatic
   access see [Restricting
   access to Amazon DataZone](user-management-portal-restricting-programmatic-access.md "user-management-portal-restricting-programmatic-access.md").
8. To activate an IAM user or role that is currently deactivated, check the
   box next to the user and select **Activate** from the
   **Actions** menu. The user will gain access to the
   Amazon DataZone Data Portal if the IAM user or role has
   `datazone:GetUserPortalLoginUrl` permissions.

## Manage SSO users

SSO users are created or synchronized with your identity provider. For more
information, see [Setting up AWS IAM Identity Center for Amazon DataZone](sso-setup.md "sso-setup.md") and [Enable IAM Identity Center for
Amazon DataZone](enable-IAM-identity-center-for-datazone.md "enable-IAM-identity-center-for-datazone.md") to enable and
configure AWS IAM Identity Center for Amazon DataZone. You can view the list of SSO
users assigned to the domain, add SSO users, and remove SSO users.

1. Sign in to the AWS Management Console and open the DataZone console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Select **View domains** and choose the domain’s name from
   the list. The name is a hyperlink.
3. On the details page for the domain, scroll down and choose **User
   management**.
4. For user type, select **SSO Users** to view the current
   list of SSO users who have previously authenticated to the data portal. When
   using implicit user assignment, SSO users who have not previously
   authenticated to the data portal will not be listed.
   - The **Name** column shows the SSO user’s
     name.
   - The **Status** column shows the current status of
     the SSO user in the domain.
     - Assigned means that the SSO user has been explicitly
       assigned to the domain. As a result, the user has access to
       Amazon DataZone. This status is only used when your domain’s
       identity provider mode is set to explicit assignment.
     - Activated means that the SSO user has accessed the
       Amazon DataZone portal for the domain. Activation happens
       automatically.
     - Deactivated means that the SSO user’s access is blocked to
       the domain’s data portal.
     - Removed means that the SSO user was previously assigned to
       the domain, but removed before they ever accessed it.

5. Add SSO users by choosing **Add** and **Add
   users**. This option is unavailable if the domain is set to
   implicit user assignment, which means that all users in the identity pool
   have access to the Amazon DataZone domain.
   - On the **Add users** page, search for the aliases
     of the users you want to add. A list will appear below the search
     box with potential matches.
   - Choose the user you want to add. Their alias will appear as a chip
     below the search box.
   - When you are satisfied with the list of users you want to add,
     choose **Add user(s)**.
   - The users are assigned to the Amazon DataZone domain with a status of
     **Assigned**.
   - When the user first accessed the domain’s data portal, the status
     will change automatically to **Activated**.

6. Remove an **Assigned** SSO user by selecting the user and
   choosing **Unassign** from the **Actions**
   menu. As a result, the user will lose access to the Amazon DataZone domain. The
   user’s status will show as **Not assigned**. This option is
   unavailable if the domain is set to implicit user assignment.
7. Deactivate an **Activated** SSO user by selecting the
   user and choosing **Deactivate** from the
   **Actions** menu. As a result, the user’s access to the
   Amazon DataZone data portal will be lost and blocked. The user’s status will show
   as **Deactivated**.
8. Activate a **Deactivated** SSO user by selecting the user
   and choosing **Activate** from the
   **Actions** menu. As a result, the user will regain
   access to the Amazon DataZone data portal. The user’s will show as
   **Activated**.

## Manage SSO groups

SSO groups are created or synchronized with your identity provider in AWS IAM
Identity Center. For more information, see [Setting up AWS IAM Identity Center for Amazon DataZone](sso-setup.md "sso-setup.md") and [Enable IAM Identity Center for
Amazon DataZone](enable-IAM-identity-center-for-datazone.md "enable-IAM-identity-center-for-datazone.md") to enable and
configure AWS IAM Identity Center for Amazon DataZone. You can view the list of SSO
groups assigned to the domain, add SSO groups, and remove SSO groups.

1. Sign in to the AWS Management Console and open the DataZone console at
   [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Select **View domains** and choose the domain’s name from
   the list. The name is a hyperlink.
3. On the details page for the domain, scroll down and choose **User
   management**.
4. For user type, select **SSO Groups** to view the current
   list of SSO groups.
   - The **Name** column shows the SSO group’s
     name.
   - The **Status** column shows the current status of
     the SSO group in the domain.
     - **Assigned** means that the SSO group has
       been explicitly assigned to the domain. As a result, all
       users in the group have access to the domain’s data portal
       (unless the user is deactivated).
     - **Not Assigned** means that the SSO group
       has been removed from the domain. Users in the group do not
       have access to the domain’s data portal via their membership
       in this group.

5. Add SSO groups by choosing **Add** and **Add
   groups**. This option is unavailable if the domain is set to
   implicit user assignment, which means that all users in the identity pool
   have access to the Amazon DataZone domain regardless of group membership.
   - On the **Add groups** page, search for the
     aliases of the groups you want to add. A list will appear below the
     search box with potential matches.
   - Choose the group you want to add. Their alias will appear as a
     chip below the search box.
   - When you are satisfied with the list of groups you want to add,
     choose **Add group(s)**.
   - The groups are assigned to the Amazon DataZone domain with a status of
     **Assigned**.
   - When a member of the group accesses the domain's data portal, the
     status will change automatically to
     **Activated**.

6. Remove an **Assigned SSO group** by selecting the group
   and choosing **Unassign** from the
   **Actions** menu. As a result, the group will lose
   access to the Amazon DataZone domain. The group’s status will show as
   **Not Assigned**. Users that gained their access to
   Amazon DataZone via their membership in this group will lose access. This option
   is unavailable if the domain is set to implicit user assignment.
