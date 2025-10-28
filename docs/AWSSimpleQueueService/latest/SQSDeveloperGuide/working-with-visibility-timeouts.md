# Configuring visibility timeouts

in Amazon SQS

To ensure reliable message processing, set the visibility timeout to be longer
than the AWS SDK read timeout. This applies when using the [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md") API with both short polling and long
polling. A longer visibility timeout prevents messages from becoming available to
other consumers before the original request completes, reducing the risk of
duplicate processing.
