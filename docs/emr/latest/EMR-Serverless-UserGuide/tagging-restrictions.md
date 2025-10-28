# Tagging limitations

The following basic limitations apply to tags:

- Each resource can have a maximum of 50 user-created tags.
- For each resource, each tag key must be unique, and each tag key can have only
  one value.
- The maximum key length is 128 Unicode characters in UTF-8.
- The maximum value length is 256 Unicode characters in UTF-8.
- Allowed characters are letters, numbers, spaces representable in UTF-8, and
  the following characters: \_ . : / = + - @.
- A tag key cannot be an empty string. A tag value can be an empty string, but
  not null.
- Tag keys and values are case sensitive.
- Do not use `AWS:` or any upper or lowercase combination of such
  as a prefix for either keys or values. These are reserved only for AWS
  use.
