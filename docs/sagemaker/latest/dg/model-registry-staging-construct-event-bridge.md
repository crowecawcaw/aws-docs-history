# Get event

notifications for ModelLifeCycle

You can get the ModelLifeCycle update notifications and events with EventBridge in
your account. The following is an example of an EventBridge rule, to be configured in
your account, in order to get the ModelLifeCycle event notifications.

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["SageMaker Model Package State Change"]
}
```

For an example EventBridge payload you may receive, see [SageMaker model package state change](automating-sagemaker-with-eventbridge.md#eventbridge-model-package "automating-sagemaker-with-eventbridge.md#eventbridge-model-package").
