

# subnet-auto-assign-public-ip-disabled
<a name="subnet-auto-assign-public-ip-disabled"></a>

Checks if Amazon Virtual Private Cloud (Amazon VPC) subnets are configured to automatically assign public IP addresses to instances launched within them. This rule is COMPLIANT if subnets do not auto-assign public IPv4 or IPv6 addresses. This rule is NON\_COMPLIANT if subnets auto-assign public IPv4 or IPv6 addresses.

**Warning**  
This rule does not distinguish between private and public Global Unicast Address (GUA) IPv6 ranges and will treat all GUA ranges as violations when auto-assignment is enabled.



**Identifier:** SUBNET\_AUTO\_ASSIGN\_PUBLIC\_IP\_DISABLED

**Resource Types:** AWS::EC2::Subnet

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## Proactive Evaluation
<a name="w2aac20c16c17b7e1565c21"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "MapPublicIpOnLaunch": {{BOOLEAN}}
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html). 

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1565c23"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).