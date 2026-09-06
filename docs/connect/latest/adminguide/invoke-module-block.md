

# Flow block in Connect Customer: Invoke a published module
<a name="invoke-module-block"></a>

This topic defines the flow block for calling a published module to create reusable sections in a flow.

## Description
<a name="invoke-module-block-description"></a>

Calls a published module, which you can use to create reusable sections of a contact flow.

For more information, see [Flow modules for reusable functions in Connect Customer](contact-flow-modules.md).

## Supported channels
<a name="invoke-module-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes | 
| Chat | Yes | 
| Task | Yes | 
| Email | Yes | 

## Flow types
<a name="invoke-module-block-types"></a>

You can use this block across all [flow types](create-contact-flow.md#contact-flow-types). If your module contains blocks that are not supported by the specific flow type, this incompatibility might cause interruptions in the flow execution.

## Properties
<a name="invoke-module-block-properties"></a>

The following image shows the **Properties** page of the **Invoke module** block.

![The properties page of the Invoke module block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/invoke-module-properties.png)


## Configured block
<a name="invoke-module-block-configured"></a>

The following image shows an example of what this block looks like when it is configured. It has two branches: **Success** and **Error**.

![A configured Invoke module block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/invoke-module-configured.png)
