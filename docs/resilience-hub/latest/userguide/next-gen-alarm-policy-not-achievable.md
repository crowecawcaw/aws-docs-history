

# Alarm: Policy not achievable
<a name="next-gen-alarm-policy-not-achievable"></a>

The following example creates an alarm that triggers when the availability SLO policy is not achievable for a service named `my-service`.

```
aws cloudwatch put-metric-alarm \
  --alarm-name "ResilienceHub-PolicyNotAchievable-AvailabilitySlo" \
  --metric-name "PolicyAchievable" \
  --namespace "ResilienceHub" \
  --dimensions Name=Service,Value=my-service Name=PolicyComponent,Value=AvailabilitySlo \
  --statistic Minimum \
  --period 86400 \
  --threshold 1 \
  --comparison-operator LessThanThreshold \
  --evaluation-periods 1 \
  --treat-missing-data notBreaching \
  --alarm-actions "arn:aws:sns:us-east-1:123456789012:resilience-hub-alerts"
```

This alarm enters the `ALARM` state when any assessment in the evaluation period reports that the policy is not achievable (metric value 0.0). The `--treat-missing-data notBreaching` setting ensures the alarm does not trigger between assessments when no data points are present.