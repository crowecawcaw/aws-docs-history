

# Connect a Dropbox data source

After you set up authentication and store your credentials in an AWS Secrets Manager secret, create the Dropbox data source in your knowledge base. This page describes how to create the data source with the AWS Management Console or the API, followed by a reference for the connector parameters you can configure.

**Note**  
Complete authentication setup first. See [Set up authentication for Dropbox](kb-managed-dropbox-auth-setup.md). You need the secret ARN and the authentication type (`OAUTH2` or `TEAM_ADMIN`) that the secret's refresh token was issued for.

## Create the data source
<a name="kb-managed-ds-dropbox-create"></a>

------
#### [ Console ]

**To connect Dropbox to your managed knowledge base**

1. Open the [Knowledge Bases page of the Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/knowledge-bases), and open your managed knowledge base.

1. Under **Data source**, provide a name for your data source, and from the **Data source type** list, select **Dropbox**.

1. Under **Authentication**, choose the authentication type:
   + **OAuth 2.0** – Crawls the Dropbox of the user who authorized the app.
   + **Team admin** – Crawls content across your Dropbox team.

   You cannot change the authentication type after you create the data source. Then select or create an AWS Secrets Manager secret containing your `clientId`, `clientSecret`, and `refreshToken`.

1. (Optional, **Team admin** only) To enable document-level access control, select **Crawl Access Control Lists (ACLs)**. This option cannot be changed after creation. For details, see [Document-level access controls](kb-managed-ds-dropbox-acl.md).

