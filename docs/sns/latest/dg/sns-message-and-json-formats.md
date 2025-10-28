# Parsing Amazon SNS message formats

When Amazon SNS sends messages to HTTP/HTTPS endpoints, they contain both HTTP headers and a
JSON message body. These messages follow a structured format that includes metadata such as
the message type, topic ARN, timestamps, and digital signatures. By correctly parsing Amazon SNS
messages, you can determine whether a message is a subscription confirmation, notification,
or unsubscribe confirmation, extract relevant data, and verify authenticity using signature
validation.
