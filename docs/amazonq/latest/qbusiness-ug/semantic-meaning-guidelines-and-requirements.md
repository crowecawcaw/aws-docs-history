

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Guidelines and requirements
<a name="semantic-meaning-guidelines-and-requirements"></a>

The following are guidelines and requirements for extracting content from images:
+ Documents can have up to 3,000 pages.
+ The IAM service role that grants Amazon Q Business permission to access your resources must have `qbusiness:GetMedia` permissions. For a policy example, see [IAM role for an Amazon Q Business web experience using IAM Identity Center](web-experience-iam-role-idc.md)
+ Image extraction is supported for the following image sources: PDF, PPT, Microsoft Word docs, Webpages (for Webcrawler), Google Slides and Google Docs (for Google Drive)
+ You can use the following connectors:
  + [Amazon S3](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-experience-iam-role-idc.html)
  + [Google Drive](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-connector.html) - Supports embedded images for Google Slides and Google Docs
  + [Confluence (Cloud)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-connector.html)
  + [Confluence (Server/Data Center)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/confluence-cloud-connector.html)
  + [SharePoint (Online)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-cloud-connector.html)
  + [SharePoint Server 2019](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2019-connector.html)
  + [SharePoint Server 2016](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/sharepoint-server-2016-connector.html)
  + [Gmail](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-connector.html)
  + [Microsoft Exchange](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-connector.html)
  + [OneDrive](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/onedrive-connector.html)
  + [Amazon WorkDocs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/workdocs-connector.html)
  + [Smartsheet](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/smartsheet-connector.html)
  + [Jira](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/jira-connector.html)
  + [Slack](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/slack-connector.html)
  + [ServiceNow](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/servicenow-connector.html)
  + [Salesforce](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/salesforce-connector.html)
  + [Web Crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-webcrawler.html) - Supports embedded images
  + [Microsoft Teams](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-connector.html)