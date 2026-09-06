

# appconfig-configuration-profile-validators-not-empty
<a name="appconfig-configuration-profile-validators-not-empty"></a>

Checks if an AWS AppConfig configuration profile includes at least one validator for syntactic or semantic check to ensure the configuration deploy functions as intended. The rule is NON\_COMPLIANT if the Validators property is an empty array. 



**Identifier:** APPCONFIG\_CONFIGURATION\_PROFILE\_VALIDATORS\_NOT\_EMPTY

**Resource Types:** AWS::AppConfig::ConfigurationProfile

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7c95c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).