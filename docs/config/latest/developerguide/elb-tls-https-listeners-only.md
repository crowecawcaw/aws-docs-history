

# elb-tls-https-listeners-only
<a name="elb-tls-https-listeners-only"></a>

Checks if your Classic Load Balancer is configured with SSL or HTTPS listeners. The rule is NON\_COMPLIANT if a listener is not configured with SSL or HTTPS. 
+ If the Classic Load Balancer does not have a listener configured, then the rule returns `NOT_APPLICABLE`.
+ The rule is COMPLIANT if the Classic Load Balancer listeners are configured with SSL or HTTPS.
+ The rule is NON\_COMPLIANT if a listener is not configured with SSL or HTTPS.

**Identifier:** ELB\_TLS\_HTTPS\_LISTENERS\_ONLY

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d803c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).