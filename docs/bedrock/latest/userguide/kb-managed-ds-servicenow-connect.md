# Connect a ServiceNow data source

After you set up authentication and store your credentials in an AWS Secrets Manager secret,
create the ServiceNow data source in your knowledge base. This page describes how to
create the data source with the AWS Management Console or the API, followed by a reference for the
connector parameters you can configure.

###### Note

Complete authentication setup first. See [Set up OAuth 2.0 Client Credentials authentication for ServiceNow](kb-managed-servicenow-oauth2-setup.md "kb-managed-servicenow-oauth2-setup.md"). You need the secret
ARN.

## Create the data source

Console

###### To connect ServiceNow to your managed knowledge base

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/"). In the
   navigation pane, choose **Knowledge Bases** and
   open your managed knowledge base.
2. Under **Data source**, provide a name for
   your data source.
3. From the **Data source type** list, select
   **ServiceNow**.
4. For **Host URL**, enter your ServiceNow
   instance URL (for example,
   `https://`INSTANCE`.service-now.com`).
5. Under **Authentication**, select or create
   an AWS Secrets Manager secret containing your `clientId`,
   `clientSecret`, and `instanceUrl`.
6. Under **Sync scope**, select the content to
   crawl: knowledge articles, service catalog items, and their
   attachments. You can also choose whether to crawl inactive
   service catalog items and whether to restrict the crawl to
   public knowledge articles only.
7. (Optional) To limit the crawl, add knowledge base, knowledge
   article category, or service catalog filters.

API
To create a ServiceNow data source, send a [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") request with an Agents for Amazon Bedrock build-time
endpoint. The following AWS Command Line Interface example creates a ServiceNow data
source. For a description of each field, see the connector parameters
reference that follows.

```
aws bedrock-agent create-data-source \
 --name "`ServiceNow-connector`" \
 --knowledge-base-id "`your-knowledge-base-id`" \
 --data-source-configuration file://servicenow-managed-connector.json
```

The `servicenow-managed-connector.json` file contains the
following:

```
{
    "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
    "managedKnowledgeBaseConnectorConfiguration": {
        "connectorParameters": {
            "type": "SERVICENOW",
            "connectorType": "SERVICENOW",
            "version": "1",
            "connectionConfiguration": {
                "secretArn": "`arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-servicenow-creds`",
                "authType": "OAUTH2",
                "hostUrl": "https://`INSTANCE`.service-now.com"
            },
            "dataEntityConfiguration": {
                "crawlKnowledgeArticles": true,
                "crawlServiceCatalogs": true,
                "crawlKnowledgeArticleAttachments": true,
                "crawlServiceCatalogAttachments": true,
                "crawlInactiveServiceCatalogItems": false,
                "crawlPublicKnowledgeArticlesOnly": false
            },
            "filterConfiguration": {
                "knowledgeArticleFilter": {
                    "inclusionKnowledgeBaseSysIds": ["`optional-kb-sys-id`"],
                    "inclusionKnowledgeArticleCategorySysIds": []
                },
                "serviceCatalogFilter": {
                    "inclusionServiceCatalogSysIds": [],
                    "inclusionServiceCatalogCategorySysIds": []
                },
                "maxFileSizeInMegaBytes": "500"
            }
        }
    }
}
```

The `dataEntityConfiguration` fields control which entities
the connector crawls. The `filterConfiguration` field is
optional; use it to scope the crawl to specific knowledge bases,
knowledge article categories, or service catalogs, and to set a maximum
file size. Without filters, the connector crawls all active knowledge
articles and service catalog items.

For managed knowledge bases, `CreateDataSource` is
asynchronous: the data source status transitions from
`CREATING` to `AVAILABLE` when the operation
completes.

## Connector parameters

The data source configuration uses the following connector parameters. Within
`connectorParameters`, set both `type` and
`connectorType` to `SERVICENOW` and set `version`
to `1`. For the fields that wrap `connectorParameters` (such as
`deletionProtectionConfiguration` and
`mediaExtractionConfiguration`), see [Connect a data source](kb-managed-connect-ds.md "kb-managed-connect-ds.md").

The following table describes the `connectionConfiguration` fields.

connectionConfiguration| Field | Required | Description |
| --- | --- | --- |
| `secretArn` | Yes | The ARN of the AWS Secrets Manager secret containing your<br>`clientId`, `clientSecret`, and<br>`instanceUrl`. |
| `hostUrl` | Yes | Your ServiceNow instance URL (for example,<br>`https://`INSTANCE`.service-now.com`). |
| `authType` | Yes | The authentication type. ServiceNow supports<br>`OAUTH2`. See [Authentication method](kb-managed-ds-servicenow.md#kb-managed-servicenow-auth-methods "kb-managed-ds-servicenow.md#kb-managed-servicenow-auth-methods"). |

The following table describes the `dataEntityConfiguration` fields,
which control the entities that the connector crawls.

dataEntityConfiguration| Field | Required | Description |
| --- | --- | --- |
| `crawlKnowledgeArticles` | Yes | Whether to crawl knowledge articles<br>(`kb_knowledge`). |
| `crawlServiceCatalogs` | Yes | Whether to crawl service catalog items<br>(`sc_cat_item`). |
| `crawlKnowledgeArticleAttachments` | Yes | Whether to crawl attachments on knowledge articles. |
| `crawlServiceCatalogAttachments` | Yes | Whether to crawl attachments on service catalog items. |
| `crawlInactiveServiceCatalogItems` | Yes | Whether to crawl inactive service catalog items. |
| `crawlPublicKnowledgeArticlesOnly` | Yes | Whether to restrict the crawl to public knowledge articles<br>only. |

The following table describes the optional `filterConfiguration`
fields, which scope the crawl.

filterConfiguration (optional)| Field | Required | Description |
| --- | --- | --- |
| `knowledgeArticleFilter` | No | Scopes knowledge article crawling. Contains<br>`inclusionKnowledgeBaseSysIds` (a list of knowledge base<br>sys IDs) and `inclusionKnowledgeArticleCategorySysIds` (a<br>list of knowledge article category sys IDs). |
| `serviceCatalogFilter` | No | Scopes service catalog crawling. Contains<br>`inclusionServiceCatalogSysIds` (a list of service catalog<br>sys IDs) and `inclusionServiceCatalogCategorySysIds` (a<br>list of service catalog category sys IDs). On large instances,<br>filtering by sys ID significantly reduces sync time. |
| `maxFileSizeInMegaBytes` | No | Maximum size, in megabytes, of any single file the connector<br>ingests. Provide as a numeric string (for example,<br>`"500"`). |

## Next steps

After you create the data source, sync it to ingest content into your knowledge
base. For details, see [Sync a data source](kb-managed-sync.md "kb-managed-sync.md"). Because ServiceNow doesn't support
document-level access control, all authenticated users who can query the knowledge
base can see all crawled content.
