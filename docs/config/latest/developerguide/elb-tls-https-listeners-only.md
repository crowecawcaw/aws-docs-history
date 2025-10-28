# elb-tls-https-listeners-only

Checks if your Classic Load Balancer is configured with SSL or HTTPS listeners. The rule is NON_COMPLIANT if a listener is not configured with SSL or HTTPS.

- If the Classic Load Balancer does not have a listener configured, then the rule returns `NOT_APPLICABLE`.
- The rule is COMPLIANT if the Classic Load Balancer listeners are configured with SSL or HTTPS.
- The rule is NON_COMPLIANT if a listener is not configured with SSL or HTTPS.
  **Identifier:** ELB_TLS_HTTPS_LISTENERS_ONLY

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (UAE), AWS Secret - West, Asia Pacific (Osaka) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
