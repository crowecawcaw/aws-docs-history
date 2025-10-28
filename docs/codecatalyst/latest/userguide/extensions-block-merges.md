Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Blocking third-party merges when workflows fail

After linking a GitHub or Bitbucket repository to CodeCatalyst, you can add CodeCatalyst workflows for pull requests. Similarly, after linking
a GitLab project repository to CodeCatalyst you can add CodeCatalyst workflows for merge requests. One or more workflow runs
can occur on a specific commit, and the run status of each workflow in CodeCatalyst is also reflected as part of the commit status in
GitHub, Bitbucket, or GitLab. When a new commit is pushed, new workflow
[run statuses](workflows-view-run.md#workflows-view-run-status "workflows-view-run.md#workflows-view-run-status")
are reflected in GitHub, Bitbucket, or GitLab for that new commit. If you run a workflow again for a commit, the new workflow run
status overrides the previous status for that commit and workflow.

You can set branch protection rules in GitHub or Bitbucket to block a pull request merge, or in GitLab to block a merge request, when the latest commit has a failed workflow run status.
With branch protection rules, the status of the latest commit affects the ability to merge a pull request in GitHub, Bitbucket, or GitLab. To learn more about workflows, see
[Running a workflow](workflows-working-runs.md "workflows-working-runs.md") and [Starting a workflow run automatically using
triggers](workflows-add-trigger.md "workflows-add-trigger.md").

Depending on which third-party repository provider you're using, see the following:

- **GitHub repositories**: GitHub’s documentation
  [About status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks")
  and [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches").
- **Bitbucket repositories**: Bitbucket’s documentation for
  [Using branch permissions](https://confluence.atlassian.com/bitbucketserver/using-branch-permissions-776639807.html "https://confluence.atlassian.com/bitbucketserver/using-branch-permissions-776639807.html") and
  [Take control with branch permissions in Bitbucket Cloud](https://bitbucket.org/blog/take-control-with-branch-restrictions "https://bitbucket.org/blog/take-control-with-branch-restrictions").
- **GitLab repositories**: GitLab’s documentation for
  [Auto merge](https://docs.gitlab.com/ee/user/project/merge_requests/auto_merge.html "https://docs.gitlab.com/ee/user/project/merge_requests/auto_merge.html") and
  [Protected branches](https://docs.gitlab.com/ee/user/project/protected_branches.html "https://docs.gitlab.com/ee/user/project/protected_branches.html").
