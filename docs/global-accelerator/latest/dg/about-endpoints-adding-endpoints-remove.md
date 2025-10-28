#

Remove a standard endpoint

This section explains how to remove an endpoint on the AWS Global Accelerator console. If you want to
use API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

You can remove endpoints from your endpoint groups, for example, if you need to service your
endpoints. Removing an endpoint takes it out of the endpoint group, so that it no longer
receives traffic through Global Accelerator, but does not affect the
endpoint otherwise. Global Accelerator stops directing traffic to an endpoint as soon as you remove it from an
endpoint group. The endpoint goes into a state where it waits for all current requests to be completed
so there's no interruption for client traffic that is in progress. You can add the endpoint back to the
endpoint group when you’re ready for it to resume receiving requests.

Note: Before you terminate or delete a resource that you've added as an endpoint behind an accelerator, we recommend
that you remove the endpoint from Global Accelerator endpoint groups.

###### Warning

Removing an endpoint immediately stops new connections from being routed to it
through Global Accelerator. If the endpoint is the only healthy target receiving traffic for your
application, or all other endpoints have a weight of 0, when you remove the endpoint,
the endpoint group (Region) might become unavailable. Before you remove an endpoint,
verify that alternate healthy endpoints exist and are receiving traffic as expected.

# To remove an endpoint

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. On the **accelerators** page, choose an accelerator.
3. In the **Listeners** section, for **Listener ID**,
   choose the ID of a listener.
4. In the **Endpoint groups** section, for **Endpoint group
   ID**, choose the ID of the endpoint group.
5. Choose **Remove endpoint**.
6. In the confirmation dialog box, choose **Remove**.
