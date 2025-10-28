End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Custom containers

AWS SimSpace Weaver apps run in containerized Amazon Linux 2 (AL2)
environments. In the AWS Cloud, SimSpace Weaver runs your simulations in Docker containers
built from an `amazonlinux:2` image served from Amazon Elastic Container Registry (Amazon ECR). You can create
a custom Docker image, store it in in Amazon ECR, and use that image for your simulation instead
of the default Docker image that we provide.

You can use a custom container to manage your software dependencies and include
additional software components that aren't in the standard Docker image. For example,
you can add the publicly-available software libraries that your app uses to the
container and only put your custom code in the app zip file.

###### Important

We only support AL2 Docker images hosted in Amazon ECR repositories, either
in Amazon ECR Public Gallery or your private Amazon ECR registry. We don't support Docker images
hosted outside Amazon ECR. For more information about Amazon ECR, see _[Amazon Elastic Container Registry Documentation](../../../ecr.md "../../../ecr.md")_.

###### Topics

- [Create a custom container](working-with_custom-containers_create.md "working-with_custom-containers_create.md")
- [Modify a project
  to use a custom container](working-with_custom-containers_modify-project.md "working-with_custom-containers_modify-project.md")
- [Frequently asked questions about custom containers](working-with_custom-containers_faq.md "working-with_custom-containers_faq.md")
- [Troubleshooting custom containers](working-with_custom-containers_troubleshooting.md "working-with_custom-containers_troubleshooting.md")
