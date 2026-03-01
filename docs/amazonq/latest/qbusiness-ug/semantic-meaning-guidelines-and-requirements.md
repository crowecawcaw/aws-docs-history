# Guidelines and requirements

The following are guidelines and requirements for extracting content from
images:

- Documents can have up to 3,000 pages.
- The IAM service role that grants Amazon Q Business permission to access your
  resources must have `qbusiness:GetMedia` permissions. For a policy
  example, see [IAM role for an Amazon Q Business web experience using IAM Identity Center](web-experience-iam-role-idc.md "web-experience-iam-role-idc.md")
- Image extraction is supported for the following image sources: PDF, PPT,
  Microsoft Word docs, Webpages (for Webcrawler), Google Slides and Google Docs
  (for Google Drive)
- You can use the following connectors:
  - [Amazon S3](web-experience-iam-role-idc.md "web-experience-iam-role-idc.md")
  - [Google
    Drive](google-connector.md "google-connector.md") - Supports embedded images for Google Slides and
    Google Docs
  - [Confluence (Cloud)](confluence-cloud-connector.md "confluence-cloud-connector.md")
  - [Confluence (Server/Data Center)](confluence-cloud-connector.md "confluence-cloud-connector.md")
  - [SharePoint (Online)](sharepoint-cloud-connector.md "sharepoint-cloud-connector.md")
  - [SharePoint Server 2019](sharepoint-server-2019-connector.md "sharepoint-server-2019-connector.md")
  - [SharePoint Server 2016](sharepoint-server-2016-connector.md "sharepoint-server-2016-connector.md")
  - [Gmail](gmail-connector.md "gmail-connector.md")
  - [Microsoft
    Exchange](exchange-connector.md "exchange-connector.md")
  - [OneDrive](onedrive-connector.md "onedrive-connector.md")
  - [Amazon
    WorkDocs](workdocs-connector.md "workdocs-connector.md")
  - [Smartsheet](smartsheet-connector.md "smartsheet-connector.md")
  - [Jira](jira-connector.md "jira-connector.md")
  - [Slack](slack-connector.md "slack-connector.md")
  - [ServiceNow](servicenow-connector.md "servicenow-connector.md")
  - [Salesforce](salesforce-connector.md "salesforce-connector.md")
  - [Web
    Crawler](connector-webcrawler.md "connector-webcrawler.md") - Supports embedded images
  - [Microsoft
    Teams](teams-connector.md "teams-connector.md")
