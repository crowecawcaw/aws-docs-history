

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create label
<a name="create-a-label"></a>

You can create labels in the Amazon Fraud Detector console, using the [put-label](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-label.html) command, using the [PutLabel](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutLabel.html) API, or using the AWS SDK for Python (Boto3).

## Create a label using the Amazon Fraud Detector console
<a name="create-a-label-console"></a>

**To create labels,**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. 

1. Navigate to Amazon Fraud Detector, choose **Labels** in the left navigation, then choose **Create**.

1. In the **Create label** page, enter your label name for fraudulent event as the label name. The label name must correspond to the label that represents fraudulent activity in your training dataset. Optionally, enter a description of the label.

1. Choose **Create label**.

1. Create a second label and enter a label name for legitimate event. Make sure the label name corresponds to the value that represents the legitimate activity in your training dataset.

## Create a label using the AWS SDK for Python (Boto3)
<a name="create-a-label-using-the-aws-python-sdk"></a>

The following AWS SDK for Python (Boto3) example code creates two labels (fraud, legit) using the [PutLabel](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutLabel.html) API. After creating the labels, you can add them to an event type to classify specific events.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_label(
name = 'fraud',
description = 'label for fraud events'
)

fraudDetector.put_label(
name = 'legit',
description = 'label for legitimate events'
)
```