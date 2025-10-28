Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing pull requests

You can view pull requests for a project in the Amazon CodeCatalyst console. The project
summary page displays all open pull requests for a project. To view all pull requests
regardless of state, navigate to the pull requests page for your project. When viewing a
pull request, you can choose to have a summary of all comments left on changes to the
pull request created for you.

###### Note

###### Note

**Powered by Amazon Bedrock**: AWS implements [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md").
Because the **Write description for me**, **Create content summary**, **Recommend tasks**, **Use Amazon Q to create or add features to a project**, and **Assign issues to Amazon Q** feature with Amazon Q Developer Agent for software development features are built on Amazon Bedrock, users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of artificial intelligence (AI).

###### To view open pull requests

1. Navigate to the project where you want to view pull requests.
2. On the project page, open pull requests are displayed, including information
   about who created the pull request, what repository contains the branches for
   the pull request, and the date the pull request was created. You can filter the
   open pull request view by source repository.
3. To view all pull requests, choose **View all**. You can use
   the selectors to choose between the options. For example, to view all pull
   requests, choose **Any status** and **Any
   author**.

Alternatively, in the navigation pane, choose **Code**, and
then choose **Pull requests**, and then use the selectors to
refine your view. 4. On the **Pull requests** page, you can sort pull requests by
ID, title, status, and more. To customize what information and how much
information is displayed on the pull requests page, choose the gear icon. 5. To view a specific pull request, choose it from the list. 6. To view the status of workflows runs associated with this pull request, if
any, choose **Overview** and review the information in the
**Pull request details** area of the pull request under
**Workflow runs**.

A workflow run will occur if the workflow is configured with pull request
create or revision events, and if the destination branch requirements in the
workflow match the destination branch specified in the pull request. For more
information, see [Adding triggers to workflows](workflows-add-trigger-add.md "workflows-add-trigger-add.md"). 7. To view linked issues, if any, choose **Overview** and review
the information in the **Pull request details** under
**Issues**. If you want to view a linked issue, choose its
ID from the list. 8. (Optional) To create a summary of comments left on the code changes in
revisions of the pull request, choose **Create content
summary**. The summary will not include any comments left on the
overall pull request.

###### Note

This functionality requires that generative AI features are enabled for the space, is not
available for linked repositories, and is only available in the
US West (Oregon) Region. For more information, see [Managing generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md"). 9. To view the code changes in the pull request, choose
**Changes**. You can quickly view how many files have
changes in the pull request, and what files in the pull request have comments on
them, in **Files changed**. The number of comments shown next
to a folder indicates the number of comments on files in that folder. Expand the
folder to view the number of comments for each file in the folder. You can also
view any comments left on specific lines of code.

###### Note

Not all changes in a pull request can be displayed in the console. For
example, you cannot view Git submodules in the console, so you cannot view
differences in a submodule in a pull request. Some differences might be too
large to display. For more information, see [Quotas for source repositories in CodeCatalyst](source-quotas.md "source-quotas.md") and [Viewing a file](source-files-view.md "source-files-view.md"). 10. To view quality reports for this pull request, choose
**Reports**.

###### Note

A workflow must be configured to generate reports in order for them to
show up in your pull requests. For more information, see [Testing with workflows](test-workflow-actions.md "test-workflow-actions.md").
