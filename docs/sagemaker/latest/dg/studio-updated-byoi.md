# Bring your own image (BYOI)

An image is a file that identifies the kernels, language packages, and other dependencies
required to run your applications. It includes:

- Programming languages (like Python or R)
- Kernels
- Libraries and packages
- Other necessary software
  Amazon SageMaker Distribution (`sagemaker-distribution`) is a set of Docker images
  that include popular frameworks and packages for machine learning, data science, and visualization.
  For more information, see [SageMaker Studio image support policy](sagemaker-distribution.md "sagemaker-distribution.md").

If you need different functionality, you can bring your own image (BYOI). You may want to
create a custom image if:

- You need a specific version of a programming language or library
- You want to include custom tools or packages
- You're working with specialized software not available in the standard images

## Key terminology

The following section defines key terms for bringing your own image to use with SageMaker AI.

- Dockerfile: A text-based document with instructions for
  building a Docker image. This identifies the language packages and other dependencies for your
  Docker image.
- Docker image: A packaged set of software and dependencies
  built from a Dockerfile.
- SageMaker AI image store: A storage of your custom images in
  SageMaker AI.

###### Topics

- [Custom image specifications](studio-updated-byoi-specs.md "studio-updated-byoi-specs.md")
- [How to bring your own image](studio-updated-byoi-how-to.md "studio-updated-byoi-how-to.md")
- [Launch a custom image in
  Studio](studio-updated-byoi-how-to-launch.md "studio-updated-byoi-how-to-launch.md")
- [View your custom image details](studio-updated-byoi-view-images.md "studio-updated-byoi-view-images.md")
- [Detach and clean up custom image
  resources](studio-updated-byoi-how-to-detach-from-domain.md "studio-updated-byoi-how-to-detach-from-domain.md")
