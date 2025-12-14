# GAMEPERF05-BP02 Move non-latency-sensitive compute tasks to

asynchronous workflows

When you are optimizing the performance for your game, it is
important to keep in mind that only some of the interactions
between the client and the game backend must be performed in a
synchronous manner. You should consider each feature from the
perspective of the player experience and determine whether certain
interactions require synchronous communications, which are
blocking and resource intensive, or whether those features can be
implemented in an asynchronous manner. When you implement network
calls, use an asynchronous, non-blocking approach. Additionally,
your game backend should also be configured to perform work in an
efficient manner by offloading tasks to queues and prioritizing fast
responses to clients where possible.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For example, updating a leader board at the end of a player
session can be implemented asynchronously so that the client does
not need to wait for the leader board update to complete. Instead,
implement this asynchronously on the game client, and consider
designing your backend service to push these types of operations
into queues, such as Amazon SQS. With this architecture, configure
your backend to accept the request, enqueue it in SQS which helps
durably store messages for asynchronous processing, and promptly
reply to the client. When the leader board update is completed,
the backend can send an update to the game client so that the
player's view of the leader board is updated.

Alternatively, the player can simply visit your game's leader
board screen to retrieve the latest data, which can issue a web
request to your backend to retrieve the latest data from cache.

### Implementation steps

- Determine if client-backend interactions require synchronous
  communication; implement asynchronous, non-blocking
  approaches where possible to optimize resource usage.
- Use Amazon SQS to offload non-critical tasks like
  leaderboard updates.
- Allow the client to fetch updated data asynchronously, such
  as retrieving the latest leaderboard data on demand or via
  background updates.

### Resources

- [Understanding
  asynchronous messaging for microservices](https://aws.amazon.com/blogs/compute/understanding-asynchronous-messaging-for-microservices/ "https://aws.amazon.com/blogs/compute/understanding-asynchronous-messaging-for-microservices/")
- [Lambda

* Using service integrations and asynchronous
  processing](../../../lambda/latest/operatorguide/integrations-asynchronous.md "../../../lambda/latest/operatorguide/integrations-asynchronous.md")
