# Quorum queues for RabbitMQ on Amazon MQ

Quorum queues are a replicated queue type made up of a leader (primary replica) and followers (other replicas).
If the leader becomes unavailable, quorum queues uses the
[Raft](https://raft.github.io/ "https://raft.github.io/") consensus algorithm
to elect a new leader node by majority of votes,
and the previous leader is demoted to a follower node in the same cluster.
The remaining followers continue replicating as before. Because each node is in a different availability zone, if one node
is temporarily unavailable, message delivery continues with the newly
elected leader replica in another availability zone.

Quorum queues are useful for handling poison messages,
which occur when a message fails and is requeued multiple times.

You should not use quorum queues if you:

- use transient queues
- have long queue backlogs
- prioritize low latency

To declare a quorum queue, set the header `x-queue-type` to `quorum`.

###### Topics

- [Migrating from classic queues to quorum queues on Amazon MQ for RabbitMQ](quorum-queues-migration.md "quorum-queues-migration.md")
- [Policy configurations for quorum queues for Amazon MQ for RabbitMQ](quorum-queues-policy-configurations.md "quorum-queues-policy-configurations.md")
- [Best practices for quorum queues for Amazon MQ for RabbitMQ](quorum-queues-best-practices.md "quorum-queues-best-practices.md")
