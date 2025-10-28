# vpc-sg-port-restriction-check

Checks if security groups restrict incoming traffic to restricted ports explicitly from 0.0.0.0/0 or ::/0. The rule is NON_COMPLIANT if security groups allow incoming traffic from 0.0.0.0/0 or ::/0 over TCP/UDP ports 22/3389 or as specified in parameters.

**Identifier:** VPC_SG_PORT_RESTRICTION_CHECK

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

restrictPorts (Optional)
Type: CSV

Comma-separated list of ports that should not be open for incoming traffic over the full IP range. Valid port numbers range from 0 to 65535. If not specified, the rule defaults to check for 22 and 3389.

protocolType (Optional)
Type: String

The Transmission Protocol Type for the rule to check. Valid values include 'TCP', 'UDP', and 'ALL' (case-insensitive). If set to 'ALL', the rule will check for rules that use either 'TCP', 'UDP', or 'ALL' (-1) protocol. Default value is 'ALL'.

excludeExternalSecurityGroups (Optional)
Type: boolean

Boolean flag to exclude the evaluation of external security groups. If set to 'true', the rule will not include external security groups in the evaluation. Otherwise, all security groups are evaluated if value is set to 'false.' Default value is 'true'.

ipType (Optional)
Type: String

The Internet Protocol (IP) version for the rule to check. Valid values include 'IPv4', 'IPv6', and 'ALL' (case-insensitive). If not specified, the rule defaults to check for 'ALL'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
