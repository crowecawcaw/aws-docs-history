# Common ElastiCache Use Cases and How ElastiCache Can Help

Whether serving the latest news, a top-10 leaderboard, a product catalog,
or selling tickets to an event, speed is the name of the game. The success of your website
and business is greatly affected by the speed at which you deliver content.

In "[For Impatient Web Users, an Eye Blink Is Just Too Long to Wait](http://www.nytimes.com/2012/03/01/technology/impatient-web-users-flee-slow-loading-sites.html?pagewanted=all&_r=0 "http://www.nytimes.com/2012/03/01/technology/impatient-web-users-flee-slow-loading-sites.html?pagewanted=all&_r=0")," the New York
Times noted that users can register a 250-millisecond (1/4 second) difference between
competing sites. Users tend to opt out of the slower site in favor of the faster site. Tests
done at Amazon, cited in [How Webpage Load Time Is Related to Visitor Loss](http://pearanalytics.com/blog/2009/how-webpage-load-time-related-to-visitor-loss/ "http://pearanalytics.com/blog/2009/how-webpage-load-time-related-to-visitor-loss/"), revealed that for every
100-ms (1/10 second) increase in load time, sales decrease 1 percent.

If someone wants data, you can deliver that data much faster if it's cached. That's true
whether it's for a webpage or a report that drives business decisions. Can your
business afford to not cache your webpages so as to deliver them with the shortest latency
possible?

It might seem intuitively obvious that you want to cache your most heavily requested items.
But why not cache your less frequently requested items? Even the most optimized database
query or remote API call is noticeably slower than retrieving a flat key from an in-memory
cache. _Noticeably slower_ tends to send customers elsewhere.

The following examples illustrate some of the ways using ElastiCache can improve overall performance
of your application.

###### Topics

- [In-Memory Data Store](#elasticache-use-cases-data-store "#elasticache-use-cases-data-store")
- [Gaming Leaderboards](#elasticache-for-redis-use-cases-gaming "#elasticache-for-redis-use-cases-gaming")
- [Messaging (Pub/Sub)](#elasticache-for-redis-use-cases-messaging "#elasticache-for-redis-use-cases-messaging")
- [Recommendation Data (Hashes)](#elasticache-for-redis-use-cases-recommendations "#elasticache-for-redis-use-cases-recommendations")
- [Semantic caching for generative AI applications](#elasticache-for-redis-use-cases-semantic-caching "#elasticache-for-redis-use-cases-semantic-caching")
- [ElastiCache Customer Testimonials](#elasticache-use-cases-testimonials "#elasticache-use-cases-testimonials")

## In-Memory Data Store

The primary purpose of an in-memory key-value store is to provide ultrafast (submillisecond
latency) and inexpensive access to copies of data. Most data stores have areas of data
that are frequently accessed but seldom updated. Additionally, querying a database is
always slower and more expensive than locating a key in a key-value pair cache. Some
database queries are especially expensive to perform. An example is queries that involve
joins across multiple tables or queries with intensive calculations. By caching such
query results, you pay the price of the query only once. Then you can quickly retrieve
the data multiple times without having to re-execute the query.

### What Should I Cache?

When deciding what data to cache, consider these factors:

**Speed and expense** – It's always slower and more
expensive to get data from a database than from a cache. Some database queries are
inherently slower and more expensive than others. For example, queries that perform
joins on multiple tables are much slower and more expensive than simple, single
table queries. If the interesting data requires a slow and expensive query to get,
it's a candidate for caching. If getting the data requires a relatively quick
and simple query, it might still be a candidate for caching, depending on other
factors.

**Data and access pattern** – Determining what to cache
also involves understanding the data itself and its access patterns. For example, it
doesn't make sense to cache data that changes quickly or is seldom accessed.
For caching to provide a real benefit, the data should be relatively static and
frequently accessed. An example is a personal profile on a social media site. On the
other hand, you don't want to cache data if caching it provides no speed or
cost advantage. For example, it doesn't make sense to cache webpages that
return search results because the queries and results are usually unique.

**Staleness** – By definition, cached data is stale
data. Even if in certain circumstances it isn't stale, it should always be
considered and treated as stale. To tell whether your data is a candidate for
caching, determine your application's tolerance for stale data.

Your application might be able to tolerate stale data in one context, but not another. For
example, suppose that your site serves a publicly traded stock price. Your customers
might accept some staleness with a disclaimer that prices might be
_n_ minutes delayed. But if you serve that stock price to a
broker making a sale or purchase, you want real-time data.

Consider caching your data if the following is true:

- Your data is slow or expensive to get when compared to cache retrieval.
- Users access your data often.
- Your data stays relatively the same, or if it changes quickly staleness is not a large
  issue.

For more information, see [Caching strategies for Memcached](Strategies.md "Strategies.md")

## Gaming Leaderboards

With Valkey or Redis OSS sorted sets you can move the computational complexity of leaderboards from your application to
your cluster.

Leaderboards, such as the top 10 scores for a game, are computationally complex. This is
especially true when there is a large number of concurrent players and continually
changing scores. Valkey and Redis OSS sorted sets guarantee both uniqueness and element ordering.
With sorted sets, each time a new element is added to the sorted set it's reranked
in real time. It's then added to the set in its correct numeric order.

In the following diagram, you can see how an ElastiCache gaming leaderboard works.

![Image: ElastiCache Gaming leaderboard diagram](images/ElastiCache-Redis-Gaming.png)

###### Example Valkey or Redis OSS Leaderboard

In this example, four gamers and their scores are entered into a sorted list using
`ZADD`. The command `ZREVRANGEBYSCORE` lists the players
by their score, high to low. Next, `ZADD` is used to update June's score
by overwriting the existing entry. Finally, `ZREVRANGEBYSCORE` lists the
players by their score, high to low. The list shows that June has moved up in the
rankings.

```
ZADD leaderboard 132 Robert
ZADD leaderboard 231 Sandra
ZADD leaderboard 32 June
ZADD leaderboard 381 Adam

ZREVRANGEBYSCORE leaderboard +inf -inf
1) Adam
2) Sandra
3) Robert
4) June

ZADD leaderboard 232 June

ZREVRANGEBYSCORE leaderboard +inf -inf
1) Adam
2) June
3) Sandra
4) Robert
```

The following command tells June where she ranks among all the players. Because ranking is
zero-based, _ZREVRANK_ returns a 1 for June, who is in second
position.

```
ZREVRANK leaderboard June
1
```

For more information, see the [Valkey documentation](https://valkey.io/topics/sorted-sets/ "https://valkey.io/topics/sorted-sets/") about sorted sets.

## Messaging (Pub/Sub)

When you send an email message, you send it to one or more specified recipients. In the Valkey and Redis OSS
pub/sub paradigm, you send a message to a specific channel not knowing who, if anyone,
receives it. The people who get the message are those who are subscribed to the channel.
For example, suppose that you subscribe to the _news.sports.golf_
channel. You and all others subscribed to the _news.sports.golf_
channel get any messages published to _news.sports.golf_.

Pub/sub functionality has no relation to any key space. Therefore, it doesn't
interfere on any level. In the following diagram, you can find an illustration of ElastiCache
messaging with Valkey and Redis OSS.

![Image: ElastiCache messaging diagram](images/ElastiCache-Redis-PubSub.png)

### Subscribing

To receive messages on a channel, you subscribe to the channel. You can subscribe to a
single channel, multiple specified channels, or all channels that match a pattern.
To cancel a subscription, you unsubscribe from the channel specified when you
subscribed to it. Or, if you subscribed using pattern matching, you unsubscribe
using the same pattern that you used before.

###### Example- Subscription to a Single Channel

To subscribe to a single channel, use the SUBSCRIBE command specifying the channel you want to subscribe to.
In the following example, a client subscribes to the _news.sports.golf_ channel.

```
SUBSCRIBE news.sports.golf
```

After a while, the client cancels their subscription to the channel using the UNSUBSCRIBE command
specifying the channel to unsubscribe from.

```
UNSUBSCRIBE news.sports.golf
```

###### Example- Subscriptions to Multiple Specified Channels

To subscribe to multiple specific channels, list the channels with the SUBSCRIBE command.
In the following example, a client subscribes to the
_news.sports.golf_,
_news.sports.soccer_, and
_news.sports.skiing_ channels.

```
SUBSCRIBE news.sports.golf news.sports.soccer news.sports.skiing
```

To cancel a subscription to a specific channel, use the UNSUBSCRIBE command and specify
the channel to unsubscribe from.

```
UNSUBSCRIBE news.sports.golf
```

To cancel subscriptions to multiple channels, use the UNSUBSCRIBE command and specify the
channels to unsubscribe from.

```
UNSUBSCRIBE news.sports.golf news.sports.soccer
```

To cancel all subscriptions, use `UNSUBSCRIBE` and specify each channel. Or use
`UNSUBSCRIBE` and don't specify a channel.

```
UNSUBSCRIBE news.sports.golf news.sports.soccer news.sports.skiing
```

or

```
UNSUBSCRIBE
```

###### Example- Subscriptions Using Pattern Matching

Clients can subscribe to all channels that match a pattern by using the PSUBSCRIBE command.

In the following example, a client subscribes to all sports channels. You don't list all
the sports channels individually, as you do using `SUBSCRIBE`.
Instead, with the `PSUBSCRIBE` command you use pattern
matching.

```
PSUBSCRIBE news.sports.*
```

###### Example Canceling Subscriptions

To cancel subscriptions to these channels, use the `PUNSUBSCRIBE` command.

```
PUNSUBSCRIBE news.sports.*
```

###### Important

- The channel string sent to a [P]SUBSCRIBE command and to the [P]UNSUBSCRIBE command must
  match. You can't `PSUBSCRIBE` to \*news.\**
  and `PUNSUBSCRIBE` from *news.sports.\** or
  `UNSUBSCRIBE` from
  *news.sports.golf\*.
- `PSUBSCRIBE` and `PUNSUBSCRIBE` are not available for ElastiCache Serverless.

### Publishing

To send a message to all subscribers to a channel, use the `PUBLISH` command,
specifying the channel and the message. The following example publishes the message,
"It’s Saturday and sunny. I’m headed to the links." to the
_news.sports.golf_ channel.

```
PUBLISH news.sports.golf "It's Saturday and sunny. I'm headed to the links."
```

A client can't publish to a channel that it is subscribed to.

For more information, see [Pub/Sub](https://valkey.io/topics/pubsub "https://valkey.io/topics/pubsub") in the Valkey documentation.

## Recommendation Data (Hashes)

Using INCR or DECR in Valkey or Redis OSS makes compiling recommendations simple. Each time a user
"likes" a product, you increment an _item:productID:like_
counter. Each time a user "dislikes" a product, you increment an
_item:productID:dislike_ counter. Using hashes, you can
also maintain a list of everyone who has liked or disliked a product.

###### Example- Likes and Dislikes

```
INCR item:38923:likes
HSET item:38923:ratings Susan 1
INCR item:38923:dislikes
HSET item:38923:ratings Tommy -1
```

## Semantic caching for generative AI applications

Operating generative AI applications at scale can be challenging due to the cost and latency associated with inference calls to large language models (LLMs). You can use ElastiCache for semantic caching in generative AI applications, allowing you to reduce the cost and latency of LLM inference calls. With semantic caching, you can return a cached response by using vector-based matching to find similarities between current and prior prompts. If a user’s prompt is semantically similar to a prior prompt, a cached response will be returned instead of making a new LLM inference call, reducing the cost of generative AI applications and providing faster responses that improve the user experience. You can control which queries are routed to the cache by configuring similarity thresholds for prompts and applying tag or numeric metadata filters.

The inline real-time index updates provided by vector search for ElastiCache help ensure that the cache updates continuously as user prompts and LLM responses flow in. This real-time indexing is crucial to maintain freshness of cached results and cache hit rates, particularly for spiky traffic. In addition, ElastiCache simplifies operations for semantic caching through mature cache primitives such as per-key TTLs, configurable eviction strategies, atomic operations, and rich data structure and scripting support.

**Memory for generative AI assistants and agents**

You can use ElastiCache to deliver more personalized, context-aware responses by implementing memory mechanisms that surface cross-session conversation history to LLMs. Conversational memory allows generative AI assistants and agents to retain and use past interactions to personalize responses and improve relevancy. However, simply aggregating all prior interactions into the prompt is ineffective since irrelevant extra tokens increase cost, degrade response quality and risk exceeding the LLM’s context window. Instead, you can use vector search to retrieve and provide only the most relevant data in the context for each LLM invocation.

ElastiCache for Valkey provides integrations with open-source memory layers, providing built-in connectors to store and retrieve memories for LLM applications and agents. Vector search for ElastiCache provides fast index updates, keeping memory up to date and making new memories immediately searchable. Low latency vector search makes memory lookups fast, enabling them to be implemented in the online path of every request, not just background tasks. Beyond vector search, ElastiCache for Valkey also provides caching primitives for session state, user preferences, and feature flags, providing a single service to store short-lived session state and long-term “memories” in one datastore.

**Retrieval augmented generation (RAG)**

RAG is the process of providing LLMs with up-to-date information in the prompt to improve the relevance of responses. RAG reduces hallucinations and improves factual accuracy by grounding outputs with real-world data sources. RAG applications use vector search to retrieve semantically relevant content from a knowledge base. Low latency vector search provided by ElastiCache makes it suitable for implementing RAG in workloads that have large datasets with millions of vectors and above. Further, support for online vector index updates makes ElastiCache suitable for assistants with upload workflows that need to ensure any uploaded data is immediately searchable. RAG in agentic AI systems ensures that agents have up-to-date information for accurate actions. Low latency vector search is also crucial for RAG in agentic AI systems where a single query can trigger multiple LLM calls and stack up latency from underlying vector search.

The following diagram illustrates an example architecture using ElastiCache to implement a semantic cache, memory mechanisms, and RAG to enhance a generative AI application in production.

![Diagram of a semantic search as performed by a generative AI assistant.](images/vector-search-gen-ai1.png)

**Semantic Search**

Vector search retrieves the most relevant text, speech, image, or video data based on closeness in meaning or features. This capability enables machine learning applications that rely on similarity search across diverse data modalities, including recommendation engines, anomaly detection, personalization, and knowledge management systems. Recommendation systems use vector representations to capture complex patterns in user behavior and item characteristics, enabling them to suggest the most relevant content. Vector search for ElastiCache is well suited for these applications because of its near real-time updates and low latency, enabling similarity comparisons that deliver instant, highly relevant recommendations based on live user interactions.

## ElastiCache Customer Testimonials

To learn about how businesses like Airbnb, PBS, Esri, and others use Amazon ElastiCache to grow their
businesses with improved customer experience, see [How Others Use
Amazon ElastiCache](https://aws.amazon.com/elasticache/testimonials/ "https://aws.amazon.com/elasticache/testimonials/").

You can also watch the [Tutorial videos](Tutorials.md#tutorial-videos "Tutorials.md#tutorial-videos") for additional
ElastiCache customer use cases.
