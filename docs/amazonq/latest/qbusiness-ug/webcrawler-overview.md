

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Web Crawler connector overview
<a name="webcrawler-overview"></a>

The following table gives an overview of the Amazon Q Business Web Crawler connector and its supported features.




- ****Security****
  - **Feature:** Authentication type / **Support:**  +  Basic <br />+  NTLM/Kerberos <br />+  Form <br />+  SAML  You don't need authentication to crawl public websites you have permission to crawl. 
  - **Feature:** Authentication credentials / **Support:** **Basic authentication**+  Website username <br />+  Website password <br />**NTLM/Kerberos authentication**+  NTLM/Kerberos username <br />+  NTLM/Kerberos password <br />**Form authentication**+  Login page URL <br />+  Website username <br />+  Website password <br />+  Username field Xpath <br />+  Password field Xpath <br />+  Password button Xpath <br />+  (Optional) Username button Xpath  <br />**SAML authentication**+  Login page URL <br />+  Website username <br />+  Website password <br />+  Username field Xpath <br />+  Password field Xpath <br />+  Password button Xpath <br />+  (Optional) Username button Xpath  
  - **Feature:** [Access Control List (ACL)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) crawling / **Support:** No
  - **Feature:** [Identity crawling](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) / **Support:** No

- ****Crawl features****
  - **Feature:** Custom metadata / **Support:** Yes
  - **Feature:** Visual content processing / **Support:** Yes. Amazon Q Business can extract and index content from images embedded in webpages and the following supported document types: PDF, PowerPoint, Microsoft Word (DOCX), Google Slides, Google Docs
  - **Feature:** Entities / **Support:** Yes. The following entities are supported: +  Web page <br />+  Attachment See [What is a document?](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-doc-crawl.html) for more details on what each connector crawls as a document.
  - **Feature:** [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings) / **Support:** Yes. For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-field-mappings).
  - **Feature:** Filters / **Support:** Yes. The following filters are supported: +  Sync specific domains and subdomains <br />+  Include files linked on web pages <br />+  Regex patterns to crawl and index specific URLs <br />+  Regex patterns to crawl and index specific files <br />+  Include web pages by crawl depth <br />+  Specify maximum file size and links per page for Amazon Q to crawl 
  - **Feature:** [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode) / **Support:** Supports full and new, modified, or deleted content sync
  - **Feature:** [File types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html) / **Support:** Supports all files supported by Amazon Q. 

