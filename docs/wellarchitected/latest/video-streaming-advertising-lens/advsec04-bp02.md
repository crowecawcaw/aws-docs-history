

# ADVSEC04-BP02 Create guardrails and controls to maintain brand safety and content moderation within your workload
<a name="advsec04-bp02"></a>

 Ad platforms decide placements faster than people can review content. Without automated classification against your organization's taxonomy, the service can serve ads next to content that violates an advertiser's brand-safety requirements. The taxonomy you designate, and the person who owns it, limit what your service can enforce. 

 **Desired outcome:** 
+  You have a named, versioned content taxonomy with an accountable owner, and every classification your service enforces maps to that taxonomy. 
+  You have a classifier for each content modality you process, and every choice beyond managed moderation is justified by a documented gap in coverage or accuracy. Classification results are precomputed and available to the decisioning path as a lookup. 
+  You have advertiser-selectable enforcement profiles whose category-to-action mappings are approved and published, rather than inferred from profile names. 
+  You have measured false-positive and false-negative rates for each category. Every classifier, prompt, or mapping change stays within the agreed limits before production. 
+  You have enforcement evidence that records each outcome as allow, block, or route for review, along with the detected categories, taxonomy version, and applied profile. 

 **Common anti-patterns:** 
+  Citing a discontinued industry program as the governing authority for classifications, which leaves no owner to resolve category disputes or approve mappings. 
+  Naming enforcement profiles after risk postures without recording which categories each profile blocks, so advertisers and service operators interpret the same name differently. 
+  Reaching for a custom classification model or a foundation model when managed moderation labels already cover the enforced categories, which adds cost and latency for no gain in coverage. 
+  Classifying content once at campaign setup and never reclassifying, so new comment threads and channel updates leave the stored classification out of date. 
+  Tracking infrastructure configuration as a proxy for brand safety when the requirement is content-level classification and enforcement. 
+  Treating confidence scores as taxonomy categories, which buries the mapping decision inside classifier output. 

 **Benefits of establishing this best practice:** 
