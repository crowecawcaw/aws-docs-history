# PatternMatch Operands

Each operand is an array of Pattern match objects.

## PatternMatch Object

###### Type

- Description: The type of the pattern match object.
- Type: String
- Valid values: `PLAIN` | `LIST` |
  `PROXIMITY` | `NUMERICAL`
- Required: Yes

###### Value

- Description: Depending on the type, value type varies.

  - If type is `PLAIN`, Value is a string.
  - If type is `LIST`, Value is an array of
    `PLAIN` PatternMatch object.
  - If type is `PROXIMITY`, Value is an object for
    format.

  ```
  {
    "Distance": number,
    "IsWithin": boolean
  }
  ```
  - If type is `NUMERICAL`, Value is an object for
    format.

  ```
  {
    "Decimal": boolean
  }
  ```
