

# Connect a Zendesk data source
<a name="kb-managed-ds-zendesk-connect"></a>

After you set up authentication and store your credentials in an AWS Secrets Manager secret, create the Zendesk data source in your knowledge base. This page describes how to create the data source with the AWS Management Console or the API, followed by a reference for the connector parameters you can configure.

**Note**  
Complete authentication setup first. See [Set up OAuth 2.0 Client Credentials authentication for Zendesk](kb-managed-zendesk-oauth2-setup.md). You need the secret ARN.

## Create the data source
<a name="kb-managed-ds-zendesk-create"></a>

------
#### [ Console ]

**To connect Zendesk to your managed knowledge base**

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/). In the navigation pane, choose **Knowledge Bases** and open your managed knowledge base.

1. Under **Data source**, provide a name for your data source.

1. From the **Data source type** list, select **Zendesk**.

1. For **Zendesk host URL**, enter your Zendesk subdomain URL (for example, `https://{{yoursubdomain}}.zendesk.com`). For multi-brand instances, provide the subdomain for the specific brand that you want to sync.

1. Under **Authentication**, the connector uses OAuth 2.0. Select or create an AWS Secrets Manager secret containing your `clientId`, `clientSecret`, and `instanceUrl`.

1. Under **Sync scope**, select the content to crawl:
   + **Articles (includes attachments)** – Crawls help center articles and their attachments.
   + **Community posts** – Crawls community posts.

1. (Optional) Under **Article filters**, enter a category or section ID to limit synced articles. All articles sync by default.

1. (Optional) Under **Community posts filter by topics**, enter topic IDs to sync posts from specific topics only. All community posts sync by default.

1. (Optional) Under **Label name filter**, enter labels to sync only articles and community posts that match specific labels. Use this filter alongside the article and topic filters to further refine synced content.

------
#### [ API ]

To create a Zendesk data source, send a [CreateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateDataSource.html) request with an Agents for Amazon Bedrock build-time endpoint. The following AWS Command Line Interface example creates a Zendesk data source. For a description of each field, see the connector parameters reference that follows.

```
aws bedrock-agent create-data-source \
 --name "{{Zendesk-connector}}" \
 --knowledge-base-id "{{your-knowledge-base-id}}" \
 --data-source-configuration file://zendesk-managed-connector.json
```

The `zendesk-managed-connector.json` file contains the following:

```
{
    "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
    "managedKnowledgeBaseConnectorConfiguration": {
        "connectorParameters": {
            "type": "ZENDESK",
            "connectorType": "ZENDESK",
            "version": "1",
            "connectionConfiguration": {
                "secretArn": "{{arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-zendesk-creds}}",
                "authType": "OAUTH2",
                "hostUrl": "https://{{yoursubdomain}}.zendesk.com"
            },
            "dataEntityConfiguration": {
                "crawlArticles": true,
                "crawlArticleAttachments": true,
                "crawlCommunityPosts": true
            },
            "filterConfiguration": {
                "maxFileSizeInMegaBytes": "10240",
                "articleFilter": {
                    "inclusionCategoryIds": ["{{category-id}}"],
                    "inclusionSectionIds": ["{{section-id}}"]
                },
                "communityPostFilter": {
                    "inclusionTopicIds": ["{{topic-id}}"]
                }
            }
        }
    }
}
```

The `dataEntityConfiguration` fields control which entities the connector crawls. The `filterConfiguration` field is optional; use it to scope the crawl to specific article categories or sections, community topics, or labels, and to set a maximum file size. Without filters, the connector crawls all articles and community posts.

For managed knowledge bases, `CreateDataSource` is asynchronous: the data source status transitions from `CREATING` to `AVAILABLE` when the operation completes.

------

## Connector parameters
<a name="kb-managed-config-zendesk"></a>

The data source configuration uses the following connector parameters. Within `connectorParameters`, set both `type` and `connectorType` to `ZENDESK` and set `version` to `1`. For the fields that wrap `connectorParameters` (such as `deletionProtectionConfiguration` and `mediaExtractionConfiguration`), see [Connect a data source](kb-managed-connect-ds.md).

The following table describes the `connectionConfiguration` fields.


**connectionConfiguration**  

| Field | Required | Description | 
| --- | --- | --- | 
| secretArn | Yes | The ARN of the AWS Secrets Manager secret containing your clientId, clientSecret, and instanceUrl. | 
| hostUrl | Yes | Your Zendesk host URL (for example, https://{{yoursubdomain}}.zendesk.com). For multi-brand instances, use the subdomain for the specific brand. This value must match the instanceUrl in the secret. | 
| authType | Yes | The authentication type. Zendesk supports OAUTH2. See [Authentication method](kb-managed-ds-zendesk.md#kb-managed-zendesk-auth-methods). | 

The following table describes the `dataEntityConfiguration` fields, which control the entities that the connector crawls. In the console, articles and their attachments are combined into a single **Articles (includes attachments)** option, but the API exposes them as separate fields.


**dataEntityConfiguration**  

| Field | Required | Description | 
| --- | --- | --- | 
| crawlArticles | Yes | Whether to crawl help center articles. | 
| crawlArticleAttachments | Yes | Whether to crawl attachments on help center articles. | 
| crawlCommunityPosts | Yes | Whether to crawl community posts. | 

The following table describes the optional `filterConfiguration` fields, which scope the crawl.


**filterConfiguration (optional)**  

| Field | Required | Description | 
| --- | --- | --- | 
| articleFilter | No | Scopes article crawling. Contains inclusionCategoryIds (a list of help center category IDs) and inclusionSectionIds (a list of section IDs). These IDs are numeric and appear in the help center URL when you view a category or section (for example, the category ID in https://{{yoursubdomain}}.zendesk.com/hc/en-us/categories/200420805 is 200420805). | 
| communityPostFilter | No | Scopes community post crawling. Contains inclusionTopicIds (a list of community topic IDs). A topic ID is numeric and appears in the URL when you view a community topic (for example, the topic ID in https://{{yoursubdomain}}.zendesk.com/hc/en-us/community/topics/360001234567 is 360001234567). | 
| inclusionLabelNames | No | A list of label names. The connector syncs only articles and community posts that match these labels. Labels are keywords or tags applied to articles and community posts, found at the bottom of any article or post in the editor. For example, if an article is tagged billing and a community post is tagged FAQ, entering those labels syncs only content matching those tags. Use alongside the article and community post filters to further refine synced content. | 
| maxFileSizeInMegaBytes | No | Maximum size, in megabytes, of any single file the connector ingests. Provide as a numeric string (for example, "10240"). | 

## Next steps
<a name="kb-managed-ds-zendesk-connect-next"></a>

After you create the data source, sync it to ingest content into your knowledge base. For details, see [Sync a data source](kb-managed-sync.md). Because Zendesk doesn't support document-level access control, all authenticated users who can query the knowledge base can see all crawled content.