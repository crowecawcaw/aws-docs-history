

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

## Common issues to watch for
<a name="smrel01-issues"></a>
+ Single encoder or single network path for live contribution with no redundancy.
+ No resume capability for large file transfers, requiring full re-upload on failure.
+ Content entering the processing pipeline without integrity or quality validation.
+ Plain RTP without retransmission for contribution over unreliable networks.