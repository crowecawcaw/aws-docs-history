

# Viewing router I/Os in MediaConnect
<a name="viewing-router-io"></a>

You can view your router inputs and outputs in the MediaConnect console. For each input and output, you can see the status, connections, and monitoring details.

## Prerequisites
<a name="viewing-router-io-prerequisites"></a>

The following procedure assumes you have at least one router I/O in your AWS account.

## Procedure
<a name="viewing-router-io-procedure"></a>

Follow these steps to view the router I/Os that are available in your AWS account.

### To view your router inputs
<a name="view-router-inputs-section"></a><a name="view-router-inputs-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Review the list of your inputs, which shows basic information such as the following:


**Router inputs list fields**  
<a name="router-inputs-list-table"></a>
<table>
<thead>
  <tr><th>Field</th><th>What it tells you</th></tr>
</thead>
<tbody>
  <tr><td>Name</td><td>The name that you gave this router input.</td></tr>
  <tr><td>Region</td><td>Where this input is located.</td></tr>
  <tr><td>Type</td><td>The type of router input.</td></tr>
  <tr><td>State</td><td>The current status of this router input. For more information, see <a href="io-state-changes.md">MediaConnect router I/O states</a>.</td></tr>
  <tr><td>Routed outputs</td><td>The number of outputs that are currently taking this input.</td></tr>
  <tr><td>Time until maintenance</td><td>The countdown that shows when the next scheduled maintenance starts for this input.</td></tr>
</tbody>
</table>


1. To see more information about a router input, select an input and choose **View details**.

1. Use these tabs to find specific information about the router input:


**Router input details tabs**  
<a name="router-input-details-tabs-table"></a>
<table>
<thead>
  <tr><th>Tab</th><th>What you'll find here</th></tr>
</thead>
<tbody>
  <tr><td>Monitoring</td><td>Live status information including properties, thumbnail data, maintenance schedule countdown, and alerts.</td></tr>
  <tr><td>Metrics</td><td>Performance data for this input.</td></tr>
  <tr><td>Assigned outputs</td><td>The outputs which are currently taking this input.</td></tr>
  <tr><td>Configuration</td><td>The current settings for this input.</td></tr>
  <tr><td>Tags</td><td>The tags that are currently applied to this input.</td></tr>
</tbody>
</table>


### To view your router outputs
<a name="view-router-outputs-section"></a><a name="view-router-outputs-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router outputs**.

1. Review the list of your outputs, which shows basic information such as the following.


**Router outputs list fields**  
<a name="router-outputs-list-table"></a>
<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Name</td><td>The name that you gave this output.</td></tr>
  <tr><td>Region</td><td>Where this output is located.</td></tr>
  <tr><td>Type</td><td>The type of output.</td></tr>
  <tr><td>State</td><td>The current status of this output. </td></tr>
  <tr><td>Routed state</td><td>The current routing status of the output.<ul><li> <b>Routing</b> - The output is in the process of connecting to an input, or disconnecting from an input. </li><li> <b>Routed</b> - The output is currently taking an input. </li><li> <b>Unrouted</b> - The output is not currently taking any input. </li></ul></td></tr>
  <tr><td>Time until maintenance</td><td>The countdown that shows when the next scheduled maintenance starts for this input.</td></tr>
</tbody>
</table>


1. To see more information about a router output, select an output and choose **View details**.

1. Use these tabs to find specific information about the router output.


**Router output details tabs**  
<a name="router-output-details-tabs-table"></a>
<table>
<thead>
  <tr><th>Tab</th><th><b>What you'll find here</b></th></tr>
</thead>
<tbody>
  <tr><td>Monitoring</td><td>Live status information for the output, including health metrics and alerts.</td></tr>
  <tr><td>Metrics</td><td>Performance data for this output.</td></tr>
  <tr><td>Assigned input</td><td>The current status of the input that this output is taking.</td></tr>
  <tr><td>Configuration</td><td>Your output's settings, network details, and tags.</td></tr>
  <tr><td>Tags</td><td>The tags that are currently assigned to this output.</td></tr>
</tbody>
</table>


## Next steps
<a name="viewing-router-io-next-steps"></a>

After reviewing your router inputs and outputs, you can perform the following actions:
+ [Starting a router I/O in MediaConnect](starting-router-io.md)
+ [Managing routes in MediaConnect](assigning-route.md)

## Additional resources
<a name="viewing-router-io-additional-resources"></a>

To view router I/Os programmatically, see the following pages in the *MediaConnect API Reference*:
+ [ListRouterInputs](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListRouterInputs.html)
+ [ListRouterOutputs](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListRouterOutputs.html)
+ [GetRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInput.html)
+ [GetRouterInputThumbnail](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInputThumbnail.html) 
+ [GetRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterOutput.html)
+ [BatchGetRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetRouterInput.html)
+ [BatchGetRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetRouterOutput.html)

This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.