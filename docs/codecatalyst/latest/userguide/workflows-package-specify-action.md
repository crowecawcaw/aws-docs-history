Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Specifying CodeCatalyst package

repositories in workflows

In CodeCatalyst, you can add a CodeCatalyst package repository to your build and test actions in
your workflow. Your package repository must be configured with a package format, such as
npm. You can also choose to include a sequence of scopes for your selected package
repository.

Use the following instructions to specify a package configuration to use with a
workflow action.

Visual

###### To specify the package configuration that an action will use (visual

editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose the **Build** or
   **Test** action with which you want to
   configure with a package repository.
8. Choose **Packages**.
9. From the **Add configuration** dropdown menu,
   choose the package configuration you want to use with your workflow
   actions.
10. Choose **Add package repository**.
11. In the **Package repository** dropdown menu,
    specify the name of your CodeCatalyst _package
    repository_ that you want the action to use.

For more information about package repositories, see [Package repositories](packages-concepts.md#packages-concepts-repository "packages-concepts.md#packages-concepts-repository"). 12. (Optional) In **Scopes - optional**, specify a
sequence of _scopes_ that you want to define in
your package registry.

When defining scopes, the specified package repository is
configured as the registry for all listed scopes. If a package with
the scope is requested through the npm client, it will use that
repository instead of the default. Each scope name must be prefixed
with "@".

If `Scopes` is omitted, then the specified package
repository is configured as the default registry for all packages
used by the action.

For more information about scopes, see [Package namespaces](packages-concepts.md#packages-concepts-package-namespaces "packages-concepts.md#packages-concepts-package-namespaces") and
[Scoped packages](https://docs.npmjs.com/cli/v10/using-npm/scope "https://docs.npmjs.com/cli/v10/using-npm/scope"). 13. Choose **Add**. 14. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 15. Choose **Commit**, enter a commit message, and
choose **Commit** again.

YAML

###### To specify the package configuration that an action will use (YAML

editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In a **Build** or **Test**
   action, add code similar to the following:

```
`action-name`:
 Configuration:
    Packages:
        NpmConfiguration:
          PackageRegistries:
            - PackagesRepository: `package-repository`
              Scopes:
                - `"@scope"`
```

For more information, see the description of the
`Packages` property in [Build and test actions YAML](build-action-ref.md "build-action-ref.md")
for your action. 8. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message, and
choose **Commit** again.
