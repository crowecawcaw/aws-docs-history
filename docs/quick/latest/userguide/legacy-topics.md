# Working with legacy Topics

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                                               |
| ------------------------------------------------------------- |
| Intended audience:<br>Amazon Quick administrators and authors |

If you created Topics before the multi-dataset Topics feature launched, your existing
Topics are now classified as _legacy Topics_. Legacy Topics continue
to work as before — their behavior and capabilities are unchanged.

## Differences between legacy Topics and new Topics

| Feature           | New Topics                                                                                                    | Legacy Topics                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Purpose           | Multi-dataset semantic layer with cross-dataset<br>relationships, runtime joins for both chat and<br>analysis | Single-dataset semantic layer for natural language<br>Q&A                                                     |
| Datasets          | Up to 12 datasets with defined relationships                                                                  | Multiple datasets can be added, but no cross-dataset<br>joins at query time                                   |
| Chat behavior     | LLM-powered chat agent generates cross-dataset SQL with<br>runtime joins                                      | ML-based fuzzy search model selects one dataset, then<br>queries only that dataset                            |
| Analysis support  | Use as data model for analysis sheets with runtime<br>joins                                                   | Limited to NLQ search bar in analysis                                                                         |
| Metadata location | Dataset enrichment lives in the dataset itself;<br>Topic holds cross-dataset logic                            | Metadata (synonyms, calculated fields, named entities,<br>filters) stored in the separate legacy Topic object |
| Relationships     | Explicit join keys defined between dataset<br>pairs                                                           | Not supported                                                                                                 |

## Migrating from legacy Topics

You can migrate your business context from legacy Topics into enriched datasets
using Dataset Enrichment in the new data preparation experience. This moves column
descriptions, synonyms, calculated fields, named entities, filters, and custom
instructions from the separate legacy Topic object into the dataset itself.

After migrating your dataset-intrinsic metadata into Dataset Enrichment, you can
create a new multi-dataset Topic that uses the enriched datasets with defined
relationships.

For detailed migration guidance, see [Data Preparation Experience (New)](data-prep-experience-new.md "data-prep-experience-new.md").
