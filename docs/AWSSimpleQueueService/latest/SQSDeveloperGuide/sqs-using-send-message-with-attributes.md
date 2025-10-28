# Sending a message with attributes

using Amazon SQS

For standard and FIFO queues, you can include structured metadata to messages, including
timestamps, geospatial data, signatures, and identifiers . For more information, see [Amazon SQS message attributes](sqs-message-metadata.md#sqs-message-attributes "sqs-message-metadata.md#sqs-message-attributes").

###### To send a message with attributes to a queue using the Amazon SQS console

1.  Open the Amazon SQS console at
    [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2.  In the navigation pane, choose **Queues**.
3.  On the **Queues** page, choose a queue.
4.  Choose **Send and receive messages**.
5.  Enter the message attribute parameters.

        1. In the name text box, enter a unique name of up to 256 characters.
        2. For the attribute type, choose **String**,
         **Number**, or **Binary**.
        3. (Optional) Enter a custom data type. For example, you could add
         `byte`, `int`, or
         `float` as custom data types for
         **Number**.
        4. In the value text box, enter the message attribute value.

    ![The Amazon SQS console displaying the Message attributes section.](images/sqs-tutorials-sending-message-with-attributes.png)

6.  To add another message attribute., choose **Add new
    attribute**.

![The Amazon SQS console displaying the Remove button in the Message attributes section.](images/sqs-tutorials-sending-message-with-attributes-custom-attribute.png) 7. You can modify the attribute values any time before sending the message. 8. To delete an attribute, choose **Remove**. To delete the first
attribute, close **Message attributes**. 9. When you finish adding attributes to the message, choose **Send
message**. Your message is sent and the console displays a success
message. To view information about the message attributes of the sent message,
choose **View details**. Choose **Done** to close
the **Message details** dialog box.
