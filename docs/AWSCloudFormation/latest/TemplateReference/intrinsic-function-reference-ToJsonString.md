This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::ToJsonString`

The `Fn::ToJsonString` intrinsic function converts an object or array to its
corresponding JSON string.

###### Important

You must use the [AWS::LanguageExtensions
transform](transform-aws-languageextensions.md "transform-aws-languageextensions.md") to use the
`Fn::ToJsonString` intrinsic function.

## Declaration

### JSON

```
{ "Fn::ToJsonString": `Object` }
```

```
{ "Fn::ToJsonString": `Array` }
```

### YAML

```
Fn::ToJsonString: `Object`
```

```
Fn::ToJsonString: `Array`
```

## Parameters

`Object`

The object you want to convert to a JSON string.

`Array`

The array you want to convert to a JSON string.

## Return value

The object or array converted to a JSON string.

## Examples

### Convert an object to a JSON string

This example snippet converts the object passed to the intrinsic function to a
JSON string.

#### JSON

```
{
//...
    "Transform": "AWS::LanguageExtensions"
    //...
        "Fn::ToJsonString": {
            "key1": "value1",
            "key2": {
                "Ref": "ParameterName"
            }
        }
//...
}
```

#### YAML

```
Transform: 'AWS::LanguageExtensions'
#...
  Fn::ToJsonString:
    key1: value1
    key2: !Ref ParameterName
#...
```

In both of these examples, if the `Ref` to
`ParameterName` resolves to `resolvedValue`, the
function resolves to the following JSON string:

```
"{\"key1\":\"value1\",\"key2\":\"resolvedValue\"}"
```

### Convert an

array to a JSON string

This example snippet converts the array passed to the intrinsic function to a JSON
string.

#### JSON

```
{
//...
    "Transform": "AWS::LanguageExtensions"
    //...
        "Fn::ToJsonString": [{
            "key1": "value1",
            "key2": {
                "Ref": "ParameterName"
            }
        }]
//...
}
```

#### YAML

```
Transform: 'AWS::LanguageExtensions'
#...
  Fn::ToJsonString:
    - key1: value1
      key2: !Ref ParameterName
#...
```

In both of these examples, if the `Ref` to
`ParameterName` resolves to `resolvedValue`, the
function resolves to the following JSON String:

```
"[{\"key1\":\"value1\"},{\"key2\":\"resolvedValue\"}]"
```

## Supported functions

You can use the following functions in the `Fn::ToJsonString` intrinsic
function or array:

- `Fn::Base64`
- `Fn::FindInMap`
- `Fn::GetAtt`
- `Fn::GetAZs`
- `Fn::If`
- `Fn::ImportValue`
- `Fn::Join`
- `Fn::Length`
- `Fn::Select`
- `Fn::Split`
- `Fn::Sub`
- `Fn::ToJsonString`
- `Ref`
