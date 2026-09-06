

# Troubleshooting
<a name="troubleshooting"></a>

Use this section to diagnose and resolve common issues with the AWS for SAP Model Context Protocol (MCP) Server. You can find CloudWatch Logs Insights queries for log analysis, common error scenarios with resolutions, and guidance on contacting AWS Support.

## CloudWatch Logs Insights queries
<a name="cw-logs-queries"></a>

The AWS for SAP MCP Server emits structured logs to CloudWatch Logs. You can use the following queries to diagnose common issues. Select the log group for your MCP Server container and set the desired time range.

 **All errors in time range** 

```
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 100
```

 **Session trace by ID** 

```
fields @timestamp, @message
| filter @message like /\[session:<session-id>\]/
| sort @timestamp asc
```

 **Authentication failures** 

```
fields @timestamp, @message
| filter @message like /ODataAuthError|AuthenticationError|401|403/
| sort @timestamp desc
| limit 50
```

 **Tool execution failures** 

```
fields @timestamp, @message
| filter @message like /TOOL CALL END \(FAILURE\)/
| sort @timestamp desc
| limit 50
```

 **Tool execution latency** 

```
fields @timestamp, @message
| filter @message like /Execution Time:/
| parse @message "Execution Time: *s" as exec_time
| stats avg(exec_time), max(exec_time), min(exec_time) by bin(5m)
```

 **Configuration validation errors at startup** 

```
fields @timestamp, @message
| filter @message like /ValidationError|Invalid configuration|ValueError/
| sort @timestamp desc
| limit 50
```

 **Function import audit log** 

```
fields @timestamp, @message
| filter @message like /\[AUDIT\]/
| sort @timestamp desc
| limit 100
```

## Common error scenarios
<a name="common-errors"></a>


| Scenario | Symptoms | Resolution | 
| --- | --- | --- | 
| SAP system unreachable | Connection timeout errors, `Error fetching SAP services` in logs. | Verify `SAP_BASE_URL` is correct and the SAP system is running. Check network connectivity and security group configuration. | 
| Invalid credentials |  `ODataAuthError`, HTTP 401 status code. | For BASIC auth: verify the AWS Secrets Manager secret contains the correct username and password. For M2M/USER\_FEDERATION: verify the OAuth provider name and scopes. | 
| CSRF token failures | HTTP 403 status code on write operations. | Retry the operation — the server fetches a fresh CSRF token on each request. If the issue persists, verify that the SAP system’s CSRF token endpoint is accessible. | 
| Service catalog empty |  `No services found` in logs. | Verify that `IWFND/CATALOGSERVICE;v=2` is accessible on the SAP system. Check SAP user authorization. If using a custom catalog, verify the Amazon S3 bucket name and JSON file validity. | 
| Configuration validation failures | Server fails to start, `ValidationError` in logs. | Review environment variables against the validation rules in [Configuration Reference](configuration-reference.md). | 
| Custom catalog: server rejects config at startup | Error logged at startup, server falls back to SAP catalog. | Verify the Amazon S3 bucket name starts with `awsforsap-mcp-server-` and that the bucket exists in the correct AWS account and Region. | 
| Custom catalog: server fails with error at startup |  `MCP_SERVER_USE_SAP_CATALOG=false` without `MCP_SERVER_CUSTOM_CATALOG_BUCKET` set. | Set `MCP_SERVER_CUSTOM_CATALOG_BUCKET` or re-enable the SAP catalog. | 
| Custom catalog: services not appearing |  `catalog.json` not found, access denied, or invalid JSON. | Verify the file is named exactly `catalog.json` and is in the correct bucket/path. Check IAM permissions. Check server logs for specific validation errors. | 
| Custom catalog: individual entry missing | Title derivation failed for that entry. | Verify the `ServiceUrl` follows the `/sap/opu/odata/{namespace}/{SERVICE_NAME}` pattern. | 
| Custom catalog: exceeds entry limit | Catalog has more than 1024 entries. | Reduce the number of entries to 1024 or fewer. | 
| Custom catalog: changes not reflected | Catalog is loaded at startup only. | Restart the MCP server to pick up changes to `catalog.json`. | 
| Private IdP unreachable | OAuth token exchange fails with connection timeout or DNS resolution errors. Server logs show failures reaching the SAP/IdP token endpoint. | If the SAP authorization server or external IdP is hosted inside a VPC, confirm that a `privateEndpoint` is configured on the AgentCore OAuth credential provider. Verify that the specified subnets and security groups allow HTTPS to the IdP. For more information, see [Connect to private identity providers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-private-idp.html). | 