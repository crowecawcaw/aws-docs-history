# Using server-side encryption with Amazon SQS queues

Use the AWS SDK for Java to add server-side encryption (SSE) to an Amazon SQS queue. Each queue uses an
AWS Key Management Service (AWS KMS) KMS key to generate the data encryption keys. This example uses the
AWS managed KMS key for Amazon SQS.

For more information about using SSE and the role of the KMS key, see [Encryption at rest in Amazon SQS](sqs-server-side-encryption.md "sqs-server-side-encryption.md").

## Adding SSE to an existing

queue

To enable server-side encryption for an existing queue, use the `SetQueueAttributes`
method to set the `KmsMasterKeyId` attribute.

The following code example sets the AWS KMS key as the AWS managed KMS key for
Amazon SQS. The example also sets the [AWS KMS key reuse
period](sqs-server-side-encryption.md#sqs-sse-key-terms "sqs-server-side-encryption.md#sqs-sse-key-terms") to 140 seconds.

Before you run the example code, make sure that you have set your AWS credentials. For
more information, see [Set up AWS Credentials and Region for Development](../../../sdk-for-java/latest/developer-guide/setup.md#setup-credentials "../../../sdk-for-java/latest/developer-guide/setup.md#setup-credentials")
in the _AWS SDK for Java 2.x Developer Guide_.

```
    public static void addEncryption(String queueName, String kmsMasterKeyAlias) {
        SqsClient sqsClient = SqsClient.create();

        GetQueueUrlRequest urlRequest = GetQueueUrlRequest.builder()
                .queueName(queueName)
                .build();

        GetQueueUrlResponse getQueueUrlResponse;
        try {
            getQueueUrlResponse = sqsClient.getQueueUrl(urlRequest);
        } catch (QueueDoesNotExistException e) {
            LOGGER.error(e.getMessage(), e);
            throw new RuntimeException(e);
        }
        String queueUrl = getQueueUrlResponse.queueUrl();


        Map<QueueAttributeName, String> attributes = Map.of(
                QueueAttributeName.KMS_MASTER_KEY_ID, kmsMasterKeyAlias,
                QueueAttributeName.KMS_DATA_KEY_REUSE_PERIOD_SECONDS, "140" // Set the data key reuse period to 140 seconds.
        );                                                                  // This is how long SQS can reuse the data key before requesting a new one from KMS.

        SetQueueAttributesRequest attRequest = SetQueueAttributesRequest.builder()
                .queueUrl(queueUrl)
                .attributes(attributes)
                .build();
        try {
            sqsClient.setQueueAttributes(attRequest);
            LOGGER.info("The attributes have been applied to {}", queueName);
        } catch (InvalidAttributeNameException | InvalidAttributeValueException e) {
            LOGGER.error(e.getMessage(), e);
            throw new RuntimeException(e);
        } finally {
            sqsClient.close();
        }
    }

```

## Disabling SSE for a queue

To disable server-side encryption for an existing queue, set the `KmsMasterKeyId`
attribute to an empty string using the `SetQueueAttributes` method.

###### Important

`null` isn't a valid value for `KmsMasterKeyId`.

## Creating a queue with

SSE

To enable SSE when you create the queue, add the `KmsMasterKeyId`
attribute to the `CreateQueue` API method.

The following example creates a new queue with SSE enabled. The queue uses the AWS
managed KMS key for Amazon SQS. The example also sets the [AWS KMS key reuse period](sqs-server-side-encryption.md#sqs-sse-key-terms "sqs-server-side-encryption.md#sqs-sse-key-terms") to 160 seconds.

Before you run the example code, make sure that you have set your AWS credentials. For
more information, see [Set up AWS Credentials and Region for Development](../../../sdk-for-java/latest/developer-guide/setup.md#setup-credentials "../../../sdk-for-java/latest/developer-guide/setup.md#setup-credentials")
in the _AWS SDK for Java 2.x Developer Guide_.

```
// Create an SqsClient for the specified Region.
SqsClient sqsClient = SqsClient.builder().region(Region.US_WEST_1).build();

// Create a hashmap for the attributes. Add the key alias and reuse period to the hashmap.
HashMap<QueueAttributeName, String> attributes = new HashMap<QueueAttributeName, String>();
final String kmsMasterKeyAlias = "alias/aws/sqs";  // the alias of the AWS managed KMS key for Amazon SQS.
attributes.put(QueueAttributeName.KMS_MASTER_KEY_ID, kmsMasterKeyAlias);
attributes.put(QueueAttributeName.KMS_DATA_KEY_REUSE_PERIOD_SECONDS, "140");

// Add the attributes to the CreateQueueRequest.
CreateQueueRequest createQueueRequest =
                CreateQueueRequest.builder()
                        .queueName(queueName)
                        .attributes(attributes)
                        .build();
sqsClient.createQueue(createQueueRequest);

```

## Retrieving SSE attributes

For information about retrieving queue attributes, see [Examples](../APIReference/API_GetQueueAttributes.md#API_GetQueueAttributes_Examples "../APIReference/API_GetQueueAttributes.md#API_GetQueueAttributes_Examples") in the _Amazon Simple Queue Service API Reference_.

To retrieve the KMS key ID or the data key reuse period for a particular queue, run
the `GetQueueAttributes` method and retrieve the
`KmsMasterKeyId` and `KmsDataKeyReusePeriodSeconds`
values.
