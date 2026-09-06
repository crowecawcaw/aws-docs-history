

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Jira connector overview
<a name="jira-overview"></a>

The following table gives an overview of the Amazon Q Business Jira connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** Basic, Basic, OAuth 2.0 with Refresh Token Flow
  - **Feature:** Authentication credentials / **Support:** +  Jira URL <br />+  Jira username <br />+  Password (Jira site token)  +  App key <br />+  App secret <br />+  Access token <br />+  [Refresh token](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/)  Access and refresh tokens expire in 1 hour. For information on regenerating tokens, see [Atlassian Developer Documentation](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#faq1).  
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-user-management.html). 
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** No
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom objects / **Support:** Yes
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Projects <br />+  Issues <br />+  Comments <br />+  Attachments <br />+  Worklogs See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-field-mappings).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include specific projects <br />+  Include/exclude statuses <br />+  Include/exclude comments <br />+  Include/exclude attachments <br />+  Include/exclude worklogs <br />+  Include/exclude bugs <br />+  Include/exclude epic <br />+  Include/exclude story <br />+  Include/exclude task <br />+  Include/exclude by file name <br />+  Include/exclude by file type <br />+  Include/exclude by file path 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.

