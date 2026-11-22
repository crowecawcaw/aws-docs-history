

# AI Assistant Memory in Amazon OpenSearch Service

AI Assistant Memory is a service-managed memory layer that powers Agentic Chat and the Investigation Agent. It retains context within your conversation or investigation, so that you have a consistent experience across different feature pages, browser tabs, and page refreshes. AI Assistant Memory works automatically and requires no user configuration.

AI Assistant Memory is built on the OpenSearch agent memory framework. Memory storage is isolated by user ID for privacy.

## Data protection
<a name="application-agentic-memory-data-protection"></a>

AI Assistant Memory is free to use. Customer data stored in AI Assistant Memory is encrypted with a service-managed key. If you enabled customer managed key (CMK) encryption for your OpenSearch UI application, your memory data will be encrypted with your CMK instead. Memory is stored in a service-managed Amazon OpenSearch Serverless collection.

For more information about CMK encryption, see [Enabling customer managed key encryption for AI Assistant Memory](application-encryption-cmk.md#application-encryption-cmk-agentic-memory).

## Limitations
<a name="application-agentic-memory-limitations"></a>

AI Assistant Memory cannot retain context across different conversation threads.