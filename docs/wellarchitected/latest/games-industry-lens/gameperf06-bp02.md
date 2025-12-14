# GAMEPERF06-BP02 Categorize and store game data based on access

patterns

Categorize your game data into different types based on their
access patterns and storage requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Common categories
include player data, game saves, persistent world storage, and
analytics data.

### Implementation steps

Use appropriate storage solutions for each data type to optimize
performance and cost-efficiency:

- **Player data:** Use Amazon DynamoDB, a fast and scalable NoSQL database, to store
  player profiles, preferences, and progression data. The
  low-latency access and automatic scaling capabilities of
  DynamoDB provide efficient retrieval and update of player
  data.
- **Game saves:** Use Amazon S3
  to store game saves and checkpoints. S3 provides high
  durability and scalability for storing large amounts of game
  save data. Consider using S3 Transfer Acceleration or Amazon CloudFront for faster uploads and downloads of game saves.
- **Persistent world storage:**
  For games with persistent world states or shared game data,
  consider using Amazon DynamoDB, Amazon ElastiCache or Amazon MemoryDB. ElastiCache and MemoryDB provide in-memory
  key-value store while DynamoDB is an SSD backed NoSQL
  database. These services provide fast access to stored data,
  reducing the time it takes for the game server process to
  save game state which improves overall process performance.
- **Analytics data:** Use
  Amazon Managed Streaming for Apache Kafka or Kinesis Data Streams
  to ingest data streams from your game data producers. Amazon
  Managed Service for Apache Flink can be used for real-time
  transformation and analysis and sent to Amazon Data Firehose
  for processing and delivery into backend data lakes,
  warehouses and analytics services.
  [Guidance
  for Game Analytics Pipeline on AWS](https://aws.amazon.com/solutions/guidance/game-analytics-pipeline-on-aws/ "https://aws.amazon.com/solutions/guidance/game-analytics-pipeline-on-aws/") illustrates how
  the services work together to provide near real-time and
  batch analytics.
