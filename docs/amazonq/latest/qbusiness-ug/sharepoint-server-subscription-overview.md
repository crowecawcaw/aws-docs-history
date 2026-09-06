

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# SharePoint Server (Subscription Edition) connector overview
<a name="sharepoint-server-subscription-overview"></a>

The following table gives an overview of the Amazon Q Business SharePoint Server (Subscription Edition) connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:** NTLM, Kerberos, SharePoint App-Only (Client Credentials Flow)
  - **Feature:** Authentication credentials / **Support:** +  SharePoint admin username <br />+  SharePoint admin password  +  LDAP Server Endpoint <br />+  LDAP Search Base <br />+  LDAP username <br />+  LDAP password  +  SharePoint admin username <br />+  SharePoint admin password  +  LDAP Server Endpoint <br />+  LDAP Search Base <br />+  LDAP username <br />+  LDAP password  +  Tenant ID <br />+  SharePoint App-Only client ID <br />+  SharePoint App-Only client secret  +  LDAP Server Endpoint <br />+  LDAP Search Base <br />+  LDAP username <br />+  LDAP password  
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-user-management.html). 
  - **Feature:** Integration with Identity Provider (IdP) / **Support:** Yes. LDAP.
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes. Supports custom metadata for File entity only.
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Files <br />+  Attachments <br />+  Link <br />+  Pages <br />+  Events <br />+  Comments See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-subscription-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include/exclude by **Links** <br />+  Include/exclude by **Pages** <br />+  Include/exclude by **Events** <br />+  Include/exclude by file name <br />+  Include/exclude by file path <br />+  Include/exclude by file type <br />+  Include/exclude by **OneNote Section** name <br />+  Include/exclude by **OneNote Page** name 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.

