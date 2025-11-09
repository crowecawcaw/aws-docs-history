Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Reviewing a pull request

You can use the Amazon CodeCatalyst console to collaboratively review and comment on the
changes included in a pull request. You can add comments to individual lines of code in
the difference between the source and destination branches, or in the difference between
revisions of the pull request. You can choose to create a summary of comments left on
the code changes in the pull request to help you quickly understand the feedback left by
other users. You can also choose to create a Dev Environment to work on code.

###### Note

###### Note

**Powered by Amazon Bedrock**: AWS implements [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md").
Because the **Write description for me**, **Create content summary**, **Recommend tasks**, **Use Amazon Q to create or add features to a project**, and **Assign issues to Amazon Q** feature with Amazon Q Developer Agent for software development features are built on Amazon Bedrock, users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of artificial intelligence (AI).

###### Tip

You can configure what pull request events you that will receive emails about as
part of your profile. For more information, see [Sending Slack and email notifications from CodeCatalyst](notifications-manage.md "notifications-manage.md").

Pull requests show what the difference will be between the revision of the pull
request and the commit that was the tip of the destination branch when you created the
pull request. This is called the merge base. For more information about differences and
merge bases in Git, see [git-merge-base](https://git-scm.com/docs/git-merge-base "https://git-scm.com/docs/git-merge-base") in the Git documentation.

###### Tip

When working in the console, particularly if you have had a pull request open for
a while, consider refreshing your browser to ensure you have the latest revision
available for a pull request before you start to review it.

###### To review a pull request in the CodeCatalyst console

1. Navigate to your project.
2. Navigate to the pull requests by doing one of the
   following:
   - If the pull request is listed on the project page, choose it from the list.
   - If the pull request is not listed on the project page, choose **View
     all**. Use the filters and sort to find the pull request, and then choose it
     from the list.
   - In the navigation pane, choose **Code**, and then choose **Pull
     requests**.

3. Choose the pull request you want to review from the list. You can filter the list of pull requests by typing
   part of its name in the filter bar.
4. In **Overview**, you can review the name and title of the pull request.
   You can create and view comments left on the pull request itself. You can also view the
   details of the pull request, including information about workflow runs, linked issues,
   reviewers, the author of the pull request, and feasible merge strategies.

###### Note

Comments left on specific lines of code appear in **Changes**. 5. (Optional) To add a comment that applies to the entire pull request, expand
**Comments on pull request**, and then choose **Create
comment**. 6. (Optional) To view a summary of all comments left on changes in revisions of this pull request, choose **Create comment summary**.

###### Note

This functionality requires that generative AI features are enabled for the space
and is only available in the US West (Oregon) Region. For more information, see [Managing
generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md"). 7. In **Changes**, you can see the differences between the destination
branch and the most recent revision of the pull request. If there is more than one revision,
you can change what revisions are compared in the difference between them. For more
information about revisions, see [Revisions](source-concepts.md#revision-concept "source-concepts.md#revision-concept").

###### Tip

You can quickly view how many files have changes in the pull request, and what files in
the pull request have comments on them, in **Files changed**. The number of
comments shown next to a folder indicates the number of comments on files in that folder.
Expand the folder to view the number of comments for each file in the folder. 8. To change the way differences are displayed, choose between **Unified**
and **Split**. 9. To add a comment to a line in the pull request, go to the line you want to comment on.
Choose the comment icon that appears for that line, enter a comment, and then choose
**Save**. 10. To view changes between revisions in a pull request, or between its source and destination
branches, choose from the available options in **Comparing**. Comments on
lines in revisions are preserved in those revisions. 11. If you’ve configured your workflow to generate a code coverage report on pull request triggers, you can view the line
and branch coverage findings in the relevant pull request. To hide code coverage findings,
choose **Hide code coverage**. For more information, see [Code coverage reports](test-workflow-actions.md#test-code-coverage-reports "test-workflow-actions.md#test-code-coverage-reports"). 12. If you want to make code changes to the pull request, you can create a Dev Environment from the pull request.
Choose **Create Dev Environment**.
Optionally add a name for the Dev Environment or edit its configuration and then choose
**Create**. 13. In
**Reports**,
you can view the quality reports in this pull request. If there is
more than one revision, you can change what revisions are compared in the difference between
them. You can filter the reports by name, status, workflow, action, and type.

###### Note

A workflow must be configured to generate reports in order for them to show up in your pull requests.
For more information, see [Configuring quality reports in an action](test-config-action.md "test-config-action.md"). 14. To view a specific report, choose it from the list. For more information, see [Testing with workflows](test-workflow-actions.md "test-workflow-actions.md"). 15. If you are listed as a reviewer of this pull request and want to approve the changes, make
sure that you are viewing the most recent revision, and then choose
**Approve**.

###### Note

All required reviewers must approve a pull request before it can be merged.
