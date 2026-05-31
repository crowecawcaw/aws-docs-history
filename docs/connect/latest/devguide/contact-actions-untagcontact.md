# UnTagContact

Removes a collection of tags on the current contact. With this type of operation,
either all tags are set or none are set.

You cannot remove system-defined tags. You can only remove already existing
user-defined tags from a contact.

## Parameter object

```
{
"TagKeys": [ an Object that holds the tag-keys for the tags to be removed.
     "Key1" Key(s) can only be set statically.
      ]
}
```

## Results and conditions

None.

## Errors

- NoMatchingError - if no other Error matches

## Restrictions

This action is supported across all the Connect Customer media channels.

This action can be used in flows of all types.

## Corresponding block in the UI

[Contact tags](../adminguide/contact-tags-block.md "../adminguide/contact-tags-block.md")
