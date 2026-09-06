

# elbv2-multiple-az
<a name="elbv2-multiple-az"></a>

Checks if an Elastic Load Balancer V2 (Application, Network, or Gateway Load Balancer) is mapped to multiple Availability Zones (AZs). The rule is NON\_COMPLIANT if an Elastic Load Balancer V2 is mapped to less than 2 AZs. For more information, see [Availability Zones for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html).



**Identifier:** ELBV2\_MULTIPLE\_AZ

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West) Region

**Parameters:**

minAvailabilityZones (Optional)Type: int  
Minimum number of expected AZs (between 2 and 10 inclusive).

## AWS CloudFormation template
<a name="w2aac20c16c17b7d779c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).