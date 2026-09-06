

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Google Drive connector overview
<a name="googledrive-v2-overview-primary"></a>

The following table gives an overview of the Amazon Q Business Google Drive connector new and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Service Account Based
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-user-management.html).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes.

- ****Crawl features****
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Files See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include/exclude by shared drive IDs <br />+  Include/exclude by MIME types (e.g., `application/pdf`, `application/vnd.google-apps.document`) <br />+  Date range filtering 
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all file types supported by Amazon Q. For more information see [Doc types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html).

