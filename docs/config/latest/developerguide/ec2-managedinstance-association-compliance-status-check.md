# ec2-managedinstance-association-compliance-status-check

Checks if the status of the AWS Systems Manager association compliance is COMPLIANT or NON_COMPLIANT after the association execution on the instance. The rule is compliant if the field status is COMPLIANT.
For more information about associations, see [What is an association?](../../../systems-manager/latest/userguide/systems-manager-state.md#state-manager-association-what-is "../../../systems-manager/latest/userguide/systems-manager-state.md#state-manager-association-what-is").

**Identifier:** EC2_MANAGEDINSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK

**Resource Types:** AWS::SSM::AssociationCompliance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Osaka), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
