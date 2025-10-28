# Step 4: Optional - Set the delivery policy for the

Amazon SNS subscription

By default, if the initial delivery of the message fails, Amazon SNS attempts up to three
retries with a delay between failed attempts set at 20 seconds. As discussed in [Step 1](SendMessageToHttp.md "SendMessageToHttp.md"), your endpoint should have code that can
handle retried messages. By setting the delivery policy on a topic or subscription, you can
control the frequency and interval that Amazon SNS will retry failed messages. You can also specify
the content type for your HTTP/S notifications in `DeliveryPolicy`. For more
information, see [Creating an HTTP/S delivery policy](sns-message-delivery-retries.md#creating-delivery-policy "sns-message-delivery-retries.md#creating-delivery-policy").
