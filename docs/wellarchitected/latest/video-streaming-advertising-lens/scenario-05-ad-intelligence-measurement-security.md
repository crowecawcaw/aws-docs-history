

# Scenario 5: Ad intelligence, measurement, and security

 Publishers and advertisers need to help protect the advertising supply chain from fraud, maintain brand safety for ad placements, generate contextual intelligence from content analysis, and validate creative integrity, all at the speed and scale required for programmatic advertising. 

## Characteristics
<a name="s05-characteristics"></a>
+  Creative validation must run in the critical path between creative ingestion and first impression, at scale with thousands of new creatives per day from programmatic sources. 
+  Brand safety classification must be available as a pre-bid signal within the bid request latency window, so it can't add synchronous ML inference latency to every bid. 
+  Supply chain fraud (domain spoofing, unauthorized resale) requires cryptographic verification through IAB transparency standards. 
+  CTV/SSAI session fabrication fraud has increased sharply year-over-year, requiring per-viewer token authentication. 
+  Contextual advertising without user-level tracking requires content classification at ingest time, not auction time. 
+  Three main categories of digital advertising fraud: placement fraud (ad stacking, domain spoofing), traffic fraud (bot traffic, click injection), and action fraud (fake conversions). 

## Reference architecture
<a name="s05-reference-architecture"></a><a name="scenario-05-fig1"></a>

![Contextual intelligence advertising using GenAI on AWS, part 1, showing pre-ingest content classification with Bedrock Data Automation and cached IAB taxonomy signals available at auction time](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-05a-contextual-intelligence-1.jpg)

*Contextual intelligence advertising using GenAI on AWS, part 1*
<a name="scenario-05-fig2"></a>

![Contextual intelligence advertising using GenAI on AWS, part 2, showing the auction-time retrieval path, non-intrusive ad rendering, and attribution feedback loop](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-05b-contextual-intelligence-2.jpg)

*Contextual intelligence advertising using GenAI on AWS, part 2*


 The architecture consists of the following components: 

1.  **Creative validation pipeline**: S3 event notifications trigger a Lambda validation pipeline when new creatives are uploaded. Amazon Rekognition provides visual content moderation (nudity, violence). Amazon Comprehend detects text toxicity. A containerized sandbox renders HTML5 and JavaScript creatives and monitors for malicious behavior (network requests to known malware domains, JavaScript obfuscation). Flagged creatives route to a quarantine S3 prefix with audit trail for TAG certification. 

1.  **Contextual classification (pre-ingest)**: Amazon Bedrock Data Automation (for video and audio) or Amazon Comprehend (for text) classifies content against IAB Content Taxonomy categories when new content is published (EventBridge trigger on S3 object creation). Results are cached in Amazon ElastiCache with 24-hour TTL. At auction time, contextual signal retrieval is a sub-millisecond cache lookup, never synchronous ML inference. 

1.  **Supply chain transparency (ads.txt / sellers.json)**: Publisher's authorized seller declarations are hosted in Amazon S3 with Object Lock (governance mode) guarding against unauthorized modification, served through Amazon CloudFront for global low-latency access. DSP bid evaluation cross-references inbound bid requests against sellers.json declarations and validates the full SupplyChain object for intermediary fraud. 

1.  **Creative hash registry (DynamoDB)**: When a creative is approved, its SHA-256 content hash is registered in DynamoDB keyed by creative ID (ACIF). Before SSAI stitching, the creative fetched from CDN is validated against the registered hash, detecting both CDN-level tampering and VAST redirect attacks. 

1.  **SSAI session authentication (CloudFront Functions)**: Per-viewer cryptographic tokens bound to viewer attributes (IP, device, and geographic region) with short TTL reduce the risk of SSAI session fabrication. CloudFront Functions validate tokens on every manifest and segment request. 

1.  **AWS WAF Bot Control**: Deployed on SSAI session creation endpoints to detect CTV session fabrication patterns (unusual User-Agent strings, impossible geolocation patterns, anomalous session creation velocity). Tuned against legitimate CTV device profiles to minimize false positives. 

1.  **AWS Shield Advanced**: Helps protect bid endpoints and ad-serving infrastructure against DDoS attacks. Per-partner traffic baselines enable detection of anomalous traffic patterns that blend with legitimate RTB spikes. Shield Response Team is engaged proactively before high-profile advertising events. 

## Configuration notes
<a name="s05-configuration-notes"></a>

### Creative validation
<a name="creative-validation"></a><a name="scenario-05-fig3"></a>

![Ad creatives generation and quality-control workflow on AWS using Amazon Bedrock for generation, a validation pipeline for brand-safety and policy checks, and quarantine routing for flagged creatives](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-05a-ad-creatives-generation-qc.jpg)

*Ad creatives generation and quality control on AWS*


 Configure S3 event notifications on your creative storage bucket to trigger validation on every upload. Route flagged creatives to a quarantine prefix with the creative ID, scan results, and disposition logged to DynamoDB with retention aligned to TAG certification audit period. Re-scan active creatives weekly that reference external JavaScript or CSS resources. These can be replaced with malicious content after initial approval. 

### Contextual classification pipeline
<a name="contextual-classification-pipeline"></a>

 Trigger classification at content publish time, not at bid time. Use Amazon Bedrock Data Automation for video content (scene detection, brand safety signals, IAB taxonomy categories) and Amazon Comprehend for text content. Cache results in ElastiCache keyed by content URL with 24-hour TTL. For FAST channel programming where content rotates on a schedule, pre-populate the cache for the next 24 hours of programming using a scheduled Lambda function. 

### Supply chain transparency
<a name="supply-chain-transparency"></a>

 Host ads.txt and sellers.json on Amazon S3 with versioning enabled for change history and Object Lock (governance mode, 12-month minimum retention) for tamper protection. Use CloudFront with a 15-minute TTL to balance propagation speed with caching efficiency. Configure S3 event notifications to validate file syntax through Lambda after each update and alert on validation failures. 

### Brand safety classification
<a name="brand-safety-classification"></a>

 Map output labels from Rekognition and Comprehend to GARM Brand Safety Floor categories. Cache per-page or per-video brand safety scores in a low-latency store (DynamoDB or ElastiCache) accessible at bid time. Implement content drift detection. Re-classify active content on a weekly schedule and pause active campaigns on inventory that has transitioned to blocked categories. 

### SSAI creative integrity
<a name="ssai-creative-integrity"></a>

 Implement the full creative trust chain: hash registration at approval → hash validation before stitching → per-viewer session tokens → WAF Bot Control on session creation. Allowlist only approved CDN origins for VAST-returned creative URLs. Log VAST responses that reference non-allowlisted domains immediately for security investigation. 