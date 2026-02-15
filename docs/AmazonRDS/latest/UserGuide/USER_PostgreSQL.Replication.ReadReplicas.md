# Creating cross-Region

cascading read replicas with RDS for PostgreSQL

RDS for PostgreSQL supports cross-Region cascading read replicas. You can create a
cross-Region replica from the source DB instance, and then create same-Region replicas
from it. You can also create a same-Region replica from the source DB instance, and then
create cross-Region replicas from it.

###### Create a cross-Region replica and then create same-Region replicas

You can use an RDS for PostgreSQL DB instance with version 14.1 or higher,
`rpg-db-main`, to do the following:

1. Start with `rpg-db-main` (US-EAST-1), create the first cross-Region
   read replica in the chain, `read-replica-1` (US-WEST-2).
2. Using the first cross-Region `read-replica-1` (US-WEST-2), create
   the second read replica in the chain, `read-replica-2`
   (US-WEST-2).
3. Using `read-replica-2`, create the third read replica in the chain,
   `read-replica-3` (US-WEST-2).

###### Create a same-Region replica and then create cross-Region replicas

You can use an RDS for PostgreSQL DB instance with version 14.1 or higher,
`rpg-db-main`, to do the following:

1. Starting with `rpg-db-main` (US-EAST-1), create the first read
   replica in the chain, `read-replica-1` (US-EAST-1).
2. Using `read-replica-1` (US-EAST-1), create the first cross-Region
   read replica in the chain, `read-replica-2` (US-WEST-2).
3. Using `read-replica-2` (US-WEST-2), create the third read replica
   in the chain, `read-replica-3` (US-WEST-2).

###### Limitations in creating cross-Region read replicas

- A cross-Region cascading chain of database replicas can span a maximum of two
  Regions, with a maximum of four levels. The four levels include the database
  source and three read replicas.

###### Advantages of using cascading read replicas

- Improved read scalability – By distributing read queries across
  multiple replicas, cascading replication helps balance the load. This improves
  performance, especially in read-heavy applications, by reducing the strain on
  the writer database.
- Geographical distribution – Cascading replicas can be located in
  different geographic locations. This reduces latency for users located far from
  the primary database and provides a local read replica, enhancing performance
  and user experience.
- High availability and disaster recovery – In the event of a primary
  server failure, replicas can be promoted to primary, ensuring continuity.
  cascading replication further enhances this by providing multiple layers of
  failover options, improving the overall resilience of the system.
- Flexibility and modular growth – As the system grows, new replicas can
  be added at different levels without major reconfiguration of the primary
  database. This modular approach allows for scalable and manageable growth of the
  replication setup.

###### Best practice for using cross-Region read replicas

- Before promoting a replica, create additional replicas. This will save time,
  and provide efficient handling of the workload.
