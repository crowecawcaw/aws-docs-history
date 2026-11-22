

# Embedded ML models using Amazon SageMaker AI on AWS Marketplace

Publication date: **August 17, 2022 ([Diagram history](diagram-history.md))**

With this architecture, you can create an environment where a buyer consumes a seller's application into their own virtual private cloud (VPC), protecting the buyer's data privacy while also protecting the seller's application intellectual property through isolated network access controls and subscription authorization.

## Embedded ML models using Amazon SageMaker AI on AWS Marketplace diagram
<a name="embedded-ml-models-using-sagemaker-on-aws-marketplace-diagram"></a>

![A seller lists an ML model on AWS Marketplace and a buyer runs it privately using Amazon SageMaker AI and AWS Lambda.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/digital-marketing/images/embedded-ml-models-using-sagemaker-on-aws-marketplace.png)


The following steps describe the architecture:

1. The seller writes and packages their model code as a Docker image and pushes the image into [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) (Amazon ECR). 

1. The seller packages and pushes the image as machine learning (ML) model for listing on [AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/). 

1. The buyer subscribes to the listing on AWS Marketplace using AWS Management Console. 

1. Upon subscription, an [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) instance is provisioned in the buyer VPC in network isolation mode along with the model container image and the invocation endpoint. 

1. The buyer runs the [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) template that deploys the [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions from the ZIP file located in the [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) repository. 

1. The buyer application invokes a Lambda initialization endpoint to validate their subscription from the seller. 

1. Lambda authorizer invokes the Lambda function running in the seller's VPC to return authorization token valid for a certain duration. 

1. The buyer application invokes a Lambda /request endpoint along with an authorization token and the data to be processed. 

1. Lambda authorizer validates the authorization token and forwards the call to the Lambda proxy. 

1. Lambda proxy calls the SageMaker AI endpoint running in network isolation mode along with the data to be processed. 

1. SageMaker AI endpoint returns the response back to the Lambda function along with the processed data. 

1. Lambda stores the response in the Amazon S3 bucket for the buyer application to use. 

## Further reading
<a name="embedded-ml-models-using-sagemaker-on-aws-marketplace-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [AWS Well-Architected Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) 