

# amplify-branch-framework-configured
<a name="amplify-branch-framework-configured"></a>

Checks if AWS Amplify branches have a framework configured. The rule is NON\_COMPLIANT if configuration.Framework does not exist. 



**Identifier:** AMPLIFY\_BRANCH\_FRAMEWORK\_CONFIGURED

**Resource Types:** AWS::Amplify::Branch

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

approvedFrameworks (Optional)Type: CSV  
Comma-separated list of approved frameworks for the rule to check. If provided, the rule is NON\_COMPLIANT if configuration.Framework is a value not specified in this parameter.

## AWS CloudFormation template
<a name="w2aac20c16c17b7c49c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).