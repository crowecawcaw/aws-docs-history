

# netfw-logging-enabled
<a name="netfw-logging-enabled"></a>

Checks if AWS Network Firewall firewalls have logging enabled. The rule is NON\_COMPLIANT if a logging type is not configured. You can specify which logging type you want the rule to check. 



**Identifier:** NETFW\_LOGGING\_ENABLED

**Resource Types:** AWS::NetworkFirewall::LoggingConfiguration

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

logType (Optional)Type: String  
logType (Optional): Log type for the rule to check for firewalls: 'alert', 'flow', or 'both'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1161c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).