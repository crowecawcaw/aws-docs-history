

# Enabling transitive matching (API)
<a name="enable-transitive-matching"></a>

**Important**  
Transitive matching is an API-only feature. You cannot enable transitive matching through the AWS Entity Resolution console.

To use transitive matching, you must create a new matching workflow with the Advanced rule type using the `CreateMatchingWorkflow` API. You cannot add transitive matching to an existing workflow.

Include the `matchingConfig` parameter with `enableTransitiveMatching` set to `true` in the request body. The following example shows a complete `CreateMatchingWorkflow` request body with transitive matching enabled:

```
{
   "workflowName": "{{my-transitive-workflow}}",
   "inputSourceConfig": [
      {
         "inputSourceARN": "{{arn:aws:glue:us-east-1:123456789012:table/my-database/my-table}}",
         "schemaName": "{{my-schema}}",
         "applyNormalization": true
      }
   ],
   "outputSourceConfig": [
      {
         "outputS3Path": "{{s3://my-bucket/output/}}",
         "output": [
            {
               "name": "{{name}}",
               "hashed": false
            }
         ]
      }
   ],
   "resolutionTechniques": {
      "resolutionType": "RULE_MATCHING",
      "ruleConditionProperties": {
         "rules": [
            {
               "ruleName": "{{Rule1}}",
               "condition": "{{Exact(Email) AND Exact(Phone)}}"
            },
            {
               "ruleName": "{{Rule2}}",
               "condition": "{{Exact(Name) AND Exact(Address)}}"
            }
         ]
      }
   },
   "matchingConfig": {
      "enableTransitiveMatching": true
   },
   "roleArn": "{{arn:aws:iam::123456789012:role/my-er-role}}"
}
```

**Important**  
The `enableTransitiveMatching` parameter is immutable. You can only set this parameter during workflow creation and you cannot change it afterward.