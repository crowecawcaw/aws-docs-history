# How Amazon Elastic Container Registry uses AWS Secrets Manager

Amazon Elastic Container Registry (Amazon ECR) is an AWS managed container image registry service that is secure,
scalable, and reliable. You can use the Docker CLI, or your preferred client, to push and pull
images to and from your repositories. For each upstream registry containing images you want to
cache in your Amazon ECR private registry, you must create a pull through cache rule. For upstream
registries that require authentication, you must store the credentials in an Secrets Manager secret. You
can create the Secrets Manager secret in either the Amazon ECR or Secrets Manager consoles. For more information, see
[Creating a pull
through cache rule](../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md "../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md") in the _Amazon ECR User Guide_.
