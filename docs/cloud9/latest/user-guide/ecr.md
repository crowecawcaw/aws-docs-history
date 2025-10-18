AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with Amazon ECR in AWS Cloud9 IDE

Amazon Elastic Container Registry (Amazon ECR) is an AWS managed container-registry service that's secure and
 scalable. Several Amazon ECR service functions are accessible from the AWS Toolkit
 Explorer:


* Creating a repository.
* Creating an AWS App Runner service for your repository or tagged image.
* Accessing image tag and repository URIs or ARNs.
* Deleting image tags and repositories.
You can also access the full-range of Amazon ECR functions through the AWS Cloud9 console by
 installing the AWS CLI and other platforms.

For more information about Amazon ECR, see [What is Amazon ECR?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html "https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html") in the
 Amazon Elastic Container Registry User Guide.


## Prerequisites


The following are pre-installed in the AWS Cloud9 IDE for AWS Cloud9 Amazon EC2 environments. They're
 required to access the Amazon ECR service from the AWS Cloud9 IDE. 


### IAM credentials


The IAM role that you created and used for authentication in the AWS
 console. For more information about IAM, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/ "https://docs.aws.amazon.com/IAM/latest/UserGuide/").


### Docker configuration


Docker is pre-installed in the AWS Cloud9 IDE for AWS Cloud9 Amazon EC2 environments. For more
 information about Docker, see [Install Docker Engine](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/").


### AWS CLI version 2 configuration


AWS CLI version 2 is pre-installed in the AWS Cloud9 IDE for AWS Cloud9 Amazon EC2 environments. For more
 information about AWS CLI version 2, see [Installing, updating, and
 uninstalling the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html").


###### Topics

* [Using Amazon ECR with AWS Cloud9 IDE](ecr-working.md "ecr-working.md")
