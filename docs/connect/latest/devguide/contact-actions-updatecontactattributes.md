

# UpdateContactAttributes
<a name="contact-actions-updatecontactattributes"></a>

Sets a collection of contact attributes on either the current contact or the related contact. With this type of operation, either all attributes are set or none are set.

## Parameter object
<a name="updatecontactattributes-parameter"></a>

```
{
    "Attributes": { an Object that holds the attributes to be set. 
        "Key": "Value" Both the key and value may be defined statically or dynamically.
    },
    "TargetContact": either "Current" or "Related". Must be defined statically.
}
```

## Results and conditions
<a name="updatecontactattributes-results"></a>

None.

## Errors
<a name="updatecontactattributes-errors"></a>
+ NoMatchingError - if no other Error matches.

## Restrictions
<a name="updatecontactattributes-restrictions"></a>

None. This can be used in any type of flow and any channel. 

## Corresponding block in the UI
<a name="updatecontactattributes-ui"></a>

[Set contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/set-contact-attributes.html) 