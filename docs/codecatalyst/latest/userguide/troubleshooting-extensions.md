Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting problems with extensions

Consult the following sections to troubleshoot problems related to extensions in CodeCatalyst.
For more information about extensions, see [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md").

###### Topics

- [I can't see the changes to a linked third-party
  repositories or search for results of those changes](#troubleshooting-detect-3p-changes "#troubleshooting-detect-3p-changes")

## I can't see the changes to a linked third-party

repositories or search for results of those changes

**Problem:** The changes in my third-party reposiory aren't showing
up in CodeCatalyst.

**Possible fixes:** CodeCatalyst currently doesn't support detecting changes
in the default branch for linked repositories. To change the default branch for a linked repository, you
must first unlink it from CodeCatalyst, change the default branch, and then link it again. For more information,
see [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories,
and Jira projects in CodeCatalyst](extensions-link.md "extensions-link.md").
