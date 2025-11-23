# Close a pull request in an AWS CodeCommit

repository

If you want to close a pull request without merging the code, you can do so in one of
several ways:

- In the console, you can close a pull request without merging the code. You might want to
  do this if you want to use the **git merge** command to merge the branches
  manually, or if the code in the pull request source branch isn't code you want merged into
  the destination branch.
- You can delete the source branch specified in the pull request. CodeCommit closes a pull
  request automatically if either the source or destination branch of the pull request is
  deleted.
- In the AWS CLI, you can update the status of a pull request from `OPEN`
  to `CLOSED`. This closes the pull request without merging the code.

###### Topics

- [Close a pull request (console)](#how-to-close-pull-request-console "#how-to-close-pull-request-console")
- [Close a pull request (AWS CLI)](#how-to-close-pull-request-cli "#how-to-close-pull-request-cli")

## Close a pull request (console)

You can use the CodeCommit console to close a pull request in a CodeCommit repository. After the
status of a pull request is changed to **Closed**, it cannot be changed back
to **Open**, but users can still comment on the changes and reply to
comments.

1. Open the CodeCommit console at [https://console.aws.amazon.com/codesuite/codecommit/home](https://console.aws.amazon.com/codesuite/codecommit/home "https://console.aws.amazon.com/codesuite/codecommit/home").
2. In **Repositories**, choose the name of the repository.
3. In the navigation pane, choose **Pull requests**.
4. By default, a list of all open pull requests is displayed. Choose the open pull
   request you want to close.

![Pull requests displayed in the CodeCommit console.](images/codecommit-pull-request-view.png) 5. In the pull request, choose **Close pull request**. This option
closes the pull request without attempting to merge the source branch into the destination
branch. This option does not provide a way to delete the source branch as part of closing
the pull request, but you can do it yourself after the request is closed.

## Close a pull request (AWS CLI)

To use AWS CLI commands with CodeCommit, install the AWS CLI. For more information, see
[Command line reference](cmd-ref.md "cmd-ref.md").

**To use the AWS CLI to close pull requests in a
CodeCommit repository**

- To update the status of a pull request in a
  repository from `OPEN` to `CLOSED`, run the
  **update-pull-request-status** command, specifying:

      + The ID of the pull request (with the **--pull-request-id**
       option).
      + The status of the pull request (with the **--pull-request-status**
       option).

  For example, to update the status of a pull request with the ID of
  `42` to a status of `CLOSED` in a
  CodeCommit repository named `MyDemoRepo`:

```
aws codecommit update-pull-request-status --pull-request-id `42` --pull-request-status `CLOSED`
```

If successful, this command produces output similar to the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codecommit:GetRepository",
 "Resource": [
 "arn:aws:codecommit:us-east-2:`111122223333`:`MySharedDemoRepo`"
 ]
 }
 ]
}`

```
