

# vpc-vpn-2-tunnels-up
<a name="vpc-vpn-2-tunnels-up"></a>

Checks if both virtual private network (VPN) tunnels provided by AWS Site-to-Site VPN are in UP status. The rule is NON\_COMPLIANT if one or both tunnels are in DOWN status. 

**Note**  
Tunnel state transitions may take up to 24 hours to be detected.

**Identifier:** VPC\_VPN\_2\_TUNNELS\_UP

**Resource Types:** AWS::EC2::VPNConnection

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1613c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).