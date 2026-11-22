

# Content integrity, brand safety, and ad fraud prevention

 Advertising decisions depend on claims about the creative, content environment, seller, supply path, and viewer session. This capability establishes evidence for those claims and keeps an approved decision valid from campaign activation through delivery. 

 The scope includes malvertising, brand suitability, supply-chain misrepresentation, creative substitution, and fabricated delivery sessions. It doesn't cover volumetric protection at the infrastructure boundary or the privacy terms governing audience data. 


|  ADVSEC04: How do you preserve content integrity and guard against unsafe placement, supply-chain fraud, and delivery manipulation?  | 
| --- | 
| [ADVSEC04-BP01 Validate and sanitize ad creative content before campaign activation](advsec04-bp01.md) | 
| [ADVSEC04-BP02 Create guardrails and controls to maintain brand safety and content moderation within your workload](advsec04-bp02.md) | 
| [ADVSEC04-BP03 Implement supply chain transparency controls to block ad fraud](advsec04-bp03.md) | 
| [ADVSEC04-BP04 Secure ad creative delivery and content integrity across converged channels](advsec04-bp04.md) | 

## Capability intent
<a name="advsec04-capability-intent"></a>
+  Evidence from an accountable authority supports creative, content, seller, supply-path, and session claims. 
+  Release, placement, and delivery decisions remain valid when dependencies, relationships, content, or threat indicators change. 
+  Blocking, quarantine, review, revocation, and fraud responses reflect defined risk states rather than informal operator judgment. 
+  Workload controls enforce advertiser and publisher policies consistently across auction, stitching, and delivery boundaries. 
+  Investigation records connect the affected asset or session to the evidence, decision, owner, and exposure window. 

## Common issues to watch for
<a name="advsec04-common-issues-to-watch-for"></a>
+  Approving only the submitted creative file although remote scripts, wrappers, media, or destinations can change its behavior after release. 
+  Classifying content only at campaign setup, which misses content drift and advertiser-specific suitability decisions during delivery. 
+  Treating public seller declarations as the commercial authority, which can preserve stale or unauthorized supply relationships. 
+  Validating only the first or last supply-path participant, which leaves intermediary misrepresentation undetected. 
+  Trusting an approved asset URL or authenticated session without verifying delivered bytes and behavior, which permits substitution and fabricated activity. 