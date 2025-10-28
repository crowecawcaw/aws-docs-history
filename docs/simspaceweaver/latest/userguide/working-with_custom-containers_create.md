End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Create a custom container

These instructions assume that you know how to use Docker and Amazon Elastic Container Registry (Amazon ECR).
For more information about Amazon ECR, see the _[Amazon ECR User Guide](../../../AmazonECR/latest/userguide.md "../../../AmazonECR/latest/userguide.md")_.

###### Prerequisites

- The IAM identity (use or role) that you use to perform these actions has the correct permissions to use Amazon ECR
- Docker is installed on your local system

###### To create a custom container

1. Create your `Dockerfile`.

A `Dockerfile` to run AWS SimSpace Weaver apps starts with
the Amazon Linux 2 image in Amazon ECR.

```
# parent image required to run AWS SimSpace Weaver apps
FROM public.ecr.aws/amazonlinux/amazonlinux:2

```

2. Build your `Dockerfile`.
3. Upload your container image to Amazon ECR.
   - [Use the
     AWS Management Console.](../../../AmazonECR/latest/userguide/getting-started-console.md "../../../AmazonECR/latest/userguide/getting-started-console.md")
   - [Use the
     AWS Command Line Interface.](../../../AmazonECR/latest/userguide/getting-started-cli.md "../../../AmazonECR/latest/userguide/getting-started-cli.md")###### Note

If you get an `AccessDeniedException` error when you try to
upload your container image to Amazon ECR, your IAM identity (user or role)
might not have the necessary permissions to use Amazon ECR.
You can attach the `AmazonEC2ContainerRegistryPowerUser` AWS
managed policy to your IAM identity and try again.
For more information about how to attach a policy, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User Guide_.
