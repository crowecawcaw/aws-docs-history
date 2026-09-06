

# elasticsearch-node-to-node-encryption-check
<a name="elasticsearch-node-to-node-encryption-check"></a>

Check that Amazon OpenSearch Service nodes are encrypted end to end. The rule is NON\_COMPLIANT if the node-to-node encryption is disabled on the domain. 



**Identifier:** ELASTICSEARCH\_NODE\_TO\_NODE\_ENCRYPTION\_CHECK

**Resource Types:** AWS::Elasticsearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## Proactive Evaluation
<a name="w2aac20c16c17b7d769c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "NodeToNodeEncryptionOptions": {{BOOLEAN}}
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html). 

## AWS CloudFormation template
<a name="w2aac20c16c17b7d769c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).