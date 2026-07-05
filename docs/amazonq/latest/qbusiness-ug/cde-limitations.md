Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Document enrichment limitations

When you use document enrichment, be aware of the following limitations that affect how you can process different types of content.

## Multimedia content limitations

Document enrichment doesn't support the following multimedia file types:

- Audio files - You can't use document enrichment operations on audio content.
- Video files - You can't use document enrichment operations on video content.

## Visual content in documents limitations

When you work with visual content in documents, the following limitations apply:

- If PostExtractionHook is configured, visual content in the document is ignored and not Indexed.

### Connector-specific Document Enrichment behavior

When you enable visual content in documents, PreExtractionHookConfiguration operations for the following connectors are limited to metadata updates only:

- Web Crawler
- ServiceNow
- Confluence
- Salesforce
- SharePoint
