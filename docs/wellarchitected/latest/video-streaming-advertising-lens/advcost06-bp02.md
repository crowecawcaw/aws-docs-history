

# ADVCOST06-BP02 Optimize VOD storage costs for FAST channel source content

 FAST channels draw from a VOD library with highly variable access patterns. Some titles play daily while others remain idle for weeks. Automatic storage tiering moves objects between access tiers based on access patterns, so storage costs drop without manual management. 

 **Desired outcome:** 
+  VOD storage costs are automatically optimized based on actual content access patterns. 
+  High-rotation titles stay on fast storage, and dormant content moves to lower-cost tiers automatically. 
+  Unused renditions (bitrates never served) are identified and removed. 

 **Common anti-patterns:** 
+  Storing all VOD assets in S3 Standard regardless of access frequency, so the same per-GB rate applies to titles played daily and to dormant content that has not been scheduled in weeks or months. 
+  Manually managing storage tiers through lifecycle policies based on content age rather than actual access patterns, which moves recently ingested but rarely scheduled titles too slowly and demotes recently re-promoted titles that are now in active rotation. 
+  Retaining every bit rate rendition generated during initial transcode without auditing which renditions your FAST channels actually serve, so storage costs continue on unused quality variants that no player ever requests. 
+  Using S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive for dormant VOD content that may be scheduled with short notice, which introduces retrieval delays that limit timely channel assembly when programming decisions change rapidly. 
+  Never analyzing per-title access patterns to identify content that should be archived or removed entirely, so the VOD library grows indefinitely with titles that have zero probability of future scheduling but continue incurring storage charges. 

 **Benefits of establishing this best practice:** 
+  Automatic cost reduction as content ages and access frequency drops 
+  No operational overhead: tiering is automated based on access patterns 
+  Intelligent-Tiering retrieval is instant for all access tiers 
+  Consolidating renditions reduces per-title storage footprint 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 A small percentage of titles (daily rotation, popular series) generate most of the read requests, while the majority of the catalog remains dormant between scheduling cycles. Paying the same per-GB storage rate for both categories wastes money on content that might not be accessed for weeks or months. 

 [S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) monitors object-level access patterns and moves objects between storage tiers automatically. Objects accessed frequently stay in the Frequent Access tier. Objects not accessed for 30 days move to Infrequent Access, which costs less. Optional Archive Access (90 days) and Deep Archive Access (180 days) tiers handle dormant content. All Intelligent-Tiering tiers provide instant retrieval with no retrieval fees, so your programming teams can schedule any title with no lead time. 

 Manual lifecycle policies move objects based on age since creation, not access patterns. This mishandles two scenarios: recently ingested content that was never scheduled (needs to tier down quickly, but lifecycle policies keep it in Standard) and older content that re-enters active rotation (lifecycle policies might have already moved it to a tier with retrieval delays). 

 Renditions are a second way to reduce storage. Initial transcode produces multiple bit rate and resolution variants, and players do not request all of them. Some quality levels receive zero requests because FAST channel players negotiate specific ABR ladders and never select certain intermediate bitrates. Removing these unused renditions reduces per-title storage footprint without affecting playback quality. 

 [S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) shows whether tiering is working. Monthly reports show how objects are distributed across tiers. If most storage remains in the Frequent Access tier despite known low-rotation content, you might need to adjust the Archive Access tier configuration. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable S3 Intelligent-Tiering on VOD asset buckets:** Enable S3 Intelligent-Tiering on all VOD storage buckets. Configure optional Archive Access tiers (objects not accessed for 90 days) and Deep Archive Access tiers (180 days) for dormant catalog content. No retrieval fees apply for the standard Intelligent-Tiering tiers. 

1.  **Audit and remove unused renditions:** Analyze CloudFront access logs to identify which renditions (resolution, bit rate, codec combinations) are actually being requested. Remove renditions that receive zero requests over a 30-day period. Document the storage savings from rendition consolidation. 

1.  **Monitor storage tier distribution using S3 Storage Lens:** Enable S3 Storage Lens on VOD buckets. Review monthly reports showing the distribution of objects across storage tiers. Track the percentage of storage in lower-cost tiers as a cost optimization metric. 

## Resources
<a name="resources"></a>

 **Related services:** 
+  [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) 
+  [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) 