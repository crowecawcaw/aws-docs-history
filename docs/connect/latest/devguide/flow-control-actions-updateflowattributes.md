# UpdateFlowAttributes

Sets a collection of attributes on the current flow. These attributes are not carried
over to the subsequent flows. With this type of operation, either all attributes are set
or none are set.

## Parameter object

```
{
    ""FlowAttributes": { An Object that holds the attributes to be set. Keys are of type String, Values are of type FlowAttribute
        "Type": {
            FlowAttribute" : "Value"
        }
    }
}
```

## Results and conditions

None. No conditions are supported.

## Errors

None.

## Restrictions

This action is supported on all channels and in all flow types.

## Corresponding block in the UI

[Set contact
attributes](../adminguide/set-contact-attributes.md "../adminguide/set-contact-attributes.md")
