

# Launching with a Container image fulfillment option
<a name="buyer-launch-container-image"></a>

For a fulfillment option with a **Container image** delivery method, use the seller-provided instructions to launch the product. This is done by pulling Docker images directly from Amazon ECR. The general steps to launch the product are as follows:

**To launch a product with a Container image fulfillment option**

1. Verify that you have installed the latest versions of the AWS Command Line Interface (AWS CLI) and Docker. For more information, see [Using Amazon ECR with the AWS CLI](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html) in the *Amazon Elastic Container Registry User Guide*.

1. Authenticate your Docker client to your Amazon ECR registry. The steps to do this will depend on your operating system.

1. Pull all of the Docker images using the provided Amazon ECR image Amazon Resource Name (ARN). For more information, see [Pulling an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon Elastic Container Registry User Guide*.

1. Review any usage instructions or external links provided by the seller for information about using the product.