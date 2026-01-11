# desired-instance-tenancy

Checks EC2 instances for a 'tenancy' value. Also checks if AMI IDs are specified to be launched from those AMIs or if Host IDs are launched on those Dedicated Hosts. The rule is COMPLIANT if the instance matches a host and an AMI, if specified, in a list.

**Identifier:** DESIRED_INSTANCE_TENANCY

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

tenancy
Type: String

Desired tenancy of the instances. Valid values are DEDICATED, HOST and DEFAULT

imageId (Optional)
Type: CSV

The rule evaluates instances launched only from AMIs with the specified IDs. Separate multiple AMI IDs with commas

hostId (Optional)
Type: CSV

The IDs of the EC2 Dedicated Hosts on which the instances are meant to be launched. Separate multiple Host IDs with commas

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
