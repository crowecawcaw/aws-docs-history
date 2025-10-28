# Publishing an action

In CodeCatalyst, you can publish multiple versions of an action, retrieve action metadata, and
manage your actions. You can publish the actions in your local catalog to the CodeCatalyst actions
catalog so that other CodeCatalyst users can use them.

###### Important

Currently, only verified partners can publish actions to the CodeCatalyst actions catalog.

###### Important

When your action is published to the CodeCatalyst actions catalog, it is available to all CodeCatalyst
users, so make sure that you want the action to be publicly available. Other users don't have to
be in your space or project to view your published action. The action's source code, including
the workflow YAML file and git history, become visible after the action is published.

###### Important

If the size of the bundle (`dist/index.js`) is more than 10 megabyte (MB),
you will not be able to publish the action to the CodeCatalyst actions catalog. The bundle grows to 10 MB or more when
an action has many large dependencies.

The action can only published from the default branch of the source repository. If you
developed the action on a feature branch, merge your feature branch with the action to the
default branch.

**To merge your feature branch to the default branch**

Create a pull request for other members to review and merge the changes from the feature
branch to the default branch. For more information, see [Working with pull
requests in Amazon CodeCatalyst](../userguide/source-pull-requests.md "../userguide/source-pull-requests.md").

After merging the feature branch with the action information to the default branch, the
action details can be configured before publishing the action to the CodeCatalyst actions catalog. The
following details can be edited:

- **Action display name** – The name that appears in the
  **Actions** list and the Amazon CodeCatalyst catalog (after the action is published).
  This is initially set in the action definition file `action.yml`.
- **Action name** – The name is derived from the space name and
  action version to form the action identifier (for example, test-space/nad-test-45tzuy@v1.0.0).
  In your workflow, the action identifier is used to specify the action. After publishing the
  action, this name can't be changed.
- **Description** – The description that appears for the action in
  the **Actions** list and the Amazon CodeCatalyst catalog (after the action is
  published).
- **Categories** – The catgories that best describe the action.
  These categories appear when you or other CodeCatalyst users choose the action's name from CodeCatalyst
  catalog while working with workflows. This category is initially empty, and at least one
  category is required before you can publish an action.
- **Support contact** – The email other CodeCatalyst users can reach out
  to regarding the action you published. This detail is initially empty and not required to
  publish your action.
- **License** – A plain text file that supplies required license
  information. This file is created when the action is bootstrapped and is stored at the root of
  action's source repository.
  **To edit action details**

1.  Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2.  Navigate to the CodeCatalyst project page
3.  In the navigation pane, choose **CI/CD**, choose
    **Actions**, and then choose the action you want to publish.
4.  Choose **Edit details** to edit the details for your action:
    1. (Optional) In the **Action display name** field, change the action
       display
       name.
    2. (Optional) In the **Action name** field, change the action
       name.

    ###### Note

    The **Action name** can't be changed after the action is
    published. 3. (Optional) In the **Description** field, change the description. 4. From the **Categories** dropdown list, choose the type of actions that
    are part of your workflow. This field is initially empty and requires at least one category
    before you can publish the action. 5. (Optional) In the **Support contact** field, enter an email. 6. Choose **Save**

5.  (Optional) Edit the license file.

        1. Choose **View license file** to open the file.
        2. Choose **Edit** and make your changes.
        3. Choose **Commit**, add a message in the **Commit
         message** field, and then choose **Commit**.

    After configuring the action details to meet all the requirements to publish, you can choose
    the action version you want to publish to the Amazon CodeCatalyst actions catalog.

**To publish your custom action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the CodeCatalyst project page.
3. In the navigation pane, choose **CI/CD**, choose
   **Actions**, and then choose the action you want to publish.
4. Choose **Publish version** to view the publish version details.
5. Choose the **Commit** dropdown list, and then choose the commit from the
   default branch you want to publish.

###### Note

The commit must meet publishing requirements, including a valid action definition, a
readme file, a license file, and entry files.

The **Code quality** section displays the code quality of your results.
Not meeting the quality results doesn't block you from publishing the action version. The
**Test details** section provides testing and code coverage results. You can
add and run unit tests to meet your requirements for the action. For more information, see
[Testing an action](testing-action.md "testing-action.md"). 6. Choose **Publish** to publish the action to the Amazon CodeCatalyst actions
catalog. In the **Versions** table, the status of the version displays
**Published** once the action version has been successfully published.
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
   view the **Inputs**, **Configuration**, and
   **Outputs** fields.

###### Note

The action now contains the identifier (for example, test-space/test-45tzuy@v1.0.0),
which is not available for the action when initially created before publishing. 9. Choose **Commit**, and on the **Commit workflow** dialog
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

10. View the workflow run status and details. For more information, see [Viewing workflow run status and details](../userguide/workflows-view-run.md "../userguide/workflows-view-run.md").
