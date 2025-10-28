# Receiving and deleting a message in Amazon SQS

After sending messages to an Amazon SQS queue, you can retrieve and delete them to process
your application workflow. This process ensures secure and reliable message handling.
This topic walks you through retrieving and deleting messages using the Amazon SQS console
and explains key settings to optimize this operation. The following are key concepts for
receiving and deleting messages:

1. **Receiving messages**
   - When you retrieve messages from an Amazon SQS queue, you cannot target
     specific messages. Instead, specify the maximum number of messages to
     retrieve in a single request (up to 10).
   - Due to Amazon SQS's distributed nature, retrieving from a queue with
     few messages may return an empty response. To mitigate this:
     - Use long polling, which waits until a message is available or
       the poll times out. This approach reduces unnecessary polling
       costs and improves efficiency.
     - Re-issue the request if needed.

2. **Message visibility and deletion**
   - Messages are not deleted automatically after retrieval. This feature
     ensures you can reprocess messages in case of application failures or
     network disruptions.
   - After processing, you must explicitly send a delete request to remove
     the message permanently. This action confirms successful
     handling.
   - Messages retrieved using the Amazon SQS console remain visible for
     re-retrieval. Adjust the visibility timeout setting for automated
     environments to temporarily hide messages from other consumers while
     they are being processed.

3. **Visibility timeout**
   - This setting determines how long a message remains hidden after
     retrieval. Set an appropriate timeout to ensure messages are processed
     only once and to prevent duplication during distributed
     processing.

###### To receive and delete a message using the console

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. On the **Queues** page, choose the
   **queue** you want to receive messages from, and then
   select **Send and receive messages**.
4. On the **Send and receive messages** page, select
   **Poll for messages**.

Amazon SQS displays a progress bar indicating the polling duration. Messages
retrieved will appear in the **Messages** section,
showing:

    * Message ID
    * Sent date
    * Size
    * Receive count

5. To delete messages, choose the ones you want to remove and select
   **Delete**.

Confirm deletion in the **Delete Messages**
dialog box by selecting **Delete**.
For more details on advanced operations, including API-based message retrieval and
deletion, see the [Amazon SQS API
Reference Guide](../APIReference/API_Operations.md "../APIReference/API_Operations.md").
