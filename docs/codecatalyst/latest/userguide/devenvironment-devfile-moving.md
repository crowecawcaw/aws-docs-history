Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Editing a repository devfile for a

Dev Environment

Use the following procedure to edit a repository devfile for a Dev Environment.

## Editing a repository devfile for a

Dev Environment in CodeCatalyst

###### To edit the repository devfile

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project that contains the source repository for which you want to
   edit the devfile.
3. In the navigation pane, choose **Code**.
4. Choose **Source Repositories**.
5. Choose the source repository that contains the devfile that you want to edit.
6. From the list of files, choose the `devfile.yaml` file.
7. Choose **Edit**.
8. Edit the devfile.
9. Choose **Commit**, or create a pull request so a team member can
   review and approve the changes.

###### Note

If you edit your devfile, you have to restart the devfile for the changes to take effect. This can be done by running
`/aws/mde/mde start --location devfile.yaml`. If there's a problem starting your devfile, it will enter
recovery mode. However, if you edit a devfile associated to a VPC-connected Dev Environment, you have to restart the Dev Environment
instead for the changes to take effect.

You can review which devfile is being used by running `/aws/mde/mde status`. The location field has
the path of the devfile relative to the environment’s `/projects` folder.

```
{
            "status": "STABLE",
            "location": "devfile.yaml"
        }
```

You can also move the default devfile in `/projects/devfile.yaml` to your source code repository. To update the
location of the devfile, use following command:
`/aws/mde/mde start --location `repository-name`/devfile.yaml`.

## Editing a repository devfile for a

Dev Environment in an IDE

To change the configuration of a Dev Environment, you must edit the devfile. We recommend that
you edit the devfile in a supported IDE and then update your Dev Environment, but you can also
edit the devfile from the root of the source repository in CodeCatalyst. If you edit the devfile in
a supported IDE, you must commit and push your changes to the source repository or create a
pull request so a team member can review and approve the devfile edits.

- [Editing the repository devfile for a Dev Environment in AWS Cloud9](../../../cloud9/latest/user-guide/devenvironment-cloud9.md#ide-toolkits-edit-devfile-cloud9 "../../../cloud9/latest/user-guide/devenvironment-cloud9.md#ide-toolkits-edit-devfile-cloud9")
- [Editing the repository devfile for a Dev Environment in VS Code](../../../toolkit-for-vscode/latest/userguide/codecatalyst-devenvironment.md#codecatalyst-devenvironment-devfile "../../../toolkit-for-vscode/latest/userguide/codecatalyst-devenvironment.md#codecatalyst-devenvironment-devfile")
- [Editing the repository devfile for a Dev Environment in JetBrains](../../../toolkit-for-jetbrains/latest/userguide/codecatalyst-overview.md#codecatalyst-overview-default "../../../toolkit-for-jetbrains/latest/userguide/codecatalyst-overview.md#codecatalyst-overview-default")
