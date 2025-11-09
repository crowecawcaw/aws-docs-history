# ebs-in-backup-plan

Check if Amazon Elastic Block Store (Amazon EBS) volumes are added in backup plans of AWS Backup. The rule is NON_COMPLIANT if Amazon EBS volumes are not included in backup plans.

**Identifier:** EBS_IN_BACKUP_PLAN

**Resource Types:** AWS::EC2::Volume

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
