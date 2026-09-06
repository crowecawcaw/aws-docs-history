

# appsync-logging-enabled
<a name="appsync-logging-enabled"></a>

Checks if an AWS AppSync API has field level logging enabled. The rule is NON\_COMPLIANT if field level logging is not enabled, or if the field logging levels for the AppSync API do not match the values specified in the '`fieldLoggingLevel`' parameter. 



**Identifier:** APPSYNC\_LOGGING\_ENABLED

**Resource Types:** AWS::AppSync::GraphQLApi

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

fieldLoggingLevel (Optional)Type: CSV  
Comma-separated list of field logging levels for the rule to check. For example, "ERROR, INFO".

## AWS CloudFormation template
<a name="w2aac20c16c17b7d197c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).