

# apprunner-service-in-vpc
<a name="apprunner-service-in-vpc"></a>

Checks if AWS App Runner services route egress traffic through custom VPC. The rule is NON\_COMPLIANT if configuration.NetworkConfiguration.EgressConfiguration.EgressType is equal to DEFAULT. 



**Identifier:** APPRUNNER\_SERVICE\_IN\_VPC

**Resource Types:** AWS::AppRunner::Service

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d169c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).