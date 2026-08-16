# Connect a Confluence data source

After you set up authentication and store your credentials in an AWS Secrets Manager secret,
create the Confluence data source in your knowledge base. This page describes how to
create the data source with the AWS Management Console or the API, followed by a reference for the
connector parameters you can configure.

###### Note

Complete authentication setup first. See [User-managed setup (3LO)](kb-managed-confluence-3lo-setup.md "kb-managed-confluence-3lo-setup.md") (simplest), [Set up Basic authentication for Confluence](kb-managed-confluence-basic-setup.md "kb-managed-confluence-basic-setup.md"), or [Set up OAuth 2.0 authentication for Confluence](kb-managed-confluence-oauth2-setup.md "kb-managed-confluence-oauth2-setup.md"). For user-managed setup
(3LO), you sign in through the console and Amazon Bedrock creates the secret for you (with a
system-generated ARN); you provide the Confluence host URL but not a secret. For the
other methods, you need the secret ARN and the Confluence host URL.

## Create the data source

Console

###### To connect Confluence to your managed knowledge base

1. Under **Data source**, provide a name for your data source.
2. Select **Confluence** from the data source dropdown.
3. Under **Source**, enter your Confluence URL (for example, `https://example.atlassian.net`).
4. Under **Authentication**, select **User-managed setup (3LO)**, **Basic authentication**, or **OAuth 2.0 authentication**. For user-managed setup (3LO), optionally enter a **secret name prefix**, then choose **Sign in** to sign in to Confluence Cloud. You do not provide a secret. Amazon Bedrock creates a secret with a system-generated ARN to store the token. For details, see [User-managed setup (3LO)](kb-managed-confluence-3lo-setup.md "kb-managed-confluence-3lo-setup.md").
5. Select or create an AWS Secrets Manager secret to store your credentials.
6. (Optional, Basic auth only) To enable document-level access control, select **Control document access with ACLs**. The secret you select must include `adminApiKey`, `organizationId`, and `directoryId`. This option cannot be changed after creation. For details, see [Document-level access controls](kb-managed-ds-confluence-acl.md "kb-managed-ds-confluence-acl.md").
7. (Optional) Expand **Sync scope** to choose which entity types to crawl (pages, blogs, page attachments, blog attachments, archived spaces, archived pages, personal spaces).
8. (Optional) Expand **Entity URLs** to use URL-based filtering to sync specific Confluence spaces, pages, and blogs.
9. (Optional) Expand **Mime types regex pattern** to include or exclude specific MIME types.

API
To create a Confluence data source, send a [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") request with an Agents for Amazon Bedrock build-time
endpoint. The following AWS Command Line Interface example creates a data source that uses
Basic authentication. To use OAuth 2.0 instead, change
`authType` to `OAUTH2`. For user-managed setup
(3LO), set `authType` to `MANAGED_OAUTH2`. You
cannot create a 3LO secret through the API: first sign in through the
console to create the secret, then set `secretArn` to that
secret's ARN (see [User-managed setup (3LO)](kb-managed-confluence-3lo-setup.md "kb-managed-confluence-3lo-setup.md")). To enable
document-level access control, set `aclEnabled` to
`true`. For a description of each field, see the connector
parameters reference that follows.

```
aws bedrock-agent create-data-source \
 --name "`Confluence-connector`" \
 --knowledge-base-id "`your-knowledge-base-id`" \
 --data-source-configuration file://confluence-managed-connector.json
```

The `confluence-managed-connector.json` file contains the
following:

```
{
    "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
    "managedKnowledgeBaseConnectorConfiguration": {
        "connectorParameters": {
            "type": "CONFLUENCE",
            "version": "1",
            "aclEnabled": false,
            "connectionConfiguration": {
                "secretArn": "`arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-confluence-basic-creds`",
                "type": "SAAS",
                "authType": "BASIC",
                "hostUrl": "`https://example.atlassian.net`"
            },
            "dataEntityConfiguration": {
                "crawlPage": true,
                "crawlBlog": true,
                "crawlPageAttachment": true,
                "crawlBlogAttachment": true
            },
            "filterConfiguration": {
                "inclusionSpaceKeys": ["`ENG`", "`DOCS`"]
            }
        }
    }
}
```

For managed knowledge bases, `CreateDataSource` is
asynchronous: the data source status transitions from
`CREATING` to `AVAILABLE` when the operation
completes.

## Connector parameters

The data source configuration uses the following connector parameters. To connect
to Confluence, specify `CONFLUENCE` as the connector type in
`connectorParameters`. For the fields that wrap
`connectorParameters` (such as
`deletionProtectionConfiguration` and
`mediaExtractionConfiguration`), see [Connect a data source](kb-managed-connect-ds.md "kb-managed-connect-ds.md").

###### Set aclEnabled explicitly

If you omit `aclEnabled`, the default depends on
`authType`: `BASIC` defaults to `true`,
and `OAUTH2` defaults to `false`. Because ACL
configuration is permanent after the data source is created, set
`aclEnabled` explicitly so the data source has the access-control
behavior you intend. For details, see [Document-level access controls](kb-managed-ds-confluence-acl.md "kb-managed-ds-confluence-acl.md").

connectionConfiguration| Field | Required | Description |
| --- | --- | --- |
| `secretArn` | Yes | The ARN of the AWS Secrets Manager secret containing your Confluence credentials. |
| `type` | Yes | The Confluence deployment type. Set to `SAAS`.<br>Confluence Server and Data Center are not supported. |
| `authType` | Yes | The authentication type. Set to `MANAGED_OAUTH2`<br>(user-managed setup, 3LO), `BASIC`, or<br>`OAUTH2`. See [Authentication methods](kb-managed-ds-confluence.md#kb-managed-confluence-auth-methods "kb-managed-ds-confluence.md#kb-managed-confluence-auth-methods"). |
| `hostUrl` | Yes | The base URL of your Confluence Cloud instance (for example,<br>`https://example.atlassian.net`). |

