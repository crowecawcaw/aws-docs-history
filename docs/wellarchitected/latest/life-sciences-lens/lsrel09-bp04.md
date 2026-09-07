

# LSREL09-BP04 Maintain auditable rollback and recovery records
<a name="lsrel09-bp04"></a>

 Capture and retain immutable, timestamped records of every rollback and recovery action, including approvals, deviations, timing, and outcomes. Audit and governance artifacts are required evidence for GxP adherence and should be integrated into change control and incident reporting. 

 **Desired outcome:** Every rollback or recovery is traceable and auditable with internal SOPs and external GxP requirements. 

 **Common anti-patterns:** 
+  Treating rollback as a purely technical process without traceability. 
+  Failing to log deviations or decisions during recovery. 
+  Storing audit records in a non-durable or unsearchable formats. 

 **Benefits of establishing this best practice:** 
+  Demonstrates regulatory adherence and governance over change activities. 
+  Enables post-event analysis and corrective actions to avoid recurrence. 
+  Supports transparent reporting to sponsors, regulators, and QA teams. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Integrate audit capture into every phase of change and rollback: record the release checksum, approvals, automated actions taken, timestamps for each step, deviations, and post-rollback verification results. Use immutable storage and tamper-evident logs and include audit evidence as part of the change record. Verify that your log retention policy meets regulatory retention policies and that search and indexing capabilities support timely retrieval for inspections. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Enable AWS CloudTrail to capture API activity and operational actions related to deployment and rollback. 

1.  Use AWS Config to record configuration state and change history for infrastructure resources. 

1.  Store immutable audit records in Amazon S3 with S3 Object Lock enabled to enforce retention and immutability. 

1.  Index and make records discoverable with Amazon OpenSearch Service or a governance catalog for rapid response to audit requests. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  Security and logging for research environments 
+  Resilient environment provisioning and lifecycle management 
+  Automated validation in deployments 