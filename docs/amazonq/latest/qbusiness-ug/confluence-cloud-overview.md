

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Confluence (Cloud) connector overview
<a name="confluence-cloud-overview"></a>

The following table contains an overview of the Amazon Q Business Confluence (Cloud) connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Basic, OAuth 2.0 with Refresh Token Flow
  - **Feature:** Authentication credentials / **Support:** +  Confluence Cloud URL <br />+  Confluence username <br />+  Password (Confluence (Cloud) site token)  +  App key <br />+  App secret <br />+  Access token <br />+  [Refresh token](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/)  Access and refresh tokens expire in 1 hour. For information on regenerating tokens, see [Atlassian Developer Documentation](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#faq1).  
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-user-management.html).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Space <br />+  Page <br />+  Blog post <br />+  Comment <br />+  Attachment See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Inclusion exclusion filters for **Space key** and **Space URL** <br />+  Inclusion exclusion filters on **File Type** for **Attachment entity** <br />+  Supports regex filters for entities <br />+  Supports inclusion and exclusion filters for **File size** 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental (new, modified, and deleted) sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.

