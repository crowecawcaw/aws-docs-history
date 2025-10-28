# Looking Up Resources That Are Discovered

by AWS Config

You can use the AWS Config console, AWS CLI, and AWS Config API to look up the resources that AWS Config has
taken an inventory of, or _discovered_, including deleted resources and
resources that AWS Config is not currently recording. AWS Config discovers supported resource types
only. For more information, see [Supported Resource Types for AWS Config](resource-config-reference.md "resource-config-reference.md").

Looking Up Resources (Console)You can use resource types or tag information to look up resources in the AWS Config
console.

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. On the **Resource inventory** page, specify the search options for the
   resources that you want to look up:
   - **Resource category** – Choose all resource
     categories or narrow results to only AWS Resources.
   - **Resource type** – Choose all resource types
     or select which resource(s) to filter by.
   - **Compliance** – Choose to filter by any
     compliance status, compliant, or noncompliant.

3. AWS Config lists the resources that match your search options. You can see the
   following information about the resources:
   - **Resource identifier** – The resource
     identifier might be a resource ID or a resource name, if applicable.
     Choose the resource identifier link to view the resource details page.
   - **Resource type** – The type of the resource
     is listed.
   - **Compliance** – The status of the resource
     that AWS Config evaluated against your rule.

Looking Up Resources
(AWS CLI)
You can use the AWS CLI to list resources that AWS Config has discovered.

Use the **AWS Configservice
[`list-discovered-resources`](../../../cli/latest/reference/configservice/list-discovered-resources.md "../../../cli/latest/reference/configservice/list-discovered-resources.md")** command:

```
$ **aws configservice list-discovered-resources --resource-type "AWS::EC2::Instance"**
        {
            "resourceIdentifiers": [
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-`nnnnnnnn`"
                }
            ]
        }
```

To view the configuration details of a resource that is listed in the response, use
the [`get-resource-config-history`](../../../cli/latest/reference/configservice/get-resource-config-history.md "../../../cli/latest/reference/configservice/get-resource-config-history.md") command, and specify the resource type
and ID. For an example of this command and the response from AWS Config, see [Viewing Configuration History](view-manage-resource-console.md#get-config-history-cli "view-manage-resource-console.md#get-config-history-cli").

Looking up Resources (API)
You specify a resource type, and AWS Config returns a list of resource identifiers for
resources of that type. For more information, see [ResourceIdentifier](../APIReference/API_ResourceIdentifier.md "../APIReference/API_ResourceIdentifier.md")
in the _AWS Config API Reference_.

Use the [ListDiscoveredResources](../APIReference/API_ListDiscoveredResources.md "../APIReference/API_ListDiscoveredResources.md") action.

To get the configuration details of a resource that is listed in the response, use the
[GetResourceConfigHistory](../APIReference/API_GetResourceConfigHistory.md "../APIReference/API_GetResourceConfigHistory.md") action, and specify the resource type and
ID.
