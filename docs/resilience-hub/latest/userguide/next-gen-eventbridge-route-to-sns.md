# Route assessment events to Amazon SNS

The following commands create an EventBridge rule that routes assessment completion events to an
Amazon SNS topic.

```

aws events put-rule \
  --name "ResilienceHub-AssessmentCompleted" \
  --event-pattern '{
    "source": ["aws.resiliencehub"],
    "detail-type": ["Assessment Completed"]
  }'

aws events put-targets \
  --rule "ResilienceHub-AssessmentCompleted" \
  --targets "Id"="1","Arn"="arn:aws:sns:us-east-1:123456789012:resilience-hub-alerts"
```
