Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Administering Dev Environments for a space

All Dev Environments are created as part of a project within a space. Space
members can create their own Dev Environments within a project at the source repository level.
Space administrators can then use the Amazon CodeCatalyst console to view, edit, delete, and
stop Dev Environments on behalf of space members. In short, space administrators
maintain Dev Environments at the space level.

**Considerations for administering Dev Environments**

- You must have the **Space administrator** role to view the
  **Dev Environments** page under **Settings** and to manage
  Dev Environments at the space level.
- Space members manage the Dev Environments that they create in projects through
  their CodeCatalyst accounts. When administering Dev Environments as a space administrator, you
  are maintaining these resources on behalf of space members.
- Dev Environments default to a specific compute and storage configuration. For information
  about billing and rates for upgrading your configuration, see the [Amazon CodeCatalyst pricing page](https://codecatalyst.aws/explore/pricing "https://codecatalyst.aws/explore/pricing").

###### Important

Dev Environments aren't available for users in spaces where Active Directory is used as the
identity provider. For more information, see [I can't create a Dev Environment
when I'm signed into CodeCatalyst using a single sign-on account](devenvironments-troubleshooting.md#troubleshoot-create-dev-env-idprovider "devenvironments-troubleshooting.md#troubleshoot-create-dev-env-idprovider").

For other considerations about Dev Environments, including stopping running instances, default
compute configuration, upgrading your compute, incurring costs, and configuring timeouts, see
[Write and modify code with Dev Environments in CodeCatalyst](devenvironment.md "devenvironment.md").

###### Topics

- [Viewing Dev Environments for your space](spaces-devenv-view.md "spaces-devenv-view.md")
- [Editing a Dev Environment for your space](spaces-devenv-edit.md "spaces-devenv-edit.md")
- [Stopping a Dev Environment for your space](spaces-devenv-stop.md "spaces-devenv-stop.md")
- [Deleting a Dev Environment for your space](spaces-devenv-delete.md "spaces-devenv-delete.md")
