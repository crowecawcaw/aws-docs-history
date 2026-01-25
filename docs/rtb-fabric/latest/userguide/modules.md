# Modules

Modules are configurable components that process RTB traffic flowing through your links.
You can use modules to implement rate limiting, filtering, error handling, and other traffic
management capabilities. RTB Fabric provides built-in modules that are available at no additional
charge, and you can configure them using the RTB Fabric API.

On a link details page, choose the **Modules** tab to view
information about modules that have been configured for the current link. RTB Fabric
only supports viewing modules in the console. You can configure modules with the RTB Fabric
API using the `UpdateLinkModuleFlow` operation.

###### Important

Modules can only be configured on **active** links.
Ensure both gateways are in `ACTIVE` status and the link is `ACTIVE`
before attempting module configuration.

###### Topics

- [Built-in modules](#built-in-modules "#built-in-modules")
- [Configuring modules](#configuring-modules "#configuring-modules")
- [Troubleshooting](#troubleshooting-modules "#troubleshooting-modules")

## Built-in modules

RTB Fabric provides the following built-in modules that you can configure for your links:

- **Rate Limiter Module** – Controls the rate of requests flowing through the link by limiting transactions per second (TPS).
  This module helps protect downstream systems from traffic spikes and ensures consistent
  performance under varying load conditions. Configure using the `rateLimiterModule` name.
- **OpenRTB Attribute Module** – Filters RTB requests based on OpenRTB protocol attributes with configurable actions and holdback percentages.
  This module enables traffic filtering, A/B testing, and custom response handling.
  Configure using the `openRtbAttributeModule` name.

All built-in modules are available at no additional charge. You can configure multiple
modules on a single link, and they will be applied in the order you specify during configuration.

## Configuring modules

Module configuration is only available through the RTB Fabric API. You cannot configure
modules using the RTB Fabric console. Use the [UpdateLinkModuleFlow API operation](../api/API_UpdateLinkModuleFlow.md "../api/API_UpdateLinkModuleFlow.md")
to add, modify, or remove modules from your links.

### Rate Limiter Module

The following example shows how to add a QPS rate limiter module to a link using the AWS Command Line Interface (AWS CLI).

**Add a QPS rate limiter module to a link**

```
`$` `aws rtbfabric update-link-module-flow \
--gateway-id `rtb-gw-source123` \
--link-id `link-abc456def` \
--client-token `"unique-update-token-789"` \
--modules `'[
 {
 "name": "rate-limiter-module",
 "version": "1.0.0",
 "dependsOn": [],
 "moduleParameters": {
 "rateLimiter": {
 "tps": 1000.0
 }
 }
 }
]'` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

### OpenRTB Attribute Module

The OpenRTB attribute module filters RTB requests based on OpenRTB protocol attributes.

**Parameters:**

- `filterType` (String, required) - `INCLUDE` or `EXCLUDE`
- `filterConfiguration` (Array, required) - Collection of filters. Empty array means no filters applied.
- `action` (Object, required) - Action to perform on filtered requests:
  - No-Bid: `{"noBid": {"noBidReasonCode": <integer>}}`
  - Header Tag: `{"headerTag": {"name": "<string>", "value": "<string>"}}`

- `holdbackPercentage` (Float, required) - Percentage (0.0-100.0) of requests to pass through regardless of filters

```
aws rtbfabric update-link-module-flow \
    --region us-east-1 \
    --gateway-id rtb-gw-abc123 \
    --link-id link-xyz789 \
    --modules '[
        {
            "name": "openRtbAttributeModule",
            "version": "20251204-105817",
            "dependsOn": [],
            "moduleParameters": {
                "openRtbAttribute": {
                    "filterType": "INCLUDE",
                    "filterConfiguration": [],
                    "action": {
                        "noBid": {
                            "noBidReasonCode": 1
                        }
                    },
                    "holdbackPercentage": 10.0
                }
            }
        }
    ]'
```

### Configuring Multiple Modules

You can configure multiple modules on a single link. Modules execute in the order specified,
with the `dependsOn` field controlling execution dependencies.

```
aws rtbfabric update-link-module-flow \
    --region us-east-1 \
    --gateway-id rtb-gw-abc123 \
    --link-id link-xyz789 \
    --modules '[
        {
            "name": "rateLimiterModule",
            "version": "20251204-105817",
            "dependsOn": [],
            "moduleParameters": {
                "rateLimiter": {
                    "tps": 1000.0
                }
            }
        },
        {
            "name": "openRtbAttributeModule",
            "version": "20251204-105817",
            "dependsOn": ["rateLimiterModule"],
            "moduleParameters": {
                "openRtbAttribute": {
                    "filterType": "INCLUDE",
                    "filterConfiguration": [],
                    "action": {
                        "noBid": {
                            "noBidReasonCode": 1
                        }
                    },
                    "holdbackPercentage": 10.0
                }
            }
        }
    ]'
```

### Viewing Module Configuration

Retrieve the current module configuration for a link using the `GetLink` operation:

```
aws rtbfabric get-link \
    --region us-east-1 \
    --gateway-id rtb-gw-abc123 \
    --link-id link-xyz789
```

The response includes:

- `flowModules` - Currently active module configuration
- `pendingFlowModules` - Module configuration pending activation (if any)

### Removing Modules

To remove all modules from a link, pass an empty modules array:

```
aws rtbfabric update-link-module-flow \
    --region us-east-1 \
    --gateway-id rtb-gw-abc123 \
    --link-id link-xyz789 \
    --modules '[]'
```

## Troubleshooting

**Common Issues:**

- **"Resource not ready to be used yet"** - Wait for gateways and links to reach `ACTIVE` status before configuring modules.
- **Module configuration not applied** - Check the `pendingFlowModules` field in the link response to see if configuration is still being processed.
- **Invalid module parameters** - Verify parameter names and value types match the module specification exactly.

Check link and module status:

```
# Check link status
aws rtbfabric get-link --region us-east-1 --gateway-id <gateway-id> --link-id <link-id> --query 'status'

# Check module configuration
aws rtbfabric get-link --region us-east-1 --gateway-id <gateway-id> --link-id <link-id> --query '{Active:flowModules,Pending:pendingFlowModules}'
```
