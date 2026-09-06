

# appconfig-freeform-profile-config-storage
<a name="appconfig-freeform-profile-config-storage"></a>

Checks if freeform configuration profiles for AWS AppConfig store their configuration data in AWS Secrets Manager or AWS AppConfig hosted configuration store. The rule is NON\_COMPLIANT if configuration.LocationUri is not secretsmanager or hosted. 



**Identifier:** APPCONFIG\_FREEFORM\_PROFILE\_CONFIG\_STORAGE

**Resource Types:** AWS::AppConfig::ConfigurationProfile

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d111c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).