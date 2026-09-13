

# Content ingestion and contribution
<a name="smrel01"></a>

Ingestion is the entry point of the streaming workflow. Failures here cascade through the entire delivery chain. Ingestion reliability covers redundant contribution paths for live sources and validated, resumable transfers for file-based content.


| SMREL01: How does your streaming workflow provide reliable content ingestion from live and offline sources? | 
| --- | 
| [SMREL01-BP01 Implement redundant live contribution paths with resilient protocols](smrel01-bp01.md) | 
| [SMREL01-BP02 Implement resilient file-based content ingestion with validation and recovery](smrel01-bp02.md) | 

## Capability intent
<a name="smrel01-intent"></a>
+ Live streams continue without interruption when individual contribution sources, encoders, or network paths fail.
+ Large media files transfer reliably with automatic recovery from network interruptions.
+ Content is validated before entering the processing pipeline.
+ Geographic redundancy helps protect against site-level failures at ingest.

## Maturity levels
<a name="smrel01-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | The organization relies on a single encoder and network path per live source. File uploads restart from the beginning after any interruption. | 
| 2 | Emerging | Basic redundancy exists for the highest-priority live feeds. Resumable uploads are available but not consistently used across all ingest workflows. | 
| 3 | Defined | All live sources use redundant contribution paths with resilient protocols. File transfers are resumable and content is validated before entering the pipeline. | 
| 4 | Proactive | Geographic redundancy helps protect against site-level failures. Automated health checks trigger failover between contribution paths without operator intervention. | 
| 5 | Optimized | Ingestion reliability is continuously measured and improved. Contribution path selection adapts dynamically based on real-time network conditions and historical failure patterns. | 

## Common issues to watch for
<a name="smrel01-issues"></a>
+ Single encoder or single network path for live contribution with no redundancy.
+ No resume capability for large file transfers, requiring full re-upload on failure.
+ Content entering the processing pipeline without integrity or quality validation.
+ Plain RTP without retransmission for contribution over unreliable networks.