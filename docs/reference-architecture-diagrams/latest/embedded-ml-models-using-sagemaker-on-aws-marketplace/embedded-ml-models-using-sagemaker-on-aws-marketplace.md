

# Embedded ML models using Amazon SageMaker AI on AWS Marketplace
<a name="embedded-ml-models-using-sagemaker-on-aws-marketplace"></a>

Publication date: **August 17, 2022 ([Diagram history](#diagram-history))**

This architecture creates an environment where a buyer can consume a seller’s application into their own virtual private cloud (VPC), protecting the buyer’s data privacy while also protecting the seller’s application intellectual property through isolated network access controls and subscription authorization.

## Embedded ML models using Amazon SageMaker AI on AWS Marketplace Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how you can use Amazon SageMaker AI on AWS Marketplace.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/embedded-ml-models-using-sagemaker-on-aws-marketplace/images/embedded-ml-models-using-sagemaker-on-aws-marketplace.png)


1. Seller writes and packages their model code as a docker image and pushes the image into **Amazon Elastic Container Registry** (Amazon ECR). 

1. Seller packages and pushes the image as machine learning (ML) model for listing on **AWS Marketplace**. 

1. Buyer subscribes to the listing on **AWS Marketplace** using **AWS Management Console**. 

1. Upon subscription, an **Amazon SageMaker AI** instance is provisioned in the buyer VPC in network isolation mode along with the model container image and the invocation endpoint. 

1. Buyer runs the CFN template that deploys the **AWS Lambda** functions from the zip file located in the **Amazon Simple Storage Service** (Amazon S3) repository. 

1. Buyer application invokes a **Lambda** initialization endpoint to validate their subscription from the seller. 

1. **Lambda** authorizer invokes the **Lambda** function running in the seller’s VPC to return authorization token valid for a certain duration. 

1. Buyer application invokes a **Lambda** /request endpoint along with an authorization token and the data to be processed. 

1. **Lambda** authorizer validates the authorization token and forwards the call to the **Lambda** proxy. 

1. **Lambda** proxy calls the **SageMaker AI** endpoint running in network isolation mode along with the data to be processed. 

1. **SageMaker AI** endpoint returns the response back to the **Lambda** function along with the processed data. 

1. **Lambda** stores the response in the **Amazon S3** bucket for the buyer application to use. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [AWS Well-Architected Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 17, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.