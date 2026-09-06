

# netfw-multi-az-enabled
<a name="netfw-multi-az-enabled"></a>

Checks if AWS Network Firewall firewalls are deployed across multiple Availability Zones. The rule is NON\_COMPLIANT if firewalls are deployed in only one Availability Zone or in fewer zones than the number listed in the optional parameter. 



**Identifier:** NETFW\_MULTI\_AZ\_ENABLED

**Resource Types:** AWS::NetworkFirewall::Firewall

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

availabilityZones (Optional)Type: int  
The number of expected Availability Zones.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1163c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).