

# sagemaker-model-private-registry-required
<a name="sagemaker-model-private-registry-required"></a>

Checks if Amazon SageMaker models that use a PrimaryContainer pull container image from a private Docker registry in a VPC. The rule is NON\_COMPLIANT if ImageConfig is missing or RepositoryAccessMode is set to Platform. 



**Identifier:** SAGEMAKER\_MODEL\_PRIVATE\_REGISTRY\_REQUIRED

**Resource Types:** AWS::SageMaker::Model

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Africa (Cape Town), Europe (Ireland), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Europe (Milan), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1483c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).