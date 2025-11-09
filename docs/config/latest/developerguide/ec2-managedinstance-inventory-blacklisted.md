# ec2-managedinstance-inventory-blacklisted

Checks whether instances managed by Amazon EC2 Systems Manager are configured to collect blacklisted inventory types.

**Identifier:** EC2_MANAGEDINSTANCE_INVENTORY_BLACKLISTED

**Resource Types:** AWS::SSM::ManagedInstanceInventory

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Asia Pacific (Taipei) Region

**Parameters:**

inventoryNames
Type: CSV

Comma separated list of Systems Manager inventory types (for example, 'AWS:Network, AWS:WindowsUpdate').

platformType (Optional)
Type: String

Platform type (for example, 'Linux').

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
