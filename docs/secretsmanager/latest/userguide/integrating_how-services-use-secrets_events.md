# How Amazon EventBridge uses

AWS Secrets Manager

Amazon EventBridge is a serverless event bus service that you can use to connect your applications
with data from a variety of sources.

When you create an Amazon EventBridge API destination, EventBridge stores the connection for it in a Secrets Manager
[managed secret](service-linked-secrets.md "service-linked-secrets.md") with the prefix
`events`. The cost of storing the secret is included with the charge for using an
API destination. To update the secret, you must use EventBridge rather than Secrets Manager. For more
information, see [API destinations](../../../eventbridge/latest/userguide/eb-api-destinations.md "../../../eventbridge/latest/userguide/eb-api-destinations.md") in the
_Amazon EventBridge User Guide_.
