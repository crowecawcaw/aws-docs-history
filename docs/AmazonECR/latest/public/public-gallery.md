# Amazon ECR Public Gallery

The Amazon ECR Public Gallery is a public website to find and share container images hosted in
Amazon ECR public repositories. There is no authentication required to browse the public
repositories and pull the images. Visit the Amazon ECR Public Gallery at [https://gallery.ecr.aws](https://gallery.ecr.aws "https://gallery.ecr.aws").

Amazon ECR users create public repositories and define the catalog data that appears in the
Amazon ECR Public Gallery. The catalog data includes the repository name, a short description, a
more detailed description on the **About** tab, and detailed usage
instructions on the **Usage** tab. AWS accounts that publish popular or
commonly used images can request a **Verified account** badge by contacting
support. For more information, see [Creating a support
case](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md").

The Amazon ECR Public Gallery provides search filters that make it easy to browse through the
public repositories. The available search filters include verified accounts, supported
operating systems, and system architectures. You can also use the search option to find a
specific repository.

You can launch some Amazon ECR Public Gallery container images as web services running on
AWS App Runner. When browsing the gallery, look for **Launch to AWS App Runner** on an
image's gallery page. An image with this option is a web application that App Runner supports. For
more information, see [Launch an App Runner service directly from the Amazon ECR Public Gallery](../../../apprunner/latest/dg/service-source-image.md#service-source-image.providers.ecrpublic "../../../apprunner/latest/dg/service-source-image.md#service-source-image.providers.ecrpublic") in the
_App Runner developer guide_.

To get started with creating your own public repository, see [Moving an image through its lifecycle in Amazon ECR Public](getting-started-cli.md "getting-started-cli.md").
