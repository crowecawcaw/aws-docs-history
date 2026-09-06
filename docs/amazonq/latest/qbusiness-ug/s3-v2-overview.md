

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Overview
<a name="s3-v2-overview"></a>

The following table gives an overview of the Amazon Q Business Amazon S3 connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Assume Role Based
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-user-management).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** No. Use [User Store APIs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html) if you want to crawl users and groups.

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** No
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Document See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include/exclude by prefix (for example `Data/`, where `Data` is a folder containing documents) <br />+  Include/exclude by file types (for example `.*\.pdf`, or `.*\.txt`) <br />+  Include/exclude by glob patterns (for example `*.java`, which specifies a pattern that represents file names ending in `.java`) 
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.

