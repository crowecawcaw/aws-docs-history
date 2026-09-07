

# LSREL12-BP01 Implement recovery processes with data integrity verification
<a name="lsrel12-bp01"></a>

 Design recovery procedures with explicit steps to verify data integrity once recovery operations complete. For regulated life sciences workloads, include checksums, reconciliation processes, or dual-control verification. Verification evidence should be documented as part of disaster recovery and audit processes. 

 **Desired outcome:** 
+  Recovered datasets are validated for completeness and accuracy. 
+  Data integrity verification is automated where possible. 
+  Audit evidence of verification steps is retained for compliance-related purposes. 

 **Common anti-patterns:** 
+  Recovery plans restore services without validating data correctness. 
+  Assuming backups are correct without performing validation checks. 
+  No retention of verification evidence for audit purposes. 

 **Benefits of establishing this best practice:** 
+  Avoids propagation of corrupted or incomplete data into research workflows. 
+  Provides regulators confidence that scientific data is accurate after recovery. 
+  Reduces risk of invalid conclusions or repeated experiments. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Define recovery procedures that integrate integrity checks, including checksum validation, record counts, and cross-system reconciliation. Automate as much as possible to reduce manual errors, and document the results. For GxP workloads, require dual sign-offs for verification evidence. Retain logs and reports as part of change and recovery records. 

### Implementation steps
<a name="implementation-steps"></a>

1.  After recovery, run checksum verification jobs with AWS Lambda across restored datasets in Amazon S3. 

1.  Use AWS Glue or AWS DataBrew to validate schema and record counts. 

1.  Store verification logs in Amazon S3 with Object Lock for immutability. 

1.  Integrate verification results into audit tracking using AWS Audit Manager. 