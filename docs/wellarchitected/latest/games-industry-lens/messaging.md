# Messaging

There are typically three primary categories of messages in games:

- Player engagement messaging targeted at a specific user or cohort of users, such as
  game invites or push notifications
- Group messaging between players, such as in-game chat
- Service-to-service messaging, such as JSON messages used to integrate two or more
  applications
  A common strategy for sending and receiving these types messages is to use
  publisher-subscriber (pub-sub) and asynchronous processing architecture patterns. AWS
  provides several services that can help you to implement messaging in your game.

[Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") provides a managed service for delivering messages between publishers
and subscribers using a pub-sub architecture pattern. Publishers send messages via API to
Amazon SNS, which delivers the messages asynchronously to subscribing applications, and can
deliver push notifications directly to mobile clients or desktops with support for some of
the most widely used push notification services out of the box. Amazon SNS can be used for push
notifications to clients as well as service-to-service messaging use cases.

[Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/ "https://aws.amazon.com/sqs/") is a fully managed queue service
that makes it easy to integrate game
servers and your game regardless of the programming language used in each. Many games tasks
can be decoupled and handled in the background such as updating a leaderboard or playtime
values in a database. This approach is a very effective way to decouple various parts of
your game and independently scale the player-facing features from backend processing.

[Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/ "https://aws.amazon.com/msk/") is a fully managed service
that makes it easy to build data streaming
and producer/consumer applications using Apache Kafka, a popular open-source platform. Kafka
is typically used for ingesting and processing real-time streaming data and can be used for
service-to-service messaging

[Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis/ "https://aws.amazon.com/elasticache/redis/") provides a fully managed
in-memory data store which includes support for the
popular pub/sub feature of Redis that is commonly used for developing chat room applications
and high-performance service-to-service messaging. Redis also supports rich data types, such
as lists and sets, that enable developers to use Redis for high-performance queuing.

[Amazon Pinpoint](https://aws.amazon.com/pinpoint/ "https://aws.amazon.com/pinpoint/") provides user engagement messaging through email, SMS, voice, and push
notifications. For example, Amazon Pinpoint can be used to deliver user engagement messages to players
to invite them back to the game, and can be used for transactional use cases such as
supporting multi-factor authentication tokens, and order confirmation and password reset
emails.
