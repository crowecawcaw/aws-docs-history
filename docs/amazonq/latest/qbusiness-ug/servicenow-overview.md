

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# ServiceNow Online connector overview
<a name="servicenow-overview"></a>

The following table gives an overview of the Amazon Q Business ServiceNow Online connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Basic, OAuth 2.0 with Resource Owner Password Flow
  - **Feature:** Authentication credentials / **Support:** +  ServiceNow Online host URL <br />+  User name <br />+  Password <br />+  ServiceNow Online version  +  ServiceNow Online host URL <br />+  User name <br />+  Password <br />+  Client ID <br />+  Client secret <br />+  ServiceNow Online version   ServiceNow Online admin privileges required. 
  - **Feature:** Supported versions / **Support:** All ServiceNow versions
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-user-management).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes 
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes. Supports custom fields for all entities.
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Knowledge articles <br />+  Knowledge article attachments <br />+  Service catalogs <br />+  Active service catalog items <br />+  Inactive service catalog items <br />+  Service catalog attachments <br />+  Incidents <br />+  Active incidents <br />+  Inactive incidents <br />+  All active incident types <br />+  Resolved incidents <br />+  Open incidents <br />+  Open – Unassigned incidents <br />+  Incident attachments See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-field-mappings).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Crawl public knowledge articles <br />+  Crawl knowledge articles with filter query <br />+  Crawl knowledge article attachments <br />+  Use regex filters for knowledge articles <br />+  Crawl service catalog items <br />+  Crawl service catalog item attachments <br />+  Use regex filters for service catalog items <br />+  Crawl incidents <br />+  Crawl incident attachments <br />+  Crawl incidents with filter query <br />+  Use regex filters for active and inactive incidents <br />+  Including and excluding content by file type <br />+  Including and excluding content based on file name <br />+  Crawl ACL for knowledge article, service catalogs, and incidents 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.

