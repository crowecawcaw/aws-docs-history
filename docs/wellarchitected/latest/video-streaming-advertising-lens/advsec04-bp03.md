

# ADVSEC04-BP03 Implement supply chain transparency controls to block ad fraud
<a name="advsec04-bp03"></a>

 Demand-side platforms (DSPs) need to verify in real time that advertisers and agencies purchase legitimate inventory across exchanges. With the IAB Tech Lab transparency stack (ads.txt, sellers.json, app-ads.txt, and the SupplyChain object), DSPs can validate each impression opportunity in the programmatic supply chain. 

 **Desired outcome:** 
+  You have published and maintained ads.txt and app-ads.txt files that declare all authorized sellers of your inventory, hosted with high availability and version control. 
+  Your bid evaluation pipeline validates the supply chain by cross-referencing bid requests against published sellers.json and ads.txt declarations. 
+  You can detect and block domain spoofing attempts where unauthorized parties impersonate your domains to sell fraudulent inventory. 

 **Common anti-patterns:** 
+  Publishing an ads.txt file once and never updating it as partnerships change, so declarations go stale and either block legitimate partners or authorize departed ones. 
+  Hosting ads.txt without version control or object lock can permit unauthorized changes that might authorize fraudulent sellers. 
+  Checking only ads.txt without validating the full SupplyChain object in bid requests, which misses intermediary fraud in multi-hop supply paths. 

 **Benefits of establishing this best practice:** 
+  Blocks domain spoofing by providing a publicly verifiable declaration of authorized sellers, which gives buyers a source for checking inventory claims. 
+  Supports the Trustworthy Accountability Group (TAG) Certified Against Fraud program requirements and advertiser supply path optimization (SPO) preferences. 
+  Helps protect publisher revenue by confirming only authorized partners can monetize your inventory, reducing the risk of unauthorized resale. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The evidence sources in a supply-chain transparency system that must agree are the commercial relationship record, the public declarations derived from it, and the chain submitted with each bid request. The commercial record is the relationship authority because it identifies who approved a seller, which inventory the seller can represent, and when that authority ends. Public files are verifiable projections of that record. The commercial relationship record remains authoritative. 

 An ads.txt entry can authorize the first seller, whereas later intermediaries can misrepresent inventory. A syntactically valid SupplyChain object can name accounts that no publisher approved. Validation therefore needs evidence for every hop and a complete supply-path decision. When sources disagree, preserve the conflict and use the relationship authority to choose a fail-closed or review outcome instead of the declaration that permits the bid. 

 Missing or incomplete evidence leaves a claim unsupported. Stale evidence supported a claim earlier but may not support it now, so the same file can warrant a hold rather than a rejection. Contradictory evidence is a question of authority rather than of freshness. Unparseable evidence is most often mishandled. A parser that can't read a file treats it as absent and applies the default, so a broken input becomes an approval. 

 The revocation window runs from a commercial termination or security decision until buyers can no longer accept the removed path. Publishing delay, cache behavior, and downstream polling all contribute to it. Assign one team to measure this window, reconcile the evidence sources, and investigate stale or unauthorized paths across engineering, ad operations, and security. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish the relationship authority:** Maintain each approved seller, seller ID, inventory scope, domain or application, approving owner, approval date, status, and revocation time in a controlled partner registry. Limit relationship changes to partner-governance role holders, and treat the registry as authoritative when a public file disagrees with it. 

1.  **Publish declarations from the approved registry:** Generate ads.txt, app-ads.txt, and sellers.json from approved relationship records. Store them in Amazon S3 with versioning and protected retention, distribute them through Amazon CloudFront, and set cache behavior from the revocation-window objective. Record the cache lifetime you publish and the revocation-window objective it derives from. 

1.  **Define the evidence each supply path hop must carry:** For every hop, require a registry record naming the approved seller and its inventory scope, a matching sellers.json entry, and a SupplyChain node whose seller and domain values correspond to both. For the first hop, require a publisher ads.txt or app-ads.txt entry authorizing that seller for the specific domain or app bundle. Record the maximum age you accept for partner declaration snapshots and how often you refresh them. 

1.  **Validate each supply path and apply a decision outcome:** Parse the SupplyChain object in each OpenRTB bid request and evaluate every hop against the evidence contract. Reject the path when required evidence is missing or incomplete, when a file or object is unparseable, or when the chain doesn't terminate at the claimed publisher. Hold for review when evidence exceeds the maximum age you accept, or when sources conflict and the registry can't resolve the disagreement. Where the registry does resolve it, apply that outcome and record which source was overruled. 

1.  **Reconcile and revoke relationships:** Compare the registry, public declarations, and externally observed files after every partner change. Alert when a removed account remains published, when an unapproved account appears, or when propagation exceeds the revocation objective. 

1.  **Bound and expire exceptions:** Permit a path that fails validation only under a time-boxed exception scoped to a named seller and inventory path, with a recorded justification. Name the authority that can grant one and the maximum duration it can run. Expire exceptions automatically and re-review them rather than renewing them without review. 

1.  **Monitor for inventory and domain spoofing:** Compare bid volume claiming each domain or application with the publisher's available inventory. Route material discrepancies and repeated unauthorized paths to ad operations and security investigation. Define how a partner disputes a rejection, and how a confirmed false positive updates the registry or the evidence contract. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC04-BP01 Validate and sanitize ad creative content before campaign activation](advsec04-bp01.md) 
+  [ADVSEC01-BP02 Restrict DSP access to allow only authorized SSPs](advsec01-bp02.md) 

 **Related documents:** 
+  [IAB Tech Lab ads.txt specification](https://iabtechlab.com/ads-txt/) 
+  [IAB Tech Lab sellers.json specification](https://iabtechlab.com/sellers-json/) 
+  [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) 
+  [TAG Certified Against Fraud](https://www.tagtoday.net/fraud) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 