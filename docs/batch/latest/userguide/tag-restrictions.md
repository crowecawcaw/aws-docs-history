# Tag restrictions

The following basic restrictions apply to tags:

- Maximum number of tags per resource – 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length – 128 Unicode characters in UTF-8
- Maximum value length – 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple AWS services and resources, remember that other services may
  have restrictions on allowed characters. Generally allowed characters are letters, numbers, spaces representable in
  UTF-8, and the following characters: + - = . \_ : / @.
- Tag keys and values are case sensitive.
- Don't use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for
  either keys or values, as it is reserved for AWS use. You can't edit or delete tag keys or values with this
  prefix. Tags with this prefix do not count against your tags-per-resource limit.
