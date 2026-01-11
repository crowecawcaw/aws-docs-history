# ssm-document-not-public

Checks if AWS Systems Manager documents owned by the account are public. The rule is NON_COMPLIANT if Systems Manager documents with the owner 'Self' are public.

**Identifier:** SSM_DOCUMENT_NOT_PUBLIC

**Resource Types:** AWS::SSM::Document

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
