

# sagemaker-data-quality-job-encrypt-in-transit
<a name="sagemaker-data-quality-job-encrypt-in-transit"></a>

Checks if Amazon SageMaker data quality job definitions have inter-container traffic encryption enabled when the instance count is 2 or greater. The rule is NON\_COMPLIANT if configuration.NetworkConfig.EnableInterContainerTrafficEncryption is false. 



**Identifier:** SAGEMAKER\_DATA\_QUALITY\_JOB\_ENCRYPT\_IN\_TRANSIT

**Resource Types:** AWS::SageMaker::DataQualityJobDefinition

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Middle East (Bahrain), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1437c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).