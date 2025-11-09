Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Disable event orchestration in Amazon Fraud Detector

You can disable event orchestration for an event anytime in the Amazon Fraud Detector console, using the `put-event-type` command, using the `PutEventType` API, or using the AWS SDK for Python (Boto3).

## Disable event orchestration in the Amazon Fraud Detector console

###### To disable event orchestration

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose **Events**.
3. In the **Events type** page, choose your event type.
4. Turn off **Enable event orchestration with Amazon EventBridge**.

## Disable event orchestration using the AWS SDK for Python (Boto3)

The following example shows a sample request for updating an event type `sample_registration` to disable event orchestration using the `PutEventType` API.

```
import boto3
fraudDetector = boto3.client('frauddetector')
fraud_detector.put_event_type(
  name = 'sample_registration',
  eventVariables = ['ip_address', 'email_address'],
  eventOrchestration = {'eventBridgeEnabled': False},
  entityTypes = ['sample_customer'])

```
