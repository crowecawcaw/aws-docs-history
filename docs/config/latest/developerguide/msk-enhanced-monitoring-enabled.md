

# msk-enhanced-monitoring-enabled
<a name="msk-enhanced-monitoring-enabled"></a>

Checks if enhanced monitoring is enabled for an Amazon MSK cluster set to PER\_TOPIC\_PER\_BROKER or PER\_TOPIC\_PER\_PARTITION. The rule is NON\_COMPLIANT if enhanced monitoring is enabled and set to DEFAULT or PER\_BROKER. 



**Identifier:** MSK\_ENHANCED\_MONITORING\_ENABLED

**Resource Types:** AWS::MSK::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1129c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).