

# elbv2-targetgroup-healthcheck-protocol-encrypted
<a name="elbv2-targetgroup-healthcheck-protocol-encrypted"></a>

Checks the target groups for load balancers healthchecks use an encrypted transport protocol. The rule is NON\_COMPLIANT if configuration.healthCheckProtocol is not HTTPS. Lambda target types are not applicable. 



**Identifier:** ELBV2\_TARGETGROUP\_HEALTHCHECK\_PROTOCOL\_ENCRYPTED

**Resource Types:** AWS::ElasticLoadBalancingV2::TargetGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d783c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).