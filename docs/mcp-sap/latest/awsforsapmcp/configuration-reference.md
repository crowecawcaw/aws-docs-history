

# Configuration Reference
<a name="configuration-reference"></a>

You configure the AWS for SAP Model Context Protocol (MCP) Server by using environment variables that begin with the prefix `MCP_SERVER_`. These variables fall into two groups: mandatory variables that must be set for the server to start, and optional variables that come with default values. When the server starts, it validates all configurations and returns a descriptive error if any validation rule is violated. After deployment, you can edit these configuration variables directly in the Amazon Bedrock AgentCore Runtime console.

As an example, to modify one of the configuration variable values:

1. Open the **Amazon Bedrock AgentCore console**.

1. In the navigation pane, choose **Runtime**.

1. Under **Build**, choose the AWS for SAP MCP Server that you would like to update from the **Runtime Resources** panel.

1. On the chosen MCP server page, choose **Update Hosting**.

1. Expand the **Advanced Configurations** panel. You will see all the environment variables (for example, `MCP_SERVER_SAP_OAUTH_FLOW`) listed with their corresponding values.

1. Change the desired MCP server configuration variable value and choose **Host agent/tool** for the changes to take effect.

## Required environment variables
<a name="required-env-vars"></a>

The following variables must be set for the server to start. Some are conditionally required based on the chosen authentication flow.


| Variable | Description | Example | 
| --- | --- | --- | 
|  `MCP_SERVER_SAP_BASE_URL`  | Base URL of the SAP OData endpoint. |  `https://sap.example.com:44301/sap/opu/odata/sap/`  | 
|  `MCP_SERVER_SAP_OAUTH_FLOW`  | Authentication flow type. Determines which credential mechanism the server uses. |  `M2M`  | 
|  `MCP_SERVER_BASIC_AUTH_SECRET_NAME`  |  AWS Secrets Manager secret name containing SAP username and password. |  `my-sap-credentials`  | 
|  `MCP_SERVER_OAUTH_PROVIDER`  | Bedrock AgentCore Identity Provider Name. Required when `MCP_SERVER_SAP_OAUTH_FLOW` is set to `M2M`, `USER_FEDERATION`, or `ON_BEHALF_OF_TOKEN_EXCHANGE`. |  `sap-oauth-provider`  | 
|  `MCP_SERVER_SAP_OAUTH_SCOPES`  | OAuth scopes for SAP access. Required when `MCP_SERVER_SAP_OAUTH_FLOW` is set to `M2M`, `USER_FEDERATION`, or `ON_BEHALF_OF_TOKEN_EXCHANGE`. |  `ZAPI_SALES_ORDER_SRV_0001`  | 
|  `MCP_SERVER_APP_CALLBACK_URL`  | Callback URL for the interactive OAuth flow. Required when `MCP_SERVER_SAP_OAUTH_FLOW` is set to `USER_FEDERATION`. |  `https://app.example.com/auth`  | 

## Optional environment variables
<a name="optional-env-vars"></a>

The following variables have default values and can be overridden to customize server behavior.


