Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Specifying the action version to use

By default, when you add an action to a workflow, Amazon CodeCatalyst adds the full version to
the workflow definition file using the format:

`v`major`.`minor`.`patch``

For example:

```
My-Build-Action:
  Identifier: aws/build@v1.0.0
```

You can shorten the full version in the `Identifier` property so that the
workflow always uses the latest minor or patch version of the action.

For example, if you specify:

```
My-CloudFormation-Action:
  Identifier: aws/cfn-deploy@v1.0
```

...and the latest patch version is `1.0.4`, then the action will use
`1.0.4`. If a later version is released, say `1.0.5`, then the
action will use `1.0.5`. If a minor version is released, say
`1.1.0`, then the action will continue to use `1.0.5`.

For detailed instructions on specifying versions, see one of the following
topics.

Use the following instructions to indicate which version of an action you want your
workflow to use. You can specify the latest major or minor version, or a specific patch
version.

We recommend using the latest minor or patch version of an action.

Visual

_Not available. Choose YAML to view the YAML
instructions._

YAML

###### To configure a workflow to use the latest version of an action, or a

specific patch version

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. Find the action whose version you want to edit.
8. Find the action's `Identifier` property, and set the
   version to one of the following:
   - action-identifier@v`major`
     – Use this syntax to have the workflow use a specific
     major version, and allow the latest minor and patch versions
     to be chosen automatically.
   - action-identifier@v`major`.`minor`
     – Use this syntax to have the workflow use a specific
     minor version, and allow the latest patch version to be
     chosen automatically.
   - action-identifier@v`major`.`minor`.`patch`
     – Use this syntax to have the workflow use a specific
     patch version.

###### Note

If you're not sure which versions are available, see [Listing the available action
versions](workflows-action-versions-determine.md "workflows-action-versions-determine.md").

###### Note

You cannot omit the major version. 9. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 10. Choose **Commit**, enter a commit message, and
choose **Commit** again.
