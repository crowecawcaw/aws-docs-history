

# netfw-policy-rule-group-associated
<a name="netfw-policy-rule-group-associated"></a>

Check AWS Network Firewall policy is associated with stateful OR stateless rule groups. This rule is NON\_COMPLIANT if no stateful or stateless rule groups are associated with the Network Firewall policy else COMPLIANT if any one of the rule group exists. 



**Identifier:** NETFW\_POLICY\_RULE\_GROUP\_ASSOCIATED

**Resource Types:** AWS::NetworkFirewall::FirewallPolicy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1169c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).