

# emr-security-configuration-encryption-transit
<a name="emr-security-configuration-encryption-transit"></a>

Checks if an Amazon EMR security configuration has encryption in transit enabled. The rule is NON\_COMPLIANT if configuration.SecurityConfiguration.EncryptionConfiguration.EnableInTransitEncryption is false. 



**Identifier:** EMR\_SECURITY\_CONFIGURATION\_ENCRYPTION\_TRANSIT

**Resource Types:** AWS::EMR::SecurityConfiguration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d813c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).