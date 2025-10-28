# Deleting a public repository policy statement

Amazon ECR public

If you're finished using a repository, you can delete it. When you delete a repository
in the AWS Management Console, all of the images that are contained in the repository are also
deleted. This action can't be undone.

###### To delete a public repository

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the AWS Region that contains the repository
   to delete.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, select the
   **Public** tab, and then select the repository to delete
   and choose **Delete**.
5. In the **Delete `repository_name`**
   window, double check the repositories that you selected to delete and choose
   **Delete**.

###### Important

Any images in the selected repositories are also deleted.
