

# batch-managed-compute-env-allocation-strategy-check
<a name="batch-managed-compute-env-allocation-strategy-check"></a>

Checks if an AWS Batch managed compute environment is configured with a specified allocation strategy. The rule is NON\_COMPLIANT if the compute environment is not configured with an allocation strategy specified in the required rule parameter. 



**Identifier:** BATCH\_MANAGED\_COMPUTE\_ENV\_ALLOCATION\_STRATEGY\_CHECK

**Resource Types:** AWS::Batch::ComputeEnvironment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

allocationStrategyType: CSV  
Comma-separated list of allocation strategies for the rule to check. Valid values include: 'BEST\_FIT', 'BEST\_FIT\_PROGRESSIVE', 'SPOT\_CAPACITY\_OPTIMIZED', and 'SPOT\_PRICE\_CAPACITY\_OPTIMIZED'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d267c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).