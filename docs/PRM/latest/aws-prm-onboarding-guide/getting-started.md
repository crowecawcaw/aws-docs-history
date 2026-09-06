

# Getting started with Partner Revenue Measurement
<a name="getting-started"></a>

Partner Revenue Measurement measures AWS service consumption driven by partner products. This enables AWS to attribute revenue to partner solutions and provide aggregated consumption data back to partners.

Partner Revenue Measurement supports three implementation methods:
+ [AWS Marketplace Metering](marketplace-metering.md) — Zero-touch revenue attribution for Amazon Machine Image (AMI) and Machine Learning (ML) products listed on AWS Marketplace
+ [Resource Tagging](resource-tagging.md) — Tag AWS resources with your product code for revenue attribution
+ [User Agent String](user-agent-string.md) — Include a User Agent string in regular AWS API/CLI calls for revenue attribution

To implement Partner Revenue Measurement, consider the following requirements:


+ What AWS services does your product use (Amazon EC2, Amazon S3, Amazon ECS, Amazon RDS)?
+ Do you have a SaaS, AMI, ML, or Professional Services product listed on AWS Marketplace?
+ Which architecture pattern does your solution follow (Partner account, Customer account, or Hybrid)?



**Note**  
Partner Revenue Measurement requires implementation of one or more methods to enable revenue attribution for [supported AWS services](included-aws-services.md).

## Partner Revenue Measurement Architecture Patterns
<a name="prm-architecture-patterns"></a>

**Pattern \#1 - Partner Account:** All components reside within the partner's AWS account or VPC.

**Pattern \#2 - Customer Account:** All components are deployed in the customer's AWS account and VPC.

**Pattern \#3 - Hybrid:** Components are distributed across both partner and customer AWS accounts and VPCs.



![Partner Revenue Measurement architecture patterns showing partner account, customer account, and hybrid deployment models](http://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/images/PRM-architecture-patterns.png)




## Implementation Steps
<a name="implementation-steps"></a>

**Partner Revenue Measurement Implementation Process**

1. **Step 1: Complete Prerequisites**

   Review [Prerequisites](resource-tagging-prerequisites.md)

1. **Step 2: Retrieve Product Code**

   [Retrieve your product code from AWS Marketplace Management Portal](product-code-retrieval.md)

1. **Step 3: Choose Implementation Method**

   Select one or more [implementation methods](implementation-methods.md) based on your product type and architecture

1. **Step 4: Complete Method-Specific Requirements and Implement**

   Review the method-specific requirements for your chosen method, then follow the implementation guide. For a low-effort approach at scale, consider using [automation](automation.md) where available.