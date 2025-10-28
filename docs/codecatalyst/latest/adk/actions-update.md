# Publishing a new action version

After publishing your initial action version, you can update your action definition and
publish a new version to the Amazon CodeCatalyst actions catalog. Unlike publishing an action initially,
you can't change the **Action name** when editing details for later
versions.

Consider following Semantic Versioning (SemVar) standards when working with updated versions
of your actions. SemVar provides a standardized way to assign and increment version numbers for
software packages. When dependencies become complex as your system grows and more packages are
integrated into a software, a clear and precise way to convey meaning about changes can help
other CodeCatalyst users understand the intentions while you make flexible and reliable specifications.
For more information, see [Semantic Versioning
2.0.0](https://semver.org/ "https://semver.org/").

The Conventional Commits specification provides a lightweight convention for structing
commit messages, which gives you the ability create an explicit commit history and write
automateed tools on top of it. This convention fits with SemVar by describing features, fixes,
and beaking changes made in commit messages, including guidelines on how commit messages should
be structured. For more information, see [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/ "https://www.conventionalcommits.org/en/v1.0.0/").

**To publish your new action version**

1. Navigate to your project that was cloned in a local folder, and make your changes in your
   existing `feature-action-name` branch that was created in
   [Step 1: Set up your project and Dev Environment](getting-started.md#set-up-workspace-first-action "getting-started.md#set-up-workspace-first-action").
   You can also create a new feature branch from your default branch and make changes in the new
   branch.
2. Build the package locally and push the source code and bundle:
   1. Run the following npm commands to build your action:

   ```
   npm install
   ```

   ```
   npm run all
   ```

   2. Run the following commands to commit the changes to your remote repository:

   ###### Important

   Make sure the code you're pushing doesn't contain any sensitive information that you
   don't want to be shared publicly.

   ```
   git add .
   ```

   ```
   git commit -m "`commit message`"
   ```

   ```
   git push
   ```

   You can also use the source control options available in the IDE you’re using for your Dev Environment.

3. Create a pull request and merge your feature branch to the default branch, and then
   publish your new action version to the CodeCatalyst actions catalog. For more information, see [Publishing an action](actions-publishing.md "actions-publishing.md").
   Optionally, you can view and test the action version you published to the Amazon CodeCatalyst actions
   catalog to ensure it works as expected.

**(Optional) To view and use your published action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the CodeCatalyst project page.
3. In the navigation pane, choose **CI/CD**, and then choose
   **Workflows**.
4. From the repository and branch dropdown menus, select the repository and feature branch in
   which you want to test the published action.
5. Choose **Create workflow**, confirm the repository and feature branch in
   which you want to test the published action, and then choose
   **Create**.
6. Choose **+ Actions**, and then search for your custom action that you
   published. You can search the name of your action by entering it in the _Search for
   actions_ field.
7. (Optional) Choose the name of the published action to view the action's details, including
   the description, documentation information, YAML preview, and license file.
8. Add the action to the workflow, choose the visual editor, and then choose the action to
   view and configure the **Inputs**, **Configuration**, and
   **Outputs** fields.

###### Note

The published action contains the identifier (for example,
test-space/test-45tzuy@v1.0.0), which is not available for the action when initially created
and not published. 9. (Optional) Choose **Validate** to validate the workflow's YAML code
before committing. 10. Choose **Commit**, and on the **Commit workflow** dialog
box, do the following:

    1. For **Workflow file name**, leave the default name or enter your
     own.
    2. For **Commit message**, leave the default message or enter your
     own.
    3. For **Repository** and **Branch**, choose the source
     repository and branch for the workflow definition file. These fields should be set to the
     repository and branch that you specified earlier in the **Create workflow**
     dialog box. You can change the repository and branch now, if you'd like.


    ###### Note

    After committing your workflow definition file, it cannot be associated with another
     repository or branch, so make sure to choose them carefully.
    4. Choose **Commit** to commit the workflow definition file.

11. View the workflow run status and details. For more information, see [Viewing workflow run status and details](../userguide/workflows-view-run.md "../userguide/workflows-view-run.md").
