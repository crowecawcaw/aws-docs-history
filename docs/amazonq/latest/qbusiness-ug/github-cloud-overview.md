

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# GitHub (Cloud) connector overview
<a name="github-cloud-overview"></a>

The following table gives an overview of the Amazon Q Business GitHub (Cloud) connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Personal token, OAuth token
  - **Feature:** Authentication credentials / **Support:** +  GitHub (Cloud) token  
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-user-management.html). 
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Repository <br />+  Repository Commit <br />+  Issue Document <br />+  Issue Comment <br />+  Issue Attachment <br />+  Pull Request Comment <br />+  Pull request Document <br />+  Pull Request Attachment See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/github-cloud-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include select repositories <br />+  Include content by specific entities. <br />+  Include specific branched by name <br />+  Include/exclude content by file name, file type, and file path 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q. 

