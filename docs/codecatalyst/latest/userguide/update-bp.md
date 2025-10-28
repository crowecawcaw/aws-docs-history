Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Changing blueprint versions in a project

If you created a project with a blueprint or added a blueprint to an existing project, then you're
notified of new versions of the blueprint. Before the blueprint version
is updated through an approved pull request, you can view the code changes and affected
environments. Lifecycle management allows you to change versions of one or more applied blueprints in your
project, so each blueprint version can be changed without impacting other areas of your project. You can also
override blueprint updates. For more information, see
[Working with lifecycle management as a blueprint user](lifecycle-management-user.md "lifecycle-management-user.md").

###### Important

To change the version of a blueprint in your CodeCatalyst project, you must be signed in with
an account that has the **Space administrator**, **Power user**, or
**Project administrator** role in the space.

###### Tip

After adding a blueprint to your project, you can configure your email and Slack notifications
to provide updates for the latest changes to the blueprint. For more information, see
[Sending notifications from CodeCatalyst](notifications.md "notifications.md").

**To update a blueprint to the latest version**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to update a blueprint's version.
3. On the space dashboard, choose the project with the blueprint that you want to
   update.
4. In the navigation pane, choose **Blueprints**.
5. In the **Status** column, choose the link to change the catalog version (for example,
   **Change catalog version 0.3.109)**.
6. Choose the **Actions** dropdown menu, and then choose **Update
   version**. The latest version is automatically selected.
7. (Optional) Under **Configure blueprint**, configure the blueprint parameters.
8. (Optional) In the **Code changes** tab, review the differences between the
   current blueprint version and the updated version. The difference displayed in a pull request is
   the changes between the current version and the latest version, which is the desired version at
   the time the pull request is created. If no changes display, the versions might be identical, or
   you might have chosen the same version for both the current version and the desired version.
9. When you’re satisfied that the pull request contains the code and changes that you want
   reviewed, choose **Apply update**. After you create the pull request,
   you can add comments. Comments can be added to the pull request or to individual lines in files
   and to the overall pull request. You can add links to resources such as files by using the
   `@` sign, followed by the name of the file.

###### Note

The blueprint won’t update until the pull request is approved and merged. For more information, see
[Reviewing a pull request](pull-requests-review.md "pull-requests-review.md") and
[Merging a pull request](pull-requests-merge.md "pull-requests-merge.md").

###### Note

If you have existing pull requests open for updating a blueprint version, close the previous pull
requests before creating a new one. When you choose **Update version**, you
will be directed to the list of pending pull requests for the blueprint. You can also view
pending pull requests from the **Blueprints** tab in the project
**Settings** and the project summary page. For more information, see [Viewing pull requests](pull-requests-view.md "pull-requests-view.md").
**To change a blueprint version**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to update a blueprint's version.
3. On the space dashboard, choose the project with the blueprint that you want to
   update.
4. In the navigation pane, choose **Blueprints**, and then choose the radio button for the
   blueprint you want to update.
5. Choose the **Actions** dropdown menu, and then choose **Configure
   blueprint**.
6. From the **Target version** dropdown menu, choose the version that you
   want to use. The latest version is automatically selected.
7. (Optional) Under **Configure blueprint**, configure the blueprint parameters.
8. (Optional) In the **Code changes** tab, review the differences between the
   current blueprint version and the updated version. The difference displayed in a pull request is
   the changes between the current version and the latest version, which is the desired version at
   the time the pull request is created. If no changes display, the versions might be identical, or
   you might have chosen the same version for both the current version and the desired version.
9. When you’re satisfied that the pull request contains the code and changes that you want
   reviewed, choose **Apply update**. After you create the pull request,
   you can add comments. Comments can be added to the pull request or to individual lines in files
   and to the overall pull request. You can add links to resources such as files by using the
   `@` sign, followed by the name of the file.

###### Note

The blueprint won’t update until the pull request is approved and merged. For more information, see
[Reviewing a pull request](pull-requests-review.md "pull-requests-review.md") and
[Merging a pull request](pull-requests-merge.md "pull-requests-merge.md").

###### Note

If you have existing pull requests open for updating a blueprint version, close the previous pull
requests before creating a new one. When you choose **Update version**, you
will be directed to the list of pending pull requests for the blueprint. You can also view
pending pull requests from the **Blueprints** tab in the project
**Settings** and the project summary page. For more information, see [Viewing pull requests](pull-requests-view.md "pull-requests-view.md").
