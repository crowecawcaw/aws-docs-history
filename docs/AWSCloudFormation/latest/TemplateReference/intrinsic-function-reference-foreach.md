This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::ForEach`

The `Fn::ForEach` intrinsic function takes a collection and a fragment, and
applies the items in the collection to the identifier in the provided fragment.
`Fn::ForEach` can contain other intrinsic functions, including
`Fn::ForEach` itself, and be used within the `Conditions`,
`Outputs`, and `Resources` (including the resource properties) sections.
It can't be used in any of the following sections, `AWSTemplateFormatVersion`,
`Description`, `Metadata`, `Transform`,
`Parameters`, `Mappings`, `Rules`, or `Hooks`
sections.

If you use the `Fn::ForEach` intrinsic function in your template, you must also
use the [AWS::LanguageExtensions
transform](transform-aws-languageextensions.md "transform-aws-languageextensions.md") .

Using the `Fn::ForEach` intrinsic function does not change the quotas, which
apply to the resultant template. Quotas include the maximum size of a template and the maximum
number of resources in a template. For more information, see [Understand CloudFormation quotas](../UserGuide/cloudformation-limits.md "../UserGuide/cloudformation-limits.md") in the
_AWS CloudFormation User Guide_.

## Declaration

### JSON

```
"Fn::ForEach::`LoopLogicalName`": [
  "`Identifier`",
  ["Value1","Value2"], // `Collection`
  {"`OutputKey`": {`OutputValue`}}
]
```

### YAML

```
'Fn::ForEach::`LoopLogicalName`':
    - `Identifier`
    - - `Value1` # `Collection`
      - `Value2`
    - '`OutputKey`':
        `OutputValue`
```

## Parameters

_Loop logical name_

A logical ID for the loop. The name must be unique within the template and can't
conflict with any logical ID values in the `Resources` section of the
template. This name isn't in the transformed output. It’s used for internal reference
within the CloudFormation template itself.

_Identifier_

An identifier for the placeholder that gets replaced in the `OutputKey`
and `OutputValue` parameters. All instances of `${Identifier}` or
`&{Identifier}` in the `OutputKey` and
`OutputValue` parameters will be replaced with the values from the
`Collection` parameter.

_Collection_

The collection of values to iterate over. This can be an array in this parameter, or
it can be a [Ref](intrinsic-function-reference-ref.md "intrinsic-function-reference-ref.md") to a `CommaDelimitedList`.
When using `&{Identifier}`, non-alphanumeric characters can be passed in
the `Collection`.

_Output key_

The key in the transformed template. `${Identifier}` or
`&{Identifier}` must be included within the `OutputKey`
parameter. For example, if `Fn::ForEach` is used in the
`Resources` section of the template, this is the logical ID of each
resource.

The `&{}` syntax allows non-alphanumeric characters in the
`Collection` to be used in `OutputKey` parameter. For an example
of this, see [Passing
non-alphanumeric characters within the Collection for
Fn::ForEach](intrinsic-function-reference-foreach-example-resource.md#intrinsic-function-reference-foreach-example-non-alphanumeric "intrinsic-function-reference-foreach-example-resource.md#intrinsic-function-reference-foreach-example-non-alphanumeric").

_Output value_

The value that's replicated in the transformed template for each item in the
`Collection` parameter. For example, if `Fn::ForEach` is used in
the `Resources` section of the template, this is the template fragment that's
repeated to configure each resource.

## Return value

An expanded object that contains the object fragment repeated once for each item in the
collection, where the identifier in the fragment is replaced with the item from the
collection.

## Supported

functions

You can use the following functions within `Fn::ForEach`.

- Condition functions:
  - [Fn::And](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-and "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-and")
  - [Fn::Equals](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-equals "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-equals")
  - [Fn::If](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if")
  - [Fn::Not](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-not "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-not")
  - [Fn::Or](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-or "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-or")

- [Fn::Base64](intrinsic-function-reference-base64.md "intrinsic-function-reference-base64.md")
- [Fn::FindInMap](intrinsic-function-reference-findinmap.md "intrinsic-function-reference-findinmap.md")
- [Fn::GetAtt](intrinsic-function-reference-getatt.md "intrinsic-function-reference-getatt.md")
- [Fn::GetAZs](intrinsic-function-reference-getavailabilityzones.md "intrinsic-function-reference-getavailabilityzones.md")
- [Fn::ImportValue](intrinsic-function-reference-importvalue.md "intrinsic-function-reference-importvalue.md")
- [Fn::Join](intrinsic-function-reference-join.md "intrinsic-function-reference-join.md")
- [Fn::Length](intrinsic-function-reference-length.md "intrinsic-function-reference-length.md")
- [Fn::Transform](intrinsic-function-reference-transform.md "intrinsic-function-reference-transform.md")
- [Fn::Select](intrinsic-function-reference-select.md "intrinsic-function-reference-select.md")
- [Fn::Sub](intrinsic-function-reference-sub.md "intrinsic-function-reference-sub.md")
- [Fn::ToJsonString](intrinsic-function-reference-ToJsonString.md "intrinsic-function-reference-ToJsonString.md")
- [Ref](intrinsic-function-reference-ref.md "intrinsic-function-reference-ref.md")

## Examples

You can find examples for the `Conditions`, `Outputs`, and
`Resources` sections in [Examples](intrinsic-function-reference-foreach-examples.md "intrinsic-function-reference-foreach-examples.md").
