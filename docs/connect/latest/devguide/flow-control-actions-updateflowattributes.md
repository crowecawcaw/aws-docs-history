

# UpdateFlowAttributes
<a name="flow-control-actions-updateflowattributes"></a>

Sets a collection of attributes on the current flow. These attributes are not carried over to the subsequent flows. With this type of operation, either all attributes are set or none are set.

To set attributes that are available to every flow that runs on the current contact, use `PersistedFlowAttributes` instead of `FlowAttributes`. Persisted flow attributes are only available in [Amazon Connect Customer instances](https://docs.aws.amazon.com/connect/latest/adminguide/enable-nextgeneration-amazonconnect.html).

## Parameter object
<a name="updateflowattributes-parameter"></a>

```
{
    "FlowAttributes": { An Object that holds the attributes to be set. Keys are of type String, Values are of type FlowAttribute.
        "attribute-name": {
            "Value": "String"
        }
    },
    "PersistedFlowAttributes": { An Object that holds the attributes to be set on the current contact, instead of FlowAttributes. Keys are of type String, Values are of type FlowAttribute.
        "attribute-name": {
            "Value": "String"
        }
    }
}
```

Example that sets a flow attribute:

```
{
  "FlowAttributes": {
    "CardLastFour": { "Value": "$.External.lastFour" }
  }
}
```

Example that sets a persisted flow attribute:

```
{
  "PersistedFlowAttributes": {
    "VerificationResult": { "Value": "$.External.verified" }
  }
}
```

## Results and conditions
<a name="updateflowattributes-results"></a>

None. No conditions are supported.

## Errors
<a name="updateflowattributes-errors"></a>
+ NoMatchingError - if the attributes couldn't be set. For example, the attributes would exceed the size limit (64 KB for flow attributes, 128 KB per contact for persisted flow attributes), or persisted flow attributes couldn't be saved. When this error occurs, no attributes are set and existing persisted flow attributes are left unchanged. To resolve it, reduce the number or size of the attributes.

## Restrictions
<a name="updateflowloggingbehavior-restrictions"></a>

This action is supported on all channels and in all flow types. `PersistedFlowAttributes` is only available in [Amazon Connect Customer instances](https://docs.aws.amazon.com/connect/latest/adminguide/enable-nextgeneration-amazonconnect.html).

## Corresponding block in the UI
<a name="updateflowloggingbehavior-ui"></a>

[Set contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/set-contact-attributes.html) 