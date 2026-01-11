# elb-acm-certificate-required

Checks if the Classic Load Balancers use SSL certificates provided by AWS Certificate Manager.
To use this rule, use an SSL or HTTPS listener with your Classic Load Balancer.
This rule is only applicable to Classic Load Balancers. This rule does not check Application Load Balancers and Network Load Balancers.

**Identifier:** ELB_ACM_CERTIFICATE_REQUIRED

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Africa (Cape Town), Asia Pacific (Osaka), Europe (Milan), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
