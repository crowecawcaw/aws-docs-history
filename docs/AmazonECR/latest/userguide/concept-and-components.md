# Concepts and components of Amazon ECR

Amazon ECR is a fully managed Docker container registry service provided by AWS. It
allows you to store, manage, and deploy Docker container images securely and reliably.
These concepts and components work together to provide a secure, scalable, and reliable
Docker container registry service within the AWS, enabling you to efficiently manage
and deploy your containerized applications.

Here are some key concepts and components of Amazon ECR:

**Registry**

An Amazon ECR registry is a private repository provided to each AWS account,
where you can create one or more repositories. These repositories allow you
to store and distribute Docker images, Open Container Initiative (OCI)
images, and other OCI-compatible artifacts within your AWS environment.
For more information, see [Amazon ECR private registry](Registries.md "Registries.md").

**Authorization token**

Your client must authenticate to an Amazon ECR private registry as an AWS
user before it can push and pull images. For more information, see [Private registry authentication in Amazon ECR](registry_auth.md "registry_auth.md").

**Repository**

A repository in Amazon ECR is a logical collection where you can store your
Docker images, Open Container Initiative (OCI) images, and other
OCI-compatible artifacts. Within a single Amazon ECR registry, you can have
multiple repositories to organize your container images. For more
information, see [Amazon ECR private repositories](Repositories.md "Repositories.md").

**Repository policy**

You can control access to your repositories and the contents within them
with repository policies. For more information, see [Private repository policies in Amazon ECR](repository-policies.md "repository-policies.md").

**Image**

You can push and pull container images to your repositories. You can use
these images locally on your development system, or you can use them in
Amazon ECS task definitions and Amazon EKS pod specifications. For more information,
see [Using Amazon ECR images with Amazon ECS](ECR_on_ECS.md "ECR_on_ECS.md") and [Using Amazon ECR Images with Amazon EKS](ECR_on_EKS.md "ECR_on_EKS.md").

**Lifecycle Policy**

Amazon ECR lifecycle policies allow you to manage the lifecycle of your images
by defining rules for pruning and expiring old or unused images. For more
information, see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](LifecyclePolicies.md "LifecyclePolicies.md").

**Image Scanning**

Amazon ECR provides an integrated image scanning capability that helps identify
software vulnerabilities in your container images. For more information, see
[Scan images for software vulnerabilities in Amazon ECR](image-scanning.md "image-scanning.md").

**Access Control**

Amazon ECR uses IAM to control access to your repositories. You can create
IAM users, groups, and roles with specific permissions to push, pull, or
manage Amazon ECR repositories. For more information, see [Security in Amazon Elastic Container Registry](security.md "security.md").

**Cross-account and Cross-region Replication**

Amazon ECR supports replicating images across multiple AWS accounts and
regions for increased availability and reduced latency. For more
information, see [Private image replication in Amazon ECR](replication.md "replication.md").

**Encryption**

Amazon ECR supports server-side encryption of your Docker images at rest using
AWS KMS. For more information, see [Data protection in Amazon ECR](data-protection.md "data-protection.md").

**AWS Command Line Interface Integration**

The AWS CLI provides commands to interact with Amazon ECR repositories, such as
creating, listing, pushing, and pulling images.

**AWS Management Console**

Amazon ECR can also be managed through the AWS Management Console, providing a
user-friendly web interface for working with your repositories and images.

**AWS CloudTrail**

Amazon ECR integrates with AWS CloudTrail, allowing you to log and
audit API calls made to Amazon ECR for security and compliance purposes. For more
information, see [Logging Amazon ECR actions with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**Amazon CloudWatch**

Amazon ECR provides metrics and logs that can be monitored using
Amazon CloudWatch, enabling you to track the performance and usage
of your Amazon ECR repositories. For more information, see [Amazon ECR repository metrics](ecr-repository-metrics.md "ecr-repository-metrics.md").

**Managed signing**

Managed signing automatically generates cryptographic signatures when images are pushed to Amazon ECR, simplifying container image signing. For more information, see [Managed signing](managed-signing.md "managed-signing.md").
