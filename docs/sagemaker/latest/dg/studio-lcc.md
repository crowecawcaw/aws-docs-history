# Use Lifecycle Configurations to Customize Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Amazon SageMaker Studio Classic triggers lifecycle configurations shell scripts during important lifecycle
events, such as starting a new Studio Classic notebook. You can use lifecycle configurations to
automate customization for your Studio Classic environment. This customization includes
installing custom packages, configuring notebook extensions, preloading datasets, and
setting up source code repositories.

Using lifecycle configurations gives you flexibility and control to configure Studio Classic
to meet your specific needs. For example, you can use customized container images with
lifecycle configuration scripts to modify your environment. First, create a minimal set of
base container images, then install the most commonly used packages and libraries in those
images. After you have completed your images, use lifecycle configurations to install
additional packages for specific use cases. This gives you the flexibility to modify your
environment across your data science and machine learning teams based on need.

Users can only select lifecycle configuration scripts that they are given access to. While
you can give access to multiple lifecycle configuration scripts, you can also set default
lifecycle configuration scripts for resources. Based on the resource that the default
lifecycle configuration is set for, the default either runs automatically or is the first
option shown.

For example lifecycle configuration scripts, see the [Studio Classic Lifecycle Configuration examples GitHub repository](https://github.com/aws-samples/sagemaker-studio-lifecycle-config-examples "https://github.com/aws-samples/sagemaker-studio-lifecycle-config-examples"). For a blog on
implementing lifecycle configuration, see [Customize Amazon SageMaker Studio Classic using Lifecycle Configurations](https://aws.amazon.com/blogs/machine-learning/customize-amazon-sagemaker-studio-using-lifecycle-configurations/ "https://aws.amazon.com/blogs/machine-learning/customize-amazon-sagemaker-studio-using-lifecycle-configurations/").

###### Note

Each script has a limit of **16384 characters**.

###### Topics

- [Create and Associate a Lifecycle Configuration with Amazon SageMaker Studio Classic](studio-lcc-create.md "studio-lcc-create.md")
- [Set Default Lifecycle Configurations for Amazon SageMaker Studio Classic](studio-lcc-defaults.md "studio-lcc-defaults.md")
- [Debug Lifecycle Configurations in Amazon SageMaker Studio Classic](studio-lcc-debug.md "studio-lcc-debug.md")
- [Update and Detach Lifecycle Configurations in Amazon SageMaker Studio Classic](studio-lcc-delete.md "studio-lcc-delete.md")
