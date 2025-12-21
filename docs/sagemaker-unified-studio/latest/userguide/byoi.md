# Bring your own image (BYOI)

An image is a file that identifies the kernels, language packages, and other dependencies
required to run your applications. It includes:

- Programming languages (like Python or R)
- Kernels
- Libraries and packages
- Other necessary software
  Amazon SageMaker AI Distribution ([`sagemaker-distribution`](https://gallery.ecr.aws/sagemaker/sagemaker-distribution "https://gallery.ecr.aws/sagemaker/sagemaker-distribution")) is a set of Docker images that include popular
  frameworks and packages for machine learning, data science, and visualization.

You can also create your own custom image, using an Amazon SageMaker AI Distribution image as a base
image, to bring your own image (BYOI). You may want to BYOI when:

- You need a specific version of a programming language or library
- You want to include custom tools or packages
- You're working with specialized software not available in the standard images

###### Topics

- [Dockerfile specifications](byoi-specifications.md "byoi-specifications.md")
- [How to BYOI](byoi-how-to.md "byoi-how-to.md")
- [Launch your custom image in Amazon SageMaker Unified Studio](byoi-launch-custom-image.md "byoi-launch-custom-image.md")
- [Speed up container startup with SOCI](byoi-soci-indexing.md "byoi-soci-indexing.md")
- [Detach and clean up custom image resources](byoi-clean-up.md "byoi-clean-up.md")
