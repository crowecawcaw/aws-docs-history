# Amazon SNS message security for FIFO topics

You can enable encryption for Amazon SNS FIFO topics and Amazon SQS FIFO queues using [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
[customer
master keys (CMKs)](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys").

- You can create new encrypted FIFO topics and queues or enable encryption for existing
  ones.
- Only the message body is encrypted. Message attributes, resource metadata, and resource
  metrics remain unencrypted.

###### Note

Adding encryption to an existing FIFO topic or queue doesn't encrypt any backlogged
messages, and removing encryption from a topic or queue leaves backlogged messages
encrypted.

SNS FIFO topics decrypt the messages immediately before delivering them to subscribed
endpoints. SQS FIFO queues decrypt the message just before returning them to the consumer
application. For more information, see [Amazon SNS data encryption](sns-data-encryption.md "sns-data-encryption.md") and the [Encrypting messages published to Amazon SNS with AWS KMS](https://aws.amazon.com/blogs/compute/encrypting-messages-published-to-amazon-sns-with-aws-kms/ "https://aws.amazon.com/blogs/compute/encrypting-messages-published-to-amazon-sns-with-aws-kms/") post on the _AWS
Compute Blog_.

In addition, SNS FIFO topics and SQS FIFO queues support message privacy with [interface VPC endpoints](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") powered by AWS PrivateLink. Using interface endpoints, you
can send messages from Amazon Virtual Private Cloud (Amazon VPC) subnets to FIFO topics and queues without traversing
the public internet. This model keeps your messaging within the AWS infrastructure and
network, which enhances the overall security of your application. When you use AWS PrivateLink,
you don't need to set up an internet gateway, network address translation (NAT), or virtual
private network (VPN). For more information, see [Securing Amazon SNS traffic with VPC
endpoints](sns-internetwork-traffic-privacy.md "sns-internetwork-traffic-privacy.md")
and the [Securing messages published to Amazon SNS with AWS PrivateLink](https://aws.amazon.com/blogs/security/securing-messages-published-to-amazon-sns-with-aws-privatelink "https://aws.amazon.com/blogs/security/securing-messages-published-to-amazon-sns-with-aws-privatelink") post on the _AWS
Security Blog_.

SNS FIFO topics also support dead-letter queues and message storage across Availability
Zones. For more information, see [Amazon SNS message durability for FIFO topics](fifo-message-durability.md "fifo-message-durability.md").
