

# Massive Scale Real-Time Messaging for Multiplayer Games
<a name="massive-scale-real-time-messaging-multiplayer-games"></a>

Publication date: **November 11, 2020 ([Diagram history](#messaging-history))**

This architecture shows how to deliver real-time messaging for multiplayer games that can scale to support millions of concurrent users (CCU). The solution uses multiple Redis PubSub clusters with [Amazon ElastiCache for Redis](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/) and WebSockets to provide horizontal scalability.

## Massive Scale Real-Time Messaging for Multiplayer Games diagram
<a name="messaging-diagram"></a>

![Reference architecture diagram showing how to deliver real-time messaging for multiplayer games by using Amazon ElastiCache for Redis PubSub clusters and WebSockets.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/massive-scale-real-time-messaging-multiplayer-games/images/massive-scale-real-time-messaging-multiplayer-games.png)


The following steps describe the architecture:

1. When a real-time messaging server starts, it checks a Service Discovery cache (using Amazon ElastiCache for Redis) for a list of available Redis PubSub instances. The server subscribes to the same topic in each PubSub instance. This approach shards traffic across multiple ElastiCache clusters while still reaching the correct server.

1. Clients send requests to a Service Discovery API to retrieve a real-time messaging server to connect to. The list of available messaging instances is stored in the Service Discovery cache.

1. The Service Discovery cache stores information about connected endpoints, including clients, real-time messaging instances, and the Redis PubSub clusters and topics that each messaging instance can receive on. If a client disconnects, this information is removed from the cache.

1. Applications use a Messaging API to deliver messages to clients. The API publishes the message to the appropriate topic that reaches the correct real-time messaging server and game client.

1. The Messaging API publishes the message to the topic in one of the Redis PubSub instances. Because each real-time messaging server listens to the same topic in every PubSub instance, the message is delivered regardless of which ElastiCache cluster receives it.

## Further reading
<a name="messaging-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="messaging-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#messaging-history) | Reference architecture diagram first published. | November 11, 2020 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.