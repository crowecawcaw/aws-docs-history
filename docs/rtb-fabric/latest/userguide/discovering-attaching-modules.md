

# Discovering and attaching modules

Modules let you filter, enrich, or rate-limit the bid requests on a link before RTB Fabric forwards them. You can attach built-in modules, AWS Marketplace modules, and modules shared by vendors. This topic shows how to find modules and subscribe to them in AWS Marketplace, attach them to a link as a *flow*, and track each change.

**Topics**
+ [Finding modules that you can attach](#finding-modules)
+ [How flows work](#how-flows-work)
+ [Attaching modules to a link](#attaching-modules-putlinkflows)
+ [Tracking a flow update](#tracking-flow-updates)

## Finding modules that you can attach
<a name="finding-modules"></a>

Modules from vendors are sold through AWS Marketplace. To use one, subscribe to it, and then attach it to a link. Built-in modules come with RTB Fabric and don't need a subscription.

**To find and subscribe to a module in AWS Marketplace**

1. Open the [Discover modules page](https://console.aws.amazon.com/rtbfabric/discover-modules) of the RTB Fabric console. In the navigation pane, it's under **Module marketplace**.

1. Search by module name, vendor, or what the module does, or filter by category. To see what a module does, the actions it takes on bid requests, its pricing, and its terms, choose **View details**.

1. On the module's page, choose **View subscription options**, or **Try for free** if the module offers a free trial.

1. Review the offer's pricing and terms, and accept the offer. AWS Marketplace creates an agreement, and charges appear on your AWS bill.

Subscribing doesn't change your traffic. A module processes bid requests only after you add it to a link's flow. To see the modules that you can attach, under **Module marketplace**, choose **My modules**. **Source** shows whether each module is from AWS Marketplace or included with RTB Fabric. Built-in modules appear here, not in **Discover modules**.

You renew and cancel subscriptions in the AWS Marketplace console. To avoid interruptions to your traffic, renew an agreement or free trial before it ends, or replace the module in your flows. The console needs AWS Marketplace and AWS License Manager permissions in addition to RTB Fabric permissions. For more information, see [Using the RTB Fabric console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console).

To find modules with the API, use the following operations. They list only the modules and versions that you can attach. If you can't attach a module, the `Get` operations return `ResourceNotFoundException`, the same as for a module that doesn't exist.


| Operation | Returns | 
| --- | --- | 
| [ListAvailableModules](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListAvailableModules.html) | The modules that you can attach, newest first. To list one kind only, set subscriptionType to AWS\_BUILT\_IN, MARKETPLACE, or PRIVATE. | 
| [GetAvailableModule](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetAvailableModule.html) | One module, with its name, description, and how you have access to it. | 
| [ListAvailableModuleVersions](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListAvailableModuleVersions.html) | A module's ACTIVE and DEPRECATED versions, highest version first. You can attach only an ACTIVE version. | 
| [GetAvailableModuleVersion](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetAvailableModuleVersion.html) | One version, with the values that you need to attach it: its Amazon Resource Name (ARN), its configurableActions, and the configurationSchema for its parameters. | 

The following AWS Command Line Interface (AWS CLI) command lists the built-in modules.

```
$ aws rtbfabric list-available-modules \
--subscription-type AWS_BUILT_IN \
--region {{us-east-1}}
```

The following AWS CLI command gets a version of a module. In the AWS CLI, the version is the `--module-version` option, because `--version` is reserved for the AWS CLI itself.

```
$ aws rtbfabric get-available-module-version \
--module-id {{module-noBid}} \
--module-version {{1.0.0}} \
--region {{us-east-1}}
```

The built-in modules have the following module IDs and versions. A module version ARN has the form `arn:aws:rtbfabric:{{region}}::modules/{{module-id}}/versions/{{version}}`. These IDs and versions apply to `PutLinkFlows`. With `UpdateLinkModuleFlow`, `moduleParameters` selects the module.


| Module | Module ID and version | Parameters in `configurationValues` | 
| --- | --- | --- | 
| Rate Limiter Module | module-rateLimiter, 1.0.0 | tps (required): the maximum transactions per second, from 1 through 16,777,216. | 
| No-bid module | module-noBid, 1.0.0 | Optional reason (up to 50 letters and digits) and reasonCode (0 through 10). reason labels the module's log events and isn't returned in the response. With reasonCode, the response is HTTP 200 with the code as nbr. Without it, the response is HTTP 204 with no body. | 
| OpenRTB Attribute Module | module-openrtbAttributeFilter, 2.0.0 | filterType, filterConfiguration, and an optional action, as described in [OpenRTB Attribute Module](modules.md#openrtb-attribute-module-example). | 

## How flows work
<a name="how-flows-work"></a>

A flow sets which modules run on a link's bid requests, and in what order.

### Flows and pipelines
<a name="flows-pipelines"></a>

A link has at most one flow. Each flow has a name and a pipeline. In a `sequential` pipeline, modules run in order, and each module sees the previous module's output. In a `phased` pipeline, phases run in order, and the modules in a phase run at the same time on the same request. A response from any module, such as a no-bid, ends the flow. Put a module that depends on another module in a later phase.

### Replacing flows
<a name="replacing-flows"></a>

`PutLinkFlows` replaces all of the link's flows. To change one module, put the whole flow again with the change. To remove every module, put an empty list of flows. After you move a link to `PutLinkFlows`, stop using `UpdateLinkModuleFlow` on it, because it replaces the flows.

### Lock tokens
<a name="flow-lock-tokens"></a>

Each `PutLinkFlows` call needs the link's current `lockToken`, which `GetLink` and `GetInboundExternalLink` return. If the link changed after you read the token, the call fails with `ConflictException`. Read the link again, apply your change to the flows that it returns, and retry with the new `lockToken`.

### Asynchronous updates
<a name="flow-async-updates"></a>

A `PutLinkFlows` change applies asynchronously. The call returns `PENDING_UPDATE` and an `updateId`, and the link keeps serving its previous flows until the change is applied. While it rolls out, some requests can still run the previous flows. The link's status is then `ACTIVE` again, whether the change succeeded or failed. To find out which, use `GetUpdate`.

### Module settings
<a name="flow-module-settings"></a>

Each module in a flow has the following settings. The modules in a flow count against your Modules per flow quota, which is 2 by default. A request over the quota fails with `ServiceQuotaExceededException`.


| Setting | Description | 
| --- | --- | 
| name | Required. A name for the module that's unique within the flow. | 
| moduleVersionArn | Required. The ARN of an ACTIVE version that you can attach. | 
| selectedActions | The capabilities to turn on, from the version's configurableActions. Optional when the version has one configurable action, which is then turned on, or none. Required when a module from a vendor has more than one. A built-in module never requires it. | 
| failureMode | What happens when the module's call fails or times out. OPEN continues the flow, and CLOSED answers the request with a no-bid response. Modules from vendors default to OPEN. For a built-in module without this setting, an error ends the request. The Rate Limiter Module doesn't accept this setting. | 
| activationPercentage | The percentage of requests reaching the module that it runs on, from 0 through 100. Each request is sampled independently. The default is 100. The no-bid module requires this setting, and the Rate Limiter Module accepts only 100. | 
| configurationValues | The module's parameters, as a JSON string that matches the version's configurationSchema. | 

A module from a vendor that you attach with `ENRICH_REQUEST_EXT` adds its result to the bid request that it forwards, under `ext.rtbfabric.modules` and the module's `name` in the flow. It adds the entry only when it has data for the request. `outcome` is `ALLOW` or `DROP`, and `payload`, when present, holds the vendor's data for the request. The following example shows the entry for a module named `domainQuality`.

```
{
    "ext": {
        "rtbfabric": {
            "modules": {
                "domainQuality": {
                    "outcome": "ALLOW",
                    "payload": {
                        "tier": 2
                    }
                }
            }
        }
    }
}
```

### Rules for built-in modules
<a name="built-in-module-rules"></a>

The built-in modules also have these rules:
+ The no-bid module requires `activationPercentage`, which sets the share of requests that it answers with a no-bid response.
+ The Rate Limiter Module runs on every request. Don't set its `failureMode`, and leave `activationPercentage` unset or at 100.
+ If you set `selectedActions` for the OpenRTB Attribute Module, select `FILTER` when its action is `noBid`, or `ENRICH_REQUEST_HEADERS` when its action is `headerTag`. To run it on a share of requests, use `activationPercentage`. Its `configurationValues` don't accept `holdbackPercentage`. When you move from `UpdateLinkModuleFlow`, set `activationPercentage` to 100 minus `holdbackPercentage` instead.

## Attaching modules to a link
<a name="attaching-modules-putlinkflows"></a>

**To attach a module to a link in the console**

1. Open the [My modules page](https://console.aws.amazon.com/rtbfabric/my-modules) of the RTB Fabric console. In the navigation pane, it's under **Module marketplace**.

1. Select the module, and choose **Attach to link**.

1. For **Gateway type**, keep **Responder gateway**. Choose the gateway and the link, and choose **Configure flows**. Only active links are shown.

1. On the **Configure flow** page, in **Modules you can add**, choose the module's version, and choose **Copy snippet**.

1. Paste the snippet into the flow's modules list in **Flow configuration (JSON)**. Adjust its settings as the vendor's usage instructions describe, and choose **Submit**.

Submitting replaces the link's whole flow, so make all your changes before you submit. The update can take up to 30 minutes, and longer in some cases. Until then, the link serves its previous flow. To change a link's flow later, open the link, and on the **Flow** tab, choose **Configure flow**.

To attach modules to a link with the AWS CLI, complete the following steps. In the commands, replace the gateway ID, link ID, lock token, and update ID with your own values.

The following IAM policy allows these steps on one link. The four discovery operations, `GetUpdate`, and `ListUpdates` don't support resource-level permissions, so they need `"Resource": "*"`. A policy that names only link ARNs blocks them.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rtbfabric:ListAvailableModules",
                "rtbfabric:GetAvailableModule",
                "rtbfabric:ListAvailableModuleVersions",
                "rtbfabric:GetAvailableModuleVersion",
                "rtbfabric:GetUpdate",
                "rtbfabric:ListUpdates"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "rtbfabric:GetLink",
                "rtbfabric:PutLinkFlows"
            ],
            "Resource": "arn:aws:rtbfabric:{{us-east-1}}:{{111122223333}}:gateway/{{rtb-gw-abc123}}/link/{{link-xyz789}}"
        }
    ]
}
```

1. Get the link's current lock token.

   ```
   $ aws rtbfabric get-link \
   --gateway-id {{rtb-gw-abc123}} \
   --link-id {{link-xyz789}} \
   --query lockToken \
   --region {{us-east-1}}
   ```

1. Put the flow. The following command caps the link at 1,000 TPS, and then answers 10 percent of the remaining requests with a no-bid response.

   ```
   $ aws rtbfabric put-link-flows \
   --gateway-id {{rtb-gw-abc123}} \
   --link-id {{link-xyz789}} \
   --lock-token {{lock-token-from-step-1}} \
   --flows '[
       {
           "name": "main",
           "pipeline": {
               "sequential": {
                   "modules": [
                       {
                           "name": "RateLimit",
                           "moduleVersionArn": "arn:aws:rtbfabric:us-east-1::modules/module-rateLimiter/versions/1.0.0",
                           "configurationValues": "{\"tps\":1000}"
                       },
                       {
                           "name": "NoBidShare",
                           "moduleVersionArn": "arn:aws:rtbfabric:us-east-1::modules/module-noBid/versions/1.0.0",
                           "activationPercentage": 10
                       }
                   ]
               }
           }
       }
   ]' \
   --region {{us-east-1}}
   ```

   The response includes the link's status, `PENDING_UPDATE`, and the `updateId` of the change.

1. Use the `updateId` from step 2 to check the update. When its status is `SUCCESSFUL`, the link is `ACTIVE` and its `flows` show the modules that you put. When its status is `FAILED`, `errorDetails` gives the cause, the link returns to `ACTIVE`, and `GetLink` continues to show the previous flows.

   ```
   $ aws rtbfabric get-update \
   --gateway-id {{rtb-gw-abc123}} \
   --update-id {{update-1a2b3c4d5e6f}} \
   --region {{us-east-1}}
   ```

   To see the link's flows, get the link.

   ```
   $ aws rtbfabric get-link \
   --gateway-id {{rtb-gw-abc123}} \
   --link-id {{link-xyz789}} \
   --query '{status:status,flows:flows}' \
   --region {{us-east-1}}
   ```

The following AWS CLI command runs two modules from vendors at the same time, after the Rate Limiter Module. Both fail open, so if a module's call fails or times out, the flow continues without its result. The link's timeout still applies to the whole request. It needs a Modules per flow quota of at least 3. Replace each `moduleVersionArn` with one that `GetAvailableModuleVersion` returns in your Region.

```
$ aws rtbfabric put-link-flows \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--lock-token {{current-lock-token}} \
--flows '[
    {
        "name": "main",
        "pipeline": {
            "phased": {
                "phases": [
                    {
                        "modules": [
                            {
                                "name": "RateLimit",
                                "moduleVersionArn": "arn:aws:rtbfabric:us-east-1::modules/module-rateLimiter/versions/1.0.0",
                                "configurationValues": "{\"tps\":1000}"
                            }
                        ]
                    },
                    {
                        "modules": [
                            {
                                "name": "Fraud",
                                "moduleVersionArn": "{{arn:aws:rtbfabric:us-east-1::modules/module-0a1b2c3d4e5f/versions/1.0.0}}",
                                "failureMode": "OPEN"
                            },
                            {
                                "name": "Viewability",
                                "moduleVersionArn": "{{arn:aws:rtbfabric:us-east-1::modules/module-9f8e7d6c5b4a/versions/1.0.0}}",
                                "failureMode": "OPEN"
                            }
                        ]
                    }
                ]
            }
        }
    }
]' \
--region {{us-east-1}}
```

The following AWS CLI command removes every module from the link.

```
$ aws rtbfabric put-link-flows \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--lock-token {{current-lock-token}} \
--flows '[]' \
--region {{us-east-1}}
```

**Note**  
Use one API to manage a link's modules. If you attach modules with `PutLinkFlows`, don't change them with `UpdateLinkModuleFlow`, which can't express phases or activation percentages. After you move a link to `PutLinkFlows`, its module metrics use the dimensions `Link`, `FlowName`, `ModuleName`, `ModuleId`, and `ModuleVersion`. Update your alarms and dashboards.

## Tracking a flow update
<a name="tracking-flow-updates"></a>

Use the `updateId` that `PutLinkFlows` returns to follow the change with `GetUpdate`. Its status is `IN_PROGRESS`, `SUCCESSFUL`, or `FAILED`. A failed update includes `errorDetails` with the cause. If an update stays `IN_PROGRESS` and blocks further changes, contact AWS Support with the gateway ID, link ID, and `updateId`.

```
$ aws rtbfabric get-update \
--gateway-id {{rtb-gw-abc123}} \
--update-id {{update-1a2b3c4d5e6f}} \
--region {{us-east-1}}
```

To see a link's recent changes, use `ListUpdates`. RTB Fabric keeps updates for 90 days.

```
$ aws rtbfabric list-updates \
--gateway-id {{rtb-gw-abc123}} \
--link-id {{link-xyz789}} \
--region {{us-east-1}}
```