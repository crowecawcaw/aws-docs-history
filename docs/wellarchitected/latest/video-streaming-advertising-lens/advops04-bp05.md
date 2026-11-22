

# ADVOPS04-BP05 Implement event-driven automation for ad placement decisions across linear logs and digital bid streams

 Deploy event-driven architectures that react to state changes in linear broadcast schedules and digital programmatic bid streams to automate ad placement decisions in real time. Use loosely coupled microservices with asynchronous event processing for deterministic, scalable ad serving across converged environments. 

 **Desired outcome:** 
+  Ad placement decisions are triggered automatically by events (SCTE-35 signals from linear playout, schedule changes from traffic systems, and bid requests from programmatic exchanges) without manual intervention. 
+  The system correlates linear and digital inventory availability in real time, optimizes placement across channels, and distributes decisions to downstream fulfillment systems with sub-second latency. 

 **Common anti-patterns:** 
+  Processing linear schedule changes and digital bid requests through separate, disconnected automation pipelines with no ability to optimize placement decisions across channels simultaneously. 
+  Using synchronous, tightly coupled point-to-point integrations between ad decisioning components that create cascading failures when any single system is unavailable. 
+  Relying on batch-processed linear broadcast logs (daily reconciliation) rather than real-time event ingestion, limiting in-flight optimization of cross-channel campaigns. 
+  Deploying ad decisioning logic without provisioned concurrency or warm execution environments, resulting in cold-start latency that exceeds bid response SLAs. 

 **Benefits of establishing this best practice:** 
+  Event-driven architectures enable real-time responsiveness to inventory changes across both linear and digital channels, maximize yield through cross-channel optimization, and provide resilience through loose coupling. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 In advertising, the system does not control its own deadlines. An RTB auction closes on the exchange's schedule, and a linear avail arrives with the SCTE-35 splice point. The decisioning system cannot finish late. A late answer means that the break airs with slate or house inventory, and the impression cannot be sold retroactively. Because the deadline is external, decide which computations run synchronously inside it and which (pacing recalculation, reconciliation, reporting, and creative refresh) can trail behind. 

 Asynchronous messaging gives you loose coupling by giving up guarantees that placement logic depends on. At-least-once delivery means the same avail notification or bid event will occasionally arrive twice. A pipeline that isn't idempotent can promise the same pod position to two buyers or count the same impression twice against a campaign budget. Pacing and budget arithmetic assume a coherent sequence of spend events. Events from independent sources (a traffic system's schedule change, a bid confirmation from an exchange) have no global order. A cancellation can be processed before the placement it cancels, and a budget decrement can land after the check that needed it. Treat decision identifiers that make duplicates detectable, and pacing state built from commutative updates rather than assumed sequence, as core requirements. Without them, correctness holds only under light traffic, where duplicates and reordering rarely occur. 

 Unrecorded load shedding is the hardest failure mode to detect. Bid volume during a live event or premiere can spike well beyond planned capacity. Every point where the pipeline sheds pressure (throttled consumers, expired messages, or dropped events) goes unrecorded in the data the pacing controllers rely on. A controller reading a delivery count below what occurred treats the campaign as behind and accelerates spend. The books are then wrong in a way that increases spend, and no alarm fires because nothing failed. Shedding load is legitimate (answering an auction with a no-bid is often correct under pressure), but it must be an explicit, counted decision so downstream arithmetic reflects what occurred. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy Amazon EventBridge as the central event bus for linear broadcast events:** Create custom EventBridge event buses for linear schedule events. Configure Lambda integrations that receive SCTE-35-triggered ad avail notifications from AWS Elemental MediaLive and translate them into structured EventBridge events. Define EventBridge rules that route linear schedule change events to the appropriate ad decisioning workflows based on content type, channel, and ad avail characteristics. 

1.  **Configure Amazon Kinesis Data Streams for high-throughput digital bid stream ingestion:** Deploy Kinesis Data Streams with partition keys set to publisher/placement ID for ordered, parallelized processing. Use the Kinesis Producer Library (KPL) for asynchronous publishing with backpressure handling. Configure enhanced fan-out consumers for low-latency, dedicated throughput for the ad decisioning pipeline. 

1.  **Implement AWS Step Functions Express Workflows for multi-step ad placement decisioning:** Create Express Workflow state machines for the ad placement decision sequence: (1) inventory availability check, (2) audience segment matching, (3) bid evaluation against floor prices, (4) placement selection and confirmation. Use synchronous execution for real-time bid response paths (within the RTB auction window) and asynchronous execution for linear schedule optimization (which can tolerate higher latency). Configure Step Functions to automatically retry transient failures with exponential backoff. 

1.  **Deploy AWS Lambda with provisioned concurrency for time-critical decisioning:** Configure provisioned concurrency on Lambda functions that handle real-time bid responses, helping achieve double-digit millisecond response times without cold-start overhead. Provision concurrency based on expected peak concurrent bid request volume, with Application Auto Scaling configured to adjust provisioned concurrency based on CloudWatch scheduled actions for predictable traffic patterns (primetime). 

1.  **Implement Amazon SNS fan-out for placement decision distribution:** Configure Amazon SNS topics to distribute finalized ad placement decisions to downstream fulfillment systems: linear playout automation (receives decisions for upcoming ad breaks), DSP bid response handlers (receives decisions formatted as OpenRTB responses), and reporting pipelines (receives decisions for real-time pacing and revenue reporting). Use FIFO SNS topics with SQS FIFO queues for ordered delivery of linear schedule updates where sequencing matters. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [AWS Event-Driven Media Workflow Automation guidance](https://aws.amazon.com/solutions/guidance/event-driven-media-workflow-automation-on-aws/) 
+  [Guidance for Capturing Advertising OpenRTB (Real-Time Bidding) Events for Analytics on AWS](https://docs.aws.amazon.com/solutions/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/) 
+  [Amazon EventBridge documentation and best practices](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 

 **Related services:** 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 