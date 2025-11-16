# Troubleshooting issues for Amazon Q Developer for

GitHub

Consult the following section to troubleshoot common problems when using Amazon Q Developer for
GitHub.

## Amazon Q Developer not generating pull

requests in repositories with branch protection rules

**Problem**: Amazon Q Developer isn't able to create a pull request in my GitHub
repository, which has branch protection rules.

**Solution**: The branch protection rules prevents Amazon Q Developer from
creating a branch to create a pull request. In order to use Amazon Q Developer for GitHub in
repositories with branch protection rules, you need to add the Amazon Q Developer app to your allow
list.

###### To add the Amazon Q Developer app to your allow list

1. If necessary, sign in to your [GitHub](https://github.com/ "https://github.com/") account
   using your GitHub credentials.
2. Navigate to your GitHub organization, and then navigate to the repository you want to
   allow list the Amazon Q Developer for GitHub app.
3. Choose **Settings**, and then choose **Branches**
   from the navigation pane.
4. Under **Branch protection rules**, choose **Edit**
   to modify the branch protection rules.
5. Choose **Restrict pushes that create matching branches**, and
   search for the Amazon Q Developer for GitHub app.
6. Choose **Save changes** to allow Amazon Q Developer to create pull requests
   for issues with Amazon Q Developer labels.

To learn more about modifying branch protection rules in GitHub, see [Creating a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule#creating-a-branch-protection-rule "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule#creating-a-branch-protection-rule").

## Amazon Q Developer labels missing in GitHub

issues

**Problem**: I don't see the **Amazon Q development
agent** or **Amazon Q transform agent** labels in GitHub
issues.

**Solution**: If the labels aren't automatically created when you
installed the Amazon Q Developer for GitHub app, or they were unintentionally delted, you can manually
create them in GitHub. The labels must be named as **Amazon Q development
agent** and **Amazon Q transform agent** in order for them to be
recognized and processed as Amazon Q Developer labels. For more information, see [Creating a label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label "https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label") in the _GitHub documentation_.

## Amazon Q Developer not creating code for GitHub

issues

**Problem**: I created a GitHub issue and invoked Amazon Q Developer to perform a
task, but I got the following series of messages regarding technical difficulties:

1. ⏳ I'm working on generating code for this issue. I'll update this issue with
   a comment and open a pull request when I'm done.
2. ⚠️ I'm having technical difficulties. I couldn't solve the issue. I'm going
   to try again. This might take some time.
3. ⚠️ I'm having technical difficulties. I couldn't solve the issue. I'm going
   to try again. This might take some time.
4. 🔴 I'm having technical difficulties. I couldn't solve the issue.

Consider reassigning this issue to a user. This will help you stay within the quotas
for generative AI feature usage.

**Solution**: If Amazon Q Developer is not able to process your issue and
generate code for it, create a new issue and apply the **Amazon Q development
agent** or the **Amazon Q transform agent** label to the new
issue. To learn more about creating an issue and applying an Amazon Q Developer agent label, see
[Developing features and iterating with Amazon Q Developer
in GitHub](github-feature-development.md "github-feature-development.md") or
[Transforming code with Amazon Q Developer in GitHub](github-code-transformation.md "github-code-transformation.md").
