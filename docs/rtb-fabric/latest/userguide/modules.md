

# Modules
<a name="modules"></a>

Modules are configurable components that process RTB traffic flowing through your links. You can use modules to implement rate limiting, filtering, error handling, and other traffic management capabilities. RTB Fabric provides built-in modules that are available at no additional charge, and you can configure them using the RTB Fabric API.

On a link details page, choose the **Modules** tab to view information about modules that have been configured for the current link. RTB Fabric only supports viewing modules in the console. You can configure modules with the RTB Fabric API using the `UpdateLinkModuleFlow` operation.

**Important**  
Modules can only be configured on **active** links. Ensure both gateways are in `ACTIVE` status and the link is `ACTIVE` before attempting module configuration.

**Topics**
+ [Built-in modules](#built-in-modules)
+ [Configuring modules](#configuring-modules)
+ [Troubleshooting](#troubleshooting-modules)

## Built-in modules
<a name="built-in-modules"></a>

RTB Fabric provides the following built-in modules that you can configure for your links:
+ **Rate Limiter Module** – Controls the rate of requests flowing through the link by limiting transactions per second (TPS). This module helps protect downstream systems from traffic spikes and ensures consistent performance under varying load conditions. Configure using the `rateLimiterModule` name.
+ **OpenRTB Attribute Module** – Filters RTB requests based on OpenRTB protocol attributes with configurable actions and holdback percentages. This module enables traffic filtering, A/B testing, and custom response handling. Configure using the `openRtbAttributeModule` name.

All built-in modules are available at no additional charge. You can configure multiple modules on a single link, and they will be applied in the order you specify during configuration.

## Configuring modules
<a name="configuring-modules"></a>

You can configure modules using the RTB Fabric API, the AWS Command Line Interface (AWS CLI), or CloudFormation. The RTB Fabric console does not support module configuration. To add, modify, or remove modules from your links, use the [UpdateLinkModuleFlow](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLinkModuleFlow.html) API operation or its equivalent in the AWS CLI or CloudFormation.

### Rate Limiter Module
<a name="rate-limiter-module-example"></a>

The following example shows how to add a QPS rate limiter module to a link using the AWS Command Line Interface (AWS CLI).

**Add a QPS rate limiter module to a link**

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-source123}} \
--link-id {{link-abc456def}} \
--client-token {{"unique-update-token-789"}} \
--modules {{'[
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
]'}} \
--region {{us-east-1}}
```

### OpenRTB Attribute Module
<a name="openrtb-attribute-module-example"></a>

The OpenRTB Attribute Module filters bid requests based on attributes in the OpenRTB request payload. You define a set of filters to divide incoming bid requests into two groups: requests that match your filters and requests that do not. You then choose which group to apply an action to, such as returning a no-bid response or adding a custom HTTP header. This lets you intelligently shed traffic before it reaches your DSP, reducing compute and networking costs.

**Warning**  
A misconfigured OpenRTB Attribute Module can unintentionally block desirable traffic. If you are unsure of the impact of a new filter configuration, we recommend starting with a high `holdbackPercentage` (for example, 90.0) and gradually decreasing it as you verify that only the intended traffic is being filtered.

The module configuration is specified inside the `openRtbAttribute` object within `moduleParameters`. It contains the following fields:
+ `filterConfiguration` – An array of filters that define which bid requests to match.
+ `filterType` – Determines which group of requests the action applies to.
+ `action` – The action to perform on the selected group of requests.
+ `holdbackPercentage` – A percentage of requests that pass through regardless of filter results.

#### Filter criteria
<a name="openrtb-attribute-module-filter-criteria"></a>

A *filter criterion* is the smallest unit of a filter. Each criterion is a predicate on a single field in the OpenRTB bid request. A criterion contains two fields:
+ `path` – A JSON path expression that identifies a field in the bid request body. Use standard JSON path syntax starting with `$.` to navigate the OpenRTB request structure (for example, `$.device.geo.country`).
+ `values` – An array of strings representing the desired values. A criterion matches when the value retrieved from the bid request field is contained in this array.

The following example criterion matches bid requests where the COPPA (Children's Online Privacy Protection Act) flag is set to `1` (true):

```
{
    "path": "$.regs.coppa",
    "values": ["1"]
}
```

The following example criterion matches bid requests originating from the United States or Canada:

```
{
    "path": "$.device.geo.country",
    "values": ["USA", "CAN"]
}
```

**Note**  
The `values` field uses string matching. Numeric fields in the OpenRTB specification (such as `regs.coppa`) must be represented as strings in the `values` array (for example, `"1"` instead of `1`).

#### Filters
<a name="openrtb-attribute-module-filters"></a>

A *filter* groups one or more filter criteria together using **AND** logic. All criteria within a filter must match for the filter to match a bid request. A filter contains a single field:
+ `criteria` – An array of filter criterion objects.

The following example filter matches bid requests that have the COPPA flag set to true **AND** originate from the United States or Canada. Both criteria must be satisfied:

```
{
    "criteria": [
        {
            "path": "$.regs.coppa",
            "values": ["1"]
        },
        {
            "path": "$.device.geo.country",
            "values": ["USA", "CAN"]
        }
    ]
}
```

#### Filter configuration
<a name="openrtb-attribute-module-filter-configuration"></a>

The `filterConfiguration` field is an array of filters combined using **OR** logic. A bid request matches the filter configuration if it matches *any one* of the filters in the array.

By combining AND logic within each filter and OR logic across filters, you can express complex filtering rules. The following example matches two types of requests:
+ Type A: Requests with COPPA flag set to true **AND** originating from the United States or Canada
+ **OR**
+ Type B: Requests from the domain `example.com`

```
"filterConfiguration": [
    {
        "criteria": [
            {
                "path": "$.regs.coppa",
                "values": ["1"]
            },
            {
                "path": "$.device.geo.country",
                "values": ["USA", "CAN"]
            }
        ]
    },
    {
        "criteria": [
            {
                "path": "$.site.domain",
                "values": ["example.com"]
            }
        ]
    }
]
```

#### Filter type
<a name="openrtb-attribute-module-filter-type"></a>

The `filterType` field determines which group of bid requests the action applies to. After the filter configuration divides requests into two groups (matched and unmatched), the filter type selects which group receives the action.
+ `INCLUDE` – The action is performed on requests that *match* the filter configuration. Use this when you want to target specific types of traffic (for example, block requests from certain regions).
+ `EXCLUDE` – The action is performed on requests that *do not match* the filter configuration. Use this when you want to define the traffic you want to keep and apply the action to everything else.

#### Actions
<a name="openrtb-attribute-module-actions"></a>

The `action` field specifies what to do with the selected group of bid requests. The following actions are available:
+ **No bid** (`noBid`) – Short-circuits the request and returns a no-bid response without forwarding it to the DSP.

  If you omit the `noBidReasonCode` field, the module returns an HTTP `204 No Content` response with no response body:

  ```
  "action": {
      "noBid": {}
  }
  ```

  If you specify a `noBidReasonCode`, the module returns an HTTP `200 OK` response with a JSON body containing the request ID (if present in the original bid request) and an `nbr` field set to the reason code you provided:

  ```
  "action": {
      "noBid": {
          "noBidReasonCode": 1
      }
  }
  
  // Example response body:
  // { "id": "request-123", "nbr": 1 }
  ```
+ **Header tag** (`headerTag`) – Adds a custom HTTP header to the request before forwarding it to the DSP. The request is not blocked; instead it is tagged with additional metadata. You specify a header `name` and `value`.

  ```
  "action": {
      "headerTag": {
          "name": "X-Custom-Filter",
          "value": "coppa-flagged"
      }
  }
  ```

#### Holdback percentage
<a name="openrtb-attribute-module-holdback"></a>

The `holdbackPercentage` field specifies a percentage of requests (from 0.0 to 100.0) that pass through the module without any action being applied, regardless of whether they match the filter configuration. This is useful for A/B testing or for gradually rolling out filtering rules. For example, setting `holdbackPercentage` to `10.0` means 10% of requests bypass the module entirely.

#### Examples
<a name="openrtb-attribute-module-examples"></a>

**Example 1: Block COPPA-flagged traffic from specific countries**

The following example returns an HTTP `204 No Content` for bid requests that have the COPPA flag set to true and originate from the United States or Canada:

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "openRtbAttributeModule",
        "version": "20251204-105817",
        "dependsOn": [],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "INCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.regs.coppa",
                                "values": ["1"]
                            },
                            {
                                "path": "$.device.geo.country",
                                "values": ["USA", "CAN"]
                            }
                        ]
                    }
                ],
                "action": {
                    "noBid": {}
                },
                "holdbackPercentage": 0.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

**Example 2: Block traffic from multiple sources using OR logic**

The following example returns a no-bid response for bid requests that match *either* of the following conditions:
+ COPPA flag is true AND the request originates from the United States or Canada
+ The request is from the domain `example.com`

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "openRtbAttributeModule",
        "version": "20251204-105817",
        "dependsOn": [],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "INCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.regs.coppa",
                                "values": ["1"]
                            },
                            {
                                "path": "$.device.geo.country",
                                "values": ["USA", "CAN"]
                            }
                        ]
                    },
                    {
                        "criteria": [
                            {
                                "path": "$.site.domain",
                                "values": ["example.com"]
                            }
                        ]
                    }
                ],
                "action": {
                    "noBid": {
                        "noBidReasonCode": 1
                    }
                },
                "holdbackPercentage": 0.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

**Example 3: Tag requests with a custom header**

The following example adds a custom HTTP header to bid requests from mobile devices instead of blocking them. The requests are still forwarded to the DSP with the additional header attached:

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "openRtbAttributeModule",
        "version": "20251204-105817",
        "dependsOn": [],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "INCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.device.devicetype",
                                "values": ["1", "4"]
                            }
                        ]
                    }
                ],
                "action": {
                    "headerTag": {
                        "name": "X-Device-Category",
                        "value": "mobile"
                    }
                },
                "holdbackPercentage": 0.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

**Example 4: Block all traffic except from specific domains with holdback**

The following example uses `EXCLUDE` filter type to keep only traffic from `trusted-publisher.com` or `premium-ads.com`, and returns a no-bid response for all other requests. A 5% holdback ensures that a small sample of excluded traffic still passes through for monitoring purposes:

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
    {
        "name": "openRtbAttributeModule",
        "version": "20251204-105817",
        "dependsOn": [],
        "moduleParameters": {
            "openRtbAttribute": {
                "filterType": "EXCLUDE",
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.site.domain",
                                "values": ["trusted-publisher.com", "premium-ads.com"]
                            }
                        ]
                    }
                ],
                "action": {
                    "noBid": {
                        "noBidReasonCode": 1
                    }
                },
                "holdbackPercentage": 5.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

### Configuring Multiple Modules
<a name="multiple-modules-example"></a>

The following example shows how to configure multiple modules on a single link using the AWS Command Line Interface (AWS CLI). In this example, the rate limiter module runs first to cap traffic at 1000 TPS, and then the OpenRTB attribute module filters COPPA-flagged requests from the remaining traffic:

**Configure multiple modules on a link**

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[
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
                "filterConfiguration": [
                    {
                        "criteria": [
                            {
                                "path": "$.regs.coppa",
                                "values": ["1"]
                            }
                        ]
                    }
                ],
                "action": {
                    "noBid": {
                        "noBidReasonCode": 1
                    }
                },
                "holdbackPercentage": 0.0
            }
        }
    }
]'}} \
--region {{us-east-1}}
```

### Viewing Module Configuration
<a name="viewing-modules"></a>

The following example shows how to retrieve the current module configuration for a link using the AWS Command Line Interface (AWS CLI).

**View module configuration for a link**

```
$ aws rtbfabric get-link \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--region {{us-east-1}}
```

The response includes:
+ `flowModules` - Currently active module configuration
+ `pendingFlowModules` - Module configuration pending activation (if any)

### Removing Modules
<a name="removing-modules"></a>

The following example shows how to remove all modules from a link using the AWS Command Line Interface (AWS CLI).

**Remove all modules from a link**

```
$ aws rtbfabric update-link-module-flow \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--modules {{'[]'}} \
--region {{us-east-1}}
```

## Troubleshooting
<a name="troubleshooting-modules"></a>

**Common Issues:**
+ **"Resource not ready to be used yet"** - Wait for gateways and links to reach `ACTIVE` status before configuring modules.
+ **Module configuration not applied** - Check the `pendingFlowModules` field in the link response to see if configuration is still being processed.
+ **Invalid module parameters** - Verify parameter names and value types match the module specification exactly.

The following example shows how to check link and module status using the AWS Command Line Interface (AWS CLI).

**Check link and module status**

```
$ aws rtbfabric get-link \
--gateway-id {{<gateway-id>}} \
--link-id {{<link-id>}} \
--query {{'{Active:flowModules,Pending:pendingFlowModules}'}} \
--region {{us-east-1}}
```