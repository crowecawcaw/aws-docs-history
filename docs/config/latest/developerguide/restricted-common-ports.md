# restricted-common-ports

###### Important

For this rule, the rule identifier (RESTRICTED_INCOMING_TRAFFIC) and rule name (restricted-common-ports) are different.

Checks if the security groups in use do not allow unrestricted incoming Transmission Control Protocol (TCP) traffic to specified ports. The rule is COMPLIANT if:

- Port access is blocked to all TCP traffic.
- Port access is open to TCP traffic through Inbound rules, where the source is either a single IPv4 address or a range of IPv4 addresses in CIDR notation which does not cover all IPv4 addresses ("0.0.0.0/0").
- Port access is open to TCP traffic through Inbound rules, where the source is either a single IPv6 address or a range of IPv6 addresses in CIDR notation which does not cover all IPv6 addresses ("::/0)").
  The rule is NON_COMPLIANT if IP addresses for inbound TCP connections are not restricted to specified ports.

**Identifier:** RESTRICTED_INCOMING_TRAFFIC

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

blockedPort1 (Optional)
Type: int
Default: 20

Blocked TCP port number. The default of 20 corresponds to File Transfer Protocol (FTP) Data Transfer.

blockedPort2 (Optional)
Type: int
Default: 21

Blocked TCP port number. The default of 21 corresponds to File Transfer Protocol (FTP) Command Control.

blockedPort3 (Optional)
Type: int
Default: 3389

Blocked TCP port number. The default of 3389 corresponds to Remote Desktop Protocol (RDP).

blockedPort4 (Optional)
Type: int
Default: 3306

Blocked TCP port number. The default of 3306 corresponds to MySQL protocol.

blockedPort5 (Optional)
Type: int

Blocked TCP port number. Used for a specific port relevant for your environment.

blockedPorts (Optional)
Type: CSV

Comma-separated list of blocked TCP port numbers. For example: 20, 21, 3306, 3389.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
