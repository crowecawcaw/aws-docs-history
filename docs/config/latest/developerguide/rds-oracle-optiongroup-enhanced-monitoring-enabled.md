

# rds-oracle-optiongroup-enhanced-monitoring-enabled
<a name="rds-oracle-optiongroup-enhanced-monitoring-enabled"></a>

Checks if Amazon RDS Oracle option groups have enhanced monitoring enabled. The rule is NON\_COMPLIANT if configuration.item.OptionName is not equal to 'OEM\_AGENT' or 'STATSPACK'. 



**Identifier:** RDS\_ORACLE\_OPTIONGROUP\_ENHANCED\_MONITORING\_ENABLED

**Resource Types:** AWS::RDS::OptionGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), Asia Pacific (Thailand), Middle East (UAE), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1291c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).