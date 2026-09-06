

# apprunner-service-no-public-access
<a name="apprunner-service-no-public-access"></a>

Checks if AWS AppRunner Services are not publicly accessible. The rule is NON\_COMPLIANT if service.configuration.NetworkConfiguration.IngressConfiguration.IsPubliclyAccessible is False. 



**Identifier:** APPRUNNER\_SERVICE\_NO\_PUBLIC\_ACCESS

**Resource Types:** AWS::AppRunner::Service

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d175c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).