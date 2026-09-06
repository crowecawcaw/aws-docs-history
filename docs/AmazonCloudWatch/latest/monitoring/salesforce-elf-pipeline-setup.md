

# CloudWatch pipelines configuration for Salesforce ELF
<a name="salesforce-elf-pipeline-setup"></a>

Collects EventLogFile and Setup AuditTrail events from Salesforce using OAuth2 authentication.

Configure the Salesforce ELF source with the following parameters:

```
source:
  salesforce_elf:
    instance_url: "<<your-instance-url>>"
    authentication:
      client_id: "${{aws_secrets:salesforce-credentials:client_id}}"
      client_secret: "${{aws_secrets:salesforce-credentials:client_secret}}"
```Parameters

`instance_url` (required)  
Salesforce instance URL. Must use HTTPS.

`authentication.client_id` (required)  
OAuth2 Consumer Key. Supports `${{aws_secrets:...}}`.

`authentication.client_secret` (required)  
OAuth2 Consumer Secret. Supports `${{aws_secrets:...}}`.

`range` (optional)  
Set backfill duration in ISO 8601 format (for example, `PT24H`, `P7D`, `P30D`). When set, overwrites both `elf_backfill` and `setup_audit_trail_backfill` with the same duration. When omitted, `elf_backfill` defaults to `P30D` (30 days) and `setup_audit_trail_backfill` defaults to `P180D` (180 days).