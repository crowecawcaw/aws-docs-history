

# Data sovereignty requirements
<a name="dssec06"></a>

 Enforcing sovereignty controls on data depends on first classifying it. Before an organization can apply those controls, it must know what data it has, where it resides, and what jurisdictional requirements govern its storage, processing, retention, and access. Sovereignty classification goes beyond standard sensitivity labels to include jurisdiction-specific attributes such as data residency requirements, applicable regulatory frameworks, and cross-border transfer restrictions. 

 This capability covers data discovery, sovereignty-aware classification, and the consistent application of sovereignty metadata through enforceable tagging. 


|  DSSEC06: How do you apply data sovereignty requirements?  | 
| --- | 
| [DSSEC06-BP01 Classify data with sovereignty attributes](dssec06-bp01.md) | 

## Capability intent
<a name="capability-intent-5"></a>
+  Data is classified with jurisdiction-specific sovereignty attributes that go beyond standard sensitivity labels to include residency, retention, and transfer requirements. 
+  Discovery and classification are automated through event-driven pipelines, so new data is classified as it arrives rather than through periodic manual review. 
+  Sovereignty metadata is attached to resources through consistent, enforceable tagging that downstream controls can evaluate programmatically. 
+  Classification decisions are traceable to specific regulatory requirements, providing auditors with a clear link between data handling and compliance obligations. 
+  The classification scheme adapts when jurisdictional requirements change, and existing data is re-evaluated against updated criteria. 

## Maturity levels
<a name="maturity-levels-5"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Data classification is informal or absent. Teams apply sensitivity labels inconsistently, and sovereignty-specific attributes are not captured. Tagging is voluntary and not enforced.  | 
|  2  |  Emerging  |  A classification scheme exists that includes some sovereignty attributes. Discovery is partially automated for known data stores. Tagging policies are defined but enforcement is inconsistent across accounts.  | 
|  3  |  Defined  |  Classification includes jurisdiction, residency, retention, and transfer attributes applied through automated pipelines. Tag policies are enforced through preventive controls that block untagged resources. New data is classified at ingestion time.  | 
|  4  |  Proactive  |  Classification rules are updated ahead of regulatory changes. Discovery pipelines scan for new data stores automatically as infrastructure changes. Misclassification is detected through drift monitoring and triggers remediation.  | 
|  5  |  Optimized  |  Classification accuracy is measured and improved through feedback loops. Historical data is periodically re-evaluated against current requirements. Classification metadata drives downstream enforcement automatically, with no manual interpretation layer between classification and control.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-5"></a>
+  Classification schemes that capture sensitivity (public, confidential, and restricted) but omit jurisdiction-specific attributes, leaving sovereignty enforcement without the metadata it needs. 
+  Tagging policies defined but not enforced through preventive controls, resulting in resources that bypass classification entirely and operate outside sovereignty governance. 
+  Discovery limited to known data stores, missing shadow data in developer accounts, temporary storage, and data replicated through cross-account sharing. 
+  Classification applied at creation time but never revisited, so data that changes jurisdiction requirements because of regulatory updates remains governed by outdated metadata. 
+  Rules-based classification that produces high false-positive rates, eroding team confidence in the system and leading to manual overrides that weaken enforcement. 