

# rds-enhanced-monitoring-enabled
<a name="rds-enhanced-monitoring-enabled"></a>

Checks if enhanced monitoring is enabled for Amazon RDS instances. This rule is NON\_COMPLIANT if '`monitoringInterval`' is '0' in the configuration item of the RDS instance, or if '`monitoringInterval`' does not match the rule parameter value. 



**Identifier:** RDS\_ENHANCED\_MONITORING\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

monitoringInterval (Optional)Type: int  
An integer value in seconds between points when enhanced monitoring metrics are collected for the database instance. The valid values are 1, 5, 10, 15, 30, and 60.

## Proactive Evaluation
<a name="w2aac20c16c17b7e1237c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
    "MonitoringInterval": {{Integer}}*,
    "Engine": {{String}}*
} 
...
```

\*For more information on valid values for these inputs, see [MonitoringInterval](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-monitoringinterval) and [Engine](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-engine) in the AWS CloudFormation User Guide.

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html). 

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1237c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).