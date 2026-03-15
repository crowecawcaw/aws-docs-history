# elbv2-targetgroup-protocol-encrypted

Checks the target groups for application and network load balancers use an encrypted transport protocol. The rule is NON_COMPLIANT if configuration.protocol is not HTTPS, TLS, or QUIC. Lambda and ALB target types are not applicable.

**Identifier:** ELBV2_TARGETGROUP_PROTOCOL_ENCRYPTED

**Resource Types:** AWS::ElasticLoadBalancingV2::TargetGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
