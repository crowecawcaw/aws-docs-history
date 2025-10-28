Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Setting publishing permissions for a custom blueprint

By default, a custom blueprint's permission is enabled if a workflow release was generated during project creation.
When publishing permissions are enabled, the blueprint can be published to the space. You can disable the permission so
that the blueprint can't be published. When the permission is disabled, the release workflow that is generated during
blueprint creation doesn't run. New changes to a blueprint can't be published unless the blueprint's permissions are
enabled.

###### Important

To enable or disable a custom blueprint project’s publishing permissions, you must be signed in with
an account that has the **Space administrator** or **Power user**
role in the space.

**To set a blueprint project's publishing permissions**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to manage a custom blueprint's publishing
   permissions.
3. On the space dashboard, choose the **Settings** tab, and then choose
   **Blueprints**.
4. Choose the **Project publishing permissions** tab to view the publishing permissions for all your
   space's blueprints.
5. Choose the blueprint that you want to manage, and then choose **Enable** or
   **Disable** to change the publishing permissions. If you're enabling the permissions, review the permission
   change details, and then choose **Enable blueprint publishing** to confirm the change.
