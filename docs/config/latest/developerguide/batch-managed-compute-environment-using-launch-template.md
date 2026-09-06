

# batch-managed-compute-environment-using-launch-template
<a name="batch-managed-compute-environment-using-launch-template"></a>

Checks if AWS Batch managed compute environments are configured using a launch template. The rule is NON\_COMPLIANT if configuration.ComputeResources.LaunchTemplate does not exist. 



**Identifier:** BATCH\_MANAGED\_COMPUTE\_ENVIRONMENT\_USING\_LAUNCH\_TEMPLATE

**Resource Types:** AWS::Batch::ComputeEnvironment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d265c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).