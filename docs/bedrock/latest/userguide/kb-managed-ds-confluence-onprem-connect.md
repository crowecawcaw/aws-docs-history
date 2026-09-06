

# Connect a Confluence Data Center data source
<a name="kb-managed-ds-confluence-onprem-connect"></a>

After you set up VPC connectivity and store your credentials in an AWS Secrets Manager secret, create the Confluence Data Center data source in your knowledge base. This page describes how to create the data source with the AWS Management Console or the API, followed by a reference for the connector parameters you can configure.

**Note**  
Complete the VPC configuration and authentication setup first. See [Configure VPC connectivity for a data source](kb-managed-vpc-configuration.md) and [Set up Basic or PAT authentication for Confluence Data Center](kb-managed-confluence-onprem-auth-setup.md). You need the VPC configuration ID and the secret ARN.

## Create the data source
<a name="kb-managed-ds-confluence-onprem-create"></a>

------
#### [ Console ]

**To connect Confluence Data Center to your managed knowledge base**

1. Under **Data source**, provide a name for your data source.

1. Select **Confluence Data Center** from the data source dropdown.

1. Under **VPC configuration**, select a VPC configuration that reaches your Confluence Data Center instance, or choose **Add VPC configuration** to create one. For details, see [Configure VPC connectivity for a data source](kb-managed-vpc-configuration.md).

1. (Optional) Under **Application context path**, enter the **Content path** under which the Confluence Data Center REST API is served (for example, `/wiki`). Leave it empty if the REST API is served at the web root.

1. (Optional, HTTPS only) Under **TLS certificate**, provide the Amazon S3 URI of the TLS certificate for your Confluence Data Center instance.

1. Under **Authentication**, select **Basic authentication** or **Personal access token**, then select the AWS Secrets Manager secret that holds the matching credentials.

1. (Optional) Expand **Sync scope** to choose which entity types to crawl (pages, page attachments, blogs, blog attachments, personal spaces).

1. (Optional) Expand **Entity URLs** to use URL-based filtering to sync specific Confluence spaces, pages, and blogs.

1. (Optional) Expand **Mime types** to include or exclude specific MIME types.

------
#### [ API ]

To create a Confluence Data Center data source, send a [CreateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateDataSource.html) request with an Agents for Amazon Bedrock build-time endpoint. The following AWS Command Line Interface example creates a data source that uses Basic authentication. To use a personal access token instead, change `authType` to `PERSONAL_TOKEN`. For a description of each field, see the connector parameters reference that follows.

```
aws bedrock-agent create-data-source \
 --name "{{Confluence-DataCenter-connector}}" \
 --knowledge-base-id "{{your-knowledge-base-id}}" \
 --data-source-configuration file://confluence-onprem-connector.json
```

The `confluence-onprem-connector.json` file contains the following:

```
{
    "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
    "managedKnowledgeBaseConnectorConfiguration": {
        "connectorParameters": {
            "type": "CONFLUENCEONPREM",
            "version": "1",
            "aclEnabled": false,
            "connectionConfiguration": {
                "authType": "BASIC",
                "secretArn": "{{arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-confluence-onprem-creds}}",
                "contextPath": "{{/wiki}}",
                "vpcConfiguration": {
                    "vpcConfigurationId": "{{your-vpc-configuration-id}}"
                },
                "certificateS3Path": {
                    "s3BucketName": "{{my-cert-bucket}}",
                    "s3KeyName": "{{confluence-dc-cert.pem}}"
                }
            },
            "dataEntityConfiguration": {
                "crawlPage": true,
                "crawlBlog": true,
                "crawlPageAttachment": true,
                "crawlBlogAttachment": true
            },
            "filterConfiguration": {
                "inclusionSpaceUrls": ["{{https://confluence.example.com/spaces/ENG/}}"]
            }
        }
    }
}
```

For managed knowledge bases, `CreateDataSource` is asynchronous: the data source status transitions from `CREATING` to `AVAILABLE` when the operation completes.

------

## Connector parameters
<a name="kb-managed-config-confluence-onprem"></a>

The data source configuration uses the following connector parameters. To connect to Confluence Data Center, specify `CONFLUENCEONPREM` as the connector type in `connectorParameters`. For the fields that wrap `connectorParameters` (such as `deletionProtectionConfiguration` and `mediaExtractionConfiguration`), see [Connect a data source](kb-managed-connect-ds.md).


**connectionConfiguration**  

| Field | Required | Description | 
| --- | --- | --- | 
| authType | Yes | The authentication type. Set to BASIC or PERSONAL\_TOKEN. See [Authentication methods](kb-managed-ds-confluence-onprem.md#kb-managed-confluence-onprem-auth-methods). | 
| secretArn | Yes | The ARN of the AWS Secrets Manager secret containing your Confluence Data Center credentials. | 
| vpcConfiguration | Yes | The private network path to your Confluence Data Center instance. Contains a vpcConfigurationId field set to the ID of a VPC configuration on your knowledge base. See [Configure VPC connectivity for a data source](kb-managed-vpc-configuration.md). | 
| contextPath | No | The application context path under which the Confluence Data Center REST API is served (for example, /wiki). Omit it if the REST API is served at the web root. | 
| certificateS3Path | No | The location of the TLS certificate for your Confluence Data Center instance, used when you connect over HTTPS. Contains s3BucketName and s3KeyName. | 


**dataEntityConfiguration (optional)**  

| Field | Required | Description | 
| --- | --- | --- | 
| crawlPage | No | Whether to crawl pages. | 
| crawlBlog | No | Whether to crawl blog posts. | 
| crawlPageAttachment | No | Whether to crawl page attachments. Crawled only when crawlPage is also true. | 
| crawlBlogAttachment | No | Whether to crawl blog post attachments. Crawled only when crawlBlog is also true. | 
| crawlPersonalSpace | No | Whether to crawl personal spaces. | 

**Note**  
Unlike Confluence Cloud, Confluence Data Center does not support crawling archived spaces or archived pages.


**filterConfiguration (optional)**  

| Field | Required | Description | 
| --- | --- | --- | 
| inclusionSpaceUrls | No | Space URLs to include. | 
| inclusionPageUrls | No | Page URLs to include. | 
| inclusionMimeTypes | No | MIME types to include. | 
| exclusionMimeTypes | No | MIME types to exclude. | 
| maxFileSizeInMegaBytes | No | Maximum size, in megabytes, of any single file the connector ingests. Provide as a numeric string (for example, "50"). | 

## Change the authentication method
<a name="kb-managed-ds-confluence-onprem-change-auth"></a>

You can change a data source's authentication method (for example, from Basic to personal access token) by updating the data source with the new `authType` and a secret that contains the matching credentials, using the [UpdateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateDataSource.html) operation or the AWS Management Console.

## Next steps
<a name="kb-managed-ds-confluence-onprem-connect-next"></a>

After you create the data source, sync it to ingest content into your knowledge base. For details, see [Sync a data source](kb-managed-sync.md).