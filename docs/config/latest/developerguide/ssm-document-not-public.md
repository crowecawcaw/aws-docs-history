

# ssm-document-not-public
<a name="ssm-document-not-public"></a>

Checks if AWS Systems Manager documents owned by the account are public. The rule is NON\_COMPLIANT if Systems Manager documents with the owner 'Self' are public. 



**Identifier:** SSM\_DOCUMENT\_NOT\_PUBLIC

**Resource Types:** AWS::SSM::Document

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1551c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).