| Variable | Default | Description | 
| --- | --- | --- | 
|  `MCP_SERVER_NAME`  |  `SAP-MCP-Server`  | Name of the MCP server instance. | 
|  `MCP_SERVER_LOG_LEVEL`  |  `INFO`  | Log verbosity. One of `DEBUG`, `INFO`, `WARNING`, `ERROR`. | 
|  `MCP_SERVER_REGION`  |  `$AWS_REGION` or `us-west-2`  |  AWS Region for AWS Secrets Manager, Amazon S3, and AgentCore Identity calls. (When deploying with the CFN template, this value is automatically set to the deployment region `$AWS_REGION`. For custom automation workflows, this parameter must be explicitly set in AgentCore to avoid deployment failures.) | 
|  `MCP_SERVER_SAP_SYSTEM`  |  `S4HANA`  | SAP system type. One of `S4HANA`, `ECC`. | 
|  `MCP_SERVER_SAP_CLIENT_NUMBER`  | None | SAP client number. Must be exactly 3 digits and cannot be `000`. | 
|  `MCP_SERVER_READ_ENABLED`  |  `true`  | Enable read tools (`find_sap_services`, `get_metadata`, `odata_read`, `odata_count`). | 
|  `MCP_SERVER_WRITE_ENABLED`  |  `false`  | Master switch for all write tools. Must be `true` before any per-operation flag takes effect. | 
|  `MCP_SERVER_CREATE_ENABLED`  |  `false`  | Enable the `odata_create` tool. Requires `WRITE_ENABLED=true`. | 
|  `MCP_SERVER_UPDATE_ENABLED`  |  `false`  | Enable the `odata_update` tool. Requires `WRITE_ENABLED=true`. | 
|  `MCP_SERVER_DELETE_ENABLED`  |  `false`  | Enable the `odata_delete` tool. Requires `WRITE_ENABLED=true`. | 
|  `MCP_SERVER_FUNCTION_IMPORT_ENABLED`  |  `false`  | Enables the `odata_function_import` tool. Requires `WRITE_ENABLED=true`. | 
|  `MCP_SERVER_CUSTOM_CATALOG_BUCKET`  | None | Amazon S3 bucket name for a custom service catalog. The S3 bucket name must start with `awsforsap-mcp-server-`. | 
|  `MCP_SERVER_USE_SAP_CATALOG`  |  `true`  | Fetch the service catalog from SAP. If `false`, `CUSTOM_CATALOG_BUCKET` is required. | 
|  `MCP_SERVER_ALLOWED_SERVICE_PREFIXES`  |  `*`  | Comma-separated list of service prefixes for filtering. `*` means all services. | 

## Enabling Write Operations
<a name="enabling-write-ops"></a>

The write tools (`odata_create`, `odata_update`, `odata_delete`, and `odata_function_import`) are disabled by default. Enabling them requires two levels of opt-in:

1.  **Master switch** — Set `MCP_SERVER_WRITE_ENABLED=true` to unlock write capabilities at the MCP Server level.

1.  **Per-operation flag** — Enable each write operation individually:


| Operation | Environment variable | 
| --- | --- | 
|  `odata_create`  |  `MCP_SERVER_CREATE_ENABLED=true`  | 
|  `odata_update`  |  `MCP_SERVER_UPDATE_ENABLED=true`  | 
|  `odata_delete`  |  `MCP_SERVER_DELETE_ENABLED=true`  | 
|  `odata_function_import`  |  `MCP_SERVER_FUNCTION_IMPORT_ENABLED=true`  | 

Both the master switch and the corresponding per-operation flag must be `true` for a write tool to be available to agents. If `MCP_SERVER_WRITE_ENABLED=true` is set but no per-operation flag is enabled, the server will fail configuration validation at startup.

## Custom catalog configuration
<a name="custom-catalog-config"></a>

With the custom catalog feature, you can extend or replace the SAP service catalog with a catalog that you define and host on Amazon S3. This is useful when your SAP system does not expose all services through `IWFND/CATALOGSERVICE;v=2`, or when you want a curated set of services available to AI agents.

### Prerequisites
<a name="custom-catalog-prereqs"></a>
+ An Amazon S3 bucket whose name starts with `awsforsap-mcp-server-` (for example, `awsforsap-mcp-server-mycatalog`).
+ Appropriate IAM permissions to read from that bucket.
+ Access to set environment variables on the AWS for SAP MCP Server.

### Create the catalog file
<a name="custom-catalog-create"></a>

Create a file named `catalog.json`. The file must use this exact name. Each entry requires two fields:
+  **Description** — A human-readable description of the service.
+  **ServiceUrl** — The full URL to the SAP OData service endpoint.

 **Example catalog.json:** 

```
{
  "SapServices": [
    {
      "Description": "Custom Business Partner API",
      "ServiceUrl": "https://my-sap-system.example.com/sap/opu/odata/sap/API_BUSINESS_PARTNER"
    },
    {
      "Description": "Custom Sales Order API with version",
      "ServiceUrl": "https://my-sap-system.example.com/sap/opu/odata/sap/API_SALES_ORDER;v=0002"
    },
    {
      "Description": "Custom Inventory Service",
      "ServiceUrl": "https://my-sap-system.example.com/sap/opu/odata/custom/Z_INVENTORY_SRV"
    }
  ]
}
```

 **Constraints:** 
+ The root object must contain an `SapServices` array.
+ The catalog supports a maximum of 1024 entries.
+ Both `Description` and `ServiceUrl` are required and must be non-empty.
+ If duplicate service names exist within your custom catalog, the server keeps the last occurrence.

