# sagemaker-notebook-no-direct-internet-access

Checks if direct internet access is disabled for an Amazon SageMaker notebook instance. The rule is NON_COMPLIANT if a SageMaker notebook instance is internet-enabled.

**Identifier:** SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS

**Resource Types:** AWS::SageMaker::NotebookInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), AWS Secret - West, Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
