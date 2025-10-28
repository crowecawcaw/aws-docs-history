# MLOps Project Templates

An Amazon SageMaker AI project template automates the setup and implementation of MLOps for your
projects. A SageMaker AI project template is an Service Catalog product that SageMaker AI makes available to
Amazon SageMaker Studio (or Studio Classic) users. These Service Catalog products are visible in your Service Catalog console
after you enable permissions when you onboard or update Amazon SageMaker Studio (or Studio Classic). For
information about enabling permissions to use SageMaker AI project templates, see [Granting SageMaker Studio Permissions
Required to Use
Projects](sagemaker-projects-studio-updates.md "sagemaker-projects-studio-updates.md"). Use SageMaker AI project templates to create a project that is an end-to-end MLOps solution.

You can use a SageMaker Projects template to implement image-building CI/CD. With this template,
you can automate the CI/CD of images that are built and pushed to Amazon ECR. Changes in the
container files in your project’s source control repositories initiate the ML pipeline and
deploy the latest version for your container. For more information, see the blog [Create Amazon SageMaker Projects with image building CI/CD pipelines](https://aws.amazon.com/blogs/machine-learning/create-amazon-sagemaker-projects-with-image-building-ci-cd-pipelines/ "https://aws.amazon.com/blogs/machine-learning/create-amazon-sagemaker-projects-with-image-building-ci-cd-pipelines/").

If you are an administrator, you can create custom project templates from scratch or modify
one of the project templates provided by SageMaker AI. Studio (or Studio Classic) users in your
organization can use these custom project templates to create their projects.

###### Topics

- [Use SageMaker AI-Provided Project Templates](sagemaker-projects-templates-sm.md "sagemaker-projects-templates-sm.md")
- [Create Custom Project Templates](sagemaker-projects-templates-custom.md "sagemaker-projects-templates-custom.md")
