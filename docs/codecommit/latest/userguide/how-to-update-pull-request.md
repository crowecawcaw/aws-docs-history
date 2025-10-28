AWS CodeCommit is no longer available to new customers. Existing customers of
AWS CodeCommit can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider")

# Update a pull request

You can update a pull request with further code changes by pushing commits to the source branch of an open pull request. For more information,
see [Create a commit in AWS CodeCommit](how-to-create-commit.md "how-to-create-commit.md").

You can use the AWS CodeCommit console or the AWS CLI to update the title or description of
a pull request. You might want to update the pull request title or description because:

- Other users don't understand the description, or the original title is misleading.
- You want the title or description to reflect changes made to the source branch of an open
  pull request.

## Update a pull request (console)

You can use the CodeCommit console to update the title and description of a pull request in an
CodeCommit repository. To update the code in the pull request, push commits to the source branch of
an open pull request.

1. Open the CodeCommit console at [https://console.aws.amazon.com/codesuite/codecommit/home](https://console.aws.amazon.com/codesuite/codecommit/home "https://console.aws.amazon.com/codesuite/codecommit/home").
2. In **Repositories**, choose the name of the repository where you want to
   update a pull request.
3. In the navigation pane, choose **Pull requests**.
4. By default, a list of all open pull requests is displayed. Choose the open pull request
   you want to update.
5. In the pull request, choose **Details**, and then choose **Edit
   details** to edit the title or description.

###### Note

You cannot update the title or description of a closed or merged pull request.

## Update pull requests (AWS CLI)

To use AWS CLI commands with CodeCommit, install the AWS CLI. For more information, see
[Command line reference](cmd-ref.md "cmd-ref.md").

You might also be interested in the following commands:

- **[update-pull-request-approval-state](how-to-review-pull-request.md#update-pull-request-approval-state "how-to-review-pull-request.md#update-pull-request-approval-state")**, to approve or revoke approval on a pull
  request.
- [create-pull-request-approval-rule](how-to-create-pull-request-approval-rule.md#how-to-create-pull-request-approval-rule-cli "how-to-create-pull-request-approval-rule.md#how-to-create-pull-request-approval-rule-cli"), to create an approval rule for
  a pull request.
- [delete-pull-request-approval-rule](how-to-edit-delete-pull-request-approval-rule.md#delete-pull-request-approval-rule "how-to-edit-delete-pull-request-approval-rule.md#delete-pull-request-approval-rule"), to delete an approval rule for
  a pull request.
- [Create a commit using the AWS CLI](how-to-create-commit.md#how-to-create-commit-cli "how-to-create-commit.md#how-to-create-commit-cli") or
  [Create a commit using a Git client](how-to-create-commit.md#how-to-create-commit-git "how-to-create-commit.md#how-to-create-commit-git"), to create
  and push additional code changes to the source branch of an open pull request.

**To use the AWS CLI to update pull requests in a
CodeCommit repository**

1.  To update the title of a pull request in a
    repository, run the **update-pull-request-title** command, specifying:

        * The ID of the pull request (with the **--pull-request-id**
         option).
        * The title of the pull request (with the **--title** option).

    For example, to update the title of a pull request with the ID of
    `47`:

```
aws codecommit update-pull-request-title --pull-request-id `47` --title "`Consolidation of global variables - updated review`"
```

2. To update the description of a pull request,
   run the **update-pull-request-description** command, specifying:
   - The ID of the pull request (with the **--pull-request-id**
     option).
   - The description (with the **--description** option).
     For example, to update the description of a pull request with the ID of
     `47` :

```
aws codecommit update-pull-request-description --pull-request-id `47` --description "Updated the pull request to remove unused global variable."
```
