# clb-desync-mode-check

Checks if Classic Load Balancers (CLB) are configured with a user defined Desync mitigation mode. The rule is NON\_COMPLIANT if CLB Desync mitigation mode does not match with user defined Desync mitigation mode.

**Identifier:** CLB\_DESYNC\_MODE\_CHECK

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

desyncMode
Type: CSV

Comma-separated list of values. You can select a max of two. Valid values include 'Defensive', 'Strictest', and 'Monitor'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
