# autoscaling-group-elb-healthcheck-required

Checks if your Amazon EC2 Auto Scaling groups that are associated with an Elastic Load Balancer use Elastic Load Balancing health checks. The rule is NON_COMPLIANT if the Amazon EC2 Auto Scaling groups are not using Elastic Load Balancing health checks.

**Identifier:** AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED

**Resource Types:** AWS::AutoScaling::AutoScalingGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

None

## Proactive Evaluation

For steps on how to run this rule in proactive mode,
see [Evaluating Your Resources with AWS Config Rules](evaluating-your-resources.md#evaluating-your-resources-proactive "evaluating-your-resources.md#evaluating-your-resources-proactive").
For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](../APIReference/API_StartResourceEvaluation.md "../APIReference/API_StartResourceEvaluation.md") API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
   "LoadBalancerNames": "`[my-load-balancer-1, my-load-balancer-2, my-load-balancer-3, ...]`",
   "HealthCheckType": `HealthCheckType`\*"
}
...

```

\*The valid values are `EC2` (default), `ELB`, and `VPC_LATTICE`. The `VPC_LATTICE` health check type is reserved for use with VPC Lattice, which is in preview release and is subject to change.
For more information, see [Health checks for Auto Scaling instances](../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md") in the Amazon EC2 Auto Scaling User Guide.

For more information on proactive evaluation, see [Evaluation Mode](evaluate-config-rules.md "evaluate-config-rules.md").

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
