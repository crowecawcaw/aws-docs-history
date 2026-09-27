

# Connect a Salesforce data source
<a name="kb-managed-ds-salesforce-connect"></a>

After you set up authentication and store your credentials in an AWS Secrets Manager secret, create the Salesforce data source in your knowledge base. This page describes how to create the data source with the AWS Management Console or the API, followed by a reference for the connector parameters you can configure.

**Note**  
Complete authentication setup first. See [Set up OAuth 2.0 Client Credentials authentication for Salesforce](kb-managed-salesforce-oauth2-setup.md). You need the secret ARN.

## Create the data source
<a name="kb-managed-ds-salesforce-create"></a>

------
#### [ Console ]

**To connect Salesforce to your managed knowledge base**

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/). In the navigation pane, choose **Knowledge Bases** and open your managed knowledge base.

1. Under **Data source**, provide a name for your data source.

1. From the **Data source type** list, select **Salesforce**.

1. For **Salesforce URL**, enter your Salesforce org URL. Use the My Domain URL found under **Setup** > **My Domain** (for example, `https://{{your-domain}}.my.salesforce.com`). Accepted URL formats are `*.my.salesforce.com` and `*.lightning.force.com`.

1. Under **Authentication**, the connector uses OAuth 2.0. Select or create an AWS Secrets Manager secret containing your `clientId`, `clientSecret`, and `instanceUrl`.

1. Under **Sync scope**, select the content to crawl:
   + **Knowledge articles (includes attachments)** – Crawls Salesforce Knowledge articles and their attachments.
   + **Archived Knowledge articles** – Crawls archived Knowledge articles.
   + **Documents** – Crawls Salesforce documents.

1. (Optional) Under **Data categories inclusion filter**, specify a category group name and category names to limit synced articles. All data categories sync by default. For **Category depth**, choose how articles are synced relative to the specified category: **At**, **Above**, **Below**, or **Above, Below**. Choose **Add categories** to add more category groups.

1. (Optional) Under **Documents filter by folders**, enter folder IDs to sync documents from specific folders only. All documents sync by default.

------
#### [ API ]

To create a Salesforce data source, send a [CreateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateDataSource.html) request with an Agents for Amazon Bedrock build-time endpoint. The following AWS Command Line Interface example creates a Salesforce data source. For a description of each field, see the connector parameters reference that follows.

```
aws bedrock-agent create-data-source \
 --name "{{Salesforce-connector}}" \
 --knowledge-base-id "{{your-knowledge-base-id}}" \
 --data-source-configuration file://salesforce-managed-connector.json
```

The `salesforce-managed-connector.json` file contains the following:

```
{
    "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
    "managedKnowledgeBaseConnectorConfiguration": {
        "connectorParameters": {
            "type": "SALESFORCE",
            "connectorType": "SALESFORCE",
            "version": "1",
            "connectionConfiguration": {
                "secretArn": "{{arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-salesforce-creds}}",
                "authType": "OAUTH2",
                "hostUrl": "https://{{your-domain}}.my.salesforce.com"
            },
            "dataEntityConfiguration": {
                "crawlKnowledgeArticles": true,
                "crawlKnowledgeArticleAttachments": false,
                "crawlArchiveKnowledgeArticleItems": false,
                "crawlDocuments": false
            },
            "filterConfiguration": {
                "maxFileSizeInMegaBytes": "500",
                "knowledgeArticleFilter": {
                    "dataCategoryConfiguration": [
                        {
                            "categoryGroupName": "{{category-group-name}}",
                            "operator": "AT",
                            "dataCategoryNames": ["{{category-name}}"]
                        }
                    ]
                },
                "documentFilter": {
                    "folderIds": ["{{folder-id}}"]
                }
            }
        }
    }
}
```

The `dataEntityConfiguration` fields control which entities the connector crawls. The `filterConfiguration` field is optional; use it to scope Knowledge article crawling to specific data categories and to set a maximum file size. Without filters, the connector crawls all Knowledge articles and documents.

For managed knowledge bases, `CreateDataSource` is asynchronous: the data source status transitions from `CREATING` to `AVAILABLE` when the operation completes.

------

## Connector parameters
<a name="kb-managed-config-salesforce"></a>

The data source configuration uses the following connector parameters. Within `connectorParameters`, set both `type` and `connectorType` to `SALESFORCE` and set `version` to `1`. For the fields that wrap `connectorParameters` (such as `deletionProtectionConfiguration` and `mediaExtractionConfiguration`), see [Connect a data source](kb-managed-connect-ds.md).

The following table describes the `connectionConfiguration` fields.


**connectionConfiguration**  

| Field | Required | Description | 
| --- | --- | --- | 
| secretArn | Yes | The ARN of the AWS Secrets Manager secret containing your clientId, clientSecret, and instanceUrl. | 
| hostUrl | Yes | Your Salesforce My Domain URL (for example, https://{{your-domain}}.my.salesforce.com). Accepted formats are \*.my.salesforce.com and \*.lightning.force.com. This value must match the instanceUrl in the secret. | 
| authType | Yes | The authentication type. Salesforce supports OAUTH2. See [Authentication method](kb-managed-ds-salesforce.md#kb-managed-salesforce-auth-methods). | 

The following table describes the `dataEntityConfiguration` fields, which control the entities that the connector crawls. In the console, Knowledge articles and their attachments are combined into a single **Knowledge articles (includes attachments)** option, but the API exposes them as separate fields.


**dataEntityConfiguration**  

| Field | Required | Description | 
| --- | --- | --- | 
| crawlKnowledgeArticles | Yes | Whether to crawl Salesforce Knowledge articles. | 
| crawlKnowledgeArticleAttachments | Yes | Whether to crawl attachments on Knowledge articles. | 
| crawlArchiveKnowledgeArticleItems | Yes | Whether to crawl archived Knowledge articles. | 
| crawlDocuments | Yes | Whether to crawl Salesforce documents. | 

The following table describes the optional `filterConfiguration` fields, which scope the crawl.


**filterConfiguration (optional)**  

| Field | Required | Description | 
| --- | --- | --- | 
| knowledgeArticleFilter | No | Scopes Knowledge article crawling. Contains dataCategoryConfiguration, a list of objects that each contain categoryGroupName (the data category group), dataCategoryNames (a list of category names), and operator (the category depth). See the category depth values that follow. | 
| documentFilter | No | Scopes document crawling. Contains folderIds (a list of Salesforce folder IDs); the connector syncs documents from those folders only. | 
| maxFileSizeInMegaBytes | No | Maximum size, in megabytes, of any single file the connector ingests. Provide as a numeric string (for example, "500"). | 

The `operator` field in `dataCategoryConfiguration` sets the category depth – which articles to sync relative to the specified category:
+ `AT` – Only articles in the exact category specified.
+ `ABOVE` – Articles in the specified category and all its parent categories.
+ `BELOW` – Articles in the specified category and all its subcategories.
+ `ABOVE_OR_BELOW` – Articles in the specified category, its parents, and its subcategories.

## Next steps
<a name="kb-managed-ds-salesforce-connect-next"></a>

After you create the data source, sync it to ingest content into your knowledge base. For details, see [Sync a data source](kb-managed-sync.md). Because Salesforce doesn't support document-level access control, all authenticated users who can query the knowledge base can see all crawled content.