### Upload the catalog to Amazon S3
<a name="custom-catalog-upload"></a>

Upload `catalog.json` to the root of your bucket, or into a subfolder:

```
# Root of bucket
aws s3 cp catalog.json s3://awsforsap-mcp-server-mycatalog/catalog.json

# Or into a subfolder
aws s3 cp catalog.json s3://awsforsap-mcp-server-mycatalog/my-environment/catalog.json
```

### Configure the MCP server environment variables
<a name="custom-catalog-configure"></a>

Two environment variables control the custom catalog feature:


| Variable | Default | Description | 
| --- | --- | --- | 
|  `MCP_SERVER_CUSTOM_CATALOG_BUCKET`  | None | Amazon S3 bucket name (and optional sub-path) for the custom catalog. Must start with `awsforsap-mcp-server-`. | 
|  `MCP_SERVER_USE_SAP_CATALOG`  |  `true`  | When `true`, the server fetches the live SAP catalog. When `false`, the server skips all SAP catalog network requests. | 

Choose one of the three configuration options below based on your use case.

 **Merged mode — SAP catalog \+ custom catalog (most common)** 

Use this when you want to supplement or override specific entries in the live SAP catalog with your own definitions. The server fetches the SAP catalog at runtime and merges your custom entries on top. Custom entries override SAP entries that share the same service name; new custom entries are added.

```
MCP_SERVER_CUSTOM_CATALOG_BUCKET="awsforsap-mcp-server-mycatalog"
# MCP_SERVER_USE_SAP_CATALOG defaults to true, no need to set it

# If your catalog.json is in a subfolder:
MCP_SERVER_CUSTOM_CATALOG_BUCKET="awsforsap-mcp-server-mycatalog/my-environment"
```

 **Custom-only mode — no SAP catalog** 

Use this when you want to disable all SAP catalog network requests and serve only the services you have explicitly defined. This is the right choice for air-gapped environments, testing without a live SAP system, or scenarios where the SAP catalog is unreliable.

```
MCP_SERVER_USE_SAP_CATALOG="false"
MCP_SERVER_CUSTOM_CATALOG_BUCKET="awsforsap-mcp-server-mycatalog"
```

Both variables are required in this mode. If you set `MCP_SERVER_USE_SAP_CATALOG` to `false` without setting `MCP_SERVER_CUSTOM_CATALOG_BUCKET`, the server fails at startup because it would have no service catalog available.

 **SAP catalog only — no custom catalog (default behavior)** 

If you do not set `MCP_SERVER_CUSTOM_CATALOG_BUCKET`, the server uses only the live SAP catalog. This is the default behavior and requires no configuration changes.

### Deploy the MCP server
<a name="custom-catalog-deploy"></a>

Deploy (or redeploy) the AWS for SAP MCP Server after setting the environment variables. During startup, check the logs to confirm your catalog loaded correctly:
+ A successful custom catalog load logs the number of entries loaded.
+ If the bucket name does not start with `awsforsap-mcp-server-`, the server rejects the configuration and logs an error, then falls back to the SAP catalog only.
+ If `catalog.json` is missing, malformed, or exceeds 1024 entries, the server logs a warning or error and continues with an empty custom catalog.

### Verify your services
<a name="custom-catalog-verify"></a>

Use the `find_sap_services` tool to search for your custom services. The tool searches across all catalog entries (SAP and custom) with no distinction between sources. Existing search and filter logic applies to all entries regardless of origin.

## Service hints configuration
<a name="service-hints-config"></a>

With service hints, you can provide custom natural-language guidance for different SAP services. AI agents can look up these hints by using the `get_service_hints` tool.

To enable custom service hints, set the following environment variable:

```
MCP_SERVER_SERVICE_HINTS_S3_URL=s3://awsforsap-mcp-server-service-hints-bucket/path/to/file.json
```

After you configure service hints, the `get_service_hints` tool becomes available to AI agents. The tool returns usage guidance for a requested service from the hints file.

### Hints file schema
<a name="service-hints-schema"></a>

The service hints file must follow the JSON schema below. The two required top-level fields are `version` and `hints`.

