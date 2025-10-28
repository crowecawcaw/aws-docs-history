Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

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
