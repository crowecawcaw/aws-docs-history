# Cross-Region data replication for Amazon MQ for ActiveMQ

Amazon MQ for ActiveMQ offers a Cross-Region data replication (CRDR) feature that allows for asynchronous message replication
from the primary broker in
a primary AWS Region to the replica broker in a replica Region. By issuing a failover request to the Amazon MQ API,
the current replica broker is promoted to the primary broker role, and the current primary broker is demoted to the replica role.

## Primary and replica brokers for cross-Region data replication

You can create primary and replica brokers for asynchronous data replication from the primary broker in
a primary AWS Region to the replica broker in a replica Region. The _primary Region_
consists of a redundant pair of active/standby brokers referred to as the _primary broker_.
The _secondary Region_ consists of a redundant pair of active/standby brokers referred to
as the _replica broker_.

The following diagram illustrates a replica broker in a secondary Region receiving asynchronous replicated
data from the primary broker in the primary Region.

![Diagram showing primary and replica brokers in different AWS regions with replication traffic flow.](images/primary-replica-connection.png)

Primary and replica brokers act as a cross-Region data recovery solution.
If the primary broker in the primary Region fails, you can promote the replica broker in the
secondary Region to primary by initiating a switchover or failover. The former primary broker then becomes
the replica broker, and the former replica broker is promoted to primary broker. For instructions on creating
a primary and replica broker, see [Creating an Amazon MQ cross-Region data replication broker](create-replica-broker.md "create-replica-broker.md").

###### Note

Only available for active/standby brokers.

Not available for mirrored queues.
