# CreateWisdomSession

Associates a Wisdom domain to a contact that is being executed in a Flow to enable
real-time recommendations on the current contact.

## Parameter object

```
{
    "WisdomAssistantArn":  ARN for the Wisdom Assistant. May be specified statically or dynamically.
}
```

## Results and conditions

None. No conditions are supported.

## Errors

NoMatchingError - if no other Error matches.

## Restrictions

This action is only supported on the voice channel. This action can be used in all
contact flow types.

## Corresponding block in the UI

[Flow
block: Amazon Q in Connect](../adminguide/wisdom.md "../adminguide/wisdom.md")
