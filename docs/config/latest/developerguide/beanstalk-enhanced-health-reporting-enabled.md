# beanstalk-enhanced-health-reporting-enabled

Checks if an AWS Elastic Beanstalk environment is configured for enhanced health reporting.
The rule is COMPLIANT if the environment is configured for enhanced health reporting.
The rule is NON\_COMPLIANT if the environment is configured for basic health reporting.

**Identifier:** BEANSTALK\_ENHANCED\_HEALTH\_REPORTING\_ENABLED

**Resource Types:** AWS::ElasticBeanstalk::Environment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
