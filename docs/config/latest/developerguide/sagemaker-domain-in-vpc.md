

# sagemaker-domain-in-vpc
<a name="sagemaker-domain-in-vpc"></a>

Checks if an Amazon SageMaker domain uses a customer owned Amazon Virtual Private Cloud (VPC) for non-EFS traffic. The rule is NON\_COMPLIANT if configuration.AppNetworkAccessType is not set to VpcOnly. 



**Identifier:** SAGEMAKER\_DOMAIN\_IN\_VPC

**Resource Types:** AWS::SageMaker::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1441c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).