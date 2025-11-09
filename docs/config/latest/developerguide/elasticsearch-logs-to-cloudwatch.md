# elasticsearch-logs-to-cloudwatch

Checks if Amazon OpenSearch Service domains are configured to send logs to Amazon CloudWatch Logs. The rule is COMPLIANT if a log is enabled for an Amazon ES domain. This rule is NON_COMPLIANT if logging is not configured.

**Identifier:** ELASTICSEARCH_LOGS_TO_CLOUDWATCH

**Resource Types:** AWS::Elasticsearch::Domain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

logTypes (Optional)
Type: CSV

Comma-separated list of logs that are enabled. Valid values are 'search', 'index', 'error'.

## Proactive Evaluation

For steps on how to run this rule in proactive mode,
see [Evaluating Your Resources with AWS Config Rules](evaluating-your-resources.md#evaluating-your-resources-proactive "evaluating-your-resources.md#evaluating-your-resources-proactive").
For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](../APIReference/API_StartResourceEvaluation.md "../APIReference/API_StartResourceEvaluation.md") API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
   "LogPublishingOptions": "`{Key : Value, ...}`"\*
}
...

```

\*An object with one or more of the following keys: `SEARCH_SLOW_LOGS`, `ES_APPLICATION_LOGS`, `INDEX_SLOW_LOGS`, `AUDIT_LOGS`, depending on the types of logs you want to publish. Each key needs a valid `LogPublishingOption` value.

For more information on proactive evaluation, see [Evaluation Mode](evaluate-config-rules.md "evaluate-config-rules.md").

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
