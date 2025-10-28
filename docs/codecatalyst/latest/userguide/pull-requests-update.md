Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Updating a pull request

You can make it easier for other project members to review code by updating the pull
request. You can update a pull request to change its reviewers, its links to issues, the
title of the pull request, or its description. For example, you might want to change the
required reviewers for a pull request to remove someone who's away on vacation, and add
someone else. You can also update a pull request with further code changes by pushing
commits to the source branch of an open pull request. Each push to the source branch of
a pull request in the CodeCatalyst source repository creates a revision. Project members can
view the differences between revisions in a pull request.

###### To update the reviewers for a pull

request

1. Navigate to the project where you want to update the reviewers of a pull
   request.
2. On the project page, under **Open pull requests**, choose the
   pull request where you want to update reviewers. Alternatively, in the
   navigation pane, choose **Code**, choose **Pull
   requests**, and then choose the pull request you want to update.
3. (Optional) In **Overview**, in the **Pull request
   details** area, choose the plus sign to add required or optional
   reviewers. Choose the **X** next to a reviewer to remove them
   as an optional or required reviewer.
4. (Optional) In **Overview**, in the **Pull request
   details** area, choose **Link issues** to link an
   issue to the pull request, and then either choose an issue from the list or
   enter its ID. To unlink an issue, choose the unlink icon next to the issue you
   want to unlink.

###### To update files and code in the source

branch of a pull request

1. To update multiple files, either [create
   a Dev Environment](devenvironment-create.md "devenvironment-create.md"), or clone the repository and its source branch and use
   a Git client or an integrated development environment (IDE) to make changes to
   the files in the source branch. Commit and push the changes to the source branch
   in the CodeCatalyst source repository to automatically update the pull request with
   the changes. For more information, see [Cloning a source repository](source-repositories-clone.md "source-repositories-clone.md") and [Understanding
   changes in source code with commits in Amazon CodeCatalyst](source-commits.md "source-commits.md").
2. To update an individual file in a source branch, you can use a Git client or
   IDE as you would for multiple files. You can also edit it directly in the CodeCatalyst
   console. For more information, see [Editing a file](source-files-edit.md "source-files-edit.md").

###### To update the title and description

of a pull request

1. Navigate to the project where you want to update the title or description of a
   pull request.
2. The project page displays open pull requests, including information about who
   created the pull request, what repository contains the branches for the pull
   request, and when the pull request was created. You can filter the open pull
   request view by source repository. Choose the pull request that you want to
   change from the list.
3. To view all pull requests, choose **View all**.
   Alternatively, in the navigation pane, choose **Code**, and
   then choose **Pull requests**. Use the filter box or sort
   functions to find the pull request you want to change, and then choose
   it.
4. In **Overview**, choose **Edit**.
5. Change the title or description, and then choose
   **Save**.
