

# CloudWatch pipelines configuration for Cisco Meraki
<a name="cisco-meraki-pipeline-setup"></a>

Collects log data from the Cisco Meraki Dashboard REST API v1 using API key authentication.

Configure the Cisco Meraki source with the following parameters:

```
source:
  cisco_meraki:
    organization_id: "<meraki-organization-ID>"
    range: "P7D"
    authentication:
      api_key: "${{aws_secrets:<secret-name>:api_key}}"
```Parameters

`organization_id` (required)  
The Cisco Meraki organization ID. Each pipeline collects data from a single organization. You can find your organization ID in the Meraki Dashboard under **Organization > Settings**, or by calling `GET /organizations`.

`authentication.api_key` (required)  
Cisco Meraki API key, stored as a key/value pair. From the preceding example, the name of the key will be `api_key`.

`range` (optional)  
The time range for log collection. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for 21 hours). Default is 0 hours, and the maximum is 90 days.

**Note**  
Store sensitive credentials like API keys in AWS Secrets Manager and reference them using the `${{aws_secrets:secret-name:key}}` syntax in your configuration.