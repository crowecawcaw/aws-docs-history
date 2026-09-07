

# LSSEC02-BP01 Determine applicable regulatory frameworks and enforce data privacy requirements by implementing controls
<a name="lssec02-bp01"></a>

 Many life sciences organizations fall under data privacy requirements or regulations which influences data security and architecture, for example where data may be physically located. 

 **Desired outcome:** Control objectives identify the locations and conditions where specific data is required to be stored and controls are implemented. 

 **Common anti-patterns:** 
+  Exporting data from shared data sets. 
+  Manually obfuscating sensitive fields. 

 **Benefits of establishing this best practice:** Clarifies requirements as well as control automation and audit. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Begin by reviewing data privacy requirements within applicable regulatory frameworks. To determine applicable regulatory frameworks, start with local regulations and frameworks for the country where your sensitive data is generated, hosted, and processed.  

 Engage with legal counsel who can assist you to define the scope of the local regulations, as well as additional regulation frameworks that may apply to you.  

 Update documentation of data residency requirements and control objectives with specific details on which data elements are subject to allowed or disallowed storage and transmission locations. For more detail, see SEC01-BP03 Identify and validate control objectives.  

 Once the determination of requirements has been made and documented, technical controls can be put in place to enforce them. Choose which geographic regions to include in your environment.  

 Control objectives should be updated to clearly indicate where data is expected to be located due to data residency requirements. Implement controls to keep data within those Regions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Update control objectives to address data residency regulatory requirements. 

1.  Separate workloads that have different data residency requirements. 

1.  Implement controls that enhance your digital sovereignty governance posture. 

1.  Tag PHI data as sensitive and grant least privilege access only where required. 

1.  Restrict access by location of resource. 

1.  Implement detective controls that notify security operations when resources are found in unauthorized locations. 

1.  Implement backups to enable recovery from data corruption and data deletion. 

1.  Update threat models to cover the accidental or malicious storage of data in unauthorized locations. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Data Residency with Hybrid Cloud Services Lens - AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens) 
+  [Data protection in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/data-protection.html) 

 **Related tools:** 
+  [AWS DataZone](https://aws.amazon.com/datazone/) 
+  [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) 