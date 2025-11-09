# Flow block in Amazon Connect: Invoke a published

module

This topic defines the flow block for calling a published module to create reusable
sections in a flow.

## Description

Calls a published module, which enables you create reusable sections of a contact
flow.

For more information, see [Flow modules for reusable functions in Amazon Connect](contact-flow-modules.md "contact-flow-modules.md").

## Supported channels

The following table lists how this block routes a contact who is using the
specified channel.

| Channel | Supported? |
| ------- | ---------- |
| Voice   | Yes        |
| Chat    | Yes        |
| Task    | Yes        |
| Email   | Yes        |

## Flow types

You can use this block in the following [flow
types](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types"):

- Inbound flow

## Properties

The following image shows the **Properties** page of the
**Invoke module** block.

![The properties page of the Invoke module block.](images/invoke-module-properties.png)

## Configured block

The following image shows an example of what this block looks like when it is
configured. It has two branches: **Success** and
**Error**.

![A configured Invoke module block.](images/invoke-module-configured.png)
