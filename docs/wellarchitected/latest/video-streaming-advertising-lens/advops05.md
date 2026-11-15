

# SGAI operations
<a name="advops05"></a>

 Server-Guided Ad Insertion (SGAI) has two patterns with materially different operational characteristics: hybrid and personalized. 

 In hybrid SGAI, the server generates manifests that contain SCTE-35 markers preserved for client-side ad decisioning, and those manifests are CDN-cacheable. 

 In personalized SGAI, the server generates per-session manifests that are not CDN-cacheable. 

 This capability focuses primarily on the hybrid SGAI pattern given its CDN-caching implications and broader scope of impact for operational failures. The goal is full visibility into the SGAI pipeline from manifest creation through ad delivery, with automated alerting on ad break completion failures. 


|  ADVOPS05: How do you achieve operational reliability and observability for your server-guided ad insertion pipeline?  | 
| --- | 
| [ADVOPS05-BP01 Implement manifest generation observability with SCTE-35 marker validation](advops05-bp01.md) | 
| [ADVOPS05-BP02 Implement observability for ad break orchestration across server and client](advops05-bp02.md) | 
| [ADVOPS05-BP03 Create SGAI-specific runbooks and playbooks for manifest and player failures](advops05-bp03.md) | 

## Capability intent
<a name="advops05-capability-intent"></a>
+  Every generated manifest is validated for SCTE-35 marker integrity before CDN distribution, with real-time alerting on validation failures and automated fallback to last-known-good manifests. 
+  Full visibility covers ad break orchestration from server-side manifest generation through CDN-cached delivery to client-side personalized ad fetching, with correlated tracing across all components. 
+  Documented, tested runbooks exist for all anticipated SGAI failure modes, enabling rapid incident response with clear escalation paths. 

## Common issues to watch for
<a name="advops05-common-issues-to-watch-for"></a>
+  Treating SCTE-35 as a monolithic signal without distinguishing between message types: spliceinsert, timesignal, splicenull, and privatecommand have distinct failure modes that require different diagnostic steps. 
+  Validating only spliceinsert markers while ignoring other message types that also affect ad break detection. 
+  Monitoring only the server-side manifest generation without visibility into CDN delivery or client-side ad fetch outcomes. 
+  Not distinguishing between hybrid and personalized SGAI operational patterns. They have distinctly different failure profiles and scope-of-impact characteristics. 