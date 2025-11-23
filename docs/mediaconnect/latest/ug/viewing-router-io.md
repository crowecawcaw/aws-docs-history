# Viewing router I/Os in MediaConnect

You can view your router inputs and outputs in the MediaConnect console. For each input and
output, you can see the status, connections, and monitoring details.

## Prerequisites

The following procedure assumes you have at least one router I/O in your
AWS account.

## Procedure

Follow these steps to view the router I/Os that are available in your
AWS account.

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router inputs**.
3. Review the list of your inputs, which shows basic information such as the
   following:

| Router inputs list fields | Field                                                                                                                                              | What it tells you |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Name                      | The name that you gave this router input.                                                                                                          |
| Region                    | Where this input is located.                                                                                                                       |
| Type                      | The type of router input.                                                                                                                          |
| State                     | The current status of this router input.<br>For more information, see [MediaConnect router I/O states](io-state-changes.md "io-state-changes.md"). |
| Routed outputs            | The number of outputs that are currently taking this input.                                                                                        |
| Time until maintenance    | The countdown that shows when the next scheduled maintenance starts<br>for this input.                                                             |

4. To see more information about a router input, select an input and choose
   **View details**.
5. Use these tabs to find specific information about the router input:

| Router input details tabs | Tab                                                                                                          | What you'll find here |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------- |
| Monitoring                | Live status information including properties, thumbnail data,<br>maintenance schedule countdown, and alerts. |
| Metrics                   | Performance data for this input.                                                                             |
| Assigned outputs          | The outputs which are currently taking this input.                                                           |
| Configuration             | The current settings for this input.                                                                         |
| Tags                      | The tags that are currently applied to this input.                                                           |

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router outputs**.
3. Review the list of your outputs, which shows basic information such as the
   following.

| Router outputs list fields | Field                                                                                                                                                                                                                                                                                         | Description |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Name                       | The name that you gave this output.                                                                                                                                                                                                                                                           |
| Region                     | Where this output is located.                                                                                                                                                                                                                                                                 |
| Type                       | The type of output.                                                                                                                                                                                                                                                                           |
| State                      | The current status of this output.                                                                                                                                                                                                                                                            |
| Routed state               | The current routing status of the output.<br>• **Routing** - The output is in the<br>process of connecting to an input, or disconnecting from an<br>input.<br>• **Routed** - The output is<br>currently taking an input.<br>• **Unrouted** - The output is not<br>currently taking any input. |
| Time until maintenance     | The countdown that shows when the next scheduled maintenance starts<br>for this input.                                                                                                                                                                                                        |

4. To see more information about a router output, select an output and choose
   **View details**.
5. Use these tabs to find specific information about the router output.

| Router output details tabs | Tab                                                                             | **What you'll find here** |
| -------------------------- | ------------------------------------------------------------------------------- | ------------------------- |
| Monitoring                 | Live status information for the output, including health metrics and<br>alerts. |
| Metrics                    | Performance data for this output.                                               |
| Assigned input             | The current status of the input that this output is taking.                     |
| Configuration              | Your output's settings, network details, and tags.                              |
| Tags                       | The tags that are currently assigned to this output.                            |

## Next steps

After reviewing your router inputs and outputs, you can perform the following
actions:

- [Starting a router I/O in MediaConnect](starting-router-io.md "starting-router-io.md")
- [Managing routes in MediaConnect](assigning-route.md "assigning-route.md")

## Additional resources

To view router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [ListRouterInputs](../api/API_ListRouterInputs.md "../api/API_ListRouterInputs.md")
- [ListRouterOutputs](../api/API_ListRouterOutputs.md "../api/API_ListRouterOutputs.md")
- [GetRouterInput](../api/API_GetRouterInput.md "../api/API_GetRouterInput.md")
- [GetRouterInputThumbnail](../api/API_GetRouterInputThumbnail.md "../api/API_GetRouterInputThumbnail.md")
- [GetRouterOutput](../api/API_GetRouterOutput.md "../api/API_GetRouterOutput.md")
- [BatchGetRouterInput](../api/API_BatchGetRouterInput.md "../api/API_BatchGetRouterInput.md")
- [BatchGetRouterOutput](../api/API_BatchGetRouterOutput.md "../api/API_BatchGetRouterOutput.md")

This includes information about how to use these operations and parameters in one of the
language-specific AWS SDKs.
