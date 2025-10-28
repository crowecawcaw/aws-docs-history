# Private registry with AWS Secrets Manager sample for CodeBuild

This sample shows you how to use a Docker image that is stored in a private registry as
your AWS CodeBuild runtime environment. The credentials for the private registry are stored in
AWS Secrets Manager. Any private registry works with CodeBuild. This sample uses Docker Hub.

###### Note

Secrets are visible to actions and are not masked when written to a file.

###### Topics

- [Private registry sample requirements](#sample-private-registry-requirements "#sample-private-registry-requirements")
- [Create a CodeBuild project with a
  private registry](private-registry-sample-create-project.md "private-registry-sample-create-project.md")
- [Configure a private registry
  credential for self-hosted runners](private-registry-sample-configure-runners.md "private-registry-sample-configure-runners.md")

##

Private registry sample requirements

To use a private registry with AWS CodeBuild, you must have the following:

- A Secrets Manager secret that stores your Docker Hub credentials. The credentials
  are used to access your private repository.

###### Note

You will be charged for secrets that you create.

- A private repository or account.
- A CodeBuild service role IAM policy that grants access to your Secrets Manager
  secret.

Follow these steps to create these resources and then create a CodeBuild build project
using the Docker images stored in your private registry.
