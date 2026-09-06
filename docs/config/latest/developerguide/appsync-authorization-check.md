

# appsync-authorization-check
<a name="appsync-authorization-check"></a>

Checks if an AWS AppSync API is using allowed authorization mechanisms. The rule is NON\_COMPLIANT if an unapproved authorization mechanism is being used. 



**Identifier:** APPSYNC\_AUTHORIZATION\_CHECK

**Resource Types:** AWS::AppSync::GraphQLApi

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

AllowedAuthorizationTypesType: CSV  
Comma-separated list of allowed AWS AppSync authorization mechanisms. Allowed values are: 'API\_KEY', 'AWS\_LAMBDA', 'AWS\_IAM', 'OPENID\_CONNECT', 'AMAZON\_COGNITO\_USER\_POOLS'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d187c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).