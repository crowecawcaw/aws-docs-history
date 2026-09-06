

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Delete an entity type
<a name="delete-entity-type"></a>

In Amazon Fraud Detector, you cannot delete an entity type that is included in an event type. You will have to first delete the event type the entity is associated with and then delete the entity type.

When you delete an entity type, Amazon Fraud Detector permanently deletes that entity type and the data is no longer stored in Amazon Fraud Detector.

An entity type can be deleted in Amazon Fraud Detector console, using the [delete-entity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-entity-type.html) command, using the [DeleteEntityType](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteEntityType.html) API, or using the AWS SDK for Python (Boto3)

## Delete an entity type in Amazon Fraud Detector console
<a name="delete-entity-type-console"></a>

**To delete an entity type,**

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector).

1. In the left navigation pane of the Amazon Fraud Detector console, choose **Resources**, then choose **Entities**.

1. Choose the entity type that you want to delete.

1. Choose **Actions**, and then choose **Delete**.

1. Enter the entity type name, and then choose **Delete entity type**.

## Delete entity type using the AWS SDK for Python (Boto3)
<a name="delete-entity-type-using-the-aws-python-sdk"></a>

The following AWS SDK for Python (Boto3) example code deletes the entity type *customer* using the [DeleteEntityType](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteEntityType.html) API.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.delete_entity_type (

name = 'customer'

)
```