

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Enable event orchestration in Amazon Fraud Detector
<a name="enable-event-orchestration"></a>

You can enable event orchestration for an event either when you are creating your event type or after you have created your event type. Event orchestration can be enabled in the Amazon Fraud Detector console, using the `put-event-type` command, using the `PutEventType` API, or using the AWS SDK for Python (Boto3). 

## Enable event orchestration in the Amazon Fraud Detector console
<a name="enable-event-orchestration-console"></a>

This example enables event orchestration for an event type that is has already been created. If you are creating a new event type and want to enable orchestration, follow instructions to [Create an event type](create-event-type.md).

**To enable event orchestration**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

1. In the left navigation pane, choose **Events**.

1. In the **Events type** page, choose your event type. 

1. Turn on **Enable event orchestration with Amazon EventBridge**.

1. Continue with step 3 instructions for [Setting up event orchestration](setting-up-event-orchestration.md).

## Enable event orchestration using the AWS SDK for Python (Boto3)
<a name="enable-event-orchestration-using-the-aws-python-sdk"></a>

The following example shows a sample request for updating an event type `sample_registration` to enable event orchestration. The example uses the `PutEventType` API and assumes you have created the variables `ip_address` and `email_address`, the labels `legit` and `fraud`, and the entity type `sample_customer`. For information on how to create these resources, see [Resources](https://docs.aws.amazon.com/frauddetector/latest/ug/create-resources.html).

```
import boto3
fraudDetector = boto3.client('frauddetector')
fraud_detector.put_event_type( 
  name = 'sample_registration',
  eventVariables = ['ip_address', 'email_address'],
  eventOrchestration = {'eventBridgeEnabled': True},
  labels = ['legit', 'fraud'],
  entityTypes = ['sample_customer'])
```