Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deleting a source repository

If a source repository for an Amazon CodeCatalyst project is no longer needed, you can delete
it. Deleting a source repository also deletes any project information stored in the
repository. If any workflows depend on the source repository, those workflows will be
deleted from the list of project workflows after the repository is deleted. Issues that
reference the source repository will not be deleted or altered, but any links to the
source repository added to issues will fail once the repository is deleted.

###### Important

Deleting a source repository cannot be undone. After you delete a source
repository, you are no longer able to clone it, pull data from it, or push data to
it. Deleting a source repository does not delete any local copies of that repository
(local repos). To delete a local repo, use your local computer's directory and file
management tools.

###### Note

You cannot delete a linked repository in the CodeCatalyst console. To delete a linked
repository, choose the link in the list of repositories to open that repository in
the service that hosts it, and then delete it. For more information, see the
documentation for the service that hosts the linked repository.

To remove a linked repository from a project, see [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-unlink.md "extensions-unlink.md").

###### To delete a source repository

1. Navigate to the project that contains the source repository you want to delete.
2. On
   the summary page for your project, choose the repository you want from the list, and then choose
   **View repository**. Alternatively, in the navigation pane,
   choose **Code**, and then choose **Source
   repositories**.
   Choose the name of the repository from the list of source repositories for the project.
3. On the home page for the repository, choose
   **More**, choose **Manage settings**,
   and then choose **Delete repository**.
4. Review the branch, pull request, and related workflow information to help ensure that you
   are not deleting a repository that is still in use or has unfinished work. If you want to
   continue, type **delete**, and then choose **Delete**.
