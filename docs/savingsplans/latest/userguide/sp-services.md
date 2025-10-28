# Services eligible for Savings Plans benefits

AWS offers three types of Savings Plans: Compute Savings Plans, EC2 Instance Savings Plans, and SageMaker Savings Plans.
Compute Savings Plans apply to usage across Amazon EC2, AWS Lambda, and AWS Fargate. EC2 Instance Savings Plans
apply to EC2 usage and SageMaker AI Savings Plans apply to SageMaker AI usage.

## Amazon EC2

Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services, Inc. (AWS) cloud.
Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and
deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual
servers as you need, configure security and networking, and manage storage. Amazon EC2
enables you to scale up or down to handle changes in requirements or spikes in
popularity, reducing your need to forecast traffic.

For more information about Amazon EC2, see [What Is Amazon EC2?](../../../AWSEC2/latest/WindowsGuide/concepts.md "../../../AWSEC2/latest/WindowsGuide/concepts.md") in the
_Amazon EC2 Getting Started Guide_.

## AWS Fargate

AWS Fargate is a serverless compute engine for containers that works with both
Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS). Fargate makes it easy for you to focus on
building your applications. Fargate removes the need to provision and manage servers,
lets you specify and pay for resources per application, and improves security through
application isolation by design.

Fargate is eligible for Compute Savings Plans.

For more information about Amazon ECS on Fargate, see [What is Amazon Elastic Container Service?](../../../AmazonECS/latest/developerguide/Welcome.md "../../../AmazonECS/latest/developerguide/Welcome.md") in the
_Amazon Elastic Container Service Developer Guide_.

For more information about Amazon EKS on Fargate, see [What is Amazon Elastic Kubernetes Service?](../../../eks/latest/userguide/what-is-eks.md "../../../eks/latest/userguide/what-is-eks.md") in the
**Amazon EKS User Guide**.

## AWS Lambda

AWS Lambda is a compute service that lets you run code without provisioning or managing
servers. AWS Lambda executes your code only when needed and scales automatically, from a
few requests per day to thousands per second. You pay only for the compute time you
consume - there is no charge when your code is not running. With AWS Lambda, you can run
code for virtually any type of application or backend service - all with zero
administration. AWS Lambda runs your code on a high-availability compute infrastructure
and performs all of the administration of the compute resources, including server and
operating system maintenance, capacity provisioning and automatic scaling, code
monitoring and logging.

Lambda is eligible for Compute Savings Plans.

For more information about Lambda, see [What Is AWS Lambda?](../../../lambda/latest/dg/services-costmanagement.md "../../../lambda/latest/dg/services-costmanagement.md") in
the _AWS Lambda Developer Guide_.

## Amazon SageMaker AI

Amazon SageMaker AI is a fully managed machine learning service. With SageMaker AI, data scientists and
developers can quickly and easily build and train machine learning models, and then
directly deploy them into a production-ready hosted environment.

SageMaker AI provides an integrated Jupyter authoring notebook instance for easy access to
your data sources for exploration and analysis, so you don't have to manage servers. It
also provides common machine learning algorithms that are optimized to run efficiently
against extremely large data in a distributed environment.

With native support for bring-your-own-algorithms and frameworks, SageMaker AI offers flexible
distributed training options that adjust to your specific workflows. Deploy a model into
a secure and scalable environment by launching it with a few clicks from SageMaker AI Studio or
the SageMaker AI console.

SageMaker AI is eligible for SageMaker AI Savings Plans.

For more information about Amazon SageMaker AI, see [What Is Amazon SageMaker AI?](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md") in the
_Amazon SageMaker AI Developer Guide_.
