

# Scenario 12: Implementation of contextual advertising with non-intrusive ads on AWS

 Contextual advertising delivers relevant ads based on content analysis rather than user-level tracking, making it privacy-safe while maintaining advertising effectiveness. Non-intrusive ad formats (squeezebacks, overlays, pause ads, and shoppable ads) appear alongside content without interrupting playback. They create ad inventory where none existed before, with higher viewer engagement than interruptive formats. 

## Characteristics
<a name="s12-characteristics"></a>
+  Advertiser needs relevant ad placements without relying on cross-site user tracking as cookies and device IDs are deprecated. 
+  Publisher wants to monetize inventory using first-party and contextual signals as identity frameworks evolve. 
+  Non-intrusive formats require content-aware placement, because an overlay on a cooking show performs differently than on a news broadcast. 
+  Ad placement decisions must complete within the bid response window, with no synchronous ML inference at auction time. 
+  Shoppable ads use image embedding-based matching to identify products in content scenes and present purchase opportunities. 
+  IAB SIMID standard provides the secure interactive container for overlay creatives, helping to avoid proprietary lock-in. 

## Reference architecture
<a name="s12-reference-architecture"></a><a name="scenario-12-fig1"></a>

![Contextual advertising with non-intrusive ads architecture on AWS showing the asynchronous content classification pipeline, auction-time signal retrieval, non-intrusive ad rendering using IAB SIMID, and shoppable ad matching pipeline](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-12-contextual-non-intrusive-ads.jpg)

*Contextual advertising with non-intrusive ads architecture on AWS showing the asynchronous content classification pipeline, auction-time signal retrieval, non-intrusive ad rendering using IAB SIMID, and shoppable ad matching pipeline*


 The architecture consists of the following components: 

1.  **Content classification pipeline**: Amazon Bedrock Data Automation (for video and audio content) or Amazon Comprehend (for text and web content) classifies publisher content at ingest time. EventBridge triggers classification when new content is published (S3 object creation event). Extracts IAB Content Taxonomy categories, scene segments, brand safety signals, and product detection for shoppable ads. 

1.  **Amazon ElastiCache (classification cache)**: Stores content classification results keyed by content URL or video segment ID with 24-hour TTL. At auction time, contextual signal retrieval is a sub-millisecond ElastiCache lookup, never a synchronous 50–200 ms foundation model inference call. 

1.  **Ad decisioning (enriched bid request)**: During bid evaluation, the ad decisioning service performs an ElastiCache lookup for the content URL. Adds IAB taxonomy categories and brand safety signals to outbound bid request extension fields (content.data.ext.iab\_categories). On cache miss (new content not classified), adds a default IAB category (IAB24: Uncategorized). 

1.  **IAB SIMID overlay rendering**: Non-intrusive creatives (L-banners, overlays, pause ads, and picture-in-picture) are rendered as a separate layer concurrent with content playback using IAB SIMID. SIMID isolates creative code from the player environment, scaling across programmatic demand and avoiding proprietary lock-in. Triggered by real-time signals (pause events, scene changes, ad break markers). 

1.  **IAB OMID measurement**: Non-linear impressions are measured with IAB OMID-compliant verification to provide advertisers standardized viewability and attention metrics for overlay and squeeze-back formats. 

1.  **Shoppable ad pipeline**: AWS Elemental MediaConvert with scene detection identifies product placement moments. Amazon Bedrock or Amazon Rekognition generates image embeddings for products in content frames. Amazon OpenSearch Service vector store stores product catalog embeddings. Similarity search matches content scene embeddings to advertiser products. 

1.  **Product catalog (Amazon S3 \+ DynamoDB)**: Advertiser product catalogs with images, pricing, and purchase URLs. Pre-processed image embeddings stored in DynamoDB for fast retrieval during scene matching. CloudFront serves product images and shoppable ad creative components. 

1.  **Viewer engagement tracking (Amazon Kinesis)**: Client-side SDK sends engagement events (hover, click, interaction, and purchase intent) to Kinesis for real-time analytics. Amazon Managed Service for Apache Flink computes engagement rates, conversion funnel metrics, and revenue attribution for shoppable ad formats. 

## Configuration notes
<a name="s12-configuration-notes"></a>

### Content classification at ingest time
<a name="content-classification-at-ingest-time"></a>

 The most important architectural principle: classify content when it is published, not when it is requested for an ad. Using EventBridge rules on S3 object creation (new video files, new web pages) to trigger asynchronous classification means results are ready before any viewer or ad request arrives. For FAST channel programming with a known 24-hour schedule, trigger pre-classification of the next day's content on a nightly schedule. 

### Cache miss handling
<a name="cache-miss-handling"></a>

 On cache miss at auction time, add a default IAB taxonomy category (IAB24: Uncategorized) rather than invoking Bedrock synchronously. A slightly less targeted ad with 0 ms additional latency is better than a precisely targeted ad with 150 ms additional latency that misses the bid deadline. Monitor cache miss rates, and target 95%\+ hit rate for established content (published more than 2 hours ago). Alert on miss rate spikes indicating either a cache configuration issue or a surge of newly published content. 

### IAB SIMID overlay implementation
<a name="iab-simid-overlay-implementation"></a>

 Adopt IAB SIMID as the interactive container standard for all overlay ad formats. SIMID securely isolates creative code from the player environment. This is essential for programmatic scale where you can't vet every creative individually. Trigger non-linear placements from real-time player events: pause events (pause ads), scene changes (contextually relevant overlays), ad break markers (squeeze-backs). Avoid server-side re-encoding of content for each ad-content combination. This approach fails at programmatic scale where campaign permutations multiply exponentially. 

### Shoppable ad matching pipeline
<a name="shoppable-ad-matching-pipeline"></a>

 Build the embedding-based matching pipeline at content ingest time (not at ad serving time). Use Amazon Bedrock Data Automation or Amazon Rekognition to detect products in content scenes during transcoding. Store scene embeddings in Amazon OpenSearch Service vector store. At serving time, retrieve matching products from the pre-built index through a sub-millisecond vector similarity search, not a real-time embedding generation call. Set minimum similarity score thresholds to limit irrelevant product matches that would frustrate viewers. 

### Privacy by design
<a name="privacy-by-design"></a>

 No user-level cross-site tracking is required for contextual advertising. All signals are collected at the content level, not the user level. This approach has strong legal standing under GDPR and CCPA. First-party logged-in user signals (user has expressed interest in cooking content within your publisher property) can supplement contextual signals without crossing into cross-site tracking. 