1. (**Team admin** only) Under **Sync scope**, select the content to crawl: **Team Folders** and **Member Drives** (members' folders, including folders shared with those members). Both are selected by default. If you add folder paths, keep both selected. The console then sends only the folder paths, not the sync scope options, and only the listed paths are crawled.

1. (Optional) Limit the crawl with filters:
   + **Folder paths** – Crawl only the listed folders, including everything under them. Folder paths must start and end with `/`.
   + **User email addresses** (**Team admin** only) – Include or exclude team members by email address.
   + **Modified date** – Crawl only files modified after or before a date.
   + **Max file size** – Skip files larger than a size in megabytes.

   MIME type filters are available only through the API.

------
#### [ API ]

To create a Dropbox data source, send a [CreateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateDataSource.html) request with an Agents for Amazon Bedrock build-time endpoint. The following AWS Command Line Interface example creates a Dropbox data source. For a description of each field, see the connector parameters reference that follows.

```
aws bedrock-agent create-data-source \
 --name "{{Dropbox-connector}}" \
 --knowledge-base-id "{{your-knowledge-base-id}}" \
 --data-source-configuration file://dropbox-managed-connector.json
```

**Team crawl (`TEAM_ADMIN`)**

The following `dropbox-managed-connector.json` crawls the folders of two team members, including folders shared with them, plus every team folder, and skips files over 50 MB. Document-level access control is disabled.

```json
{
    "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
    "managedKnowledgeBaseConnectorConfiguration": {
        "connectorParameters": {
            "type": "DROPBOX",
            "connectorType": "DROPBOX",
            "version": "1",
            "aclEnabled": false,
            "connectionConfiguration": {
                "secretArn": "{{arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-dropbox-creds}}",
                "authType": "TEAM_ADMIN"
            },
            "dataEntityConfiguration": {
                "crawlMemberDrives": true,
                "crawlTeamFolders": true
            },
            "filterConfiguration": {
                "inclusionUserEmailAddresses": ["{{alice@example.com}}", "{{bob@example.com}}"],
                "excludeMimeTypes": ["application/zip"],
                "maxFileSizeInMegaBytes": "50"
            }
        }
    }
}
```

**Team crawl scoped by path (`TEAM_ADMIN`)**

The following `connectorParameters` crawl PDF and text files under `/Finance/Reports/` as they appear in Alice's Dropbox, and skip files modified before 2025. The `dataEntityConfiguration` object is empty because the content toggles cannot be combined with path filters.

```json
"connectorParameters": {
    "type": "DROPBOX",
    "connectorType": "DROPBOX",
    "version": "1",
    "aclEnabled": false,
    "connectionConfiguration": {
        "secretArn": "{{arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-dropbox-creds}}",
        "authType": "TEAM_ADMIN"
    },
    "dataEntityConfiguration": {},
    "filterConfiguration": {
        "inclusionFolderPaths": ["{{/Finance/Reports/}}"],
        "inclusionUserEmailAddresses": ["{{alice@example.com}}"],
        "includeMimeTypes": ["application/pdf", "text/*"],
        "modifiedDateAfter": "2025-01-01T00:00:00Z"
    }
}
```

**Single-user crawl (`OAUTH2`)**

The following `connectorParameters` crawl one folder in the authorizing user's Dropbox. With `OAUTH2`, `dataEntityConfiguration` must be empty and `aclEnabled` must be `false`.

```json
"connectorParameters": {
    "type": "DROPBOX",
    "connectorType": "DROPBOX",
    "version": "1",
    "aclEnabled": false,
    "connectionConfiguration": {
        "secretArn": "{{arn:aws:secretsmanager:us-west-2:123456789012:secret:bedrock-dropbox-user-creds}}",
        "authType": "OAUTH2"
    },
    "dataEntityConfiguration": {},
    "filterConfiguration": {
        "inclusionFolderPaths": ["{{/Projects/Handbook/}}"]
    }
}
```

**Folder paths for individual Dropbox accounts**  <a name="kb-managed-dropbox-individual-paths"></a>
If the authorizing user has an individual Dropbox account (a Basic, Plus, or Essentials plan) rather than a Dropbox team account, each `inclusionFolderPaths` entry must start with the user's member folder name, which is the display name on their Dropbox account. For example, if the display name is Alice Smith, use `/Alice Smith/Projects/Handbook/` to crawl the `/Projects/Handbook/` folder. The name matches case-insensitively. A path without the member folder name matches nothing.

The `filterConfiguration` field is optional. Without filters, a `TEAM_ADMIN` data source crawls every member's folders, including folders shared with them, and every team folder. An `OAUTH2` data source crawls the user's whole Dropbox.

For managed knowledge bases, `CreateDataSource` is asynchronous: the data source status transitions from `CREATING` to `AVAILABLE` when the operation completes.

------

## Connector parameters
<a name="kb-managed-config-dropbox"></a>

The data source configuration uses the following connector parameters. Within `connectorParameters`, set both `type` and `connectorType` to `DROPBOX` and set `version` to `1`. For the fields that wrap `connectorParameters` (such as `deletionProtectionConfiguration` and `mediaExtractionConfiguration`), see [Connect a data source](kb-managed-connect-ds.md).

**Set aclEnabled explicitly**  
If you omit `aclEnabled`, it defaults to `true` for `TEAM_ADMIN` and to `false` for `OAUTH2`. Because ACL configuration is permanent after the data source is created, set `aclEnabled` explicitly so the data source has the access-control behavior you intend. For details, see [Document-level access controls](kb-managed-ds-dropbox-acl.md).

The following table describes the `connectionConfiguration` fields.


**connectionConfiguration**  

| Field | Required | Description | 
| --- | --- | --- | 
| secretArn | Yes | The ARN of the AWS Secrets Manager secret containing your clientId, clientSecret, and refreshToken. | 
| authType | Yes | The authentication type: OAUTH2 (one user's Dropbox) or TEAM\_ADMIN (your Dropbox team). It must match the kind of refresh token in the secret. See [Authentication methods](kb-managed-ds-dropbox.md#kb-managed-dropbox-auth-methods). | 

Dropbox has no per-tenant host, so the connection configuration has no host URL.

The following table describes the `dataEntityConfiguration` fields, which control the content that a team crawl covers. `dataEntityConfiguration` is required but can be empty. Each field defaults to `true` when omitted. These fields apply to `TEAM_ADMIN` only; with `OAUTH2`, leave `dataEntityConfiguration` empty.


**dataEntityConfiguration (TEAM\_ADMIN only)**  

| Field | Required | Description | 
| --- | --- | --- | 
| crawlMemberDrives | No | Whether to crawl team members' folders, including folders shared with those members. Use inclusionUserEmailAddresses and exclusionUserEmailAddresses to choose which members. | 
| crawlTeamFolders | No | Whether to crawl team folders. | 

The following table describes the optional `filterConfiguration` fields, which scope the crawl. Every filter applies on top of the others (AND).


**filterConfiguration (optional)**  

| Field | Required | Description | 
| --- | --- | --- | 
| inclusionFolderPaths | No | A list of up to 350 folder paths to crawl (for example, /Finance/Reports/). Every file under each folder is crawled, at any depth. Each path starts and ends with / and has 3–1,024 characters; / alone is not accepted (omit the path filters to crawl everything). The trailing / means /HR/ matches only the HR folder, not a sibling folder such as /HR2/. Paths match case-insensitively on whole path components. With OAUTH2, paths are in the user's Dropbox; if the user has an individual Dropbox account, start each path with the user's member folder name, as described in [Folder paths for individual Dropbox accounts](#kb-managed-dropbox-individual-paths). With TEAM\_ADMIN, each path is looked up in the Dropbox of every team member in scope. | 
| inclusionUserEmailAddresses | No | TEAM\_ADMIN only. A list of up to 100 team member email addresses. Only these members are in scope. Without path filters, this narrows whose folders are crawled, including folders shared with those members, and does not affect team folders. With path filters, it decides whose Dropbox each path is looked up in. Matched case-insensitively. | 
| exclusionUserEmailAddresses | No | TEAM\_ADMIN only. A list of up to 100 team member email addresses to remove from the scope. Matched case-insensitively. | 
| includeMimeTypes | No | A list of up to 100 MIME types ({{type}}/{{subtype}}, or {{type}}/\* to match every subtype). Only files whose MIME type matches an entry are crawled. | 
| excludeMimeTypes | No | A list of up to 100 MIME types in the same format. Files whose MIME type matches an entry are skipped. | 
| modifiedDateAfter | No | An ISO 8601 timestamp with a time zone (for example, 2025-01-01T00:00:00Z). Only files modified after this time are crawled. | 
| modifiedDateBefore | No | An ISO 8601 timestamp with a time zone. Only files modified before this time are crawled. | 
| maxFileSizeInMegaBytes | No | Maximum size, in megabytes, of any single file the connector ingests. Provide as a numeric string (for example, "50"). | 


**aclEnabled (optional)**  

| Field | Required | Description | 
| --- | --- | --- | 
| aclEnabled | No | Whether to enable document-level access control, which filters query results by each user's Dropbox permissions. Supported only with TEAM\_ADMIN. Defaults to true for TEAM\_ADMIN and false for OAUTH2. You cannot change this setting after you create the data source. For details, see [Document-level access controls](kb-managed-ds-dropbox-acl.md). | 

## Configuration rules
<a name="kb-managed-dropbox-config-rules"></a>

`CreateDataSource` and `UpdateDataSource` reject the following combinations, so you find out before a sync starts:
+ With `OAUTH2`: any `dataEntityConfiguration` field, either email list, or `aclEnabled` set to `true`.
+ A path filter (`inclusionFolderPaths`) together with any `dataEntityConfiguration` field, whether `true` or `false`. With a path filter, only the named paths are crawled.
+ Either email list together with `crawlMemberDrives` set to `false`.
+ With `TEAM_ADMIN`: both `dataEntityConfiguration` fields set to `false`.
+ An `inclusionFolderPaths` entry that does not start and end with `/`.
+ The same email address in both email lists (ignoring case), or the same entry in both MIME type lists.
+ A `modifiedDateAfter` that is not earlier than `modifiedDateBefore`.
+ Changing `aclEnabled` after the data source is created.
+ A secret that is missing `clientId`, `clientSecret`, or `refreshToken`.

## Next steps
<a name="kb-managed-ds-dropbox-connect-next"></a>

After you create the data source, sync it to ingest content into your knowledge base. For details, see [Sync a data source](kb-managed-sync.md). To filter query results by each user's Dropbox permissions, see [Document-level access controls](kb-managed-ds-dropbox-acl.md).