```
{
  "version": "1.0",
  "_description": "Optional human-readable description of the hints file",
  "hints": [
    {
      "pattern": "API_BUSINESS_PARTNER",
      "priority": 10,
      "service_type": "Business Partner API",
      "known_issues": [
        "Pagination may return inconsistent results when filters change between pages"
      ],
      "workarounds": [
        "Use $skiptoken instead of $skip for stable pagination"
      ],
      "notes": [
        "Always include AddressData in $expand for complete partner records"
      ],
      "field_hints": {
        "BusinessPartner": {
          "type": "Edm.String",
          "format": "10-digit numeric string",
          "example": "0001000000",
          "description": "Unique business partner identifier",
          "constraints": {
            "required": true,
            "maxLength": 10,
            "pattern": "^[0-9]{10}$"
          }
        }
      },
      "tags": ["master-data", "business-partner"]
    }
  ]
}
```

### Schema field reference
<a name="service-hints-fields"></a>

 **Top-level fields:** 


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `version`  | String | Yes | Schema version identifier (for example, `1.0`). | 
|  `hints`  | Array | Yes | Array of service-specific hint configurations. | 
|  `_description`  | String | No | Human-readable description of the hints file purpose. | 
|  `_note`  | String | No | Additional notes about how hints are processed. | 

 **Hint entry fields:** 


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `pattern`  | String | Yes | URL pattern or exact service name to match. Supports wildcards (`*`). | 
|  `priority`  | Integer | No | Priority level for hint matching. Higher values override lower ones. Default: `10`. | 
|  `service_type`  | String | No | Human-readable service type or name. | 
|  `known_issues`  | Array of strings | No | List of known issues with this service. | 
|  `workarounds`  | Array of strings | No | List of workarounds for known issues. | 
|  `notes`  | Array of strings | No | Additional notes and guidance for using this service. | 
|  `field_hints`  | Object | No | Field-specific hints and metadata. Keys are field names, values are field hint objects. | 
|  `tags`  | Array of strings | No | Optional tags for categorizing or filtering hints. Must be unique. | 
|  `metadata`  | Object | No | Additional metadata for extensibility. | 

 **Field hint fields:** 


| Field | Type | Description | 
| --- | --- | --- | 
|  `type`  | String | Data type of the field (for example, `Edm.String`, `Edm.Int32`). | 
|  `format`  | String | Format or pattern description for the field value. | 
|  `example`  | String, number, boolean, or array | Example value for the field. | 
|  `description`  | String | Detailed description of the field and its usage. | 
|  `constraints`  | Object | Field constraints including `required`, `minLength`, `maxLength`, `pattern`, and `enum`. | 
|  `notes`  | Array of strings | Additional notes about the field. | 

## Service Prefixes
<a name="service-prefix-filtering"></a>

Service prefix filtering restricts which SAP OData services are discoverable by AI agents. When enabled, the `find_sap_services` tool returns only services whose technical name starts with one of the configured prefixes.

```
# Allow only services starting with ZAPI_ or ZCUSTOM_
MCP_SERVER_ALLOWED_SERVICE_PREFIXES=ZAPI_,ZCUSTOM_
```

```
# Allow all services
MCP_SERVER_ALLOWED_SERVICE_PREFIXES=*
```

## Cross-validation Rules
<a name="cross-validation-rules"></a>

The server enforces the following cross-validation rules at startup. If any rule is violated, the server logs a descriptive error and exits.

1.  **Write operations require at least one operation enabled.** If `MCP_SERVER_WRITE_ENABLED=true`, at least one of `MCP_SERVER_CREATE_ENABLED`, `MCP_SERVER_UPDATE_ENABLED`, `MCP_SERVER_DELETE_ENABLED`, or `MCP_SERVER_FUNCTION_IMPORT_ENABLED` must also be `true`.

1.  **Custom catalog required when SAP catalog is disabled.** If `MCP_SERVER_USE_SAP_CATALOG=false`, then `MCP_SERVER_CUSTOM_CATALOG_BUCKET` must be set.

1.  **OAuth provider validated at startup.** When the authentication flow is `M2M`, `USER_FEDERATION`, or `ON_BEHALF_OF_TOKEN_EXCHANGE`, the server validates the `MCP_SERVER_SAP_OAUTH_PROVIDER` value against Bedrock AgentCore Identity during startup.

1.  **Basic auth secret validated at startup.** When the authentication flow is `BASIC`, the server validates that the secret specified in `MCP_SERVER_BASIC_AUTH_SECRET_NAME` exists in AWS Secrets Manager.