dataEntityConfiguration (optional)| Field | Required | Description |
| --- | --- | --- |
| `crawlPage` | No | Whether to crawl pages. |
| `crawlBlog` | No | Whether to crawl blog posts. |
| `crawlPageAttachment` | No | Whether to crawl page attachments. Crawled only when<br>`crawlPage` is also `true`. |
| `crawlBlogAttachment` | No | Whether to crawl blog post attachments. Crawled only when<br>`crawlBlog` is also `true`. |
| `crawlArchivedSpace` | No | Whether to crawl archived spaces. |
| `crawlArchivedPage` | No | Whether to crawl archived pages. |
| `crawlPersonalSpace` | No | Whether to crawl personal spaces. |

filterConfiguration (optional)| Field | Required | Description |
| --- | --- | --- |
| `inclusionSpaceKeys` | No | Space keys to include. |
| `inclusionSpaceUrls` | No | Space URLs to include. |
| `inclusionMimeTypes` | No | MIME types to include. |
| `exclusionMimeTypes` | No | MIME types to exclude. |
| `maxFileSizeInMegaBytes` | No | Maximum size, in megabytes, of any single file the connector<br>ingests. Provide as a numeric string (for example,<br>`"500"`). Defaults to `"500"`. |

aclEnabled (optional)| Field | Required | Description |
| --- | --- | --- |
| `aclEnabled` | No | Whether document-level access control is enabled. Set to<br>`true` to enable, or `false` to disable. If<br>you omit this field, the default depends on `authType`:<br>`BASIC` defaults to `true`;<br>`OAUTH2` defaults to `false`. ACL on<br>`BASIC` requires a secret that includes Atlassian<br>organization admin credentials. You cannot change this setting<br>after you create the data source. For details, see [Document-level access controls](kb-managed-ds-confluence-acl.md "kb-managed-ds-confluence-acl.md"). |

## Change the authentication method

You can change a data source's authentication method (for example, from OAuth 2.0
to Basic) by updating the data source with the new `authType` and a
secret that contains the matching credentials, using the [UpdateDataSource](../APIReference/API_agent_UpdateDataSource.md "../APIReference/API_agent_UpdateDataSource.md") operation
or the AWS Management Console. The document-level access control setting is fixed when you
create a data source, so to add or remove ACLs you must create a new data
source.

## Next steps

After you create the data source, sync it to ingest content into your knowledge
base. For details, see [Sync a data source](kb-managed-sync.md "kb-managed-sync.md"). To filter query results by user permissions,
see [Document-level access controls](kb-managed-ds-confluence-acl.md "kb-managed-ds-confluence-acl.md").
