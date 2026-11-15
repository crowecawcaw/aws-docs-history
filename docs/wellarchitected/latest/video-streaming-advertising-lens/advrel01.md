

# Design for reliability and change management
<a name="advrel01"></a>

 Advertising systems require architectural decisions that determine how failures propagate, how quickly revenue recovers, and whether code changes introduce new failure modes under production traffic. Architecture choices (event-driven compared to synchronous, per-component recovery objectives, and elastic scaling) directly affect whether a single partner outage cascades into total auction failure or is absorbed without revenue impact. Change management choices (testing depth, deployment topology, and rollback authority) determine whether a new release improves reliability or degrades it undetected during peak campaign hours. 


|  ADVREL01: How do you design and evolve your advertising workload to be resilient, scalable, and recoverable while managing changes safely?  | 
| --- | 
| [ADVREL01-BP01 Use loosely-coupled architectures to enable graceful recovery from failures](advrel01-bp01.md) | 
| [ADVREL01-BP02 Architect your system with appropriate recovery objectives](advrel01-bp02.md) | 
| [ADVREL01-BP03 Architect for variable demand](advrel01-bp03.md) | 
| [ADVREL01-BP04 Implement chaos engineering practices](advrel01-bp04.md) | 
| [ADVREL01-BP05 Through your CI/CD pipeline, implement regression, performance, and canary tests](advrel01-bp05.md) | 
| [ADVREL01-BP06 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful](advrel01-bp06.md) | 

## Capability intent
<a name="advrel01-capability-intent"></a>
+  Your advertising workloads use loosely coupled architectures ([Amazon EventBridge](https://aws.amazon.com/eventbridge/), [Amazon SQS](https://aws.amazon.com/sqs/), [Amazon SNS](https://aws.amazon.com/sns/)) that isolate failures to individual services rather than cascading across the auction pipeline. 
+  Recovery objectives (RPO and RTO) are defined per component based on business criticality: auction-path services carry sub-minute targets, analytics and reporting tolerate minutes to hours. 
+  Your architecture elastically scales to absorb peak advertising events (live sports, tentpole campaigns, and flash crowds) using [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) predictive policies and pre-warmed capacity. 
+  Chaos engineering experiments using [AWS Fault Injection Service](https://aws.amazon.com/fis/) run quarterly to discover new failure modes before they affect production campaigns. 
+  Your CI/CD pipeline includes end-to-end regression testing, performance benchmarks against bidding SLO baselines, and canary validation before changes reach production. 
+  Deployments use phased strategies (blue/green, rolling) with automated rollback triggered by [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms on 5xx error rates and p99 latency. 

## Common issues to watch for
<a name="advrel01-common-issues-to-watch-for"></a>
+  Tightly coupled service dependencies where a single component failure cascades across the entire auction pipeline, converting a partner outage into total revenue loss. 
+  Over-architecting with multiple layers of redundancy when the business criticality doesn't justify it, inflating cost without proportional reliability benefit. 
+  Applying the same RPO/RTO to all advertising components regardless of business criticality (analytics compared to real-time bidding), leading to over-investment in low-criticality recovery or under-investment in high-criticality paths. 
+  Discovering faults for the first time during production incidents rather than through controlled [AWS FIS](https://aws.amazon.com/fis/) chaos experiments. 
+  Deploying changes to all auction servers simultaneously without canary validation, creating a window where a latent defect affects 100% of traffic before detection. 
+  Not testing performance in CI/CD, so a change that passes all functional tests but introduces a 5ms regression in bid evaluation can exceed the bid response SLO undetected. 