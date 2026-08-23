# transfer-family-server-no-ftp

Checks if a server created with AWS Transfer Family uses FTP for endpoint connection. The rule is NON\_COMPLIANT if the server protocol for endpoint connection is FTP-enabled.

**Identifier:** TRANSFER\_FAMILY\_SERVER\_NO\_FTP

**Resource Types:** AWS::Transfer::Server

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
