# Data tiering limitations

Data tiering has the following limitations:

- The node type you use must be from the r6gd family, which is available in the following regions:
  `us-east-2`, `us-east-1`, `us-west-2`, `us-west-1`, `eu-west-1`, `eu-west-3`,
  `eu-central-1`, `ap-northeast-1`, `ap-southeast-1`, `ap-southeast-2`,
  `ap-south-1`, `ca-central-1` and `sa-east-1`.
- You cannot restore a snapshot of an r6gd cluster into another cluster unless it also uses r6gd.
- You cannot export a snapshot to Amazon S3 for data-tiering clusters.
- Forkless save is not supported.
- Scaling is not supported from a data tiering cluster (for example, a cluster using an r6gd node type) to a cluster that does not use data tiering (for example, a cluster using an r6g node type).
- Data tiering only supports `volatile-lru`, `allkeys-lru` and `noeviction` maxmemory policies.
- Items larger than 128 MiB are not moved to SSD.
