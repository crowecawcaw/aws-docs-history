

# ADVSEC02-BP04 Implement confidential computing for cross-party measurement without exposing raw viewer data
<a name="advsec02-bp04"></a>

 Cross-party advertising measurement requires combining datasets from competing parties to answer questions about deduplicated reach, frequency, and attribution. Even with AWS Clean Rooms access controls, some measurement computations require temporary processing of raw data. Confidential computing cryptographically protects raw data during computation. Attestation proves to all parties which code processed their data. 

 **Desired outcome:** 
+  You have measurement computations that process raw viewer data from multiple parties within cryptographically isolated environments that no operator can access. 
+  Your measurement partners can verify through attestation which approved algorithm and runtime configuration processed their data. 
+  You have coordinated approval, rollback, and output-release controls for changes to attested measurement workloads. 

 **Common anti-patterns:** 
+  Processing cross-party measurement joins in standard compute environments where operators or co-tenants can access raw input data during execution. 
+  Automatically updating decryption policy after an enclave image changes, which bypasses the partner approval that the attested release contract requires. 
+  Deploying measurement algorithms without attestation or build evidence, so contributing parties can't verify which code processed their data. 

 **Benefits of establishing this best practice:** 
+  Supports cross-environment deduplication without either party seeing the other's raw viewer data. 
+  Provides cryptographic evidence that partners can use during methodology review and dispute resolution. 
+  Helps protect panel membership and other record-level inputs while preserving an auditable measurement process. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Cross-party measurement separates *method authority* from infrastructure operation. The method authority is the group of contributors that approves the algorithm, permitted inputs, and releasable outputs. The operator runs the workload but can't change those decisions alone. Capture them in an *attested release contract* that identifies the approved image, input schema, output schema, and disclosure rules before any party contributes data. 

 The *record-level boundary* determines when confidential computing is warranted. A method crosses the record-level boundary when it must hold or compare individual records during execution and can't use aggregate query restrictions to perform the computation. Hardware isolation protects those records from the operator, but it doesn't prove that the method is statistically valid or that its output is safe. Input minimization, methodology review, and disclosure control therefore remain independent safeguards. 

 Attestation creates a coordinated lifecycle. A rebuilt image changes its platform configuration register (PCR) values and can stop decryption for every contributor. The operating agreement needs approval and rollback windows, evidence retention, and a dispute authority that can determine whether an image or result satisfied the release contract. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create the attested release contract:** Record the method authority, record-level boundary decision, approved algorithm version, required input fields, expected output schema, and disclosure checks. Obtain contributor approval before accepting encrypted inputs. 

1.  **Build and deploy the approved enclave image:** Produce a reproducible AWS Nitro Enclaves image from the approved source. Configure AWS Key Management Service (AWS KMS) key policies to release data keys only when the enclave presents the PCR values recorded in the release contract. 

1.  **Enforce the output contract:** Validate each result against the approved schema, minimum cohort size, and statistical bounds before release. Hold results that expose small cohorts or differ materially from the approved contract for independent review. 

1.  **Give partners independent verification evidence:** Publish the signed image manifest, expected PCR values, build provenance, and attestation-verification procedure. Retain each partner's verification result with the measurement record. 

1.  **Operate image changes through joint approval:** Stage a candidate image, collect contributor approval for its new evidence, and preserve the last approved image for rollback. Record rejected changes and disputes without changing key policy to bypass a contributor decision. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) 
+  [ADVSEC05-BP02 Design for compliance across both linear and digital data flows](advsec05-bp02.md) 

 **Related documents:** 
+  [AWS Nitro Enclaves cryptographic attestation](https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html) 
+  [KMS condition keys for attestation](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-attestation.html) 
+  [AWS Clean Rooms Cryptographic Computing](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing.html) 
+  [AWS Clean Rooms Differential Privacy](https://aws.amazon.com/clean-rooms/differential-privacy/) 
+  [Multi-party computation with Nitro Enclaves](https://aws.amazon.com/blogs/compute/leveraging-aws-nitro-enclaves-to-perform-computation-of-multiple-sensitive-datasets/) 

 **Related services:** 
+  [AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/) 
+  [AWS KMS](https://aws.amazon.com/kms/) 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 