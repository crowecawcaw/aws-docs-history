# GAMEREL03-BP02 Implement loose coupling of game features to

handle failures with minimal impact to player experience

Decoupling components refers to the concept of designing server
components so that they can operate as independently as possible.
Some aspects of gaming are difficult to decouple since data needs
to be as up to date as possible to provide a good in-game
experience for players. However, many components and gaming tasks
can be decoupled. For example, leaderboards and stats services are
not critical to the gameplay experience, and the reads and writes
to these services can be performed asynchronously from the game.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implement graceful degradation for features in your game that can
be disabled automatically or by an administrator if issues are
detected, as well as configure upstream services that depend on
the feature to be able to gracefully handle the failure. For
example, if specific player data is not properly loading within
your game client, you should consider whether this data is
critical to the gameplay experience. If not, configure the game
client to gracefully handle this failure without disrupting the
experience for the player, optioning to retry fetching this data
later when the player revisits the screen.

Employ logic such as timeouts, retries, and backoff to handle
errors and failures. Timeouts keep systems from hanging for
unreasonably long periods. Retries can provide high availability
of transient and random errors.

Define non-critical components which can be loosely coupled to
critical components. Loose coupling allows systems to be more
resilient since failure in one component does not cascade to
others. When game features do not require stateful connections to
your game servers or backend, you should implement stateless
protocols to scale dynamically and recover from transient
failures. Develop your non-critical components where it can be
loosely coupled with stateless protocols using an HTTP/JSON API.
Implement network calls from the game client to be asynchronous
and non-blocking to minimize the impact to players from
slow-performing game features or other dependent services.

To further improve resiliency through loose coupling, use a
messaging service such as a queuing, streaming, or a topic-based
system between components that can be handled asynchronously. This
model is suitable for an interaction that does not require an
immediate response or where an acknowledgment that a request has
been registered is sufficient. This solution involves one
component that generates events and another that consumes them.
The two components will not integrate through direct
point-to-point interaction but through an intermediate such as a
durable storage or queuing layer. This also assists to improve
system's reliability by preserving messages when processing fails.

Research and select an appropriate messaging mechanism, as various
messaging services have different characteristics, such as
ordering and delivery mechanisms. Design operations to be
idempotent so the chosen message system delivers messages at least
once. As an example, consider a typical game use case where your
game needs to track player playtime, stats, or other relevant data
which can lead to a high write-throughput use case at times of
peak player concurrency.

To implement a reliable architecture, consider whether the use
case requires read-after-write consistency as perceived by the
player. Typically, scenarios such as these are suitable for
asynchronous processing and can be achieved by implementing a
write-queueing pattern where the requests are ingested into a
scalable and durable message queue such as Amazon SQS and can be
inserted into your backend database in batches using a consumer
service, such as a Lambda function. This approach is more reliable
than synchronous communication between multiple distributed
components including the player's game client, your backend web
and application servers, and your internal database system. It
also reduces costs because the backend database does not need to
be scaled to meet peak write throughput since the consumer
processing from the write queue can be used to slow down this
ingestion rate as needed.

### Implementation steps

- Decouple non-critical components like leaderboards and stats
  services from critical gameplay features to allow
  asynchronous operations and enhance resiliency.
- Implement graceful degradation for non-critical features
  with logic for timeouts, retries, and backoff, and verify
  that the game client handles failures without disrupting the
  player experience.
- Use messaging systems like Amazon SQS for asynchronous
  communication between components, enabling scalable,
  durable, and reliable processing of high throughput use
  cases.

### Resources

- [Build
  highly scalable and reliable workloads using microservice
  architecture](../reliability-pillar/design-your-workload-service-architecture.md "../reliability-pillar/design-your-workload-service-architecture.md")
- [Integrating
  microservices by using AWS serverless services](../../../prescriptive-guidance/latest/modernization-integrating-microservices/welcome.md "../../../prescriptive-guidance/latest/modernization-integrating-microservices/welcome.md")
- [Understanding
  asynchronous messaging for microservices](https://aws.amazon.com/blogs/compute/understanding-asynchronous-messaging-for-microservices/ "https://aws.amazon.com/blogs/compute/understanding-asynchronous-messaging-for-microservices/")
- [Introduction
  to Scalable Game Development Patterns on AWS](https://d1.awsstatic.com/whitepapers/aws-scalable-gaming-patterns.pdf "https://d1.awsstatic.com/whitepapers/aws-scalable-gaming-patterns.pdf")
- Implementing
  [Graceful
  Degradation](../reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.md#:~:text=Implementing%20graceful%20degradation%20helps%20minimize%20the%20impact%20of,means%20considering%20potential%20failure%20modes%20during%20dependency%20design. "../reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.md#:~:text=Implementing%20graceful%20degradation%20helps%20minimize%20the%20impact%20of,means%20considering%20potential%20failure%20modes%20during%20dependency%20design.")
