# ec2-stopped-instance

Checks if there are Amazon Elastic Compute Cloud (Amazon EC2) instances stopped for more than the allowed number of days. The rule is NON_COMPLIANT if the state of an Amazon EC2 instance has been stopped for longer than the allowed number of days, or if the amount of time cannot be determined.

**Identifier:** EC2_STOPPED_INSTANCE

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

AllowedDays (Optional)
Type: int
Default: 30

The number of days an Amazon EC2 instance can be stopped before the rule is NON_COMPLIANT. The default number of days is 30.

###### Note

The number of days selected needs to be less than the configured retention period since this rule relies on the historical data collected.
For more information about historical data retention,
see [Deleting AWS Config Data](delete-config-data-with-retention-period.md "delete-config-data-with-retention-period.md").

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
