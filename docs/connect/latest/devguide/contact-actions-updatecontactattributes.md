# UpdateContactAttributes

Sets a collection of contact attributes on either the current contact or the related
contact. With this type of operation, either all attributes are set or none are
set.

## Parameter object

```

{
    "Attributes": { an Object that holds the attributes to be set.
        "Key": "Value" Both the key and value may be defined statically or dynamically.
    },
    "TargetContact": either "Current" or "Related". Must be defined statically.
}

```

## Results and conditions

None.

## Errors

- NoMatchingError - if no other Error matches.

## Restrictions

None. This can be used in any type of flow and any channel.

## Corresponding block in the UI

[Set contact
attributes](../adminguide/set-contact-attributes.md "../adminguide/set-contact-attributes.md")
