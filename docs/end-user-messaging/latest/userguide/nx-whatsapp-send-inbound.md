

# Inbound messaging
<a name="nx-whatsapp-send-inbound"></a>

Within an open conversation window, recipients can reply to your WhatsApp messages. To receive those inbound messages and the status events for your outbound messages, you turn on message and event publishing for your WhatsApp phone number and point it at an Amazon SNS topic. Your application reads the topic and replies with `SendWhatsAppMessage` while the window is open.

## Step 1: Route inbound messages to an Amazon SNS topic
<a name="nx-whatsapp-send-inbound-configure"></a>

Message and event publishing sends both inbound messages and outbound status events to a standard Amazon SNS topic that you own. You can turn it on while adding the phone number (see [Step 2: Add a WhatsApp business phone number](nx-whatsapp-gsu-add-number.md)) or afterward on the phone number's settings.

**To route inbound WhatsApp messages to an SNS topic**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. Under **Social messaging**, choose **WhatsApp business accounts**, choose your WABA, and then choose the phone number.

1. Turn on **Message and event publishing**.

1. For the destination, choose a new or existing standard Amazon SNS topic. FIFO topics are not supported.

1. Save the phone number settings.

**Note**  
Amazon SNS standard topics deliver with best-effort ordering, so inbound messages are not guaranteed to arrive in the order they were sent. If your application needs ordered processing, use the timestamp in each record to order messages at the application layer.

## Step 2: Consume inbound messages and reply
<a name="nx-whatsapp-send-inbound-consume"></a>

Subscribe a consumer to the Amazon SNS topic – for example an Lambda function, an Amazon SQS queue, or an HTTPS endpoint. Each inbound message and status event is delivered to the topic as a record. When a record is an inbound message from a customer, your application can reply with `SendWhatsAppMessage`. While the conversation window the customer opened is still active, you can send free-form messages (set the message `type` to `text` or another supported type) without a template; once the window closes, you must start a new conversation with an approved template.

For the event-record format and the full set of event destinations, see [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md).