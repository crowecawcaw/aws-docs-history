# Developing features and iterating with Amazon Q Developer in GitHub

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

You can use Amazon Q Developer in GitHub to streamline development by automatically implementing new features
and bug fixes, taking tasks from idea to a completed pull request. When you add the feature
development label to an issue or use the `/q dev` slash command, Amazon Q Developer uses the issue,
including its title and description, as well as repository code as context to generate new code fixes
and create a pull request. On the pull request, you can provide feedback and Amazon Q Developer iterates on the
suggested code.

You can have Amazon Q Developer perform feature development a limited number of times per month. You can increase
your free usage at any time by registering your Amazon Q Developer app installation with your AWS account.
For more information, see [Increasing usage limits and configuring details in Amazon Q Developer
console](github-register-app-install.md "github-register-app-install.md").

###### Important

The Amazon Q Developer app attempts to automatically create the **Amazon Q development agent**
and the **Amazon Q transform agent** labels in GitHub repositories you authorize
access to. If the labels are not automatically created, or if they're unintentionally deleted,
you can manually create them in GitHub. The labels must be named as **Amazon Q development
agent** and **Amazon Q transform agent** in order for them to be
recognized and processed as Amazon Q Developer labels. For more information, see
[Creating
a label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label "https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label") in the _GitHub documentation_.

###### To use Amazon Q Developer for feature development

1. If necessary, sign in to your [GitHub](https://github.com/ "https://github.com/") account
   using your GitHub credentials.
2. Navigate to your GitHub organization, and then navigate to the repository you want to implement
   new features with Amazon Q Developer.
3. Choose **Issues**, and then create a new issue or choose an existing issue. For more
   information, see [Create
   an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue "https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue") in the _GitHub documentation_.
   1. For a new issue, in the **Add a title** text input field, enter a title that
      provides context to Amazon Q Developer for the feature development (example: "Create an image recognition
      app"). The issue description should also be included as it also provides context.

   For an existing issue, you can edit the issue title and description to provide context to
   Amazon Q Developer for the feature development. For more informaiton, see
   [Editing
   an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue "https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue") in the _GitHub documentation_.

4. When creating an issue or configuring an existing issue, you can apply the feature development Amazon Q Developer label
   or use the `/q dev` slash command. Do one of the following:
   - To apply the label to the issue, do one of the following:
     - Choose the **Assign to Amazon Q** dropdown menu provided as a browser extension, and
       then choose the **Amazon Q development agent** label.
     - In the right side menu, choose **Labels**, and then choose the **Amazon Q
       development agent** label.

   - To use the `/q dev` slash command in a comment:
     1. Within the issue, navigate to **Add a comment**, and in the comment text input
        field, enter `/q dev`.
     2. Choose **Comment**.

5. For a new issue, choose **Create issue** to finish creating the issue with the
   necessary details for Amazon Q Developer to develop features. If you configure an existing issue, ensure you
   save the changes. For more informaiton, see
   [Editing
   an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue "https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue") in the _GitHub documentation_.

When Amazon Q Developer finishes generating code changes for the feature development, it comments on the
issue and opens a pull request. 6. Navigate to the comment left by Amazon Q Developer (example: "`I finished generating the 
 proposed code changes and opened a pull request: Resolve Create an image recognition app`"),
and then choose the pull request link.

You can also navigate to the **Pull requests** tab, and then choose the pull request
created by Amazon Q Developer. 7. Choose the **Files changed** tab to view the code changes. 8. If you're satisfied with the suggested code changes, you can merge the pull request. For more information,
see [Merge
a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request").
You can also review the pull request for the feature development and iterate on the suggested code changes by
providing feedback to Amazon Q Developer.

###### To iterate on Amazon Q Developer feature development code

1. Choose the pull request created by Amazon Q Developer, and then
   choose the **Files changed** tab to view the code changes.
2. For the line of code you want to leave feedback for and have Amazon Q Developer iterate, choose **+**
   to add a comment with feedback, and then choose **Start a review**.

After you submit the review, Amazon Q Developer begins reviewing the code based on your feedback. When
Amazon Q Developer is done revising your feedback, it commits the changes to the pull request and updates
you with a comment. 3. Choose **Finish your review**, choose the **Request changes** radio button,
and then choose **Submit review** to have your feedback reviewed. 4. If you're satisfied with the updated code changes, you can merge the pull request or iterate on the code again
with new feedback. For more information, see
[Merge
a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request").
Amazon Q Developer integrates with GitHub Actions workflows to create an intelligent feedback loop system. When a pull
request is created, configured workflows, such as unit tests, automatically execute. If the workflow fails,
Amazon Q Developer analyzes the output, and based on the results and failure information, it iterates on the code changes.
As code changes are pushed and workflows execute, Amazon Q Developer interprets the results and uses this information to refine
its approach. That creates a continuous learning loop where each iteration builds upon previous attempts and Amazon Q Developer is
able to evolve its solutions.

The effectiveness of a feedback loop is dependent on having well-defined tests and workflows that provide meaningful
feedback to Amazon Q Developer to interpret and act upon. You can configure workflows using GitHub Actions YAML files in your
repository, allowing for customized testing and validation processes that Amazon Q Developer can respond to. For more information,
see [Understanding GitHub
Actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions "https://docs.github.com/en/actions/about-github-actions/understanding-github-actions")in the _GitHub documentation_.
