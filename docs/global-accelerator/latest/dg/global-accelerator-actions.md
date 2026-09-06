

# Common API actions for AWS Global Accelerator
<a name="global-accelerator-actions"></a>

This section lists common AWS Global Accelerator actions that you can use with Global Accelerator resources, with links to relevant documentation.

**Actions to use with standard accelerators**

The following table lists common Global Accelerator actions that you can use with standard accelerators, with links to relevant documentation.


| Action | Using the Global Accelerator Console | Using the Global Accelerator API | 
| --- | --- | --- | 
| Create a standard accelerator | See [Getting started with a standard accelerator](getting-started-standard.md) | See [`CreateAccelerator`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateAccelerator.html) | 
| Create a listener for a standard accelerator | See [Listeners for standard accelerators in AWS Global Accelerator](about-listeners.md) | See [`CreateListener`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateListener.html) | 
| Create an endpoint group for a standard accelerator | See [Endpoint groups for standard accelerators in AWS Global Accelerator](about-endpoint-groups.md) | See [`CreateEndpointGroup`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateEndpointGroup.html) | 
| Update a standard accelerator | See [Standard accelerators in AWS Global Accelerator](about-accelerators.md) | See [`UpdateAccelerator`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateAccelerator.html) | 
| Update an endpoint group | See [Add a standard endpoint group](about-endpoint-groups.create-endpoint-group.md) | See [`UpdateEndpointGroup`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html) | 
| Add an endpoint | See [Add a standard endpoint](about-endpoints-adding-endpoints.md) | See [`AddEndpoints`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AddEndpoints.html) | 
| Remove an endpoint | See [Add a standard endpoint](about-endpoints-adding-endpoints.md) | See [`RemoveEndpoints`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_RemoveEndpoints.html) | 
| List standard accelerators | See [View your accelerators](about-accelerators.viewing.md) | See [`ListAccelerators`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListAccelerators.html)  | 
| Get all information about an accelerator | See [View your accelerators](about-accelerators.viewing.md) | See [`DescribeAccelerator`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAccelerator.html) | 
| Delete an accelerator | See [Create accelerator](about-accelerators.creating-editing.md) | See [`DeleteAccelerator`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteAccelerator.html) | 

**Actions to use with custom routing accelerators**

The following table lists common Global Accelerator actions that you can use with custom routing accelerators, with links to relevant documentation.


| Action | Using the Global Accelerator Console | Using the Global Accelerator API | 
| --- | --- | --- | 
| Create a custom routing accelerator | See [Getting started with a custom routing accelerator](getting-started-custom-routing.md) | See [`CreateCustomRoutingAccelerator`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingAccelerator.html) | 
| Create a listener for a custom routing accelerator | See [Listeners for custom routing accelerators in Global Accelerator](about-custom-routing-listeners.md) | See [`CreateCustomRoutingListener`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingListener.html) | 
| Create an endpoint group for a custom routing accelerator | See [Endpoint groups for custom routing accelerators in Global Accelerator](about-custom-routing-endpoint-groups.md) | See [`CreateCustomRoutingEndpointGroup`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingEndpointGroup.html) | 
| Update a custom routing accelerator | See [Custom routing accelerators in AWS Global Accelerator](about-custom-routing-accelerators.md) | See [`UpdateCustomRoutingAccelerator`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCustomRoutingAccelerator.html) | 
| List your custom routing accelerators | See [View custom routing accelerators in Global Accelerator](about-custom-routing-accelerators.viewing.md) | See [`ListCustomRoutingAccelerators`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingAccelerators.html)  | 
| Get all information about a custom routing accelerator | See [View custom routing accelerators in Global Accelerator](about-custom-routing-accelerators.viewing.md) | See [`DescribeCustomRoutingAccelerator`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingAccelerator.html) | 
| Delete a custom routing accelerator | See [Create a custom routing accelerator in Global Accelerator](about-custom-routing-accelerators.creating-editing.md) | See [`DeleteCustomRoutingAccelerator`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCustomRoutingAccelerator.html) | 
| Get the static port mapping for a custom routing accelerator | N/A | See [`ListCustomRoutingPortMappings`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingPortMappings.html) | 
| Allow all destination traffic for a subnet in a custom routing accelerator | See [Add a VPC subnet endpoint for a custom routing accelerator](about-custom-routing-endpoints-adding-endpoints.md) | See [`AllowCustomRoutingTraffic`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html) | 
| Deny all destination traffic for a subnet in a custom routing accelerator | See [Add a VPC subnet endpoint for a custom routing accelerator](about-custom-routing-endpoints-adding-endpoints.md) | See [`DenyCustomRoutingTraffic`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DenyCustomRoutingTraffic.html) | 
| Allow traffic to specific destinations in a custom routing accelerator | See [Add a VPC subnet endpoint for a custom routing accelerator](about-custom-routing-endpoints-adding-endpoints.md) | See [`AllowCustomRoutingTraffic`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html) | 
| Deny traffic to specific destinations in a custom routing accelerator | See [Add a VPC subnet endpoint for a custom routing accelerator](about-custom-routing-endpoints-adding-endpoints.md) | See [`DenyCustomRoutingTraffic`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DenyCustomRoutingTraffic.html) | 

**Actions to use with cross-account support in Global Accelerator**

The following table lists common Global Accelerator actions that you can use with cross-account support in Global Accelerator, with links to relevant documentation.


| Action | Using the Global Accelerator Console | Using the Global Accelerator API | 
| --- | --- | --- | 
| Create a cross-account attachment | See [Create a cross-account attachment in AWS Global Accelerator](cross-account-resources.create-attachment.md) | See [`CreateCrossAccountAttachment`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCrossAccountAttachment.html) | 
| Delete a cross-account attachment | See [Create a cross-account attachment in AWS Global Accelerator](cross-account-resources.create-attachment.md) | See [`DeleteCrossAccountAttachment`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCrossAccountAttachment.html) | 
| Describe the information in a cross-account attachment | See [Identify your cross-account resources in Global Accelerator](cross-account-resources.identify-cross-account.md) | See [`DescribeCrossAccountAttachment`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCrossAccountAttachment.html) | 
| List cross-account attachments in an account | See [Identify your cross-account resources in Global Accelerator](cross-account-resources.identify-cross-account.md) | See [`ListCrossAccountAttachments`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCrossAccountAttachments.html) | 
| Update a cross-account attachment | See [Create a cross-account attachment in AWS Global Accelerator](cross-account-resources.create-attachment.md) | See [`UpdateCrossAccountAttachment`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCrossAccountAttachment.html) | 