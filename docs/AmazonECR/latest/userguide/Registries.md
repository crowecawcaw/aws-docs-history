

# Amazon ECR private registry
<a name="Registries"></a>

An Amazon ECR private registry hosts your container images in a highly available and scalable architecture. You can use your private registry to manage private image repositories consisting of Docker and Open Container Initiative (OCI) images and artifacts. Each AWS account is provided with a default private Amazon ECR registry. For more information about Amazon ECR public registries, see [Public registries](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html) in the *Amazon Elastic Container Registry Public User Guide*.

## Private registry concepts
<a name="registry_concepts"></a>
+ The URL for your default private registry is  `https://``{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com` .
+ By default, your account has read and write access to the repositories in your private registry. However, users require permissions to make calls to the Amazon ECR APIs and to push or pull images to and from your private repositories. Amazon ECR provides several managed policies to control user access at varying levels. For more information, see [Amazon Elastic Container Registry Identity-based policy examples](security_iam_id-based-policy-examples.md).
+ You must authenticate your Docker client to your private registry so that you can use the **docker push** and **docker pull** commands to push and pull images to and from the repositories in that registry. For more information, see [Private registry authentication in Amazon ECR](registry_auth.md).
+ Private repositories can be controlled with both user access policies and repository policies. For more information about repository policies, see [Private repository policies in Amazon ECR](repository-policies.md).
+ The repositories in your private registry can be replicated across AWS Regions in your own private registry and across separate accounts by configuring replication for your private registry. For more information, see [Private image replication in Amazon ECR](replication.md).