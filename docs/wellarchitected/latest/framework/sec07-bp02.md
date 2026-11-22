

# SEC07-BP02 Apply data protection controls based on data sensitivity

 Not all data needs the same protection. Applying controls that match each sensitivity level guards your most sensitive data from unauthorized access while keeping lower-sensitivity data available. 

 **Desired outcome:** 
+  You have a mapping that assigns each data type in your workload to a sensitivity level from your classification policy. 
+  You publish guidelines for each level covering approved storage services, locations, and their required configuration. 
+  You implement controls sized to the protection each level requires and the cost you accept. 
+  You have monitoring and alerting that detects data in unauthorized locations, access by unauthorized actors, and non-compliant service configuration. 

 **Common anti-patterns:** 
+  Teams apply the same controls to all data, over-provisioning for low-sensitivity data and underprotecting the most sensitive. 
+  Security, compliance, and business stakeholders are left out when data protection controls are defined. 
+  Teams overlook the operational overhead and cost of maintaining protection controls. 
+  Data protection controls are never reviewed, so they drift out of alignment with classification policy. 
+  No one maintains a complete inventory of where data resides at rest and in transit. 

 **Benefits of establishing this best practice:** 
+  Investment concentrates where it matters, with higher control on the data that carries the most risk. 
+  Lower-sensitivity data becomes more accessible and complete for your workforce, customers, or constituents. 
+  Costs align with risk, because controls are not uniform across all data. 
+  Controls map to the industry regulations and legal requirements that apply to each level. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Decide where each class of data is allowed to exist. An *isolation boundary* separates data of one sensitivity level from another, so that a failure or unauthorized access on one side does not expose the other. Permissions inside a single account form a weak boundary, because one misconfigured policy can cross them. Separate accounts form a strong boundary. 

 We recommend separating data of different sensitivity into different AWS accounts. Use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to restrict which services and actions are available in each account. This enforces least privilege at a coarse grain, where a restricted account cannot call a service that would move data outside its boundary. Layer finer controls inside each boundary, such as encryption, access policies, and auditing, so that no single control failure exposes the data. For specific controls, see [Protecting data at rest](sec08.md) and [Protecting data in transit](sec09.md). 

 You can also lower sensitivity by changing the data itself. Tokenization replaces a sensitive value with a surrogate and stores the mapping in a separate protected system. Anonymization removes the link to an individual entirely. Both techniques shrink the set of systems that must carry heavy controls. The trade-off is utility and operational overhead, because anonymized data cannot be reversed and a central tokenization service is another system you must run and secure. Apply these techniques where reducing sensitivity is worth the additional overhead of the service. 

 The data you hold, the threats against it, and the regulations you must follow can all change, so controls that once matched your policy may drift out of alignment. Review the classification mapping and its controls on a regular cadence, and test that each control still works. Train staff on the classification scheme and their role in it. Without that awareness, they might route sensitive data into places your controls do not cover. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map your data to sensitivity levels:** Identify the classification and sensitivity level of each data type in your workload, and record where you store and process it. 

1.  **Define isolation boundaries and an enforcement strategy:** For each sensitivity level, decide the boundary that separates it from others and how you enforce it, such as separate accounts governed by [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html). 

1.  **Implement the controls each level requires:** Apply the access, encryption, auditing, and retention controls your classification policy defines for each level. See [Protecting data at rest](sec08.md) and [Protecting data in transit](sec09.md) for the relevant techniques. 

1.  **Reduce sensitivity where it helps:** Evaluate tokenization or anonymization to lower the sensitivity level of data where doing so preserves the value you need. Consider a centralized service for tokenization and de-tokenization to apply consistent policy across your workloads. 

1.  **Verify controls with automated testing and monitoring:** Continuously monitor your configured resources and test that controls behave as intended, alerting when configuration becomes non-compliant. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md) 
+  [SEC07-BP03 Automate identification and classification](sec07-bp03.md) 
+  [SEC08-BP02 Enforce encryption at rest](sec08-bp02.md) 
+  [SEC09-BP02 Enforce encryption in transit](sec09-bp02.md) 
+  [COST03-BP03 Enforce data retention policies](cost03-bp03.md) 

 **Related documents:** 
+  [Data classification whitepaper](https://docs.aws.amazon.com/pdfs/whitepapers/latest/data-classification/data-classification.pdf) 
+  [Best practices for security, identity, and compliance](https://aws.amazon.com/architecture/security-identity-compliance/) 
+  [Security of AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-security.html) 

 **Related examples:** 
+  [Guidance for tokenization to improve data security and reduce audit scope on AWS](https://docs.aws.amazon.com/solutions/tokenization-to-improve-data-security-and-reduce-audit-scope-on-aws/) 
+  [Data tokenization in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/data-tokenization.html) 

 **Related tools:** 
+  [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) 
+  [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 