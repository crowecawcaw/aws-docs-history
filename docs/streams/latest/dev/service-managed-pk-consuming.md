

# Read records from service-managed streams

Consumers reading from service-managed streams use the same APIs as streams with user-managed partition keys. The primary difference is in how the `PartitionKey` field appears in the response. Consumers continue to read records from shards in sequence regardless of the distribution strategy.