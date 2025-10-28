# Customize Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

There are four options for customizing your Amazon SageMaker Studio Classic environment. You bring your own
SageMaker image, use a lifecycle configuration script, attach suggested Git repos to Studio Classic,
or create kernels using persistent Conda environments in Amazon EFS. Use each option
individually, or together.

- Bring your own SageMaker image: A SageMaker image is a file
  that identifies the kernels, language packages, and other dependencies required to
  run a Jupyter notebook in Amazon SageMaker Studio Classic. Amazon SageMaker AI provides many built-in images for
  you to use. If you need different functionality, you can bring your own custom
  images to Studio Classic.
- Use lifecycle configurations with Amazon SageMaker Studio Classic:
  Lifecycle configurations are shell scripts triggered by Amazon SageMaker Studio Classic lifecycle
  events, such as starting a new Studio Classic notebook. You can use lifecycle
  configurations to automate customization for your Studio Classic environment. For
  example, you can install custom packages, configure notebook extensions, preload
  datasets, and set up source code repositories.
- Attach suggested Git repos to Studio Classic: You can
  attach suggested Git repository URLs at the Amazon SageMaker AI domain or user profile level.
  Then, you can select the repo URL from the list of suggestions and clone that into
  your environment using the Git extension in Studio Classic.
- Persist Conda environments to the Studio Classic Amazon EFS
  volume: Studio Classic uses an Amazon EFS volume as a persistent storage layer.
  You can save your Conda environment on this Amazon EFS volume, then use the saved
  environment to create kernels. Studio Classic automatically picks up all valid
  environments saved in Amazon EFS as KernelGateway kernels. These kernels persist through
  restart of the kernel, app, and Studio Classic. For more information, see the
  **Persist Conda environments to the Studio Classic EFS volume** section in
  [Four approaches to manage Python packages in Amazon SageMaker Studio Classic
  notebooks](https://aws.amazon.com/blogs/machine-learning/four-approaches-to-manage-python-packages-in-amazon-sagemaker-studio-notebooks/ "https://aws.amazon.com/blogs/machine-learning/four-approaches-to-manage-python-packages-in-amazon-sagemaker-studio-notebooks/").
  The following topics show how to use these three options to customize your Amazon SageMaker Studio Classic
  environment.

###### Topics

- [Custom Images in Amazon SageMaker Studio Classic](studio-byoi.md "studio-byoi.md")
- [Use Lifecycle Configurations to Customize Amazon SageMaker Studio Classic](studio-lcc.md "studio-lcc.md")
- [Attach Suggested Git Repos to Amazon SageMaker Studio Classic](studio-git-attach.md "studio-git-attach.md")
