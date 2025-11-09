Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding a user to a team directly

You can add team members to your team. When you add a user, the new user will inherit
permissions from all existing roles on the team.

Whether your space is set up for AWS Builder ID user support or identity federation, you
can set up your space to add users directly.

###### Note

When your space is set up to manage team members by using SSO groups, the option to
use **Add users directly** is not available. To use SSO groups, see [Adding an SSO group to a team](managing-teams-add-sso.md "managing-teams-add-sso.md").

You must have the **Space administrator** role to manage teams.

###### To add a user directly

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space. Choose **Settings**, and then choose
   **Teams**.
3. Choose the **Members** tab.
4. Choose **Add member**.

###### Note

Users being added to a team must already be members of a space. You cannot add
or invite a team member who is not a member of the space. 5. Choose a user in the drop-down field, and then choose **Save**.
Choose either AWS Builder ID users or SSO users that are already set up in IAM Identity Center.
