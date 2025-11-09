Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding Dev Environments components to a blueprint

Managed development environments (MDE) are used to create and stand up MDE Workspaces in
CodeCatalyst. The component generates a `devfile.yaml` file. For more information,
see [Introduction to Devfile](https://redhat-developer.github.io/devfile/ "https://redhat-developer.github.io/devfile/")
and [Editing a repository devfile for a
Dev Environment](devenvironment-devfile-moving.md "devenvironment-devfile-moving.md").

```
new Workspace(this, repository, SampleWorkspaces.default);
```

**To import Amazon CodeCatalyst blueprints workspaces components**

In your `blueprint.ts` file, add the following:

```
import {...} from '@amazon-codecatalyst/codecatalyst-workspaces'
```
