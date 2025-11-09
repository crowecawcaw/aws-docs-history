Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Connecting source repositories to workflows

A _source_, also called an _input source_, is a source
repository to which a [workflow action](workflows-actions.md "workflows-actions.md") connects
in order to obtain the files it needs to carry out its operations. For example, a
workflow action might connect to a source repository to obtain application source files in
order to build an application.

CodeCatalyst workflows support the following sources:

- CodeCatalyst source repositories – For more information, see [Store and collaborate on code with source repositories in CodeCatalyst](source.md "source.md").
- GitHub repositories, Bitbucket repositories, and GitLab project repositories
  – For more information, see [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md").

###### Topics

- [Specifying a workflow file's
  source repository](workflows-sources-specify-workflow-def.md "workflows-sources-specify-workflow-def.md")
- [Specifying a workflow action's source
  repository](workflows-sources-specify-action.md "workflows-sources-specify-action.md")
- [Referencing source repository
  files](workflows-sources-reference-files.md "workflows-sources-reference-files.md")
- ['BranchName' and 'CommitId'
  variables](workflows-sources-variables.md "workflows-sources-variables.md")
