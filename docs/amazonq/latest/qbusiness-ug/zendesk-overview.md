

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Zendesk connector overview
<a name="zendesk-overview"></a>

The following table gives an overview of the Zendesk connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** OAuth 2.0 with implicit grant authentication, OAuth 2.0 authentication
  - **Feature:** Authentication credentials / **Support:** +  OAuth 2.0 with Resource Owner Password Flow - Implicit grant token <br />+  OAuth 2.0 authentication - Zendesk Client ID <br />+  OAuth 2.0 authentication - Zendesk Client secret <br />+  OAuth 2.0 authentication - Zendesk Username <br />+  OAuth 2.0 authentication - Zendesk Password 
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-user-management.html). 
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Ticket <br />+  Ticket comment <br />+  Ticket comment attachment <br />+  Community topic <br />+  Community post <br />+  Community post comment <br />+  Article <br />+  Article attachment <br />+  Article comment  Each instance of an entity is crawled as a single document. See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/zendesk-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Organization name filter <br />+  Crawl tickets <br />+  Crawl ticket comments <br />+  Crawl ticket comment attachments <br />+  Crawl articles <br />+  Crawl article attachments <br />+  Crawl article comments <br />+  Crawl community topics <br />+  Crawl community posts <br />+  Crawl community post comments <br />+  Including and excluding content by file type <br />+  Including content based on a specific date 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.
  - **Feature:** [Crawled as a document](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html#connector-doc-crawl) / **Support:** +  Each ticket <br />+  Each ticket comment <br />+  Each ticket comment attachment <br />+  Each article <br />+  Each article attachment <br />+  Each article comment <br />+  Each community topic <br />+  Each community post <br />+  Each community post comment 

