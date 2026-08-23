# rds-instance-subnet-igw-check

Checks if RDS DB instances are deployed in a public subnet with a route to the internet gateway. The rule is NON\_COMPLIANT if RDS DB instances is deployed in a public subnet

**Identifier:** RDS\_INSTANCE\_SUBNET\_IGW\_CHECK

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
