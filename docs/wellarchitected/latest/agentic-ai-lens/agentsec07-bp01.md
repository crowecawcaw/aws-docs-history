

# AGENTSEC07-BP01 Implement cognitive load management
<a name="agentsec07-bp01"></a>

 A human reviewer is only as effective as the workload lets them be. Prioritization, queue management, and maximum review rates keep human oversight grounded in genuine judgment rather than fatigue-driven rubber-stamping. 

 **Desired outcome:** 
+  Human reviewers receive a manageable volume of well-prioritized decisions, with sufficient context and time to make informed judgments. 
+  You monitor review queues for backlog accumulation, with automatic escalation or load balancing helping prevent any single reviewer from being overwhelmed. 
+  Review quality metrics detect signs of rubber-stamping that indicate cognitive overload. 

 **Common anti-patterns:** 
+  Routing all agent decisions requiring review to a single queue without prioritization, so high-priority security decisions wait behind routine approvals. 
+  Not monitoring reviewer workload or queue depth, letting backlogs accumulate silently until reviewers begin approving without adequate evaluation. 
+  Setting no maximum review rate per person, so a single reviewer can be assigned an unlimited number of decisions in a short period. 

 **Benefits of establishing this best practice:** 
+  Workload management keeps reviewers in a position to make genuine, informed decisions rather than rubber-stamping under pressure. 
+  Review quality metrics (average review time, approval rate) surface when the oversight process is breaking down, enabling intervention before it fails silently. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Amazon SQS standard queues don't support priority ordering natively, so the prioritization layer has to sit above the queue. A coarse-grained option is separate Amazon SQS queues per priority tier (high, medium, low), where the assignment function polls high-priority first and falls back to lower tiers only when the upper one is empty. A more flexible option uses a single ingest queue consumed by an AWS Lambda function that classifies each request by priority and writes it to an Amazon DynamoDB table with a sort key based on priority and submission time. The reviewer assignment function queries DynamoDB for the highest-priority unassigned items, marks them as assigned, and delivers them to the reviewer. The DynamoDB pattern gives you full control over prioritization logic, supports re-prioritization of pending items, and keeps a durable record of all review requests regardless of their current state. Items that are not immediately assigned stay in DynamoDB rather than sitting in a queue with an expiring visibility timeout. 

 Priority classification is about potential impact of the action proceeding incorrectly: the more damaging a mistaken approval would be, the higher the priority. Concrete factors include data sensitivity (PII, financial records, healthcare information), reversibility (deletes, external communications, and financial transactions can't be undone), whether the action is a first-time operation for this agent (no behavioral baseline, so reviewers can't pattern-match to shortcut judgment, and the first-time operation is itself a signal worth investigating), and time sensitivity (operations that become harder to reverse over time, or where delay has its own cost). Automate the classification by tagging review requests with metadata from the agent's tool invocation context, data classification tags on target resources, and the agent's historical usage patterns. 

 Amazon CloudWatch watches the DynamoDB review table for backlog accumulation (unassigned items by priority tier), average time-to-assignment, and average time-to-decision. Alarms fire on high-priority items remaining unassigned beyond defined thresholds. 

 Reviewer load balancing distributes decisions across available reviewers based on current workload. Amazon DynamoDB tracks reviewer assignment counts and availability, and an AWS Lambda-based assignment function routes new decisions to the reviewer with the lowest current load. Configure maximum assignment limits per reviewer per time window to help prevent overload. 

 Review quality metrics are the trailing indicator. Track average review time, approval rate, and decision reversal rate (cases where a second reviewer overrides the first), publish the metrics to Amazon CloudWatch, and alarm on patterns that suggest rubber-stamping: unusually short review times or abnormally high approval rates during periods of high queue volume. Automatic escalation routes unreviewed decisions past defined time thresholds to senior reviewers, or triggers a safe default (typically blocking the operation) to help prevent indefinite delays. 

 Approval bounds, how long an approval remains valid, whether it can be revoked, whether high-risk operations require step-up re-confirmation, are covered in AGENTSEC04-BP02, which details the persistent-trust patterns that determine the scope and lifetime of each approval decision. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up the ingest-classify-store pipeline:** Use an Amazon SQS ingest queue, an AWS Lambda classifier that assigns priority, and an Amazon DynamoDB review table with a sort key on priority and submission time. 

1.  **Build the reviewer assignment function:** Query the DynamoDB table for the highest-priority unassigned items, mark them as assigned, and deliver them to the appropriate reviewer. 

1.  **Cap assignments per reviewer and escalate:** Set maximum review assignment limits per reviewer per time window and configure automatic escalation when limits are reached or high-priority items age beyond thresholds. 

1.  **Measure review quality:** Track average review time, approval rate, and reversal rate in Amazon CloudWatch, and configure alarms on patterns that suggest rubber-stamping. 

1.  **Monitor the review table:** Alarm on backlog accumulation by priority tier, average time-to-assignment, and average time-to-decision, and alert when high-priority items age beyond thresholds. 

1.  **Review load metrics periodically:** Use cognitive load metrics to refine prioritization logic and reviewer capacity planning on a regular cadence. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC04-BP02 Human-in-the-loop for critical decisions](agentsec04-bp02.html) 
+  [AGENTSEC07-BP03 Multiple reviewers for critical operations](agentsec07-bp03.html) 
+  [AGENTSEC07-BP04 Behavioral anomaly detection and agent containment](agentsec07-bp04.html) 

 **Related documents:** 
+  [Amazon SQS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) 
+  [AWS Step Functions human approval](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html) 
+  [Implement human-in-the-loop confirmation with Amazon Bedrock Agents](https://aws.amazon.com/blogs/machine-learning/implement-human-in-the-loop-confirmation-with-amazon-bedrock-agents/) 

 **Related services:** 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 