

# elb-predefined-security-policy-ssl-check
<a name="elb-predefined-security-policy-ssl-check"></a>

Checks if your Classic Load Balancer SSL listeners use a predefined policy. The rule is NON\_COMPLIANT if the Classic Load Balancer HTTPS/SSL listener's policy does not equal the value of the parameter '`predefinedPolicyName`'. 



**Identifier:** ELB\_PREDEFINED\_SECURITY\_POLICY\_SSL\_CHECK

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

predefinedPolicyNameType: String  
Name of the predefined policy.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d799c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).