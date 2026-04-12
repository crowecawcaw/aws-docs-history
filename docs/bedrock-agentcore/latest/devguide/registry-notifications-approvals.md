# Notifications for pending approvals

## Event details

- **Source:**
  `aws.bedrock-agentcore`
- **Detail type:**
  `Registry Record State changed to Pending Approval`
- **Bus:** Default Amazon EventBridge bus
- **Resources:** Full ARN of the registry record
- **Detail:** Contains `registryRecordId` and `registryId`

## Example event

```
{
 "version":"0",
 "detail-type":"Registry Record State changed to Pending Approval",
 "source":"aws.bedrock-agentcore",
 "account":"123456789012",
 "region":"us-west-2",
 "resources":["arn:aws:bedrock-agentcore:us-west-2:123456789012:registry/REG_ID/record/REC_ID"],
 "detail":{"registryRecordId":"REC_ID","registryId":"REG_ID"}
}
```

## Create an Amazon EventBridge rule

For more information on how to create Amazon EventBridge Rules, see [Creating Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-create-rule-visual.md "../../../eventbridge/latest/userguide/eb-create-rule-visual.md") . AWS Agent Registry events can be found under the source: `aws.bedrock-agentcore` and detail-type: `Registry Record State changed to Pending Approval`.

You can configure the rule to any [Target](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md") supported by Amazon EventBridge.
