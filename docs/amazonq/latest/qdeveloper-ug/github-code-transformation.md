# Transforming code with Amazon Q Developer in GitHub

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

With the code transformation feature, you can update your technology stack, enhance performance, and ensure future
compatibility while preserving the core functionality of your existing code. With Amazon Q Developer, you can avoid technical
debt and build your applications for long-term sustainability and scalability.

When you add the code transformation label to an issue or use the `/q transform` slash command,
Amazon Q Developer transforms your code from Java version 8 or 11 to version 17. Amazon Q Developer then creates a pull request
with the changes and summary of the changes that you can merge into your mainline.

You can have Amazon Q Developer perform a code transformation a limited number of times per month. You can increase your
free usage at any time by registering your Amazon Q Developer app installation with your AWS account. For more information,
see [Increasing usage limits and configuring details in Amazon Q Developer
console](github-register-app-install.md "github-register-app-install.md").

## Prerequisites

Before transforming you codebase with Amazon Q Developer, consider the following requirements:

- Ensure your GitHub repository has GitHub Actions enabled. For more information, see
  [Understanding
  GitHub Actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions "https://docs.github.com/en/actions/about-github-actions/understanding-github-actions") and
  [Enabling
  a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow#enabling-a-workflow "https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow#enabling-a-workflow")in the _GitHub documentation_.
- Create and configure your workflow file in the `.github/workflows/`
  directory to handle code transformation tasks. For more information, see
  [Customizing a workflow for code transformation](github-code-transformation-workflow.md "github-code-transformation-workflow.md").

After meeting the prerequisites, you can apply the **Amazon Q transform agent** label
and upgrade your codebase in your GitHub repository.

###### Important

The Amazon Q Developer app attempts to automatically create the **Amazon Q development agent**
and the **Amazon Q transform agent** labels in GitHub repositories you authorize
access to. If the labels are not automatically created, or if they're unintentionally deleted,
you can manually create them in GitHub. The labels must be named as **Amazon Q development
agent** and **Amazon Q transform agent** in order for them to be
recognized and processed as Amazon Q Developer labels. For more information, see
[Creating
a label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label "https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label") in the _GitHub documentation_.

###### To upgrade your codebase

1. If necessary, sign in to your [GitHub](https://github.com/ "https://github.com/") account using your
   GitHub credentials.
2. Navigate to your GitHub organization, and then navigate to the repository you want to transform
   your codebase.
3. Choose **Issues**, and then create a new issue. For more information, see
   [Create
   an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue "https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue") in the _GitHub documentation_.
4. In the **Add a title** text input field, enter a title that
   provides context to Amazon Q Developer for code transformation (example: "Upgrade codebase"). The issue
   description should also be included as it also provides context.
5. When creating an issue or configuring an existing issue, you can apply the code transformation Amazon Q Developer label
   or use the `/q transform` slash command. Do one of the following:
   - To apply the label to the issue, do one of the following:
     - Choose the **Assign to Amazon Q** dropdown menu provided as a browser extension, and
       then choose the **Amazon Q transform agent** label.
     - In the right side menu, choose **Labels**, and then choose the **Amazon Q
       transform agent** label.

   - To use the `/q transform` slash command in a comment:
     1. Within the issue, navigate to **Add a comment**, and in the comment text input
        field, enter `/q transform`.
     2. Choose **Comment**.

6. Choose **Create issue** to finish creating the issue with the
   necessary details for Amazon Q Developer to transform your code.

When Amazon Q Developer finishes generating code changes for the feature development, it will comment on the
issue and opens a pull request. 7. Navigate to the comment left by Amazon Q Developer (example: "`I finished upgrading your code and 
 opened a pull request: Resolve Upgrade codebase.`"), and then choose the pull request link.

You can also navigate to the **Pull requests** tab, and then choose the pull request
created by Amazon Q Developer. 8. Choose the **Files changed** tab to view the changes. 9. If you're satisfied with the suggested code changes, you can merge the pull request. For more information,
see [Merge
a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request").
Amazon Q Developer leaves a comment that provides a transformation summary with details regarding files that it updated.
You can find the summary in the `build_logs.txt` file provided in the comment. If Amazon Q Developer can't
perform a complete code transformation, it also provides a summary regarding the errors that prevented the complete
transformation.
