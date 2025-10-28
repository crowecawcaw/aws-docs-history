# Other object in ASFF

In the AWS Security Finding Format (ASFF), the `Other` object specifies custom fields and values.
For more information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

By using the `Other` object, you can specify custom fields and values for a
resource. You can use the `Other` object for the following cases:

- The resource type does not have a corresponding `Details` object. To
  specify details for a resource, use the `Other` object.
- The `Details` object for the resource type does not include all the
  attributes that you want to specify. In this case, use the `Details`
  object for the resource type to specify available attributes. Use the
  `Other` object to specify attributes that are not in the
  type-specific `Details` object.
- The resource type is not one of the provided types. In this case, set
  `Resource.Type` to `Other` and use the `Other`
  object to specify the details.
  **Type:** Map of up to 50 key-value pairs

Each key-value pair must meet the following requirements.

- The key must contain fewer than 128 characters.
- The value must contain fewer than 1,024 characters.
