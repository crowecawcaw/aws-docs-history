# Deleting an action version

Use the following instructions to delete a published version of an action. Deleting a
version removes it from the action catalog so that it is no longer available for use in
workflows. Any workflows that currently use the deleted version will stop working.

###### Important

To avoid disruption to those who are currently using your action in their
workflows, only delete an action version if you've reached the version limit, or if the version
contains security vulnerabilities or other critical issues that are impossible to solve with a
new version.

###### To delete an action version

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the CodeCatalyst project page.
3. In the navigation pane, choose **CI/CD**, and then choose
   **Actions**.

Your custom actions appear. 4. Choose the name of the action whose version you want to delete. 5. Choose the radio button next to the version. 6. Choose **Delete**.

###### Note

If there is only one version available, it cannot be deleted.
