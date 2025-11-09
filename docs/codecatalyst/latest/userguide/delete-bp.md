Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deleting a published custom blueprint or version

When you delete a custom blueprint’s version or the blueprint itself from your Amazon CodeCatalyst space,
all your access is removed to the resources of the blueprint project or blueprint version. When you
have deleted a blueprint version or the blueprint, project members will be unable to access
project resources, and any workflows that are prompted by third-party source repositories will be
stopped.

###### Note

If you delete a blueprint, it doesn’t affect a project that is applied the blueprint. Resources of the
blueprint aren't removed from the project.

If a blueprint version is published to the space’s blueprint catalog, choose a new version for
the catalog before you delete the published version.

###### Important

To delete a published custom blueprint or a custom blueprint's catalog version from your
space, you must be signed in with an account that has the **Space administrator** or
**Power user** role in the space.

**To delete a custom blueprint's catalog version**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to delete a custom blueprint's catalog version.
3. On the space dashboard, choose the **Settings** tab, and then choose
   **Blueprints**.
4. Choose the name of the blueprint with the catalog version that you want to delete.
5. Choose the radio button for the catalog version that you want to delete, and then choose
   **Delete version**.
6. Review the details, and then choose another blueprint version from the **Choose a new
   blueprint catalog version** dropdown menu.
7. Enter `delete` to confirm the deletion of the blueprint catalog version.
8. Choose **Delete**.
   If a blueprint version isn't in the space’s blueprints catalog, you can delete the version
   without choosing a new version.

**To delete a custom blueprint version**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to delete a custom blueprint version.
3. On the space dashboard, choose the **Settings** tab, and then choose
   **Blueprints**.
4. Choose the name of the blueprint with the version that you want to delete.
5. Choose the radio button for the version that you want to delete, and then choose
   **Delete version**.
6. Enter `delete` to confirm the blueprint version deletion.
7. Choose **Delete**.
   Deleting a blueprint from the space's blueprints catalog deletes all versions of the
   blueprint. The space's projects that are using the blueprint aren't affected by the
   deletion.

**To delete a custom blueprint version**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to delete a custom blueprint.
3. On the space dashboard, choose the **Settings** tab, and then choose
   **Blueprints**.
4. On the **Space blueprints** table, choose the radio button for the custom blueprint that you want to delete, and then choose
   **Delete blueprint**.
5. Enter `delete` to confirm the custom blueprint deletion.
6. Choose **Delete**.
