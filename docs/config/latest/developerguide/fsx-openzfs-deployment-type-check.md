# fsx-openzfs-deployment-type-check

Checks if the Amazon FSx for OpenZFS file systems are configured with certain deployment types. The rule is NON\_COMPLIANT if FSx for OpenZFS file systems are not configured with the deployment types you specify.

**Identifier:** FSX\_OPENZFS\_DEPLOYMENT\_TYPE\_CHECK

**Resource Types:** AWS::FSx::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Melbourne), Canada West (Calgary) Region

**Parameters:**

deploymentTypes
Type: CSV

Comma-separated list of allowed Deployment types for the rule to check.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
