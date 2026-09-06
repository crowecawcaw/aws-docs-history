

# CreateWisdomSession
<a name="createwisdomsession"></a>

Associates a Wisdom domain to a contact that is being executed in a Flow to enable real-time recommendations on the current contact.

## Parameter object
<a name="createwisdomsession-parameter"></a>

```
{
    "WisdomAssistantArn":  ARN for the Wisdom Assistant. May be specified statically or dynamically.
}
```

## Results and conditions
<a name="createwisdomsession-results"></a>

None. No conditions are supported.

## Errors
<a name="createwisdomsession-errors"></a>

NoMatchingError - if no other Error matches.

## Restrictions
<a name="createwisdomsession-restrictions"></a>

This action is only supported on the voice channel. This action can be used in all contact flow types.

## Corresponding block in the UI
<a name="createwisdomsession-ui"></a>

[Flow block: Amazon Q in Connect](https://docs.aws.amazon.com/connect/latest/adminguide/wisdom.html)