# subnet-auto-assign-public-ip-disabled

Checks if Amazon Virtual Private Cloud (Amazon VPC) subnets are assigned a public IP address.
The rule is COMPLIANT if Amazon VPC does not have subnets that are assigned a public IP address.
The rule is NON_COMPLIANT if Amazon VPC has subnets that are assigned a public IP address.

**Identifier:** SUBNET_AUTO_ASSIGN_PUBLIC_IP_DISABLED

**Resource Types:** AWS::EC2::Subnet

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

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
   "MapPublicIpOnLaunch": `BOOLEAN`
}
...

```

For more information on proactive evaluation, see [Evaluation Mode](evaluate-config-rules.md "evaluate-config-rules.md").

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
