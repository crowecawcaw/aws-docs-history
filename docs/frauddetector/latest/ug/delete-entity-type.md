Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete an entity type

In Amazon Fraud Detector, you cannot delete an entity type that is included in an event type. You will have to first delete the event type the entity is associated with and then delete the entity type.

When you delete an entity type, Amazon Fraud Detector permanently deletes that entity type and the data is no longer stored in Amazon Fraud Detector.

An entity type can be deleted in Amazon Fraud Detector console, using the [delete-entity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-entity-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-entity-type.html") command, using the [DeleteEntityType](../api/API_DeleteEntityType.md "../api/API_DeleteEntityType.md") API, or using the AWS SDK for Python (Boto3)

## Delete an entity type in Amazon Fraud Detector console

###### To delete an entity type,

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector").
2. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Resources**, then choose
   **Entities**.
3. Choose the entity type that you want to delete.
4. Choose **Actions**, and then choose
   **Delete**.
5. Enter the entity type name, and then choose **Delete entity
   type**.

## Delete entity type using the

AWS SDK for Python (Boto3)

The following AWS SDK for Python (Boto3) example code deletes the entity type _customer_ using the [DeleteEntityType](../api/API_DeleteEntityType.md "../api/API_DeleteEntityType.md") API.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.delete_entity_type (

name = 'customer'

)

```
