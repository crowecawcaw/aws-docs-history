# Deleting a private repository in Amazon ECR

If you're finished using a repository, you can delete it. When you delete a repository
in the AWS Management Console, all of the images contained in the repository are also deleted; this
cannot be undone.

###### Important

Images in the deleted repositories are also deleted. You cannot undo this
operation.

###### To delete a repository (AWS Management Console)

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that contains the repository to
   delete.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, choose the
   **Private** tab and then select the repository to delete
   and choose **Delete**.
5. In the **Delete `repository_name`**
   window, verify that the selected repositories should be deleted and choose
   **Delete**.
