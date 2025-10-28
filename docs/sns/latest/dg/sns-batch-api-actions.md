# Amazon SNS message batching

## What is message batching?

An alternative to publishing messages to either Standard or FIFO topics in individual
`Publish` API requests, is using the Amazon SNS `PublishBatch` API
to publish up to 10 messages in a single API request. Sending messages in batches can
help you reduce the costs associated with connecting distributed applications ([A2A messaging](sns-system-to-system-messaging.md "sns-system-to-system-messaging.md")) or sending
notifications to people ([A2P messaging](sns-user-notifications.md "sns-user-notifications.md"))
with Amazon SNS by a factor of up to 10. Amazon SNS has quotas on how many messages you can
publish to a topic per second based on the region in which you operate. See the [Amazon SNS endpoints and
quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") page in the _AWS General Reference_ guide for more
information on API quotas.

###### Note

The total aggregate size of all messages that you send in a single
`PublishBatch` API request can’t exceed 262,144 bytes (256
KiB).

The `PublishBatch` API uses the same `Publish` API action
for IAM policies.

## How does message batching work?

Publishing messages with the `PublishBatch` API is similar to publishing
messages with the `Publish` API. The main difference is that each message
within a `PublishBatch` API request needs to be assigned a unique batch ID
(up to 80 characters). This way, Amazon SNS can return individual API responses for every
message within a batch to confirm that each message was either published or that a
failure occurred. For messages being published to FIFO topics, in addition to including
assigning a unique batch ID, you still need to include a
`MessageDeduplicationID` and `MessageGroupId` for each
individual message.

## Examples

**Publishing a batch of 10 messages to a Standard
topic**

```
// Imports
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.PublishBatchRequest;
import software.amazon.awssdk.services.sns.model.PublishBatchRequestEntry;
import software.amazon.awssdk.services.sns.model.PublishBatchResponse;
import software.amazon.awssdk.services.sns.model.SnsException;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

// Code
private static final int MAX_BATCH_SIZE = 10;

public static void publishBatchToTopic(SnsClient snsClient, String topicArn, int batchSize) {
    try {
        // Validate the batch size
        if (batchSize > MAX_BATCH_SIZE) {
            throw new IllegalArgumentException("Batch size cannot exceed " + MAX_BATCH_SIZE);
        }

        // Create the batch entries
        List<PublishBatchRequestEntry> entries = IntStream.range(0, batchSize)
                .mapToObj(i -> PublishBatchRequestEntry.builder()
                        .id("id" + i)
                        .message("message" + i)
                        .build())
                .collect(Collectors.toList());

        // Build the batch request
        PublishBatchRequest request = PublishBatchRequest.builder()
                .topicArn(topicArn)
                .publishBatchRequestEntries(entries)
                .build();

        // Publish the batch request
        PublishBatchResponse response = snsClient.publishBatch(request);

        // Handle successful messages
        response.successful().forEach(success -> {
            System.out.println("Successful Batch Id: " + success.id());
            System.out.println("Message Id: " + success.messageId());
        });

        // Handle failed messages
        response.failed().forEach(failure -> {
            System.err.println("Failed Batch Id: " + failure.id());
            System.err.println("Error Code: " + failure.code());
            System.err.println("Sender Fault: " + failure.senderFault());
            System.err.println("Error Message: " + failure.message());
        });

    } catch (SnsException e) {
        // Log and handle exceptions
        System.err.println("SNS Exception: " + e.awsErrorDetails().errorMessage());
    } catch (IllegalArgumentException e) {
        System.err.println("Validation Error: " + e.getMessage());
    }
}
```

**Publishing a batch of 10 messages to a FIFO
topic**

```
// Imports
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.PublishBatchRequest;
import software.amazon.awssdk.services.sns.model.PublishBatchRequestEntry;
import software.amazon.awssdk.services.sns.model.PublishBatchResponse;
import software.amazon.awssdk.services.sns.model.BatchResultErrorEntry;
import software.amazon.awssdk.services.sns.model.SnsException;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

// Code
private static final int MAX_BATCH_SIZE = 10;

public static void publishBatchToFifoTopic(SnsClient snsClient, String topicArn) {
    try {
        // Create the batch entries to send
        List<PublishBatchRequestEntry> entries = IntStream.range(0, MAX_BATCH_SIZE)
                .mapToObj(i -> PublishBatchRequestEntry.builder()
                        .id("id" + i)
                        .message("message" + i)
                        .messageGroupId("groupId")
                        .messageDeduplicationId("deduplicationId" + i)
                        .build())
                .collect(Collectors.toList());

        // Create the batch request
        PublishBatchRequest request = PublishBatchRequest.builder()
                .topicArn(topicArn)
                .publishBatchRequestEntries(entries)
                .build();

        // Publish the batch request
        PublishBatchResponse response = snsClient.publishBatch(request);

        // Handle the successfully sent messages
        response.successful().forEach(success -> {
            System.out.println("Batch Id for successful message: " + success.id());
            System.out.println("Message Id for successful message: " + success.messageId());
            System.out.println("Sequence Number for successful message: " + success.sequenceNumber());
        });

        // Handle the failed messages
        response.failed().forEach(failure -> {
            System.err.println("Batch Id for failed message: " + failure.id());
            System.err.println("Error Code for failed message: " + failure.code());
            System.err.println("Sender Fault for failed message: " + failure.senderFault());
            System.err.println("Failure Message for failed message: " + failure.message());
        });

    } catch (SnsException e) {
        // Handle any exceptions from the request
        System.err.println("SNS Exception: " + e.awsErrorDetails().errorMessage());
    }
}
```
