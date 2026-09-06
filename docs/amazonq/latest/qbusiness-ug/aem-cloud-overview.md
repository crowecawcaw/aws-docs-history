

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# AEM (Cloud) connector overview
<a name="aem-cloud-overview"></a>

The following table gives an overview of the Amazon Q Business AEM (Cloud) connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Basic, OAuth 2.0 with Client Credentials Flow
  - **Feature:** Authentication credentials / **Support:** +  AEM (Cloud) host URL <br />+  Username of AEM user <br />+  Password of AEM user  +  AEM (Cloud) host URL <br />+  Client ID <br />+  Client secret <br />+  Private key <br />+  Organization ID <br />+  Technical Account ID <br />+  Adobe Identity Management System (IMS) host   Admin privileges required. 
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-user-management.html). 
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Pages <br />+  Assets See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/aem-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include/exclude by asset name <br />+  Include/exclude by asset type <br />+  Include/exclude by asset path <br />+  Include/exclude by page name <br />+  Include/exclude by page path 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.

