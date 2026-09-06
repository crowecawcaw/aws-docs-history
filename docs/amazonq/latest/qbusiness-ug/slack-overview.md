

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Slack connector overview
<a name="slack-overview"></a>

The following table gives an overview of the Amazon Q Business Slack connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Token based authentication
  - **Feature:** Authentication credentials / **Support:** +  Slack workspace ID  <br />+  Either Slack Bot token or User token <br />User token lets you make API requests on behalf of the user. Bot token lets you make API requests as a Slack bot. 
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-user-management.html). 
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes 
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** No
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Public channels <br />+  Private channels <br />+  Group messages <br />+  Private messages <br />+  Bot messages <br />+  Archived messages See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Crawl public channel <br />+  Crawl private channel <br />+  Crawl group messages <br />+  Crawl private messages <br />+  Crawl channel by type <br />+  Crawl channel by name <br />+  Including and excluding content by file type <br />+  Including and excluding content based on file name 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.
  - **Feature:** [Crawled as a document](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html#connector-doc-crawl) / **Support:** +  Each message <br />+  Each message attachment <br />+  Each channel post 

