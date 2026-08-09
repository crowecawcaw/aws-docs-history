# Connect a Box data source

After you set up authentication and store your credentials in an AWS Secrets Manager secret,
create the Box data source in your knowledge base. This page describes how to create the
data source with the AWS Management Console or the API, followed by a reference for the connector
parameters you can configure.

###### Note

Complete authentication setup first. See [Set up Client Credentials Grant authentication for Box](kb-managed-box-ccg-setup.md "kb-managed-box-ccg-setup.md") (recommended) or [Set up OAuth 2.0 authentication for Box](kb-managed-box-oauth2-setup.md "kb-managed-box-oauth2-setup.md"). You need the secret ARN.

## Create the data source

Console

###### To connect Box to your managed knowledge base

1. Under **Data source**, provide a name for your data source.
2. Select **Box** from the data source dropdown.
3. Under **Authentication**, select your authentication method and choose a secret. Client Credentials Grant (CCG) is for crawling content across your Box enterprise; OAuth 2.0 is for crawling content for a specific user.
4. (Optional) To enable document-level access control, select **Control document access with ACLs**. This option is available only with Client Credentials Grant authentication and cannot be changed after creation. For details, see [Document-level access controls](kb-managed-ds-box-acl.md "kb-managed-ds-box-acl.md").
5. (Optional) For OAuth 2.0 crawls, enter specific file and folder URLs you want to crawl.

API
To create a Box data source, send a [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") request with an Agents for Amazon Bedrock build-time
endpoint. The following AWS Command Line Interface example creates a data source that uses
Client Credentials Grant authentication. To use OAuth 2.0 instead, change
`authType` to `OAUTH2`. To enable
document-level access control, set `aclEnabled` to
`true`. For a description of each field, see the connector
parameters reference that follows.

```
aws bedrock-agent create-data-source \
 --name "`Box-connector`" \
 --knowledge-base-id "`your-knowledge-base-id`" \
 --data-source-configuration file://box-managed-connector.json
```

The `box-managed-connector.json` file contains the
following:

```
{
    "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
    "managedKnowledgeBaseConnectorConfiguration": {
        "connectorParameters": {
            "type": "BOX",
            "version": "1",
            "aclEnabled": false,
            "connectionConfiguration": {
                "secretArn": "`arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-box-ccg-creds`",
                "authType": "CCG"
            },
            "filterConfiguration": {
                "maxFileSizeInMegaBytes": "500"
            }
        }
    }
}
```

For an OAuth 2.0 data source, set `authType` to
`OAUTH2`. You can optionally add a
`dataEntityConfiguration` with
`inclusionFolderIds` and `inclusionFileIds` to
crawl specific folders and files:

```
{
    "type": "BOX",
    "version": "1",
    "connectionConfiguration": {
        "secretArn": "`arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-box-oauth2-creds`",
        "authType": "OAUTH2"
    },
    "dataEntityConfiguration": {
        "inclusionFolderIds": ["`123456789`"],
        "inclusionFileIds": ["`987654321`"]
    }
}
```

For managed knowledge bases, `CreateDataSource` is
asynchronous: the data source status transitions from
`CREATING` to `AVAILABLE` when the operation
completes.

## Connector parameters

The data source configuration uses the following connector parameters. To connect
to Box, specify `BOX` as the connector type in
`connectorParameters`. For the fields that wrap
`connectorParameters` (such as
`deletionProtectionConfiguration` and
`mediaExtractionConfiguration`), see [Connect a data source](kb-managed-connect-ds.md "kb-managed-connect-ds.md").

connectionConfiguration| Field | Required | Description |
| --- | --- | --- |
| `secretArn` | Yes | The ARN of the AWS Secrets Manager secret containing your Box credentials. |
| `authType` | Yes | The authentication type: `CCG` (recommended) or<br>`OAUTH2`. See [Authentication methods](kb-managed-ds-box.md#kb-managed-box-auth-methods "kb-managed-ds-box.md#kb-managed-box-auth-methods"). |

dataEntityConfiguration (OAuth 2.0 only)| Field | Required | Description |
| --- | --- | --- |
| `inclusionFolderIds` | No | A list of folder IDs to crawl. |
| `inclusionFileIds` | No | A list of file IDs to crawl. |

filterConfiguration (optional)| Field | Required | Description |
| --- | --- | --- |
| `maxFileSizeInMegaBytes` | No | Maximum size, in megabytes, of any single file the connector<br>ingests. Provide as a numeric string (for example,<br>`"500"`). Defaults to `"500"`. |

aclEnabled (optional)| Field | Required | Description |
| --- | --- | --- |
| `aclEnabled` | No | Set to `true` to enable document-level access control.<br>Requires `CCG` authentication. You cannot change this<br>setting after you create the data source. For details, see [Document-level access controls](kb-managed-ds-box-acl.md "kb-managed-ds-box-acl.md"). |

## Change the authentication method

You can change a data source's authentication method (for example, from OAuth 2.0
to Client Credentials Grant) by updating the data source with the new
`authType` and a secret that contains the matching credentials, using the
[UpdateDataSource](../APIReference/API_agent_UpdateDataSource.md "../APIReference/API_agent_UpdateDataSource.md") operation or the AWS Management Console. The document-level access
control setting is fixed when you create a data source, so to add or remove ACLs you
must create a new data source.

## Next steps

After you create the data source, sync it to ingest content into your knowledge
base. For details, see [Sync a data source](kb-managed-sync.md "kb-managed-sync.md"). To filter query results by user permissions,
see [Document-level access controls](kb-managed-ds-box-acl.md "kb-managed-ds-box-acl.md").
