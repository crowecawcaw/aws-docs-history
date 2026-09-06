

# InvokeFlowModule
<a name="flow-language-actions-invoke-flow-module"></a>

Invokes a flow module. *Flow modules* are reusable sections of a flow. You use them to extract repeatable logic across your flows, and create common functions. For more information about flow modules, see [Flow modules for reusable functions](https://docs.aws.amazon.com/connect/latest/adminguide/contact-flow-modules.html), in the *Connect Customer Administrator Guide*. 

## Parameter object
<a name="invoke-flow-module-parameter-object"></a>

```
{
    "FlowModuleId": The flow module ID or flow module ARN to be invoked. May be defined statically or dynamically.
}
```

## Results and conditions
<a name="invoke-flow-module-results-conditions"></a>

None.

## Errors
<a name="invoke-flow-module-errors"></a>

`NoMatchingError` if no other Error matches.

## Restrictions
<a name="invoke-flow-module-restrictions"></a>

This action is supported by all channels and only supports Inbound flow types.

## Corresponding block in the UI
<a name="invoke-flow-module-ui-block"></a>

[Flow block: Invoke module](https://docs.aws.amazon.com/connect/latest/adminguide/invoke-module-block.html).