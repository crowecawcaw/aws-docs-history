

# codepipeline-deployment-count-check
<a name="codepipeline-deployment-count-check"></a>

Checks if the first deployment stage of AWS CodePipeline performs more than one deployment. Optionally checks if each of the subsequent remaining stages deploy to more than the specified number of deployments (`deploymentLimit`). 



**Identifier:** CODEPIPELINE\_DEPLOYMENT\_COUNT\_CHECK

**Resource Types:** AWS::CodePipeline::Pipeline

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Asia Pacific (Osaka), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

deploymentLimit (Optional)Type: int  
The maximum number of deployments each stage can perform.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d405c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).