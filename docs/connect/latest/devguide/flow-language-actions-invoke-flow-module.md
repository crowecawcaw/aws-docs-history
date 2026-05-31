# InvokeFlowModule

Invokes a flow module. _Flow modules_ are reusable sections of a
flow. You use them to extract repeatable logic across your flows, and create common
functions. For more information about flow modules, see [Flow modules for reusable
functions](../adminguide/contact-flow-modules.md "../adminguide/contact-flow-modules.md"), in the _Connect Customer Administrator Guide_.

## Parameter object

```
{
    "FlowModuleId": The flow module ID or flow module ARN to be invoked. May be defined statically or dynamically.
}
```

## Results and conditions

None.

## Errors

`NoMatchingError` if no other Error matches.

## Restrictions

This action is supported by all channels and only supports Inbound flow
types.

## Corresponding block in the UI

[Flow block: Invoke
module](../adminguide/invoke-module-block.md "../adminguide/invoke-module-block.md").
