

# Working with legacy Topics
<a name="legacy-topics"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  Amazon Quick administrators and authors  | 

If you created Topics before the multi-dataset Topics feature launched, your existing Topics are now classified as *legacy Topics*. Legacy Topics continue to work as before — their behavior and capabilities are unchanged.

## Differences between legacy Topics and new Topics
<a name="legacy-topics-differences"></a>


| Feature | New Topics | Legacy Topics | 
| --- | --- | --- | 
| Purpose | Multi-dataset semantic layer with cross-dataset relationships, runtime joins for both chat and analysis | Single-dataset semantic layer for natural language Q&A | 
| Datasets | Up to 12 datasets with defined relationships | Multiple datasets can be added, but no cross-dataset joins at query time | 
| Chat behavior | LLM-powered chat agent generates cross-dataset SQL with runtime joins | ML-based fuzzy search model selects one dataset, then queries only that dataset | 
| Analysis support | Use as data model for analysis sheets with runtime joins | Limited to NLQ search bar in analysis | 
| Metadata location | Dataset enrichment lives in the dataset itself; Topic holds cross-dataset logic | Metadata (synonyms, calculated fields, named entities, filters) stored in the separate legacy Topic object | 
| Relationships | Explicit join keys defined between dataset pairs | Not supported | 

## Migrating from legacy Topics
<a name="legacy-topics-migration"></a>

You can migrate your business context from legacy Topics into enriched datasets using Dataset Enrichment in the new data preparation experience. This moves column descriptions, synonyms, calculated fields, named entities, filters, and custom instructions from the separate legacy Topic object into the dataset itself.

After migrating your dataset-intrinsic metadata into Dataset Enrichment, you can create a new multi-dataset Topic that uses the enriched datasets with defined relationships.

For detailed migration guidance, see [Data Preparation Experience (New)](data-prep-experience-new.md).