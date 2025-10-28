# ec2-spot-fleet-request-ct-encryption-at-rest

Checks if Amazon EC2 Spot Fleet request launch parameters set encrypted to True for attached EBS volumes. The rule is NON_COMPLIANT if any EBS volumes has encrypted set to False. The rule does not evaluate spot fleet requests using launch templates.

**Identifier:** EC2_SPOT_FLEET_REQUEST_CT_ENCRYPTION_AT_REST

**Resource Types:** AWS::EC2::SpotFleet

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Ireland), US East (N. Virginia), Asia Pacific (Seoul), US West (Oregon), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
