# Example analysis logs

The following examples show representative analysis log entries. The examples use
fictional identifiers.

###### Example Query log when an analysis runs

```
{
  "eventId": "ffffffff-0000-4111-8222-333333333333",
  "eventTimestamp": 1723392245000,
  "collaborationId": "11111111-2222-4333-8444-555555555555",
  "logStage": "SUBMISSION",
  "analysisCategory": "SQL",
  "analysisCategoryVersion": "1.0",
  "schemaName": "publisher-conversions",
  "configuredTableId": "99999999-aaaa-4bbb-8ccc-dddddddddddd",
  "analysisTemplateArn": "arn:aws:cleanrooms:us-east-1:444455556666:membership/66666666-7777-4888-8999-aaaaaaaaaaaa/analysistemplate/77777777-8888-4999-8aaa-bbbbbbbbbbbb",
  "parameters": "{\"minimum_overlap\":\"100\"}",
  "queryText": "SELECT COUNT(*) FROM publisher_conversions WHERE overlap >= :minimum_overlap",
  "directQueryAnalysisRuleType": "AGGREGATION",
  "directQueryAnalysisRulePolicy": "{\"v1\":{\"custom\":{\"allowedAnalyses\":[\"arn:aws:cleanrooms:us-east-1:444455556666:membership/66666666-7777-4888-8999-aaaaaaaaaaaa/analysistemplate/77777777-8888-4999-8aaa-bbbbbbbbbbbb\"]}}}",
  "queryValidationErrors": null,
  "resultReceivers": "[\"444455556666\"]",
  "queryRunners": "[\"444455556666\"]",
  "resultRegions": "[\"us-east-1\"]",
  "memberSchemaMapping": "{\"444455556666\":\"publisher-conversions\"}",
  "memberDisplayNames": "{\"444455556666\":\"Example Publisher\"}"
}
```

###### Example Query log when an analysis finishes

```
{
  "eventId": "ffffffff-0000-4111-8222-333333333333",
  "eventTimestamp": 1723392305000,
  "collaborationId": "11111111-2222-4333-8444-555555555555",
  "logStage": "TERMINATION",
  "analysisCategory": "SQL",
  "analysisCategoryVersion": "1.0",
  "status": "COMPLETED",
  "errorCode": null,
  "errorMessage": null
}
```

###### Example Job log when an analysis runs

```
{
  "eventId": "00000000-1111-4222-8333-444444444444",
  "eventTimestamp": 1723392365000,
  "collaborationId": "11111111-2222-4333-8444-555555555555",
  "logStage": "SUBMISSION",
  "analysisCategory": "PYSPARK",
  "analysisCategoryVersion": "1.0",
  "schemaName": "publisher-conversions",
  "configuredTableId": "99999999-aaaa-4bbb-8ccc-dddddddddddd",
  "analysisTemplateArn": "arn:aws:cleanrooms:us-east-1:444455556666:membership/66666666-7777-4888-8999-aaaaaaaaaaaa/analysistemplate/77777777-8888-4999-8aaa-bbbbbbbbbbbb",
  "analysisTemplateArtifactHashList": "[\"abc123def456\"]",
  "directJobAnalysisRuleType": "CUSTOM",
  "directJobAnalysisRulePolicy": "{\"v1\":{\"custom\":{\"allowedAnalyses\":[\"arn:aws:cleanrooms:us-east-1:444455556666:membership/66666666-7777-4888-8999-aaaaaaaaaaaa/analysistemplate/77777777-8888-4999-8aaa-bbbbbbbbbbbb\"]}}}",
  "jobValidationErrors": null,
  "jobRunners": "[\"444455556666\"]",
  "memberSchemaMapping": "{\"444455556666\":\"publisher-conversions\"}",
  "memberDisplayNames": "{\"444455556666\":\"Example Publisher\"}"
}
```

###### Example Job log when an analysis finishes

```
{
  "eventId": "00000000-1111-4222-8333-444444444444",
  "eventTimestamp": 1723392605000,
  "collaborationId": "11111111-2222-4333-8444-555555555555",
  "logStage": "TERMINATION",
  "analysisCategory": "PYSPARK",
  "analysisCategoryVersion": "1.0",
  "status": "COMPLETED",
  "errorCode": null,
  "errorMessage": null
}
```
