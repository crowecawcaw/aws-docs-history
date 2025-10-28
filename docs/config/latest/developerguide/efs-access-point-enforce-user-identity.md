# efs-access-point-enforce-user-identity

Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a user identity. The rule is NON_COMPLIANT if 'PosixUser' is not defined or if parameters are provided and there is no match in the corresponding parameter.

**Identifier:** EFS_ACCESS_POINT_ENFORCE_USER_IDENTITY

**Resource Types:** AWS::EFS::AccessPoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

approvedUids (Optional)
Type: CSV

Comma-separated list of POSIX user ID that are approved for EFS access point user enforcement.

approvedGids (Optional)
Type: CSV

Comma-separated list of POSIX group IDs that are approved for EFS access point user enforcement.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
