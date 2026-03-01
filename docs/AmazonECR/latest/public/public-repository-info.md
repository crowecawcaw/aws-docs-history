# Viewing the contents and details of a repository in Amazon ECR public

After you create a public repository, you can view details about it in the AWS Management Console.
For each image in the repository, you can view the image size, the URI for pulling the
image, the SHA digest, the image tags, and the time when the image was last pushed. You
can review the catalog data for the Amazon ECR Public Gallery. You can also see the
repository permission policies that are associated with the repository.

###### Note

Beginning with Docker version 1.9, the Docker client compresses image layers
before pushing them to a V2 Docker registry. The output of the **docker
images** command shows the uncompressed image size. Therefore, the image
size that's returned might be larger than the image sizes that are shown in the
AWS Management Console.

###### To view public repository information

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that the repository to view is
   in.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, select the
   **Public** tab, and then choose the repository to view the
   details of.
5. On the **Repositories >
   `repository_name`** page, choose
   **View public listing** to navigate to the repository
   detail page in the Amazon ECR Public Gallery in a new tab or use the navigation bar
   to view more details about the repository.
   - Choose **Images** to view information about the
     images in the repository. If there are untagged images that you want to
     delete, you can select the box to the left of the repositories to delete
     and choose **Delete**. For more information, see [Deleting an image in a public repository in Amazon ECR public](public-image-delete.md "public-image-delete.md").
   - Choose **Gallery detail** to view the public catalog
     data for the repository.
   - Choose **Permissions** to view the repository
     policies that are applied to the repository. For more information, see
     [Public repository policies in Amazon ECR Public](public-repository-policies.md "public-repository-policies.md").
