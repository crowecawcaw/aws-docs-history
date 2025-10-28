# ec2-managedinstance-patch-compliance-status-check

Checks if the compliance status of the AWS Systems Manager patch compliance is COMPLIANT or NON_COMPLIANT after the patch installation on the instance. The rule is compliant if the field status is COMPLIANT.

**Identifier:** EC2_MANAGEDINSTANCE_PATCH_COMPLIANCE_STATUS_CHECK

**Resource Types:** AWS::SSM::PatchCompliance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Asia Pacific (Osaka), Europe (Milan), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
