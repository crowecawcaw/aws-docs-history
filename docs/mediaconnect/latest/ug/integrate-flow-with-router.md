# Integrating router

I/Os with MediaConnect
flows

You can integrate your AWS Elemental MediaConnect flows with your router I/Os to extend your media workflow
capabilities. This enables you to combine the flexibility of the router with the distribution
features of flows.

You can connect your flows to your router setup in two ways:

1. **Use a flow as a source for a router input**

When you connect a flow to a router input, you can incorporate existing flow
workflows into your routing setup. This is useful when you want to:

    * Route content from existing flows through the router matrix
    * Combine flow and router capabilities in the same workflow
    * Maintain existing flow setups while adding routing capabilities

2. **Use a flow as a destination for a router output**

When you connect a router output to a flow, you can use your flow as a distribution
amplifier for your routed content. This setup is useful when you want to:

    * Distribute router output to multiple destinations
    * Enable cross-account access through flow entitlements
    * Send content to AWS Elemental MediaLive using managed outputs

## Prerequisites

Before you start, review these important considerations:

- **For connections between router inputs and flows**
  - The router inputs and flow outputs must be in the same availability zone and AWS Region.
  - A flow output can connect to one router input at a time. To switch connections,
    disconnect the flow output first.
  - You can't delete connected resources. You must disconnect the flow from the
    router input before you can delete either resource.

- **For connections between router outputs and flows**
  - If the flow has two sources, both sources must be connected to the router output.
  - A router output can connect to one flow at a time.
  - You can connect two router outputs to two flow sources on the same flow and
    perform fail over between them.
  - Only failover is supported between flow sources. Merge is not supported.
  - You can't delete connected resources. You must disconnect the flow from the
    router output before you can delete either resource.
  - When switching the content being routed to a connected flow source, we
    recommend using the **Take Router Input** operation
    on the connected router output. This performs a faster and cleaner switch than
    changing the router output directly, which can potentially cause brief video
    interruptions.

## Procedure

###### To connect a flow output to a router input

1. [Add an output](outputs-add.md "outputs-add.md") to your flow, making sure that
   the flow output has **Router integration** enabled.
2. [Create](creating-router-io.md "creating-router-io.md") or [update](editing-router-io.md "editing-router-io.md") a router input with the following
   settings:
   - Choose **Flow** as the configuration type
   - Specify the desired flow output from step 1

3. [Start the flow](flows-start.md "flows-start.md").
4. [Start the router input](starting-router-io.md "starting-router-io.md").
   When the router input and the flow are running, and the router input is assigned to an active router output, the stream is forwarded from the flow through the router.

###### To connect a router output to a flow source

1. [Create](outputs-add.md "outputs-add.md") or [update](flows-update.md "flows-update.md") a flow, making sure that the flow soure has **Router
   integration** enabled.
2. [Create](creating-router-io.md "creating-router-io.md") or [update](editing-router-io.md "editing-router-io.md") a router input with the following
   settings:
   - Choose **Flow** as the configuration type
   - Specify the desired flow source from step 1

3. [Start the flow](flows-start.md "flows-start.md").
4. [Start the router output](starting-router-io.md "starting-router-io.md").
   When the router output and the flow are running, and the router output is taking an active router input, the stream is forwarded through the router to the flow.

## Additional resources

Connection management is focused on the router. You use the router API operations to
select a flow output to feed into your router input, or a flow source to receive content
from your router output.

To connect flows to router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [CreateRouterInput](../api/API_CreateRouterInput.md "../api/API_CreateRouterInput.md")
- [CreateRouterOutput](../api/API_CreateRouterOutput.md "../api/API_CreateRouterOutput.md")
- [UpdateRouterInput](../api/API_UpdateRouterInput.md "../api/API_UpdateRouterInput.md")
- [UpdateRouterOutput](../api/API_UpdateRouterOutput.md "../api/API_UpdateRouterOutput.md")

This includes information about how to use thesee operations and parameters in one of the
language-specific AWS SDKs.
