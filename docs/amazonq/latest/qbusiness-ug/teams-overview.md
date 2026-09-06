

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Microsoft Teams connector overview
<a name="teams-overview"></a>

The following table shows the Amazon Q Business Microsoft Teams connector features and capabilities.




- ****Security****
  - **Feature:** Authentication type / **Latest Connector:** OAuth 2.0 with Client Credentials Flow / **Legacy Connector:** OAuth 2.0 with Client Credentials Flow
  - **Feature:** Authentication credentials / **Latest Connector:** +  Microsoft Teams Client ID <br />+  Microsoft Teams Client secret  / **Legacy Connector:** +  Microsoft Teams Client ID <br />+  Microsoft Teams Client secret 
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Latest Connector:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-user-management.html). / **Legacy Connector:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-user-management.html).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Latest Connector:** Yes / **Legacy Connector:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Latest Connector:** No / **Legacy Connector:** Yes

- ****
  - **Feature:** Customer Managed Key (CMK) support
  - **Latest Connector:** No
  - **Legacy Connector:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Latest Connector:** No / **Legacy Connector:** Yes
  - **Feature:** Entities / **Latest Connector:** Chat messages, Channel posts / **Legacy Connector:** Yes. The following entities are supported: +  Chat messages <br />+  Chat attachments <br />+  Channel posts <br />+  Channel file attachments <br />+  Wiki <br />+  Meeting chats <br />+  Meeting details <br />+  Meeting notes <br />+  Meeting files See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Latest Connector:** No / **Legacy Connector:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-field-mappings.html).
  - **Feature:** Filters / **Latest Connector:** Only Date range / **Legacy Connector:** Yes. The following filters are supported: +  Include/exclude using user email <br />+  Include/exclude using team name <br />+  Include/exclude using channel name <br />+  Include/exclude using file name <br />+  Include/exclude using file type <br />+  Chat message <br />+  Chat attachment <br />+  Channel post <br />+  Channel attachment <br />+  Channel wiki <br />+  Calendar meeting <br />+  Meeting chat <br />+  Meeting file <br />+  Meeting note 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Latest Connector:** Full sync only / **Legacy Connector:** Supports full and incremental sync

