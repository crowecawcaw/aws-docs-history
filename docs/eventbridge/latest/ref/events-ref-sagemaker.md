# Amazon SageMaker AI events

SageMaker AI sends service events directly to EventBridge, as well as via AWS CloudTrail.

## SageMaker AI service events

SageMaker AI sends the following events directly to EventBridge:

- SageMaker Training Job State Change
- SageMaker HyperParameter Tuning Job State Change
- SageMaker Transform Job State Change
- SageMaker Endpoint Config State Change
- SageMaker Endpoint State Change
- SageMaker Model State Change
- SageMaker Notebook Instance State Change
- SageMaker Notebook Lifecycle Config State Change
- SageMaker Algorithm State Change
- SageMaker Model Package State Change
- SageMaker Processing Job State Change
- SageMaker Feature Group State Change
- SageMaker Image State Change
- SageMaker Image Version State Change
- SageMaker Endpoint Deployment State Change
- SageMaker Model Card State Change
- SageMaker Model Card Export Job State Change
- SageMaker Monitoring Schedule State Change
- SageMaker HyperPod Cluster State Change
- SageMaker HyperPod Cluster Node Health Event
- SageMaker HyperPod Cluster Event
- SageMaker A2I HumanLoop Status Change
- SageMaker Human Loop Finished
- SageMaker Human Loop Step Execution Finished
- SageMaker Human Task Accepted
- SageMaker Human Task Created
- SageMaker Human Task Declined
- SageMaker Human Task Expired
- SageMaker Human Task Returned
- SageMaker Human Task Submitted
- SageMaker Ground Truth Labeling Job State Change
- SageMaker Model Building Pipeline Execution Status Change
- SageMaker Model Building Pipeline Execution Step Status Change
- SageMaker Ground Truth Labeling Job Task Status Change
- SageMaker Evaluation Job Status Change
- SageMaker Tracking Server Creating
- SageMaker Tracking Server Created
- SageMaker Tracking Server Create Failed
- SageMaker Tracking Server Updating
- SageMaker Tracking Server Updated
- SageMaker Tracking Server Update Failed
- SageMaker Tracking Server Deleting
- SageMaker Tracking Server Deleted
- SageMaker Tracking Server Delete Failed
- SageMaker Tracking Server Starting
- SageMaker Tracking Server Started
- SageMaker Tracking Server Start Failed
- SageMaker Tracking Server Stopping
- SageMaker Tracking Server Stopped
- SageMaker Tracking Server Stop Failed
- SageMaker Tracking Server Maintenance In Progress
- SageMaker Tracking Server Maintenance Complete
- SageMaker Tracking Server Maintenance Failed
- SageMaker MLFlow Tracking Server Creating Run
- SageMaker MLFlow Tracking Server Creating RegisteredModel
- SageMaker MLFlow Tracking Server Creating ModelVersion
- SageMaker MLFlow Tracking Server Transitioning ModelVersion Stage
- SageMaker MLFlow Tracking Server Setting Registered Model Alias

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.sagemaker

```
{
  "source": ["aws.sagemaker"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["`SageMaker Training Job State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## SageMaker AI events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from SageMaker AI to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.sagemaker
- `eventSource`: sagemaker.amazonaws.com

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sagemaker.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sagemaker.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
