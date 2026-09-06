

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Dropbox connector overview
<a name="dropbox-overview"></a>

The following table gives an overview of the Amazon Q Business Dropbox connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** OAuth 2.0 short‑lived access token and refresh token (offline access)
  - **Feature:** Authentication credentials / **Support:** OAuth 2.0 short‑lived access token and refresh token (offline access) +  App key <br />+  App secret <br />+  Access token <br />+  Refresh token (recommended)  
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-user-management.html). 
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Files <br />+  Dropbox Paper <br />+  Dropbox Paper Templates <br />+  Shortcuts See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/dropbox-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include/ exclude **Files** **Dropbox Paper**, **Dropbox Paper templates**, and **Shortcuts**. <br />+  Include/exclude content by file name, file type, and file path. 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q. 

