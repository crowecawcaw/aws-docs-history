

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Granting project roles for a team
<a name="projects-teams-project-roles"></a>

A team can have role permissions, such as **Power user**, in a space. You can change the space role for a team, but note that all members of the team will inherit those permissions.

**To add or change a project role**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your space. Choose **Project settings**, and then choose **Teams**.

1. To change a role, choose the selector next to the team in this list, and then choose **Change role**. To add a role, choose **Add project role**. In **Project**, choose the project you want to add and in **Role**, choose the role. Choose one of the available project roles:
   + **Project administrator** - For details, see [Project administrator role](ipa-role-types.md#ipa-role-project-admin).
   + **Contributor** - For details, see [Contributor role](ipa-role-types.md#ipa-role-contributor).
   + **Reviewer** - For details, see [Reviewer role](ipa-role-types.md#ipa-role-reviewer).
   + **Read only** - For details, see [Read only role](ipa-role-types.md#ipa-role-read-only).

1. Choose **Save**.