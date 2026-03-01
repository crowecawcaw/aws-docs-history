# Prerequisites and limitations

Before getting started with global datastores, be aware of the following:

- Global datastores are supported in the following AWS Regions:
  - **Africa** - Cape Town
  - **Asia Pacific** - Hong Kong, Hyderabad, Jakarta,
    Malaysia, Melbourne, Mumbai, Osaka, Seoul, Singapore, Sydney, Thailand, and Tokyo
  - **Canada** - Canada Central and Canada West (Calgary)
  - **China** - Beijing and Ningxia
  - **Europe** - Frankfurt,
    London, Ireland, Milan, Paris, Spain, Stockholm, and Zurich
  - **AWS GovCloud** -US-West and
    US-East
  - **Israel** - Tel Aviv
  - **Middle East** - Bahrain and UAE
  - **US** - East (N. Virginia and Ohio) and US West (N.
    California and Oregon)
  - **South America** - Mexico (Central) and São Paulo

- All clusters—primary and secondary—in your global datastore should
  have the same number of primary nodes, node type, engine version, and number of
  shards (in case of cluster-mode enabled). Each cluster in your global datastore can
  have a different number of read replicas to accommodate the read traffic local to
  that cluster.

Replication must be enabled if you plan to use an existing single-node
cluster.

- Global datastores are supported on the following instance families in size
  large and above: M5, M6g, M7g, R5, R6g, R6gd, R7g, and C7gn. Previous generation
  instance types (such as M4 and R4) are not supported.
- You can set up replication for a primary cluster from one AWS Region to a
  secondary cluster in up to two other AWS Regions.

###### Note

The exception to this are China (Beijing) Region and China (Ningxia) regions,
where replication can only occur between the two regions.

- You can work with global datastores only in VPC clusters. For more information,
  see [Access Patterns for Accessing an ElastiCache Cache in an Amazon VPC](elasticache-vpc-accessing.md "elasticache-vpc-accessing.md"). Global datastores aren't supported
  when you use EC2-Classic. For more information, see [EC2-Classic](../../../AWSEC2/latest/UserGuide/ec2-classic-platform.md "../../../AWSEC2/latest/UserGuide/ec2-classic-platform.md") in the _Amazon EC2 User Guide._

###### Note

At this time, you can't use global datastores in [Using local zones with ElastiCache](Local_zones.md "Local_zones.md").

- ElastiCache doesn't support autofailover from one AWS Region to another. When
  needed, you can promote a secondary cluster manually. For an example, see [Promoting the secondary cluster to primary](Redis-Global-Datastores-Console.md#Redis-Global-Datastores-Console-Promote-Secondary "Redis-Global-Datastores-Console.md#Redis-Global-Datastores-Console-Promote-Secondary").
- To bootstrap from existing data, use an existing cluster as primary to create a
  global datastore. We don't support adding an existing cluster as secondary. The
  process of adding the cluster as secondary wipes data, which may result in data loss.
- Parameter updates are applied to all clusters when you modify a local parameter
  group of a cluster belonging to a global datastore.
- You can scale regional clusters both vertically (scaling up and down) and
  horizontally (scaling in and out). You can scale the clusters by modifying the global
  datastore. All the regional clusters in the global datastore are then scaled without
  interruption. For more information, see [Scaling ElastiCache](Scaling.md "Scaling.md").
- Global datastores support [encryption at rest](at-rest-encryption.md "at-rest-encryption.md"),
  [encryption in transit](in-transit-encryption.md "in-transit-encryption.md"), and [AUTH](auth.md "auth.md").
- Global datastores doesn't support Internet Protocol version 6 (IPv6).
- Global datastores support AWS KMS keys. For more information, see [AWS
  key management service concepts](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys") in the
  _AWS Key Management Service Developer Guide._

###### Note

Global datastores support [pub/sub messaging](../red-ug/elasticache-use-cases.md#elasticache-for-redis-use-cases-messaging "../red-ug/elasticache-use-cases.md#elasticache-for-redis-use-cases-messaging") with the following stipulations:

- For cluster-mode disabled, pub/sub is fully supported. Events published on the
  primary cluster of the primary AWS Region are propagated to secondary AWS
  Regions.
- For cluster mode enabled, the following applies:
  - For published events that aren't in a keyspace, only subscribers in the
    same AWS Region receive the events.
  - For published keyspace events, subscribers in all AWS Regions receive
    the events.
