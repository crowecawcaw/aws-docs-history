Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create an entity type

You can create an entity type in the Amazon Fraud Detector console, using the [put-entity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-entity-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-entity-type.html") command,
using the [PutEntityType](../api/API_PutEntityType.md "../api/API_PutEntityType.md") API, or using the AWS SDK for Python (Boto3).
The examples below creates an entity type `customer` in the Amazon Fraud Detector console and using the SDK for Python (Boto3). If you are creating an entity type to associate with an event type for training a fraud detection model,
use the entity type from your event dataset that is appropriate for your use case.

## Create an entity type using the Amazon Fraud Detector console

###### To create an entity type,

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
2. Navigate to Amazon Fraud Detector, choose
   **Entities** in the left navigation, then choose
   **Create**.
3. In the **Create entity** page, enter **customer** as the entity type name.
   Optionally, enter a description of the entity.
4. Choose **Create entity**.

## Create an entity type using the AWS SDK for Python (Boto3)

The following AWS SDK for Python (Boto3) code example uses the `PutEntityType` API to create an entity type `customer`. If you are creating an entity type to associate with an event type for training a fraud detection model,
use the entity from your event dataset that is appropriate for your use case.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_entity_type(
name = 'customer',
description = 'customer'
)

```
