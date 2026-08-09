# ec2-volume-inuse-check

Checks if EBS volumes are attached to EC2 instances. Optionally checks if EBS volumes are marked for deletion when an instance is terminated. The rule is COMPLIANT if an EBS volume is attached to running or stopped EC2 instances. The rule is NON\_COMPLIANT if an EBS volume is not attached to any EC2 instance or is attached to a terminated EC2 instance. This rule may briefly report a transient NON\_COMPLIANT status shortly after EC2 instance lifecycle events. This transient evaluation self-corrects when AWS Config re-evaluates the resource after EC2 completes the state propagation.

**Identifier:** EC2\_VOLUME\_INUSE\_CHECK

**Resource Types:** AWS::EC2::Volume

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

deleteOnTermination (Optional)
Type: boolean

EBS volumes are marked for deletion when an instance is terminated. Possible values: True or False (other input values are marked as NON\_COMPLIANT).
If set to `True`, the rule is NON\_COMPLIANT if a terminated EBS volume is not marked for deletion.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
