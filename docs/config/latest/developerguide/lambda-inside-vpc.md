

# lambda-inside-vpc
<a name="lambda-inside-vpc"></a>

Checks if a Lambda function is allowed access to a virtual private cloud (VPC). The rule is NON\_COMPLIANT if the Lambda function is not VPC enabled. 



**Identifier:** LAMBDA\_INSIDE\_VPC

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Ningxia) Region

**Parameters:**

subnetIds (Optional)Type: CSV  
Comma-separated list of subnet IDs that Lambda functions must be associated with.

## Proactive Evaluation
<a name="w2aac20c16c17b7e1075c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "VpcConfig": {
         "SubnetIds": "{{[SubnetId-1, SubnetId-2, SubnetId-3, ...]}}"
   }
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html). 

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1075c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).