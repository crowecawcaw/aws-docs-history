

# CloudWatch metrics reference
<a name="next-gen-cloudwatch-metrics"></a>

When a failure mode assessment completes successfully, Next generation Resilience Hub publishes policy achievability metrics to your account's Amazon CloudWatch (CloudWatch) under the `ResilienceHub` namespace. Metrics are emitted only upon assessment completion. If no assessment has run, or if the assessment did not produce achievability results, no metrics are reported.

Your service's permission model must include an invoker role with the `cloudwatch:PutMetricData` permission for Next generation Resilience Hub to emit metrics to your account.