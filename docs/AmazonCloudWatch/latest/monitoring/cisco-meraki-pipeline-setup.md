# CloudWatch pipelines configuration for Cisco Meraki

Collects log data from the Cisco Meraki Dashboard REST API v1 using API key
authentication.

Configure the Cisco Meraki source with the following parameters:

```
source:
  cisco_meraki:
    organization_id: "<meraki-organization-ID>"
    authentication:
      api_key: "${{aws_secrets:<secret-name>:api_key}}"
```

###### Parameters

`organization_id` (required)

The Cisco Meraki organization ID. Each pipeline collects data from a
single organization. You can find your organization ID in the Meraki
Dashboard under **Organization > Settings**,
or by calling `GET /organizations`.

`authentication.api_key` (required)

Cisco Meraki API key, stored as a key/value pair. From the above example,
the name of the key will be `api_key`.

###### Note

Store sensitive credentials like API keys in AWS Secrets Manager and reference them using
the `${{aws_secrets:secret-name:key}}` syntax in your
configuration.
