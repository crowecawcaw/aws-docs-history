

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create an entity type
<a name="create-an-entity-type"></a>

You can create an entity type in the Amazon Fraud Detector console, using the [put-entity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-entity-type.html) command, using the [PutEntityType](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutEntityType.html) API, or using the AWS SDK for Python (Boto3). The examples below creates an entity type `customer` in the Amazon Fraud Detector console and using the SDK for Python (Boto3). If you are creating an entity type to associate with an event type for training a fraud detection model, use the entity type from your event dataset that is appropriate for your use case. 

## Create an entity type using the Amazon Fraud Detector console
<a name="create-an-entity-type-using-console"></a>

**To create an entity type,**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. 

1. Navigate to Amazon Fraud Detector, choose **Entities** in the left navigation, then choose **Create**.

1. In the **Create entity** page, enter **customer** as the entity type name. Optionally, enter a description of the entity.

1. Choose **Create entity**.

## Create an entity type using the AWS SDK for Python (Boto3)
<a name="create-an-entity-type-using-the-aws-python-sdk"></a>

The following AWS SDK for Python (Boto3) code example uses the `PutEntityType` API to create an entity type `customer`. If you are creating an entity type to associate with an event type for training a fraud detection model, use the entity from your event dataset that is appropriate for your use case. 

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_entity_type(
name = 'customer',
description = 'customer'
)
```