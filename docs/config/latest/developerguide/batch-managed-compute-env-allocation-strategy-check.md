# batch-managed-compute-env-allocation-strategy-check

Checks if an AWS Batch managed compute environment is configured with a specified allocation strategy. The rule is NON_COMPLIANT if the compute environment is not configured with an allocation strategy specified in the required rule parameter.

**Identifier:** BATCH_MANAGED_COMPUTE_ENV_ALLOCATION_STRATEGY_CHECK

**Resource Types:** AWS::Batch::ComputeEnvironment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

allocationStrategy
Type: CSV

Comma-separated list of allocation strategies for the rule to check. Valid values include: 'BEST_FIT', 'BEST_FIT_PROGRESSIVE', 'SPOT_CAPACITY_OPTIMIZED', and 'SPOT_PRICE_CAPACITY_OPTIMIZED'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
