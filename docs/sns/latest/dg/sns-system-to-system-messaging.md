

# Using Amazon SNS for application-to-application messaging
<a name="sns-system-to-system-messaging"></a>

Amazon SNS simplifies application-to-application (A2A) messaging by separating publishers from subscribers, which supports microservices, distributed systems, and serverless applications. Messages are sent to Amazon SNS topics, where they can be filtered and delivered to subscribers like Lambda, Amazon SQS, or HTTP endpoints. If delivery fails, the messages are stored in a dead-letter queue for further analysis or reprocessing.

![Amazon SNS facilitates application-to-application messaging by decoupling publishers from subscribers using topics. Messages from systems or services are routed through an Amazon SNS topic, where they can be filtered and distributed to subscribers like Lambda, Amazon SQS, or email systems. If delivery fails, messages are stored in a dead-letter queue for later analysis or reprocessing.](http://docs.aws.amazon.com/sns/latest/dg/images/sns-a2a-overview.png)
