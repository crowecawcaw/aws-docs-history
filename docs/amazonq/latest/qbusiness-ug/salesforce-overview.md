

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Salesforce Online connector overview
<a name="salesforce-overview"></a>

The following table gives an overview of the Salesforce Online connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** OAuth 2.0 with Resource Owner Password Flow Note that Require Proof Key for Code Exchange (PKCE) is not supported and must be disabled.
  - **Feature:** Authentication credentials / **Support:** +  Salesforce authentication URL <br />+  Username Client secret <br />+  Password username <br />+  Security token  <br />+  Consumer key <br />+  Consumer secret 
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-user-management). 
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes
  - **Feature:** Supported versions / **Support:** +  API 30-56 <br />+  Lightning, Classic <br />+  Sandbox 

- ****Crawl features****
  - **Feature:** Custom objects / **Support:** Yes
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Account <br />+  Campaign <br />+  Partner <br />+  Pricebook <br />+  Case <br />+  Contact <br />+  Contract <br />+  Document <br />+  Group <br />+  Idea <br />+  Lead <br />+  Opportunity <br />+  Product <br />+  Profile <br />+  Solution <br />+  Task <br />+  User <br />+  Chatter <br />+  Knowledge Articles See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-field-mappings).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Attachment filter for supported entities <br />+  Regex filters for entities <br />+  Inclusion and exclusion filters on file type for Documents <br />+  Inclusion and exclusion filters on File Name and File Type for Attachments 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports incremental sync only if ACL is turned off, otherwise only full sync will be used.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.
  - **Feature:** [Crawled as a document](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html#connector-doc-crawl) / **Support:** +  Each account <br />+  Each contact <br />+  Each campaign <br />+  Each contract <br />+  Each case <br />+  Each partner <br />+  Each opportunity <br />+  Each group <br />+  Each lead <br />+  Each user <br />+  Each task <br />+  Each idea <br />+  Each profile <br />+  Each solution <br />+  Each chatter <br />+  Each document <br />+  Each custom entity <br />+  Each knowledge article 

