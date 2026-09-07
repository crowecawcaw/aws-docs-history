

# LSREL13-BP03 Track reliability metrics aligned to regulatory needs
<a name="lsrel13-bp03"></a>

 Define and monitor reliability metrics that align with both operational resilience and regulatory requirements. For GxP-regulated systems, include system availability, backup/restore success, recovery test completion, and data integrity checks. Retain metric history for audit evidence. 

 **Desired outcome:** 
+  Clear visibility into workload reliability health. 
+  Metrics aligned with both business SLAs and regulatory expectations. 
+  Historical reporting available for audits and inspections. 

 **Common anti-patterns:** 
+  Collecting technical metrics without mapping to regulatory requirements. 
+  Not retaining monitoring data for required regulatory periods. 
+  No baselines to measure whether reliability is improving or degrading. 

 **Benefits of establishing this best practice:** 
+  Provides measurable evidence of system reliability for regulators and auditors. 
+  Builds trust with researchers and clinical teams in system performance. 
+  Supports proactive investment in reliability improvements based on trends. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Define metrics in collaboration with QA, governance, and IT teams. Track technical indicators (uptime, error rates, and RTO and RPO adherence) alongside compliance-related ones (backup success, recovery validation, and audit trail completeness). Retain reliability data in tamper-evident storage for required retention periods. Review metrics periodically to drive improvement. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Collect uptime and error metrics using Amazon CloudWatch and log retention policies. 

1.  Monitor backup success using AWS Backup Audit Manager. 

1.  Track recovery validation evidence in AWS Audit Manager. 

1.  Store metric histories in Amazon S3 with Object Lock for immutability. 

1.  Build dashboards using Quick for regulators and QA stakeholders. 