# Developing features and iterating with Amazon Q Developer

in GitHub

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

You can use Amazon Q Developer in GitHub to streamline development by automatically implementing new
features and bug fixes, taking tasks from idea to a completed pull request. When you add the
feature development label to an issue or use the `/q dev` slash command, Amazon Q Developer
uses the issue, including its title and description, as well as repository code as context to
generate new code fixes and create a pull request. On the pull request, you can provide
feedback and Amazon Q Developer iterates on the suggested code.

You can have Amazon Q Developer perform feature development a limited number of times per month.
You can increase your free usage at any time by registering your Amazon Q Developer app installation
with your AWS account. For more information, see [Increasing usage limits and configuring details
in Amazon Q Developer console](github-register-app-install.md "github-register-app-install.md").

###### Important

The Amazon Q Developer app attempts to automatically create the **Amazon Q development
agent** label in GitHub
repositories you authorize access to. If the label is not automatically created, or if
it's unintentionally deleted, you can manually create it in GitHub. The label must be
named as **Amazon Q development agent** in order for it to be recognized and processed as a Amazon Q Developer label.
For more information, see [Creating a label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label "https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label") in the _GitHub documentation_.

###### To use Amazon Q Developer for feature development

1. If necessary, sign in to your [GitHub](https://github.com/ "https://github.com/") account
   using your GitHub credentials.
2. Navigate to your GitHub organization, and then navigate to the repository you want to
   implement new features with Amazon Q Developer.
3. Choose **Issues**, and then create a new issue or choose an existing
   issue. For more information, see [Create an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue "https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue") in the _GitHub documentation_.
   1. For a new issue, in the **Add a title** text input field, enter a
      title that provides context to Amazon Q Developer for the feature development (example:
      "Create an image recognition app"). The issue description should also be included as
      it also provides context.

   For an existing issue, you can edit the issue title and description to provide
   context to Amazon Q Developer for the feature development. For more informaiton, see [Editing an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue "https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue") in the _GitHub documentation_.

4. When creating an issue or configuring an existing issue, you can apply the feature
   development Amazon Q Developer label or use the `/q dev` slash command. Do one of the
   following:
   - To apply the label to the issue, do one of the following:
     - Choose the **Assign to Amazon Q** dropdown menu provided as a
       browser extension, and then choose the **Amazon Q development
       agent** label.
     - In the right side menu, choose **Labels**, and then choose
       the **Amazon Q development agent** label.

   - To use the `/q dev` slash command in a comment:
     1. Within the issue, navigate to **Add a comment**, and in the
        comment text input field, enter `/q dev`.
     2. Choose **Comment**.

5. For a new issue, choose **Create issue** to finish creating the issue
   with the necessary details for Amazon Q Developer to develop features. If you configure an
   existing issue, ensure you save the changes. For more informaiton, see [Editing an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue "https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue") in the _GitHub documentation_.

When Amazon Q Developer finishes generating code changes for the feature development, it
comments on the issue and opens a pull request. 6. Navigate to the comment left by Amazon Q Developer (example: "`I finished the
 proposed code changes, and the pull request is ready for review: [PR link]`"), and then choose the pull request link.

You can also navigate to the **Pull requests** tab, and then choose
the pull request created by Amazon Q Developer. 7. Choose the **Files changed** tab to view the code changes. 8. If you're satisfied with the suggested code changes, you can merge the pull request.
For more information, see [Merge a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request").
You can also review the pull request for the feature development and iterate on the
suggested code changes by providing feedback to Amazon Q Developer.

###### To iterate on Amazon Q Developer feature development code

1. Choose the pull request
   created by Amazon Q Developer, and then choose the **Files changed** tab to view
   the code changes.
2. Optionally, for specific lines of code you want to provide feedback on, choose
   **+** to add a comment with feedback.

In the conversation, you can use the `/q` command followed by your
instructions in natural language (for example, `/q implement my suggestions`
or `/q refactor this function for better performance`). Amazon Q Developer will
respond with a comment describing the changes it will make based on your feedback (for
example, "I will implement the following changes based on the feedback: ..."). When the
implementation is complete, Amazon Q Developer will post another comment confirming the changes
(for example, "I have implemented the suggested changes.") along with a link to the
generated commit where you can view the changes. 3. Review the changes made by Amazon Q Developer by following the commit link provided in the
conversation. You can continue to provide additional feedback using the `/q`
command for further iterations as needed. 4. If you're satisfied with the updated code changes, you can merge the pull request or
iterate on the code again with new feedback. For more information, see [Merge a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request").
