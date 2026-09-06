

# elasticsearch-logs-to-cloudwatch
<a name="elasticsearch-logs-to-cloudwatch"></a>

Checks if OpenSearch Service (previously called Elasticsearch) domains are configured to send logs to CloudWatch Logs. The rule is COMPLIANT if a log is enabled for an OpenSearch Service domain. The rule is NON\_COMPLIANT if logging is not configured. 



**Identifier:** ELASTICSEARCH\_LOGS\_TO\_CLOUDWATCH

**Resource Types:** AWS::Elasticsearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

logTypes (Optional)Type: CSV  
Comma-separated list of logs that are enabled. Valid values are 'search', 'index', 'error'

## Proactive Evaluation
<a name="w2aac20c16c17b7d767c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive). For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "LogPublishingOptions": "{{{Key : Value, ...}}}"*
} 
...
```

\*An object with one or more of the following keys: `SEARCH_SLOW_LOGS`, `ES_APPLICATION_LOGS`, `INDEX_SLOW_LOGS`, `AUDIT_LOGS`, depending on the types of logs you want to publish. Each key needs a valid `LogPublishingOption` value.

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html). 

## AWS CloudFormation template
<a name="w2aac20c16c17b7d767c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).