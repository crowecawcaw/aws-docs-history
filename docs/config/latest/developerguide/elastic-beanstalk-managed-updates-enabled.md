# elastic-beanstalk-managed-updates-enabled

Checks if managed platform updates in an AWS Elastic Beanstalk environment is enabled.
The rule is COMPLIANT if the value for `ManagedActionsEnabled` is set to true.
The rule is NON_COMPLIANT if the value for `ManagedActionsEnabled` is set to false, or if a parameter is provided and its value does not match the existing configurations.

**Identifier:** ELASTIC_BEANSTALK_MANAGED_UPDATES_ENABLED

**Resource Types:** AWS::ElasticBeanstalk::Environment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Zurich) Region

**Parameters:**

UpdateLevel (Optional)
Type: String

Indicates whether update levels are set to 'minor' version updates or a 'patch' version updates.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
