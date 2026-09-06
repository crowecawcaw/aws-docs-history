

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# SharePoint (Online) connector overview
<a name="sharepoint-cloud-overview"></a>

The following table gives an overview of the Amazon Q Business SharePoint (Online) connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:**  In order from most to least secure authentication type: +  Microsoft Entra ID (formerly Azure AD) App-Only (OAuth 2.0 Certificate) (This is the preferred method of connection) <br />+  SharePoint App-Only with Client Credentials Flow <br />+  OAuth 2.0 with Resource Owner Password Flow <br />+  Basic authentication 
  - **Feature:** Authentication credentials / **Support:**  +  Tenant ID <br />+  Certificate path <br />+  Client ID <br />+  Private key  +  Tenant ID <br />+  Microsoft Entra ID (formerly Azure AD) Client ID <br />+  Microsoft Entra ID (formerly Azure AD) Client secret <br />+  SharePoint App-Only Client ID <br />+  SharePoint App-Only Client secret  +  SharePoint Tenant ID <br />+  SharePoint admin username <br />+  SharePoint admin password <br />+  Client ID <br />+  Client secret  +  SharePoint (Online) admin username <br />+  SharePoint (Online) admin password  
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** Yes. For more information, see [ACL crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-user-management.html). 
  - **Feature:** Integration with Identity Provider (IdP) / **Support:** Yes. Microsoft Entra ID (formerly Azure AD).
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** Yes
  - **Feature:** [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc) / **Support:** Yes

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes. Supports custom metadata for File entity only.
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Files <br />+  Attachments <br />+  Link <br />+  Pages <br />+  Events <br />+  Comments <br />+  List Data See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. Supports both default and custom field mappings. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-field-mappings.html).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Include/exclude by **Links** <br />+  Include/exclude by **Pages** <br />+  Include/exclude by **Events** <br />+  Include/exclude by file name <br />+  Include/exclude by file path <br />+  Include/exclude by file type <br />+  Include/exclude by **OneNote Section** name <br />+  Include/exclude by **OneNote Page** name 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and incremental sync.
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q.
  - **Feature:** [Crawled as a document](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html#connector-doc-crawl) / **Support:** +  Each event <br />+  Each page <br />+  Each file <br />+  Each link <br />+  Each file attachment <br />+  Each comment <br />+  Each OneNote 

