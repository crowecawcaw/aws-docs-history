# Creating an Amazon ECR public repository to store images

Before you can push your Docker or Open Container Initiative (OCI) images to Amazon ECR,
you must create a repository to store them in. Public repositories are visible on the
Amazon ECR Public Gallery and are open to publicly pull images from. If you want to create a
private repository instead, see [Repositories](../userguide/Repositories.md "../userguide/Repositories.md") in the
_Amazon Elastic Container Registry User Guide_.

###### To create a public repository (AWS Management Console)

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the AWS Region to create your public
   repository in.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, choose **Create
   repository**.
5. For **Visibility settings**, choose
   **Public**.
6. For **Repository name**, enter a unique name for your public
   repository. The repository name can be specified on its own (for example,
   `nginx-web-app`) or prepended with a namespace to group the
   repository into a category (for example,
   `project-a/nginx-web-app`).

###### Note

The repository name may container a maximum of `205`
characters. The name must start with a letter and can only contain lowercase
letters, numbers, hyphens, underscores, periods and forward slashes. Using a
double hyphen, double underscore, or double forward slash isn't
supported. 7. For **Repository logo**, choose **Upload
file** and select a local image file to use as the repository logo.
Amazon ECR uploads your logo as a base64-encoded payload to a publicly available Amazon S3
bucket.

###### Note

The repository logo is only publicly visible in the Amazon ECR Public Gallery
for verified accounts. A verified account is an account that is AWS Marketplace
certified. 8. For **Short description** enter a description of the
repository. The description field is displayed on the Amazon ECR Public Gallery in
the search results and on the repository detail page. 9. For **Content types** select the operating system and system
architecture tags to associate with the repository. These tags are publicly
displayed in the Amazon ECR Public Gallery as badges on the repository and are used
as search filters. 10. For **About**, enter a detailed description for the
repository. This text should be in Github Flavored Markdown format. For format
examples, see [Specifying the repository catalog data in Amazon ECR public](public-repository-catalog-data.md "public-repository-catalog-data.md"). This field is publicly
visible on the Amazon ECR Public Gallery on the repository detail page. 11. For **Usage**, enter details about how to use the images in
the repository. This text should be in Github Flavored Markdown format. For
format examples, see [Specifying the repository catalog data in Amazon ECR public](public-repository-catalog-data.md "public-repository-catalog-data.md"). This field is publicly
visible on the Amazon ECR Public Gallery on the repository detail page. 12. Choose **Create repository**.

## Next steps

To view the steps to push an image to your repository, select the repository and
choose **View push commands**. For more information about pushing
an image to your repository, see [Pushing an image to a public repository in Amazon ECR public](docker-push-ecr-image.md "docker-push-ecr-image.md").
