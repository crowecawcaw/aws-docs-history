

# Consume records from a stream with queues

A queue delivers records from an On-demand Kinesis data stream to a queue consumer and tracks the delivery state of each record. A queue works alongside your existing stream consumers and requires no changes to your producers. A queue counts as one registered consumer and shares the stream's registered consumer limit with enhanced fan-out consumers.

A queue consumer receives records with `ReceiveQueueRecords`, which returns up to 10 records at a time, processes them, and acknowledges the records it successfully processes by calling `AcknowledgeQueueRecords`, up to 10 per call. A queue delivers each record at least once: it redelivers any record that is not acknowledged before its visibility timeout expires, and in rare cases it can deliver a record again after you acknowledge it. Design your queue consumer to be idempotent, so that processing the same record more than once is safe. A queue also does not necessarily deliver records in the order that producers wrote them to the stream. Dead-letter handling is built into every queue, so a record that is received too many times without an acknowledgment becomes a dead-letter record that you handle through a separate set of operations. A queue can deliver a record only while the stream still retains it, so a record that is never acknowledged, including a dead-letter record, expires when the stream's retention period ends for that record.

**Topics**
+ [Supported AWS Regions](#queues-supported-regions)
+ [Consume records with a queue](queues-overview.md)
+ [How queues work](queues-how-queues-work.md)
+ [Get started with queues using the AWS CLI](queues-getting-started.md)
+ [Manage queues in the console](queues-console.md)
+ [Handle dead-letter records in a queue](queues-dead-letter-records.md)
+ [Monitor a queue](queues-monitoring.md)
+ [IAM permissions for queues](queues-iam.md)
+ [Quotas and limits for queues](queues-quotas.md)

## Supported AWS Regions
<a name="queues-supported-regions"></a>

You can create a queue in the following AWS Regions.


| Region code | Region name | 
| --- | --- | 
| af-south-1 | Africa (Cape Town) | 
| ap-east-1 | Asia Pacific (Hong Kong) | 
| ap-east-2 | Asia Pacific (Taipei) | 
| ap-northeast-1 | Asia Pacific (Tokyo) | 
| ap-northeast-2 | Asia Pacific (Seoul) | 
| ap-northeast-3 | Asia Pacific (Osaka) | 
| ap-south-1 | Asia Pacific (Mumbai) | 
| ap-south-2 | Asia Pacific (Hyderabad) | 
| ap-southeast-1 | Asia Pacific (Singapore) | 
| ap-southeast-2 | Asia Pacific (Sydney) | 
| ap-southeast-3 | Asia Pacific (Jakarta) | 
| ap-southeast-4 | Asia Pacific (Melbourne) | 
| ap-southeast-5 | Asia Pacific (Malaysia) | 
| ap-southeast-6 | Asia Pacific (New Zealand) | 
| ap-southeast-7 | Asia Pacific (Thailand) | 
| ca-central-1 | Canada (Central) | 
| ca-west-1 | Canada West (Calgary) | 
| eu-central-1 | Europe (Frankfurt) | 
| eu-central-2 | Europe (Zurich) | 
| eu-north-1 | Europe (Stockholm) | 
| eu-south-1 | Europe (Milan) | 
| eu-south-2 | Europe (Spain) | 
| eu-west-1 | Europe (Ireland) | 
| eu-west-2 | Europe (London) | 
| eu-west-3 | Europe (Paris) | 
| il-central-1 | Israel (Tel Aviv) | 
| sa-east-1 | South America (São Paulo) | 
| us-east-1 | US East (N. Virginia) | 
| us-east-2 | US East (Ohio) | 
| us-west-1 | US West (N. California) | 
| us-west-2 | US West (Oregon) | 