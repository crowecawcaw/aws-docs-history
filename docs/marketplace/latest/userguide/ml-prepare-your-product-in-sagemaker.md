

# Preparing your product in SageMaker AI

Before you can publish your product in AWS Marketplace, you must prepare it in Amazon SageMaker AI. There are two types of SageMaker AI products listed in AWS Marketplace: model packages and algorithms. For more information, see [Machine learning products in AWS Marketplace](machine-learning-products.md). This topic provides an overview of the three steps that are required to prepare your product:

1. [Packaging your product](ml-packaging-your-code-into-images.md) – To prepare a model package or algorithm product, you must create the Docker container images for your product. 

1. [Uploading your images to Amazon Elastic Container Registry](ml-uploading-your-images.md) – After packaging your code in container images and testing them locally, upload the images and scan them for known vulnerabilities. Fix any vulnerabilities before continuing. 

1.  [Creating your Amazon SageMaker AI resource](ml-creating-your-amazon-sagemaker-resource.md) – After your images are scanned successfully, you can use them to create a model package or algorithm resource in SageMaker AI.

In AWS Partner Central, **Step 2: Delivery configuration** of your listing has an optional card, **Prepare your product in SageMaker AI**, that links to these three topics. When you finish, choose **Complete**. To list your resource, add a version. For more information, see [Adding the initial version](add-initial-version.md).