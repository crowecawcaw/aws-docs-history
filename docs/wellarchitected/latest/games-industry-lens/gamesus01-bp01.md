# GAMESUS01-BP01 Use storage technologies that fit the patterns adapted to user content, subscriber information, and in-game purchases

You should classify your data by type, retention need and frequency
of access. This enables you to select the most optimized storage
solution for the myriad data types of your game or backend services
produce. Fast changing data should be stored in key-value or
in-memory database services. Transactional data should be store in
relational database services. Large files, game assets, or
user-generated content should be stored in object storage services.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Games produce and consume a large variety of data types that
require storage solutions optimized for frequency of access,
latency, and cost. Data stored should be classified using tags to
differentiate data that can be removed or needs to be stored
long-term.

The following services work well for a variety of Games use-cases:

[Amazon Aurora](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/") (compatible with MySQL and PostgreSQL) offers high
availability, low-latency, and automatic scaling, making it an
excellent choice for handling large amounts of transactional data,
such as player account management and authentication, in-game
economies, leaderboards and player rankings, game state
persistence, event and campaign management, and multi-Region and
high-availability deployment.

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") is a fully managed NoSQL database known for its
low-latency, high throughput, and seamless scalability, which
makes it ideal for handling real-time player data, session
management, inventory, in-game economy, real-time multiplayer game
state, matchmaking, event logging, and scaling for global
audience.

[Amazon DocumentDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/") (compatible with MongoDB) provides a scalable,
low-latency document-oriented database service, perfect for
storing flexible, semi-structured data, such as inventory system,
player profiles and customization's, game worlds and procedurally
generated content, social and player interactions, analytics and
behavior tracking, and in-game metadata and configurations.

[Amazon ElastiCache](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/") supports in-memory caching with Redis or
Memcached, offering rapid data access and reduced response times,
which is critical for real-time multiplayer games where speed and
performance are essential for a smooth user experience.
ElastiCache is utilized in gaming for real-time leaderboards,
session management, caching game metadata, in-game chat and
messaging, matchmaking, real-time analytics and telemetry, and
scaling for high-traffic events.

[Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/?nc=sn&loc=0 "https://aws.amazon.com/s3/?nc=sn&loc=0") can be used to store objects
like game assets, videos, pictures, text log files and more. S3 is
an object storage service offering industry-leading scalability,
data availability, security, and performance.

If it offers multiple storage classes that support frequent and
in-frequent data access, and cost-effective archive storage. For
data that is frequently accessed throughout development, studios
should store objects in
[S3
Standard](https://aws.amazon.com/s3/storage-classes/?nc=sn&loc=3 "https://aws.amazon.com/s3/storage-classes/?nc=sn&loc=3") for low latency and high throughput performance.
For data that frequently goes from hot to cold or vice versa,
studios should investigate
[S3
Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/ "https://aws.amazon.com/s3/storage-classes/intelligent-tiering/"). Intelligent-Tiering monitors the
access patterns of your data and automatically moves data to the
most cost-effective access tier.

For studios that need high throughput, low latency and are ok with
it living in a single Availability Zone use
[S3
Express One Zone.](https://aws.amazon.com/s3/storage-classes/express-one-zone/ "https://aws.amazon.com/s3/storage-classes/express-one-zone/") This replicates data to a single AZ and
can improve data access speeds compared to S3 standard. For deep
archive needs of historical data Amazon also offers
[Amazon Glacier.](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/") The Amazon Glacier storage classes are
purpose-built for data archiving, providing you with high
performance, retrieval flexibility, and low cost archive storage
in the cloud.

[Amazon Elastic Block Store](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/") can be used to store game servers' binaries,
executable files and configurations your game servers or asset
repositories need to function. You should snapshot and delete
unused volumes that are not attached to an EC2 instance. This
alleviates you from storage charges incurred while lowering the
usage of unneeded services and hardware.

### Implementation steps

- Classify game data by type, retention needs, and access
  frequency, tagging data to distinguish between short-term
  and long-term storage requirements.
- Use Amazon Aurora for transactional data, DynamoDB for
  real-time player data, DocumentDB for semi-structured data,
  and ElastiCache for low-latency caching of time-critical
  game information.
- Store game assets, logs, and user-generated content in
  Amazon S3, selecting appropriate storage classes (for
  example, Intelligent-Tiering, One Zone, and Glacier) based
  on access patterns and archive needs, and use EBS for game
  server binaries and configurations with regular snapshot
  management.
