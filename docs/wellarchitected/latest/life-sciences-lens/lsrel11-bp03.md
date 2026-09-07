

# LSREL11-BP03 Plan redundancy for critical laboratory equipment
<a name="lsrel11-bp03"></a>

 Design redundancy strategies for critical laboratory equipment by maintaining hot spares, parallelized runs, or vendor service agreements. Effective redundancy maintains continuity of operations even during failures of high-value or high-throughput instruments. 

 **Desired outcome:** 
+  Continuous operation of critical research workflows during equipment failures. 
+  Reduced delays in experiments and studies by having spare capacity. 
+  Documented continuity plans for audits and inspections. 

 **Common anti-patterns:** 
+  Treating equipment equally without prioritizing critical instruments. 
+  Failing to budget or plan for spare capacity in core systems. 
+  Assuming vendor maintenance SLAs are sufficient for continuity of research operations. 

 **Benefits of establishing this best practice:** 
+  Reduces operational risk by maintaining continuity during unexpected failures. 
+  Increases confidence in meeting research timelines and commitments. 
+  Demonstrates resilience and preparedness to regulators and auditors. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Start by classifying lab equipment by criticality and throughput to identify which instruments require redundancy. Define strategies such as hot spares, workload sharing, or vendor backup agreements. Maintain documented runbooks for failover to redundant equipment, and periodically simulate outages to test readiness. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Track redundancy configurations using AWS Config for reporting. 

1.  Store redundancy plans, SLAs, and vendor contracts in Amazon S3, and enable fast search with Amazon OpenSearch Service. 

1.  Orchestrate escalation procedures using Amazon SNS and AWS Lambda when failures are detected. 

1.  Record continuity outcomes in Amazon DynamoDB for audit traceability. 

1.  Periodically simulate infrastructure and application-level failures with AWS Fault Injection Service (FIS) to validate the continuity of data capture, workflow orchestration, and failover processes supporting laboratory equipment. 

1.  For physical instruments, conduct tabletop or vendor-led failure simulations to keep redundancy plans practical. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  Business continuity and disaster recovery planning 
+  Risk-based classification of lab assets 
+  Vendor management and SLA governance 