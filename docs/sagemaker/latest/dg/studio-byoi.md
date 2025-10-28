# Custom Images in Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

A SageMaker image is a file that identifies the kernels, language packages, and other
dependencies required to run a Jupyter notebook in Amazon SageMaker Studio Classic. These images are used to
create an environment that you then run Jupyter notebooks from. Amazon SageMaker AI provides many built-in
images for you to use. For the list of built-in images, see [Amazon SageMaker Images Available for Use With
Studio Classic Notebooks](notebooks-available-images.md "notebooks-available-images.md").

If you need different functionality, you can bring your own custom images to Studio Classic. You
can create images and image versions, and attach image versions to your domain or shared space,
using the SageMaker AI control panel, the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html"), and the [AWS Command Line Interface (AWS CLI)](../../../cli/latest/reference/sagemaker.md "../../../cli/latest/reference/sagemaker.md"). You can also create images
and image versions using the SageMaker AI console, even if you haven't onboarded to a SageMaker AI domain. SageMaker AI
provides sample Dockerfiles to use as a starting point for your custom SageMaker images in the [SageMaker Studio Classic
Custom Image Samples](https://github.com/aws-samples/sagemaker-studio-custom-image-samples/ "https://github.com/aws-samples/sagemaker-studio-custom-image-samples/") repository.

The following topics explain how to bring your own image using the SageMaker AI console or AWS CLI,
then launch the image in Studio Classic. For a similar blog article, see [Bringing
your own R environment to Amazon SageMaker Studio Classic](https://aws.amazon.com/blogs/machine-learning/bringing-your-own-r-environment-to-amazon-sagemaker-studio/ "https://aws.amazon.com/blogs/machine-learning/bringing-your-own-r-environment-to-amazon-sagemaker-studio/"). For notebooks that show how to bring your
own image for use in training and inference, see [Amazon SageMaker Studio Classic Container Build CLI](https://github.com/aws/amazon-sagemaker-examples/tree/main/aws_sagemaker_studio/sagemaker_studio_image_build "https://github.com/aws/amazon-sagemaker-examples/tree/main/aws_sagemaker_studio/sagemaker_studio_image_build").

## Key terminology

The following section defines key terms for bringing your own image to use with Studio Classic.

- Dockerfile: A Dockerfile is a file that
  identifies the language packages and other dependencies for your Docker
  image.
- Docker image: The Docker image is a built
  Dockerfile. This image is checked into Amazon ECR and serves as the basis of the SageMaker AI
  image.
- SageMaker image: A SageMaker image is a holder for a set of SageMaker AI
  image versions based on Docker images. Each image version is immutable.
- Image version: An image version of a SageMaker image
  represents a Docker image and is stored in an Amazon ECR repository. Each image version is
  immutable. These image versions can be attached to a domain or shared space and used with
  Studio Classic.

###### Topics

- [Custom SageMaker Image Specifications for Amazon SageMaker Studio Classic](studio-byoi-specs.md "studio-byoi-specs.md")
- [Prerequisites for Custom Images in Amazon SageMaker Studio Classic](studio-byoi-prereq.md "studio-byoi-prereq.md")
- [Add a Docker Image Compatible with
  Amazon SageMaker Studio Classic to Amazon ECR](studio-byoi-sdk-add-container-image.md "studio-byoi-sdk-add-container-image.md")
- [Create a Custom SageMaker Image for Amazon SageMaker Studio Classic](studio-byoi-create.md "studio-byoi-create.md")
- [Attach a Custom SageMaker Image in Amazon SageMaker Studio Classic](studio-byoi-attach.md "studio-byoi-attach.md")
- [Launch a Custom SageMaker Image in Amazon SageMaker Studio Classic](studio-byoi-launch.md "studio-byoi-launch.md")
- [Clean Up Resources for Custom Images in Amazon SageMaker Studio Classic](studio-byoi-cleanup.md "studio-byoi-cleanup.md")
