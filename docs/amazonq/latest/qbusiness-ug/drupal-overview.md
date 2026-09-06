

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Drupal connector overview
<a name="drupal-overview"></a>

The following table gives an overview of the Amazon Q Business Drupal connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Basic, OAuth 2.0 with Client Credentials Flow
  - **Feature:** Authentication credentials / **Support:** +  Username <br />+  Password <br />+  Client email <br />+  Private key **OAuth 2.0 with Client Credentials Flow**+  Username <br />+  Password <br />+  Client ID <br />+  Client Secret 
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-user-management.html). 
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Contents <br />+  Comments <br />+  Attachments See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/drupal-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include/ exclude articles, article comments, and article attachments <br />+  Include/exclude basic pages, basic page comments, and basic page attachments <br />+  Include/exclude basic blocks, basic block comments, and basic block attachments <br />+  Include custom content types <br />+  Include custom blocks <br />+  Include/exclude content by article title, basic page title, basic block title, custom content title, custom block title, and file name 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q. 

