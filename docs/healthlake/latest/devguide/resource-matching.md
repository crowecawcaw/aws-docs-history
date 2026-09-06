

# Matching duplicate FHIR resources
<a name="resource-matching"></a>

Resource matching identifies FHIR resources in a HealthLake data store that represent the same real-world entity and links them without modifying or merging the original resources. When aggregating data from multiple systems, resource matching connects the same entity written as several separate resources so you can build an accurate, unified view without operating a master data management system.

**Important**  
Resource matching is available as a preview capability and is subject to change. The features, and documentation described in this guide may be modified before general availability.

Resource matching is non-destructive: when it finds a match, it creates a FHIR `Linkage` resource that points to the linked resources and leaves the originals unchanged.

**Note**  
Resource matching links resources based on the healthcare identifiers present in your data. It does not perform probabilistic or demographic fuzzy matching on names, dates of birth, or addresses.

**Topics**
+ [How it works](resource-matching-how-it-works.md)
+ [Supported resources](resource-matching-supported-types.md)
+ [Filtering placeholder values](resource-matching-placeholder-filtering.md)
+ [Working with Linkage](resource-matching-linkage-resources.md)
+ [Querying linked data](resource-matching-querying.md)
+ [Tracking linkage history](resource-matching-tracking-history.md)
+ [Enable resource matching](resource-matching-enabling.md)