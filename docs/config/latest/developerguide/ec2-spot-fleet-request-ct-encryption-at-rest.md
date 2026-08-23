# ec2-spot-fleet-request-ct-encryption-at-rest

Checks if Amazon EC2 Spot Fleet request launch parameters set encrypted to True for attached EBS volumes. The rule is NON\_COMPLIANT if any EBS volumes has encrypted set to False. The rule does not evaluate spot fleet requests using launch templates.

**Identifier:** EC2\_SPOT\_FLEET\_REQUEST\_CT\_ENCRYPTION\_AT\_REST

**Resource Types:** AWS::EC2::SpotFleet

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
