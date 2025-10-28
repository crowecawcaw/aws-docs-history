# Building and using type definitions in capability schema documents

All elements in the schemas resolve to type definitions. These type definitions are either _primitive type definitions_ (such as booleans, strings, numbers) or
_namespaced type definitions_ (type definitions built from primitive type definitions for convenience).

When you define a custom schema, you can use both primitive definitions and namespace type definitions.

###### Contents

- [Primitive type definitions](type-definitions.md#primitive-type-definitions "type-definitions.md#primitive-type-definitions")
  - [Booleans](type-definitions.md#boolean-types "type-definitions.md#boolean-types")
  - [Integer type support](type-definitions.md#integers-support "type-definitions.md#integers-support")
  - [Numbers](type-definitions.md#numbers "type-definitions.md#numbers")
  - [Strings](type-definitions.md#strings "type-definitions.md#strings")
  - [Nulls](type-definitions.md#nulls "type-definitions.md#nulls")
  - [Arrays](type-definitions.md#arrays "type-definitions.md#arrays")
  - [Objects](type-definitions.md#objects "type-definitions.md#objects")

- [Namespaced type definitions](type-definitions.md#namespaced-type-definitions "type-definitions.md#namespaced-type-definitions")
  - [matter types](type-definitions.md#matter-types "type-definitions.md#matter-types")
  - [aws types](type-definitions.md#aws-types "type-definitions.md#aws-types")
    - [Bitmap type definition](type-definitions.md#bitmap-type-definition "type-definitions.md#bitmap-type-definition")
    - [Enum type definition](type-definitions.md#enum-type-definition "type-definitions.md#enum-type-definition")

## Primitive type definitions

Primitive type definitions are the building blocks for all type definitions defined in managed integrations. All namespace definitions, including custom type definitions,
resolve to a primitive type definition either through the `$ref` keyword or the `type` keyword.

All primitive types are nullable by using the `nullable` keyword, and you can identify all primitive types by using the `type` keyword.

### Booleans

Boolean types support default values.

Sample definition:

```
{
    "type" : "boolean",
    "default" : "false",
    "nullable" : true
}
```

### Integer type support

Integer types support the following:

- `default` values
- `maximum` values
- `minimum` values
- `exclusiveMaximum` values
- `exclusiveMinimum` values
- `multipleOf` values

If `x` is the value being validated, the following must be true:

- `x` ≥ `minimum`
- `x` > `exclusiveMinimum`
- `x` < `exclusiveMaximum`

###### Note

Numbers with a zero fractional part are considered integers, but floating point numbers are rejected.

```
1.0 // Schema-Compliant
3.1415926 // NOT Schema-Compliant
```

While you can specify both `minimum` and `exclusiveMinimum` or both `maximum` and `exclusiveMaximum`, we don't recommend using both simultaneously.

Sample definitions:

```
{
    "type" : "integer",
    "default" : 2,
    "nullable" : true,
    "maximum" : 10,
    "minimum" : 0,
    "multipleOf": 2
}
```

Alternative definition:

```
{
    "type" : "integer",
    "default" : 2,
    "nullable" : true,
    "exclusiveMaximum" : 11,
    "exclusiveMinimum" : -1,
    "multipleOf": 2
}
```

### Numbers

Use the number type for any numeric type, including integers and floating point numbers.

Number types support the following:

- `default` values
- `maximum` values
- `minimum` values
- `exclusiveMaximum` values
- `exclusiveMinimum` values
- `multipleOf` values. The multiple can be a floating point number.

If `x` is the value being validated, the following must be true:

- `x` ≥ `minimum`
- `x` > `exclusiveMinimum`
- `x` < `exclusiveMaximum`

While you can specify both `minimum` and `exclusiveMinimum` or both `maximum` and `exclusiveMaximum`, we don't recommend using both simultaneously.

Sample definitions:

```
{
    "type" : "number",
    "default" : 0.4,
    "nullable" : true,
    "maximum" : 10.2,
    "minimum" : 0.2,
    "multipleOf": 0.2
}
```

Alternative definition:

```
{
    "type" : "number",
    "default" : 0.4,
    "nullable" : true,
    "exclusiveMaximum" : 10.2,
    "exclusiveMinimum" : 0.2,
    "multipleOf": 0.2
}
```

### Strings

String types support the following:

- `default` values
- length constraints (must be non-negative numbers) including `maxLength` and `minLength` values
- `pattern` values for regular expressions

When you define regular expressions, the string is valid if the expression matches anywhere within the string. For example, the
regular expression `p` matches any string containing a p, such as "apple", not just the string "p". For clarity, we recommend
surrounding regular expressions with `^...$` (for example, `^p$`), unless you have a specific reason not to do so.

Sample definition:

```
{
    "type" : "string",
    "default" : "defaultString",
    "nullable" : true,
    "maxLength": 10,
    "minLength": 1,
    "pattern" : "^([0-9a-fA-F]{2})+$"
}
```

### Nulls

Null types accept only a single value: `null`.

Sample definition:

```
{ "type": "null" }
```

### Arrays

Array types support the following:

- `default` — a list that will be used as the default value.
- `items` — JSON type definition imposed on all of the array elements.
- Length constraints (must be a non-negative number)
  - `minItems`
  - `maxItems`

- `pattern` values for Regex
- `uniqueItems` — a boolean indicating if the elements in the array need to be unique
- `prefixItems` — an array where each item is a schema that corresponds to each index of the document's array.
  That is, an array where the first element validates the first element of the input array, the second element validates the second element of the input array, and so on.

Sample definition:

```
{
   "type": "array",
   "default": ["1", "2"],
   "items" : {
        "type": "string",
        "pattern": "^([a-zA-Z0-9_ -/]+)$"
    },
    "minItems" : 1,
    "maxItems": 4,
    "uniqueItems" : true,
}
```

Examples of array validation:

```
//Examples:
["1", "2", "3", "4"] // Schema-Compliant
[]                   // NOT Schema-Compliant: minItems=1
["1", "1"]           // NOT Schema-Compliant: uniqueItems=true
["{"]                // NOT Schema-Compliant: Does not match the RegEx pattern.
```

Alternative definition using tuple validation:

```
{
    "type": "array",
    "prefixItems": [
        { "type": "number" },
        { "type": "string" },
        { "enum": ["Street", "Avenue", "Boulevard"] },
        { "enum": ["NW", "NE", "SW", "SE"] }
    ]
}

//Examples:
[1600, "Pennsylvania", "Avenue", "NW"]               // Schema-Compliant

// And, by default, it's also okay to add additional items to end:
[1600, "Pennsylvania", "Avenue", "NW", "Washington"] // Schema-Compliant
```

### Objects

Object types support the following:

- Property constraints
  - `properties` — Define the properties (key-value pairs) of an object by using the `properties`keyword.
    The value of `properties` is an object, where each key is the name of a property and each value is a schema used to validate that property.
    Any property that doesn't match any of the property names in the `properties` keyword is ignored by this keyword.
  - `required` — By default, the properties defined by the `properties` keyword are not required.
    However, you can provide a list of required properties using the `required` keyword. The `required` keyword takes an
    array of zero or more strings. Each of these strings must be unique.
  - `propertyNames` — This keyword allows control over the RegEx pattern for property names. For example, you might want to enforce that
    all properties of an object have names following a specific convention.
  - `patternProperties` — This maps regular expressions to schemas. If a property name matches the given regular expression, the property value must validate against the
    corresponding schema. For example, use `patternProperties` to specify that a value should match a particular schema, given a particular kind of property name.
  - `additionalProperties` — This keyword controls how extra properties are handled.
    Extra properties are properties whose names are not listed in the properties keyword or that match any of the regular expressions in `patternProperties`. By default,
    additional properties are allowed. Setting this field to `false` means that no additional properties are allowed.
  - `unevaluatedProperties` — This keyword is similar to `additionalProperties` except that it can recognize properties declared in subschemas.
    `unevaluatedProperties` works by collecting any properties that are successfully validated when processing the schemas and using those as the allowed list of properties.
    This allows you to do more complex things such as conditionally adding properties. Refer to the example below for more details.

- `anyOf` — This keyword's value MUST be a non-empty array. Each item of the array MUST be a valid JSON Schema. An instance
  validates successfully against this keyword if it validates successfully against _at least_ one schema defined by this keyword's value.
- `oneOf` — This keyword's value MUST be a non-empty array. Each item of the array MUST be a valid JSON Schema. An instance
  validates successfully against this keyword if it validates successfully against _exactly_ one schema defined by this keyword's value.

Example of required:

```
{
  "type": "object",
  "required": ["test"]
}

// Schema Compliant
{
  "test": 4
}

// NOT Schema Compliant
{}
```

PropertyNames example:

```
{
  "type": "object",
  "propertyNames": {
    "pattern": "^[A-Za-z_][A-Za-z0-9_]*$"
  }
}

// Schema Compliant
{
  "_a_valid_property_name_001": "value"
}

// NOT Schema Compliant
{
  "001 invalid": "value"
}
```

PatternProperties example:

```
{
  "type": "object",
  "patternProperties": {
    "^S_": { "type": "string" },
    "^I_": { "type": "integer" }
  }
}

// Schema Compliant
{ "S_25": "This is a string" }
{ "I_0": 42 }

// NOT Schema Compliant
{ "S_0": 42 } // Value must be a string
{ "I_42": "This is a string" } // Value must be an integer
```

AdditionalProperties example:

```
{
  "type": "object",
  "properties": {
    "test": {
        "type": "string"
    }
  },
  "additionalProperties": false
}

// Schema Compliant
{
  "test": "value"
}
OR
{}

// NOT Schema Compliant
{
    "notAllowed": false
}
```

UnevaluatedProperties example:

```
{
  "type": "object",
  "properties": {
    "standard_field": { "type": "string" }
  },
  "patternProperties": {
    "^@": { "type": "integer" } // Allows properties starting with '@'
  },
  "unevaluatedProperties": false // No other properties allowed
}

// Schema Compliant
{
  "standard_field": "some value",
  "@id": 123,
  "@timestamp": 1678886400
}
// This passes because "standard_field" is evaluated by properties,
// "@id" and "@timestamp" are evaluated by patternProperties,
// and no other properties remain unevaluated.

// NOT Schema Compliant
{
  "standard_field": "some value",
  "another_field": "unallowed"
}
// This fails because "another_field" is unevaluated and doesn't match
// the @ pattern, leading to a violation of unevaluatedProperties: false
```

AnyOf example:

```
{
  "anyOf": [
    { "type": "string", "maxLength": 5 },
    { "type": "number", "minimum": 0 }
  ]
}

// Schema Compliant
"short"
12

// NOT Schema Compliant
"too long"
-5
```

OneOf example:

```
{
  "oneOf": [
    { "type": "number", "multipleOf": 5 },
    { "type": "number", "multipleOf": 3 }
  ]
}

// Schema Compliant
10
9

// NOT Schema compliant
2  // Not a multiple of either 5 or 3
15 // Multiple of both 5 and 3 is rejected.
```

## Namespaced type definitions

Namespaced type definitions are types built from primitive types. These types must follow the format ``namespace`.`typename`.`
 Managed integrations provides predefined types under the`aws`and`matter`namespaces. You can use any namespace for custom types except the reserved`aws`and`matter` namespaces.

To find available namespaced type definitions, use the [ListSchemaVersions](../APIReference/API_ListSchemaVersions.md "../APIReference/API_ListSchemaVersions.md")
API with the `Type` filter set to `definition`.

### `matter` types

Find data types under the `matter` namespace using the [ListSchemaVersions](../APIReference/API_ListSchemaVersions.md "../APIReference/API_ListSchemaVersions.md") API with the
`Namespace` filter set to `matter` and the `Type` filter set to `definition`.

### `aws` types

Find data types under the `aws` namespace using the [ListSchemaVersions](../APIReference/API_ListSchemaVersions.md "../APIReference/API_ListSchemaVersions.md") API with the
`Namespace` filter set to `aws` and the `Type` filter set to `definition`.

#### Bitmap type definition

Bitmaps have two required properties:

- `type` must be an object
- `properties` must be an object containing each bit definition. Each bit
  is an object with properties `extrinsicId` and `value`. Each bit's value must be an integer with a minimum value of 0 and a maximum value of at least 1.

Sample bitmap definition:

```
{
    "title" : "Sample Bitmap Type",
    "description" : "Type definition for SampleBitmap.",
    "$ref" : "/schema-versions/definition/aws.bitmap@1.0 ",
    "type" : "object",
    "additionalProperties" : false,
    "properties" : {
        "Bit1" : {
            "extrinsicId" : "0x0000",
            "value" : {
                "type" : "integer",
                "maximum" : 1,
                "minimum" : 0
            }
        },
        "Bit2" : {
            "extrinsicId" : "0x0001",
            "value" : {
                "type" : "integer",
                "maximum" : 1,
                "minimum" : 0
            }
        }
    }
}

// Schema Compliant
{
    "Bit1": 1,
    "Bit1": 0
}

// NOT Schema Compliant
{
    "Bit1": -1,
    "Bit1": 0
}
```

#### Enum type definition

Enums require three properties:

- `type` must be an object
- `enum` must be an array of unique strings, with a minimum of one item
- `extrinsicIdMap` is an object with properties that are the enum values. The value of each of the
  properties should be the extrinsic identifier that correspond to the enum value.

Sample enum definition:

```
{
    "title" : "SampleEnum Type",
    "description" : "Type definition for SampleEnum.",
    "$ref" : "/schema-versions/definition/aws.enum@1.0",
    "type" : "string",
    "enum" : [
        "EnumValue0",
        "EnumValue1",
        "EnumValue2"
    ],
    "extrinsicIdMap" : {
        "EnumValue0" : "0",
        "EnumValue1" : "1",
        "EnumValue2" : "2"
    }
}

// Schema Compliant
"EnumValue0"
"EnumValue1"
"EnumValue2"

// NOT Schema Compliant
"NotAnEnumValue"
```
