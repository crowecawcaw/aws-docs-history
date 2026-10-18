

# Verifiable data controls
<a name="dssec07"></a>

 Contractual assurances and policy declarations alone do not prove sovereignty. Organizations need to demonstrate that data residency, privacy, and lineage controls are enforced through technical mechanisms. Region deny controls, digital sovereignty governance controls, privacy-enhancing technologies, and data lineage tracking together produce the evidence that connects a claim to what the system actually does. 

 This capability covers enforcing data residency through governance controls, applying privacy-enhancing techniques to protect personal data, and tracking data lineage to show where data has been and who has accessed it. 


|  DSSEC07: How do you apply verifiable controls over sensitive data?  | 
| --- | 
| [DSSEC07-BP01 Enhance your digital sovereignty governance posture](dssec07-bp01.md) | 
| [DSSEC07-BP02 Provide technical options to enhance privacy](dssec07-bp02.md) | 
| [DSSEC07-BP03 Track data lineage](dssec07-bp03.md) | 

## Capability intent
<a name="capability-intent-6"></a>
+  Data residency is enforced through technical controls (Region deny, digital sovereignty governance controls) that prevent data from leaving approved jurisdictions, regardless of individual user actions. 
+  Privacy-enhancing techniques such as tokenization, differential privacy, and secure computation protect personal data while preserving analytical utility. 
+  Data lineage is tracked from origin through processing and storage. The resulting record is auditable and demonstrates adherence to residency and privacy requirements. 
+  Governance controls are applied at the organizational level and can't be overridden by individual account administrators, so enforcement stays consistent across the environment. 
+  Verifiable evidence of control effectiveness is produced continuously and available for regulatory review without separate preparation efforts. 

## Common issues to watch for
<a name="common-issues-to-watch-for-6"></a>
+  Region deny controls that restrict new resource creation but don't address data already replicated to non-approved Regions through legacy configurations or service defaults. 
+  Privacy-enhancing techniques applied uniformly without considering the data utility requirements of downstream consumers. This reduces analytical value without a proportionate privacy benefit. 
+  Data lineage that tracks storage locations but not processing flows, missing scenarios where data is temporarily decrypted or copied during compute operations. 
+  Governance controls that can be overridden by account administrators through policy exceptions, undermining the centralized enforcement they are designed to provide. 
+  Lineage records stored in a jurisdiction different from the data they describe, so the proof of compliance is itself noncompliant. 