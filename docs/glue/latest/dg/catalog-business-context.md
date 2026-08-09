# Adding business context

###### Note

Business context and semantic search are in preview for AWS Glue in the following
AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), and Europe (Ireland).
This feature is subject to change.

By enriching assets with additional context in AWS Glue Data Catalog, assets are more easily discoverable and understandable. Assets are
automatically populated in the catalog when tables, views, and columns are registered. You
enrich these assets with glossary terms, custom metadata fields, and
skill assets. Using the new Glue Search API, you can discover data by
semantic meaning in addition to exact keyword matching.

You can add the following types of context:

- **Custom metadata fields** – Pre-defined
  key-value templates that standardize metadata that can be attached to assets.
- **Glossary terms** – Defined vocabulary entries
  (for example, "PII" or "Active User") that provide consistent business definitions
  across your organization.
- **Skill assets** – References to URI locations
  containing instructions and references such as domain definitions, usage rules, and
  query patterns.

## Limitations

The following limitations apply during preview:

- There is no asset-level access control. Access is managed through IAM.

###### Topics

- [Getting started with business context in the Data Catalog](catalog-business-context-getting-started.md "catalog-business-context-getting-started.md")
- [Attaching forms](catalog-metadata-forms.md "catalog-metadata-forms.md")
- [Business glossaries for AWS Glue Data Catalog](catalog-business-glossaries.md "catalog-business-glossaries.md")
- [Skill assets for AI agents](catalog-skill-assets.md "catalog-skill-assets.md")
- [Semantic search for AWS Glue Data Catalog](catalog-semantic-search.md "catalog-semantic-search.md")
