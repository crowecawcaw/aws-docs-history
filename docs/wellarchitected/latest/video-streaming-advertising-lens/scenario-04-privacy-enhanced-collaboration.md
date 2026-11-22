

# Scenario 4: Privacy-enhanced collaboration

 Publishers, advertisers, and measurement providers need to collaborate on audience analysis, campaign attribution, and reach measurement without sharing raw personal data across organizational boundaries. Privacy-enhancing technologies (PETs) enable these insights while maintaining individual privacy. 

## Characteristics
<a name="s04-characteristics"></a>
+  Multiple parties each hold portions of the data needed for cross-party measurement. 
+  Raw personal data can't be shared because of contractual, regulatory, or competitive confidentiality constraints. 
+  Measurement computations (audience deduplication, attribution) require temporarily combining datasets containing personal data. 
+  Partners need cryptographic proof that their data was processed by the agreed algorithm. 
+  MRC accreditation requirements demand auditability of measurement methodology. 
+  Identity signal loss from deprecated third-party cookies and device IDs requires alternative collaboration approaches. 
+  GDPR, CCPA, and consent framework compliance must be maintained throughout the collaboration lifecycle. 

## Reference architecture
<a name="s04-reference-architecture"></a><a name="scenario-04-fig1"></a>

![Privacy-enhanced collaboration architecture on AWS showing publisher and advertiser data connecting through AWS Clean Rooms for privacy-preserved analysis, with Nitro Enclaves for computations requiring cryptographic isolation and AWS Entity Resolution for cross-platform identity resolution](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-04a-cdp-datalake-cleanrooms.jpg)

*Privacy-enhanced collaboration architecture on AWS showing publisher and advertiser data connecting through AWS Clean Rooms for privacy-preserved analysis, with Nitro Enclaves for computations requiring cryptographic isolation and AWS Entity Resolution for cross-platform identity resolution*


 The architecture consists of the following components: 

1.  **Customer Data Platforms (publisher \+ advertiser)**: Each party's first-party data, managed within their own AWS account. Data is stored in Amazon S3 with SSE-KMS encryption using per-party customer-managed keys. 

1.  **AWS Clean Rooms collaboration**: Provides a secure environment where multiple parties can analyze combined datasets without exposing raw data to each other. Analysis rules enforce minimum aggregation thresholds (100\+ users for audience analysis, 1,000\+ impressions for measurement cells) and restrict which columns each party can access. Clean Rooms Differential Privacy adds mathematically proven noise to reduce the risk of re-identification. 

1.  **AWS Nitro Enclaves**: For computations that require raw data access during processing (panel-to-digital matching, cross-publisher frequency deduplication), Nitro Enclaves provide isolated compute environments with no persistent storage, no interactive access, and cryptographic attestation. KMS key policies are bound to enclave PCR hash values, so data decrypts only within the approved measurement algorithm. 

1.  **AWS Entity Resolution**: Cross-platform identity matching that operates on encrypted datasets without requiring decryption. Matches linear household identifiers (STB IDs, ACR device fingerprints) with digital identifiers (device IDs, first-party IDs, CTV device IDs). Integrates with LiveRamp RampID through AWS Marketplace. 

1.  **AWS KMS (Multi-Region keys)**: Per-collaboration encryption keys help protect each data contribution with cryptographic controls tied to specific collaboration IDs. KMS maintains a complete audit trail of all key usage for regulatory adherence. 

1.  **AWS CloudTrail \+ Clean Rooms analysis logs**: Every query execution, participating account, query text, and result metadata is logged. These logs support regulatory adherence, partner dispute resolution, and TAG certification audit requirements. 

1.  **Amazon S3 (collaboration output)**: Analysis results are written to each party's output bucket with S3 Object Lock guarding against modification. Result data is retained according to data handling agreements and regulatory requirements. 

## Configuration notes
<a name="s04-configuration-notes"></a>

### Standard collaboration setup
<a name="standard-collaboration-setup"></a>

 Create Clean Rooms collaborations for specific advertising scenarios: measurement attribution, audience overlap analysis, yield analysis. Define each party's role (can query, can receive results, can contribute data) with restrictions per use case. Configure analysis rules with advertising-appropriate thresholds before adding collaborators. Enable Clean Rooms analysis logs before any query runs. Retroactive log enablement isn't possible. 

### Differential privacy configuration
<a name="differential-privacy-configuration"></a>

 Enable Clean Rooms Differential Privacy on measurement collaborations where query results need protection against re-identification. Configure epsilon values appropriate for advertising measurement (balance privacy protection with statistical significance for campaign performance reporting). Monitor privacy budget consumption, and alert at 75% to allow time for query prioritization before exhaustion. 

### Sensitive computation with Nitro Enclaves
<a name="sensitive-computation-with-nitro-enclaves"></a>

 For panel-to-digital matching and cross-publisher deduplication, package measurement code as enclave images signed by your CI/CD pipeline. Create KMS key policies requiring specific PCR values (enclave code hash). Provide partners with PCR values for independent attestation verification. This is the mechanism by which partners confirm that the agreed algorithm processed their data. Test the full attestation flow in staging before using with partner data. 

### Consent boundary enforcement
<a name="consent-boundary-enforcement"></a>

 Before any cross-source data joining operation, validate that both source records have consent for the intended purpose. Implement the intersection rule in Lambda pre-processing: only purposes consented to in both datasets may proceed. Reject joins where consent scopes don't intersect, logging all rejections for compliance audit. Build consent withdrawal pipelines that cascade deletions across all identity mapping tables within GDPR's 30-day requirement. 

### Identity resolution
<a name="identity-resolution"></a>

 Use AWS Entity Resolution matching workflows configured with appropriate namespace mappings for each identifier type pair. Enable audit logging through CloudTrail for all resolution operations. Implement TTL on all cross-platform identity mapping records aligned to consent validity periods. Delete mappings when underlying consent expires or is withdrawn. 