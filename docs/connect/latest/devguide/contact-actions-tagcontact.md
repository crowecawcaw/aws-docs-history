# TagContact

Sets a collection of tag to the current contact. With this type of operation, either
all tags are set or none are set.

Each tag on a contact is a key-value pair, that is, it is composed of a key and a
value. There are two types of tags: user-defined tags and system tags. You create a
user-defined tag. A system tag is automatically created by AWS services.
A system tag is prefixed with `aws:`. You cannot change it.

The TagContact action parameters correspond to user-defined tags that are applied on a
contact.

## Parameter object

```
{
"Tags": { an Object that holds the tags to be set.
       "Key1":"Value1" Both the key and value may be defined statically or dynamically.
        }
}
```

## Results and conditions

None.

## Errors

None.

## Restrictions

None. This can be used in any type of flow and any channel.

## Corresponding block in the UI

[Contact tags](../adminguide/contact-tags-block.md "../adminguide/contact-tags-block.md")
