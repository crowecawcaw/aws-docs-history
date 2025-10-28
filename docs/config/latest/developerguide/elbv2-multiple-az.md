# elbv2-multiple-az

Checks if an Elastic Load Balancer V2 (Application, Network, or Gateway Load Balancer) is mapped to multiple Availability Zones (AZs).
The rule is NON_COMPLIANT if an Elastic Load Balancer V2 is mapped to less than 2 AZs.
For more information, see [Availability Zones for your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-subnets.md "../../../elasticloadbalancing/latest/application/load-balancer-subnets.md").

**Identifier:** ELBV2_MULTIPLE_AZ

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

minAvailabilityZones (Optional)
Type: int

Minimum number of expected AZs (between 2 and 10 inclusive).

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
