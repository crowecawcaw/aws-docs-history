

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Fn::ForEach`
<a name="intrinsic-function-reference-foreach"></a>

The `Fn::ForEach` intrinsic function takes a collection and a fragment, and applies the items in the collection to the identifier in the provided fragment. `Fn::ForEach` can contain other intrinsic functions, including `Fn::ForEach` itself, and be used within the `Conditions`, `Outputs`, and `Resources` (including the resource properties) sections. It can't be used in any of the following sections, `AWSTemplateFormatVersion`, `Description`, `Metadata`, `Transform`, `Parameters`, `Mappings`, `Rules`, or `Hooks` sections.

If you use the `Fn::ForEach` intrinsic function in your template, you must also use the [`AWS::LanguageExtensions` transform](transform-aws-languageextensions.md) .

Using the `Fn::ForEach` intrinsic function does not change the quotas, which apply to the resultant template. Quotas include the maximum size of a template and the maximum number of resources in a template. For more information, see [Understand CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User Guide*.

## Declaration
<a name="intrinsic-function-reference-foreach-declaration"></a>

### JSON
<a name="intrinsic-function-reference-foreach-declaration.json"></a>

```
"Fn::ForEach::{{LoopLogicalName}}": [
  "{{Identifier}}",
  ["Value1","Value2"], // {{Collection}}
  {"{{OutputKey}}": {{{OutputValue}}}}
]
```

### YAML
<a name="intrinsic-function-reference-foreach-declaration.yaml"></a>

```
'Fn::ForEach::{{LoopLogicalName}}':
    - {{Identifier}}
    - - {{Value1}} # {{Collection}}
      - {{Value2}}
    - '{{OutputKey}}':
        {{OutputValue}}
```

## Parameters
<a name="intrinsic-function-reference-foreach-parameters"></a>

*Loop logical name*  
A logical ID for the loop. The name must be unique within the template and can't conflict with any logical ID values in the `Resources` section of the template. This name isn't in the transformed output. It’s used for internal reference within the CloudFormation template itself.

*Identifier*  
An identifier for the placeholder that gets replaced in the `OutputKey` and `OutputValue` parameters. All instances of `${Identifier}` or `&{Identifier}` in the `OutputKey` and `OutputValue` parameters will be replaced with the values from the `Collection` parameter.

*Collection*  
The collection of values to iterate over. This can be an array in this parameter, or it can be a [`Ref`](intrinsic-function-reference-ref.md) to a `CommaDelimitedList`. When using `&{Identifier}`, non-alphanumeric characters can be passed in the `Collection`.

*Output key*  
The key in the transformed template. `${Identifier}` or `&{Identifier}` must be included within the `OutputKey` parameter. For example, if `Fn::ForEach` is used in the `Resources` section of the template, this is the logical ID of each resource.  
The `&{}` syntax allows non-alphanumeric characters in the `Collection` to be used in `OutputKey` parameter. For an example of this, see [Passing non-alphanumeric characters within the `Collection` for `Fn::ForEach`](intrinsic-function-reference-foreach-example-resource.md#intrinsic-function-reference-foreach-example-non-alphanumeric).

*Output value*  
The value that's replicated in the transformed template for each item in the `Collection` parameter. For example, if `Fn::ForEach` is used in the `Resources` section of the template, this is the template fragment that's repeated to configure each resource.

## Return value
<a name="intrinsic-function-reference-foreach-return-value"></a>

An expanded object that contains the object fragment repeated once for each item in the collection, where the identifier in the fragment is replaced with the item from the collection.

## Supported functions
<a name="intrinsic-function-reference-foreach-nested-functions"></a>

You can use the following functions within `Fn::ForEach`.
+ Condition functions:
  + [`Fn::And`](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-and)
  + [`Fn::Equals`](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-equals)
  + [`Fn::If`](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if)
  + [`Fn::Not`](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-not)
  + [`Fn::Or`](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-or)
+ [`Fn::Base64`](intrinsic-function-reference-base64.md)
+ [`Fn::FindInMap`](intrinsic-function-reference-findinmap.md)
+ [`Fn::GetAtt`](intrinsic-function-reference-getatt.md)
+ [`Fn::GetAZs`](intrinsic-function-reference-getavailabilityzones.md)
+ [`Fn::ImportValue`](intrinsic-function-reference-importvalue.md)
+ [`Fn::Join`](intrinsic-function-reference-join.md)
+ [`Fn::Length`](intrinsic-function-reference-length.md)
+ [`Fn::Transform`](intrinsic-function-reference-transform.md)
+ [`Fn::Select`](intrinsic-function-reference-select.md)
+ [`Fn::Sub`](intrinsic-function-reference-sub.md)
+ [`Fn::ToJsonString`](intrinsic-function-reference-ToJsonString.md)
+ [`Ref`](intrinsic-function-reference-ref.md)

## Examples
<a name="intrinsic-function-reference-foreach-example-pointer"></a>

You can find examples for the `Conditions`, `Outputs`, and `Resources` sections in [Examples](intrinsic-function-reference-foreach-examples.md).