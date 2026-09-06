

# autoscaling-group-elb-healthcheck-required
<a name="autoscaling-group-elb-healthcheck-required"></a>

Checks if your Amazon EC2 Auto Scaling groups that are associated with an Elastic Load Balancer use Elastic Load Balancing health checks. The rule is NON\_COMPLIANT if the Amazon EC2 Auto Scaling groups are not using Elastic Load Balancing health checks. 



**Identifier:** AUTOSCALING\_GROUP\_ELB\_HEALTHCHECK\_REQUIRED

**Resource Types:** AWS::AutoScaling::AutoScalingGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## Proactive Evaluation
<a name="w2aac20c16c17b7d233c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "LoadBalancerNames": "{{[my-load-balancer-1, my-load-balancer-2, my-load-balancer-3, ...]}}",
   "HealthCheckType": {{HealthCheckType}}*"
} 
...
```

\*The valid values are `EC2` (default), `ELB`, and `VPC_LATTICE`. The `VPC_LATTICE` health check type is reserved for use with VPC Lattice, which is in preview release and is subject to change. For more information, see [Health checks for Auto Scaling instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html) in the Amazon EC2 Auto Scaling User Guide.

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html). 

## AWS CloudFormation template
<a name="w2aac20c16c17b7d233c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).