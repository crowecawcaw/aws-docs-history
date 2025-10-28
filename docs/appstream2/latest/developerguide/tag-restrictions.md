# Tag Restrictions for Amazon AppStream 2.0

- The maximum number of tags per AppStream 2.0 resource is 50.
- The maximum key length is 128 Unicode characters in UTF-8.
- The maximum value length is 256 Unicode characters in UTF-8.
- Tag keys and values are case-sensitive.
- Do not use the "aws:" prefix in your tag names or values because it is a system tag that is reserved for AWS use. You cannot edit or delete tag names or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
- Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the
  following special characters: + - = . \_ : / @.
- Although you can share the same key and value across multiple resources, you cannot have duplicate keys on the same resource.
- You can add tags for resources during resource creation. You can also add,
  edit, and delete tags for resources that are already created.
