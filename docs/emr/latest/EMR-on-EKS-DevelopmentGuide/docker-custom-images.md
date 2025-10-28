# Customizing Docker images for Amazon EMR on EKS

You can use customized Docker images with Amazon EMR on EKS. Customizing the Amazon EMR on EKS runtime image
provides the following benefits:

- Package application dependencies and runtime environment into a single immutable
  container that promotes portability and simplifies dependency management for each
  workload.
- Install and configure packages that are optimized to your workloads. These packages may
  not be widely available in the public distribution of Amazon EMR runtimes.
- Integrate Amazon EMR on EKS with current established build, test, and deployment processes
  within your organization, including local development and testing.
- Apply established security processes, such as image scanning, that meet compliance and
  governance requirements within your organization.

###### Topics

- [How to customize Docker images](docker-custom-images-steps.md "docker-custom-images-steps.md")
- [Details for selecting a base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md")
- [Considerations for customizing images](docker-custom-images-considerations.md "docker-custom-images-considerations.md")
