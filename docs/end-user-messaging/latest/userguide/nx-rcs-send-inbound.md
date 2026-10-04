

# Inbound messaging
<a name="nx-rcs-send-inbound"></a>

You can test inbound RCS messaging by configuring a keyword with an auto-response and then sending a message from your test device that matches that keyword.

**To test inbound messaging with auto-response keywords**

1. In the AWS End User Messaging console, navigate to your AWS RCS Agent and configure a keyword. For example, set the keyword `RCSINBOUNDTESTING` with an auto-response message such as "Inbound test successful\! Your message was received."

1. On the **Testing** tab, choose **Inbound deep link**.

1. In the **Default message body** field, enter the keyword you configured (for example, `RCSINBOUNDTESTING`).

1. Choose **Generate link**. The console generates an inbound deep link URL using the GSMA standard `sms:` URI scheme. This deep link is embedded in the QR code displayed on the screen.

1. Scan the QR code with your verified tester phone. This opens the native messaging app with a pre-populated message addressed to your AWS RCS Agent.

1. Send the message from your test device.

1. Verify that you receive the auto-response message on your test device.

Testing auto-response keywords does not require setting up an event destination or Amazon SNS topic. The auto-response is handled entirely by AWS End User Messaging based on the keyword configuration on your AWS RCS Agent. To receive and process arbitrary inbound messages (not just keyword matches), you configure an Amazon SNS topic for two-way messaging and consume the inbound message events. For details on configuring event destinations, see [Monitoring](nx-rcs-scale-monitoring.md).