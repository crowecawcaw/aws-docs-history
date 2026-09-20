

# DSSEC07-BP02 Provide technical options to enhance privacy
<a name="dssec07-bp02"></a>

 Digital sovereignty requirements demand that organizations secure data and provide verifiable evidence of privacy protection measures. Technical privacy enhancement options enable organizations to process sensitive data while minimizing exposure risks. These options support business objectives and regulatory mandates through cryptographic techniques, data minimization, and privacy-preserving technologies. 

 **Desired outcome:** 
+  Sensitive data remains protected throughout its lifecycle with technical privacy controls that minimize exposure risks. 
+  Organizations maintain auditable evidence of privacy protection measures for regulatory adherence. 
+  Data utility is preserved for legitimate business operations while privacy controls are maintained. 

 **Common anti-patterns:** 
+  Relying solely on access controls without implementing data-level privacy protections. This leaves sensitive information vulnerable when permission boundaries are compromised. 
+  Using static masking or tokenization techniques that can't be customized per use case, user role, or data type. 
+  Implementing privacy controls as an afterthought rather than baking in privacy by design principles into the software development lifecycle (SDLC) activities. 

 **Benefits of establishing this best practice:** 
+  Advanced privacy techniques demonstrate due diligence in protecting citizen data. They assist in meeting digital sovereignty requirements across multiple jurisdictions. 
+  Privacy-preserving technologies enable legitimate data use cases while maintaining strong privacy protections. This supports business innovation within regulatory constraints. 
+  Logging and monitoring of privacy controls provide verifiable evidence for regulatory audits and compliance assessments. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The most durable privacy control is to avoid holding sensitive data you don't need. Data you don't collect or retain can't be exposed in a breach. For the data you must keep, layer protections so that a single failure doesn't expose it. Access controls alone are not effective once a boundary is breached, so add field-level controls such as encryption, tokenization, and masking beneath them. Match the strength of each control to data sensitivity and use case, accepting that stronger privacy usually trades against data utility and operational complexity. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess data sensitivity and privacy requirements**: 
   +  Conduct data mapping to identify sensitive data types including PII, PHI, financial information, and confidential business data. 
   +  Define privacy requirements based on applicable data privacy-related legislation such as GDPR, HIPAA, CCPA, and industry-specific regulations. 
   +  Establish data classification schemas that match privacy protection levels and regulatory requirements. 
   +  Use [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/data-classification.html), [sensitive data detection in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html), and [Amazon Comprehend PII entity detection](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html) to automatically discover and classify sensitive data across your AWS environment. Use [Amazon Q Developer](https://aws.amazon.com/q/developer/) to find [potential security vulnerabilities](https://docs.aws.amazon.com/codeguru/detector-library/) in your application code. 

1.  **Consider tokenization, data masking, and privacy enhancements**: 
   +  Implement [format-preserving encryption (FPE)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38G.pdf) to maintain data utility while protecting sensitive values. 
   +  Deploy tokenization systems that replace sensitive data with non-sensitive tokens. 
   +  Configure data masking based on user roles and access patterns. 
   +  Use AWS Secrets Manager to securely store and rotate tokenization keys and masking rules. 
   +  Deploy secure aggregation methods for statistical analysis. These methods don't expose individual data points. For example, provide only summary tables. 
   +  Go beyond aggregation methods with differential privacy, which adds calibrated statistical noise so query results don't reveal any single record while preserving the utility of aggregate data. [AWS Clean Rooms Differential Privacy](https://docs.aws.amazon.com/clean-rooms/latest/userguide/differential-privacy.html) provides this as a fully managed capability. 

1.  **Consider applying specialized data protection measures**: 
   +  Implement secure multi-party computation (SMPC) protocols for collaborative data analysis without data sharing. Consider [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html) to collaborate with your partners without sharing raw data. 
   +  Consider a privacy vault pattern: a dedicated, access-controlled store that centralizes PII and PHI behind query APIs, reducing data sprawl and supporting data minimization. Implement the pattern with AWS building blocks (for example, tokenization backed by a dedicated data store, with AWS Secrets Manager for key custody) or a partner solution from AWS Marketplace. 

1.  **Implement privacy monitoring and compliance**: 
   +  Configure Amazon CloudWatch to monitor privacy control effectiveness and detect anomalous access patterns with intelligent threat detection capabilities offered by Amazon GuardDuty. 
   +  Use AWS Config to detect deviations of privacy-related controls from baseline configurations. 
   +  Deploy AWS Security Hub CSPM to aggregate privacy and security findings across your environment. 

1.  **Enable data subject rights and consent management**: 
   +  Implement automated data subject access request (DSAR) processing. 
   +  Deploy consent management systems to track user preferences and consent status. 

1.  **Implement data minimization**: 
   +  Archive data not in use. 
     +  Use Amazon S3 lifecycle policies to archive data to Amazon Glacier. 
     +  Use Amazon Data Lifecycle Manager to delete Amazon Elastic Block Store (Amazon EBS) snapshots no longer in use. 
   +  Use Amazon DynamoDB TTL to delete items that are no longer relevant. Use cases include in-session game data or similar event data that have already been persisted to another long-term storage solution (for example, to S3). 
   +  Don't copy datasets to enable individual use cases. Instead, build data adapters with built-in authorization policies, and recorded audit trails. 
   +  Minimize proliferation of database views constructed over tables. Instead, use data access policies with column, row and cell level filters to enable predefined use cases. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [Data Analytics Lens - Best practice 3.1 – Privacy by Design](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.1-privacy-by-design.html) 
+  [SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html) 
+  [SEC08-BP02 Enforce encryption at rest](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html) 
+  [SEC08-BP03 Automate data at rest protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_automate_protection.html) 
+  [SEC03-BP01 Define access requirements](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define.html) 
+  [SEC07-BP01 Understand your data classification scheme](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_identify_data.html) 

 **Related documents:** 
+  [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 
+  [Amazon Macie User Guide](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) 
+  [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - State of the Art: AWS data protection in 2025 (ft. Vanguard) (SEC203)](https://www.youtube.com/watch?v=MMdXKVcSH-o) 
+  [AWS re:Invent 2025 - Privacy-preserving AI primitives: Building blocks for regulated industries (ARC328)](https://www.youtube.com/watch?v=vfkKJhllnx4) 

 **Related services:** 
+  [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) 
+  [Amazon Macie](https://aws.amazon.com/macie/) 
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) 