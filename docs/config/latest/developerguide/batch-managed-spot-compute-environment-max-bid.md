# batch-managed-spot-compute-environment-max-bid

Checks if an AWS Batch managed Spot compute environment is configured to have a bid percentage less than or equal to the specified value. The rule is NON_COMPLIANT if the bid percentage is greater than the value specified in the required rule parameter.

**Identifier:** BATCH_MANAGED_SPOT_COMPUTE_ENVIRONMENT_MAX_BID

**Resource Types:** AWS::Batch::ComputeEnvironment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

maxBidPercentage
Type: int

The maximum bid percentage value for the rule to check. The rule is NON_COMPLIANT if an AWS Batch managed Spot compute environment is configured with a bid percentage greater than this value. Valid values are 1 to 100.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
