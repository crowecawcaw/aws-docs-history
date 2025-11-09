Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating a pull request

Creating pull requests helps other users see and review your code changes before you
merge them into another branch. First, you create a branch for your code changes. This
is referred to as the source branch for a pull request. After you commit and push
changes to the repository, you can create a pull request that compares the contents of
the source branch to the contents of the destination branch.

You can create a pull request in the Amazon CodeCatalyst console from a specific branch, from
the pull requests page, or from the project overview. Creating a pull request from a
specific branch automatically provides the repository name and source branch on the pull
request creation page. When you create a pull request, you will automatically receive
emails about any updates to the pull request, as well as when the pull request is merged
or closed.

###### Note

While you are creating a pull request, the difference displayed is the difference
between the tip of the source branch and the tip of the destination branch. Once the
pull request has been created, the displayed difference will be between the revision
of the pull request you choose and the commit that was the tip of the destination
branch when you created the pull request. For more information about differences and
merge bases in Git, see [git-merge-base](https://git-scm.com/docs/git-merge-base "https://git-scm.com/docs/git-merge-base") in the Git documentation.

You can use the **Write description for me** feature when creating
pull requests to have Amazon Q automatically create a description of the changes
contained in a pull request. When you choose this option, Amazon Q analyzes the
differences between the source branch that contains the code changes and the destination
branch where you want to merge these changes. It then creates a summary of what those
changes are, as well as its best interpretation of the intent and effect of those
changes. This feature is only available in the US West (Oregon) Region for CodeCatalyst pull
requests. The **Write description for me** feature is not available for
pull requests in linked repositories.

###### Note

###### Note

**Powered by Amazon Bedrock**: AWS implements [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md").
Because the **Write description for me**, **Create content summary**, **Recommend tasks**, **Use Amazon Q to create or add features to a project**, and **Assign issues to Amazon Q** feature with Amazon Q Developer Agent for software development features are built on Amazon Bedrock, users can take full advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the responsible use of artificial intelligence (AI).

###### To create a pull request

1. Navigate to your project.
2. Do one of the following:
   - In the navigation pane, choose **Code**, choose **Pull
     requests**, and then choose **Create pull request**.
   - On the repository home page, choose **More**, and then choose
     **Create pull request**.
   - On the project page, choose **Create pull request**.

3. In **Source repository**, make sure that the specified source repository
   is the one that contains the committed code. This option only appears if you did not create
   the pull request from the repository's main page.
4. In **Destination branch**, choose the branch to merge the code into after
   it is reviewed.
5. In **Source branch**, choose the branch that contains the committed code.
6. In **Pull request title**, enter a title that helps other users
   understand what needs to be reviewed and why.
7. (Optional) In **Pull request description**, provide information such as a
   link to issues or a description of your changes.

###### Tip

You can choose **Write description for me** to have CodeCatalyst automatically
generate a description of the changes contained in the pull request. You can make changes to the
automatically generated description after you add it to the pull request.

This functionality requires that generative AI features are enabled for the space
and is not available for pull requests in linked repositories. For more information, see
[Managing
generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md"). 8. (Optional) In **Issues**, choose **Link issues**, and
then either choose an issue from the list or enter its ID. To unlink an issue, choose the
unlink icon. 9. (Optional) In **Required reviewers**, choose **Add required
reviewers**. Choose from the list of project members to add them. Required
reviewers must approve the changes before the pull request can be merged into the destination
branch.

###### Note

You cannot add a reviewer as both a required reviewer and an optional reviewer. You
cannot add yourself as a reviewer. 10. (Optional) In **Optional reviewers**, choose **Add optional
reviewers**. Choose from the list of project members to add them. Optional
reviewers do not have to approve the changes as a requirement before the pull request can be
merged into the destination branch. 11. Review the differences between the branches. The difference displayed in a pull request is
the changes between the revision in the source branch and the merge base, which is the head
commit of the destination branch at the time the pull request was created. If no changes display, the branches might be
identical, or you might have chosen the same branch for both the source and the destination. 12. When you are satisfied that the pull request contains the code and changes you want
reviewed, choose **Create**.

###### Note

After you create the pull request, you can add comments. Comments can be added to the
pull request or to individual lines in files as well as to the overall pull request. You can
add links to resources, such as files, by using the @ sign followed by the name of the
file.

###### To create a pull request from a

branch

1. Navigate to the project where you want to create a pull request.
2. In the navigation pane, choose **Source repositories**, and
   then choose the repository that contains the branch where you have code changes
   to review.
3. Choose the drop-down arrow next to the default branch name, and then choose
   the branch you want from the list. To view all the branches for a repository,
   choose **View all**.
4. Choose **More**, and then choose **Create pull
   request**.
5. The repository and the source branch are preselected for you. In
   **Destination branch**, choose the branch where you will
   merge the code once it has been reviewed. In **Pull request
   title**, enter a title that will help other project users
   understand what must be reviewed and why. Optionally, provide more information
   in **Pull request description**, such as pasting in a link to
   related issues in CodeCatalyst, or adding a description of the changes you
   made.

###### Note

Workflows that are configured to run for pull request create events will
run after the pull request is created, if the destination branch for the
pull request matches one of the branches specified in the workflow. 6. Review the differences between the branches. If no changes are displayed, the
branches might be identical, or you might have chosen the same branch for both
the source and the destination. 7. (Optional) In **Issues**, choose **Link
issues**, and then either choose an issue from the list or enter
its ID. To unlink an issue, choose the unlink
icon. 8. (Optional) In **Required reviewers**, choose **Add
required reviewers**. Choose from the list of project members to
add them. Required reviewers must approve the changes before the pull request
can be merged into the destination branch.

###### Note

You can't add a reviewer as both required and optional. You can't add
yourself as a reviewer. 9. (Optional) In **Optional reviewers**, choose **Add
optional reviewers**. Choose from the list of project members to
add them. Optional reviewers do not have to approve the changes before the pull
request can be merged into the destination branch. 10. When you are satisfied that the pull request contains the changes that you
want reviewed and includes the required reviewers, choose
**Create**.
If you have any workflows configured to run where the branch matches the destination
branch in the pull request, you will see information about those workflow runs in
**Overview** in the **Pull request details** area
after the pull request is created. For more information, see [Adding triggers to workflows](workflows-add-trigger-add.md "workflows-add-trigger-add.md").
