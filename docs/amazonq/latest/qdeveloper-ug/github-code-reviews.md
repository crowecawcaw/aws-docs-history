# Reviewing code with Amazon Q Developer in GitHub

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

Amazon Q Developer enables automated code reviews within GitHub. When you create a new pull request
or reopen a closed pull request, Amazon Q Developer automatically performs a code review and provides
feedback on code quality, potential issues, and high-severity findings. Each review includes a
code review summary with threaded findings. Amazon Q Developer also generates fixes for the identified
issues, which you can review and choose to commit to the pull request. You can use the
`/q` command in pull request comments to ask questions and interact regarding the
code review findings. Automatic code reviews are not triggered by subsequent commits made
within an existing pull request.

You can also initiate code reviews within pull requests with the `/q review`
slash command. The slash command can be added to a new pull request comment, which initiates a
new code review of the pull request in its current state, including any comments and new
commits. For more information, see [Initiating code reviews within GitHub pull
requests](#github-code-reviews-in-pr "#github-code-reviews-in-pr").

You can have Amazon Q Developer perform a code review for a limited amount of lines per month. You
can increase your free usage at any time by registering your Amazon Q Developer app installation with
your AWS account. For more information, see [Increasing usage limits and configuring details
in Amazon Q Developer console](github-register-app-install.md "github-register-app-install.md").

###### Note

If the code review capability was previously disabled, it must be enabled in the [Amazon Q Developer
console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github "https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github") before you can apply the label in GitHub. For more information, see [Editing features for Amazon Q Developer in GitHub](github-configuration.md#github-edit-features "github-configuration.md#github-edit-features").

## Prerequisites

Before you can initiate code reviews with Amazon Q Developer, you need the appropriate
permissions for the target GitHub repository. The supported repository roles are Write,
Maintain, or Admin. Users with Read or Triage roles, as well as members without a role,
cannot initiate code reviews with Amazon Q Developer.

GitHub users with the Triage role can still review pull requests in a repository. Any
user, regardless of role, can review pull requests in public repositories.

For more information, see [Repository roles for organizations](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#repository-roles-for-organizations "https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#repository-roles-for-organizations") and [About pre-defined organization roles](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-pre-defined-organization-roles "https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#about-pre-defined-organization-roles") in the _GitHub
documentation_.

## Initiating code reviews for GitHub pull

requests

When you open a new pull request or reopen a previously closed one, Amazon Q Developer
automatically runs a code review and delivers feedback on code quality, possible problems,
and critical findings.

###### To use Amazon Q Developer for code reviews and apply fixes

Before you start a review, you can customize a code quality review by defining custom
coding standards in simple Markdown files in the `project-root/.amazonq/rules`
directory. Amazon Q automatically follows your guidelines, ensuring consistent code quality
across your entire project. For more information, see [Creating project rules for Amazon Q Developer in third-party
platforms](third-party-context-project-rules.md "third-party-context-project-rules.md").

1. If necessary, sign in to your [GitHub](https://github.com/ "https://github.com/") account
   using your GitHub credentials.
2. Navigate to your GitHub organization, and then navigate to the repository you want to
   perform a code review with Amazon Q Developer.
3. Create a new a pull request for changes made to your source code. For more
   information, see [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request") in the _GitHub
   documentation_.

When you create a new pull request, Amazon Q Developer automatically begins a code review to
find potential issues. Once Amazon Q Developer completes the review, it provides a code review
summary. Each finding appears as a threaded comment under the summary, along with
suggested fixes that you can commit to the pull request. 4. Ask the agent to implement changes and create commits directly on your pull
request's source branch. You can do this by posting a comment starting with
`/q` and followed by your request in natural language for the agent to make
changes. 5. (Optional) Ask questions about specific findings. Within the pull request, navigate
to **Add a comment**, and in the comment text input field, enter
`/q` followed by your question (for example, "`/q explain the
 importance of this finding`"). 6. Review the proposed code changes by Amazon Q Developer, choose **Commit
suggestion**, and then choose **Commit changes** to update
the pull request. 7. If you're satisfied with the suggested code fixes, you can merge the pull request to
apply the code changes suggested by Amazon Q Developer. For more information, see [Merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request") in the _GitHub documentation_.

## Initiating code reviews within GitHub pull

requests

After an automatic code review performed by Amazon Q Developer for a new or reopened GitHub pull
request, you can initiate additional code reviews to iterate on your code using the `/q
 review` slash command. The code review is performed on the entire pull request's
diff.

###### Note

You can only initiate a code review within a pull request with a new comment. The
`/q review` slash command will not work in an existing comment thread.

###### To use initiate code reviews in a pull request

1. If necessary, sign in to your [GitHub](https://github.com/ "https://github.com/") account
   using your GitHub credentials.
2. Navigate to your GitHub organization, and then navigate to the pull request you want
   to perform a code review with Amazon Q Developer. For more information, see [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests").
3. Within the pull request, navigate to **Add a comment**, and in the
   comment text input field, enter `/q review`.
4. Choose **Comment** to initiate the code review.

It can take a few minutes for Amazon Q Developer to complete analyzing the pull request
code. After Amazon Q Developer finishes analyzing, it provides a code review summary. Each
finding appears as a threaded comment under the summary, along with proposed changes you
can choose to commit and update the pull request. 5. (Optional) Ask questions about specific findings. Within the pull request, navigate
to **Add a comment**, and in the comment text input field, enter
`/q` followed by your question (for example, "`/q explain the
 importance of this finding`"). 6. If you're satisfied with the suggested code fixes, you can merge the pull request to
apply the code changes suggested by Amazon Q Developer. For more information, see [Merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request") in the _GitHub documentation_.
