

# Recall and warranty management
<a name="recall-warranty-management"></a>

Recall and warranty management turns blanket recalls into targeted service and manual warranty claims into automatic recovery. It matches each recall to the vehicles it affects, uses telemetry to separate vehicles that show the defect from vehicles that only match by VIN, and catches component failures that are still under warranty.

## What it can do
<a name="rwm-what-it-can-do"></a>
+  **Recall dashboard** — active recalls, affected vehicle counts, severity, and completion progress.
+  **Confirmed and population vehicles** — each affected vehicle is classified as `CONFIRMED`, where telemetry shows the defect, or `POPULATION`, where only the VIN range matches.
+  **Affected-vehicle map** — affected vehicles and the nearest dealers with parts available, on an Amazon Location Service map.
+  **Warranty dashboard** — warranty-eligible failures, open claims, and recovered totals.
+  **Claim drafting** — claims pre-filled with telemetry evidence. After the operator approves, the Dealer Management System (DMS) accelerator files the claim and records the recovery.
+  **Action Queue** — recommendations to ground a vehicle, schedule service, or file a claim, each with severity, confidence, and estimated impact. See [Fleet Intelligence Action Queue](fi-action-queue.md).
+  **Compliance reports** — recall completion and regulatory reporting, plus warranty expiration alerts.

The portal’s Warranty screen is described in [Warranty](fleet-manager-console.md#fm-warranty).

## How it works
<a name="rwm-how-it-works"></a>

1.  **Recall and warranty ingestion.** Recall notices arrive from OEM feeds and from the NHTSA recall database through scheduled AWS Lambda pollers, on the `cms-recall-notices` and `cms-warranty-claims` Kafka topics. Warranty coverage terms are stored in Amazon DynamoDB, and bulk warranty terms and the parts catalog are uploaded to Amazon S3. Vehicle telemetry, DTCs, maintenance history, and VIN data come from the existing CMS normalization pipeline. Dealer locations and parts availability are maintained in DynamoDB.

1.  **Recall and warranty processing.** On Amazon Managed Service for Apache Flink, the Recall Processor matches recall VIN ranges against the fleet, cross-references telemetry to classify each vehicle as `CONFIRMED` or `POPULATION`, and assigns a severity. The Warranty Processor monitors component failures against coverage rules and flags warranty-eligible events. Both write to Iceberg tables in Amazon S3, Amazon ElastiCache for Redis, and DynamoDB.

1.  **History.** Recall and warranty history lands in ADP as curated Iceberg products, with AWS Lake Formation enforcing row-level isolation per fleet. Amazon Athena views provide recall status, completion tracking, warranty eligibility, claim tracking, recovered totals, and compliance reports. Redis serves the real-time recall and warranty state of each vehicle. Each new recall match or warranty-eligible failure starts the recall and warranty agent.

1.  **Recall and warranty agent.** The recall and warranty agent (`agent-fi-recall-warranty`) is an AVX Tier 2 agent: a Claude model on Amazon Bedrock that runs on each new recall match, each warranty-eligible failure and a daily compliance review. Recall-to-VIN matching, the `CONFIRMED` and `POPULATION` classification, recall severity, and warranty eligibility are deterministic rules the agent reads and cannot change; the SageMaker model scores component degradation. The agent decides what to do about them: which vehicles to book first, given severity, degradation and how hard each vehicle is used; which nearby dealer has the part and a slot; whether a vehicle should be grounded until the remedy; and what evidence a warranty claim needs. It grounds itself in recall playbooks, warranty coverage rules and NHTSA requirements in the ADP knowledge base, and writes each booking, grounding or claim draft to the Action Queue. A recall’s safety text is shown word for word.

1.  **Portal.** The Recall and Warranty dashboards read through Amazon API Gateway and AWS Lambda, Amazon Location Service renders the affected-vehicle map, and Amazon Cognito restricts each operator to their fleets.

1.  **Human in the loop and execution.** Recommendations appear in the Action Queue. An approved booking becomes a repair order in DMS. An approved warranty claim goes to DMS, which files it and records the recovery. An approved grounding updates the vehicle in the fleet record. Amazon EventBridge schedules daily compliance reviews and warranty expiration alerts, and notifies the rebalancing agent when a vehicle is grounded so that [Dynamic fleet rebalancing](dynamic-fleet-rebalancing.md) can cover the gap.

Four guardrails, enforced in the execution path, apply to every recall and warranty action whatever the auto-approval rules say. See [Guardrails](fi-action-queue.md#fi-aq-guardrails).

## Architecture details
<a name="rwm-architecture"></a>

![Recall and warranty management architecture: recall notices and warranty data enter through Amazon MSK](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/recall-warranty-management-architecture.png)



| Component | Role | 
| --- | --- | 
| AWS Lambda (NHTSA recall feed) | Scheduled pollers that fetch recall notices from OEM feeds and the NHTSA database. | 
| Amazon MSK |  `cms-recall-notices` and `cms-warranty-claims` topics. | 
| Amazon DynamoDB | Warranty coverage terms, recall events, dealer locations and parts availability, and recall and warranty events with anomaly flags. | 
| Amazon S3 and ADP curated products | Bulk warranty terms and the parts catalog in Amazon S3; recall and warranty history in ADP Iceberg tables. | 
| Amazon Managed Service for Apache Flink | The Recall Processor (VIN matching, telemetry cross-reference, severity) and the Warranty Processor (coverage rules, eligible-failure flags). | 
| AWS Lake Formation and Amazon Athena | Row-level isolation per fleet; recall, warranty, claim, recovery, and compliance views. | 
| Amazon ElastiCache for Redis | Active recall state and warranty state per vehicle. | 
| AVX recall and warranty agent (`agent-fi-recall-warranty`), Amazon Bedrock, and the ADP knowledge base | Tier 2 agent that prioritizes affected vehicles, picks dealers, decides when to ground, and drafts claims. Amazon Bedrock Guardrails filter its output. | 
| AVX Findings and Actions | The Action Queue and the four guardrails. See [Fleet Intelligence Action Queue](fi-action-queue.md). | 
| Amazon SageMaker | Component degradation scoring. | 
| Amazon CloudFront, Amazon Cognito, Amazon API Gateway, AWS Lambda, and Amazon Location Service | Serve the Recall and Warranty dashboards and the affected-vehicle map. | 
| AVX executors, DMS, and Amazon EventBridge | Execute approved actions (repair orders and claim filing in DMS, groundings in CMS), run daily compliance reviews and expiration alerts, and notify the rebalancing agent of grounded vehicles. | 