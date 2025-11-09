# elb-custom-security-policy-ssl-check

Checks whether your Classic Load Balancer SSL listeners are using a custom policy. The rule is only applicable if there are SSL listeners for the Classic Load Balancer.

**Identifier:** ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

sslProtocolsAndCiphers
Type: String

Comma separated list of ciphers and protocols.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
