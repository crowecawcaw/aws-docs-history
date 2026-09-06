

# appconfig-deployment-strategy-replicate-to-ssm
<a name="appconfig-deployment-strategy-replicate-to-ssm"></a>

Checks if AWS AppConfig deployment strategies save the deployment strategy to an AWS Systems Manager (SSM) document. The rule is NON\_COMPLIANT if configuration.ReplicateTo is not 'SSM\_DOCUMENT'. 



**Identifier:** APPCONFIG\_DEPLOYMENT\_STRATEGY\_REPLICATE\_TO\_SSM

**Resource Types:** AWS::AppConfig::DeploymentStrategy

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d101c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).