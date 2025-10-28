# alb-waf-enabled

Checks if AWS WAF is enabled on Application Load Balancers (ALBs). The rule is NON_COMPLIANT if key: waf.enabled is set to false.

**Identifier:** ALB_WAF_ENABLED

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Asia Pacific (Osaka) Region

**Parameters:**

wafWebAclIds (Optional)
Type: CSV

Comma separated list of web ACL ID (for WAF) or web ACL ARN (for WAFV2) checking for ALB association.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