+  Category disputes and exception requests reach a named decision-maker, so classification changes don't stall. 
+  Advertisers can see which categories a profile blocks, which supports transparency reporting and contract commitments. 
+  Scheduled reclassification catches content that moves into a blocked category after approval, before an advertiser reports an unsuitable placement. 
+  Measured error rates give safety and yield teams the same numbers to negotiate over. 
+  Recorded taxonomy versions help reviewers interpret historical enforcement decisions during an advertiser audit. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Brand-safety classification once had a cross-industry coordinator. The World Federation of Advertisers discontinued the Global Alliance for Responsible Media (GARM) in 2024, and a settlement with X in 2026 confirmed that WFA will not restart it. No governing body took over that coordination role. In April 2026 the US Federal Trade Commission and eight states charged the largest agency holding companies with unlawfully agreeing on common brand-safety standards, and the resulting orders prohibit such agreements. Your organization is now accountable for the taxonomy it enforces. A shared taxonomy remains useful as a technical vocabulary for implementation, and advertiser requirements guide how your service applies the taxonomy. 

 A *content taxonomy* names and identifies categories so that two systems can exchange a label. A *suitability framework* assigns risk levels to content within those categories. An *enforcement profile* is your own mapping from categories and risk levels to actions. Category counts differ by source, which is why the recorded version matters more than the name. IAB Tech Lab's Content Taxonomy 2.2, co-developed with GARM in 2020, defined 11 sensitive topic categories across four risk levels of Floor, High Risk, Medium Risk, and Low Risk. GARM later added Misinformation, which brought its framework to 12 categories. The 4A's Brand Safety Floor names 13. Content Taxonomy 3.0 expanded the wider taxonomy from roughly 400 categories to more than 1,500, and version 3.1 followed in December 2024. Record the taxonomy version with each classification so that reviewers can interpret its categories using the vocabulary in effect at the time. 

 Managed moderation services classify content against provider-defined labels without requiring you to train a classifier. Coverage varies by category, modality, and language. Service labels and taxonomy categories serve different purposes, so your workload needs a mapping layer between them. That mapping is a policy decision rather than a classifier output. 

 The classifier type determines how the provider and your team divide responsibility for classifier development and versioning. Your team remains responsible for validating classifier behavior in your workload. A managed moderation model ships inside the service and changes version on the provider's schedule, as Amazon Rekognition Content Moderation does. A custom classification model is one your team trains and retrains on your own labeled data. A foundation model (FM) on [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) takes category definitions as instructions instead of learning them from labels. 

 Choose a classifier type that meets the documented category, modality, and accuracy requirements. Add another classifier type only for a measured coverage or accuracy gap. Rekognition Custom Moderation adapters use annotated images to improve moderation accuracy for a specific use case. Use a custom classification model when tests show that managed moderation or an FM doesn't meet a required domain distinction. This option makes your team responsible for labeled data, evaluation, deployment, retraining, and ongoing maintenance of the custom classifier. An FM can apply category definitions outside the selected managed service's label set. Measure classification quality, response consistency, latency, and cost for the selected classifier and configuration. 

 Classification can exceed the workload-specific latency budget for a bid decision, so the auction path uses precomputed classifications. Precomputing introduces staleness. A page classified as safe yesterday can have unsafe comments today, and a channel can publish new content under an approved identifier. You choose how much staleness to tolerate, because you can't remove it entirely. Don't reuse latency figures from another workload. Response times move with media size and duration, the classifier type and version you deployed, Region, concurrency, retry behavior, and how you wire the pipeline. 

 False positives cost inventory. Blocking a page removes every ad opportunity that page would have served, and that number depends on slots per page, fill rate, and how often the page is requested. Safety teams and yield teams talk past each other when they use different denominators. An agreed error budget for each category, expressed in measured ad opportunities rather than page views, gives both teams one number to negotiate over. Stricter thresholds reduce unsafe placements and reject valid inventory at the same time, and no threshold avoids both. 

 Taxonomy requires an owner that approves category mappings, resolves disputes when a classifier and a reviewer disagree, grants time-bound exceptions, and schedules the review that catches upstream taxonomy changes. Without that role the mapping table becomes the real policy, and anyone with code access can change it. A name such as Conservative or Moderate describes a posture rather than a category set, so advertisers and service operators can interpret the same name differently unless the blocked categories are documented. Such names are not defined by GARM, by IAB Tech Lab, or by any service, and the major services each publish their own labels, such as Expanded, Standard, and Restrictive on Amazon DSP, or Maximum, Moderate, and Limited on Google Ads and Display and Video 360. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Designate and version your governing taxonomy:** Record the taxonomy source, version or retrieval date, accountable owner, exception authority, approval date, and next review date in a versioned artifact. Pin the [IAB Tech Lab Content Taxonomy](https://iabtechlab.com/standards/content-taxonomy/) release you deploy for the technical vocabulary. Cite the [WFA statement on GARM](https://wfanet.org/leadership/garm) only as historical origin, never as a current authority. 

1.  **Select a classifier for each modality and language you process:** List the content modalities your workload actually carries, such as image, video, speech, and text, along with the languages you serve. For each modality-language pair, identify which enforced categories the managed labels cover. Consider using [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html) for images and stored video, [Amazon Comprehend toxicity detection](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html) for text, and [Amazon Transcribe toxicity detection](https://docs.aws.amazon.com/transcribe/latest/dg/toxicity.html) for speech. Record every enforced category that has no managed-label coverage for that pair. For each recorded gap, evaluate whether an adapter, a custom classification model, or an FM meets the requirement. Deploy classifiers only for content modalities present in source content or resolved dependencies. 

1.  **Publish the classifier-to-category mapping as reviewable code:** Map the output labels of every selected classifier to your designated categories, and set a confidence threshold for each mapping. Store the mapping next to the taxonomy version in source control. Require the taxonomy owner's approval on every change, because a threshold edit changes enforcement without changing any classifier. 

1.  **Define each enforcement profile as an explicit category-to-action table:** For every profile, list each category, the applicable risk level, and the action of allow, block, or route for review. Require the taxonomy owner's approval on each table, then publish those tables to advertisers rather than the profile names alone. Treat any category missing from a table as a configuration error instead of a default allow. 

1.  **Precompute classifications and expose them as a bid-time lookup:** Run classification outside the auction path and write results to [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.html) or [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html), keyed by content identifier. Store the assigned categories, the taxonomy version, and the classification timestamp with each record. Before launch, define and test whether a lookup miss blocks the placement, routes it for review, or applies another fallback the taxonomy owner approved. 

1.  **Measure classification and lookup latency in your own workload:** Publish percentile metrics to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) for each classification path and for the bid-time lookup. Record the media profiles, the type and version of the classifier, the Region, and the concurrency you used during measurement. Set separate latency objectives for classification and bid-time lookup from these measurements. Repeat the measurements after any classifier or Region change. 

1.  **Set the accuracy gate a change must pass before production:** Build a labeled evaluation set for each category from your own inventory. Measure the false-positive and false-negative rates for each category, then convert the false-positive rate to lost ad opportunities using measured slots and fill rate for the affected inventory. Gate every change behind the agreed false-positive and false-negative limits for each affected category, and any additional limits you document for that category, whether the change is a classifier version, a prompt, retraining data, or a mapping edit. If managed moderation can't meet those limits for a category, evaluate an adapter, a custom classification model, or an FM rather than weakening the limits. 

1.  **Reclassify active content and act on drift:** Schedule reclassification for pages, videos, and channels that remain eligible, at a cadence derived from your staleness tolerance. Alert when a previously eligible item moves into a blocked category. Pause ad delivery on the inventory carried by that item, and notify the advertisers whose profiles block the newly assigned category. 

1.  **Record enforcement evidence for each decision:** Log each outcome as allow, block, or route for review, together with every detected category, its risk level and confidence value, the taxonomy version, the applied profile, and the classification timestamp. Retain these records for the period your advertiser contracts require. If your workload participates in a certification program, also retain any additional evidence that program requires. Route review outcomes back into the labeled evaluation set. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC04-BP01 Validate and sanitize ad creative content before campaign activation](advsec04-bp01.md) 
+  [ADVSEC04-BP03 Implement supply chain transparency controls to block ad fraud](advsec04-bp03.md) 

 **Related documents:** 
+  [IAB Tech Lab Content Taxonomy](https://iabtechlab.com/standards/content-taxonomy/) 
+  [Amazon Rekognition moderating content](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html) 
+  [Amazon Comprehend trust and safety](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html) 
+  [Amazon Transcribe detecting toxic speech](https://docs.aws.amazon.com/transcribe/latest/dg/toxicity.html) 
+  [WFA statement on the Global Alliance for Responsible Media, historical](https://wfanet.org/leadership/garm) 
+  [FTC action on brand-safety standard-setting, April 2026](https://www.ftc.gov/news-events/news/press-releases/2026/04/ftc-takes-action-restore-competition-digital-advertising-ecosystem) 
+  [TAG Brand Safety Certified program](https://www.tagtoday.net/brand-safety) 

 **Related services:** 
+  [Amazon Rekognition](https://aws.amazon.com/rekognition/) 
+  [Amazon Comprehend](https://aws.amazon.com/comprehend/) 
+  [Amazon Transcribe](https://aws.amazon.com/transcribe/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 