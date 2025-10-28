# Delete a package group

You can delete a package group using the CodeArtifact console or the AWS Command Line Interface (AWS CLI).

Note the following behavior when deleting package groups:

- The root package group, `/*`, cannot be deleted.
- The packages and package versions that are associated with that package group
  are not deleted.
- When a package group is deleted, the direct child package groups will become children of the package group's
  direct parent package group. Therefore, if any of the child groups are inheriting any settings from the parent, those settings
  could change.

## Delete a package group (console)

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. In the navigation pane, choose **Domains**, and then choose the domain that contains
   the package group you want to view or edit.
3. Choose **Package groups**.
4. Choose the package group you want to delete and choose **Delete**.
5. Enter delete in the field and choose **Delete**.

## Delete a package group (AWS CLI)

To delete a package group, use the `delete-package-group` command.

```
aws codeartifact delete-package-group \
         --domain `my_domain` \
         --domain-owner `111122223333` \
         --package-group `'/nuget/*'`
```
