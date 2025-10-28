This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::FindInMap

enhancements`

The `AWS::LanguageExtensions` transform enhances the functionality of the
`Fn::FindInMap` intrinsic function in CloudFormation templates.

The `Fn::FindInMap` function is used to retrieve a value from a mapping defined
in the `Mappings` section of a CloudFormation template. However, the standard
`Fn::FindInMap` function has limitations, such as the inability to handle
missing mappings or use a `Fn::FindInMap` function with some intrinsic functions
embedded inside it.

The `AWS::LanguageExtensions` transform addresses these limitations by
introducing the following enhancements:

- Default value support – You can specify a
  default value to be returned if a mapping is not found.
- Intrinsic function support – You can also
  use a wider range of intrinsic functions to define the fields of
  `Fn::FindInMap` than with the standard `Fn::FindInMap`
  function.

## Declaration

### JSON

```
{ "Fn::FindInMap" : [
    "`MapName`",
    "`TopLevelKey`",
    "`SecondLevelKey`",
    {"DefaultValue": "`DefaultValue`"}
  ]
}
```

### YAML

Syntax for the full function name:

```
Fn::FindInMap:
  `- MapName`
  `- TopLevelKey`
  `- SecondLevelKey`
  - DefaultValue: `DefaultValue`
```

Syntax for the short form:

```
!FindInMap
  `- MapName`
  `- TopLevelKey`
  `- SecondLevelKey`
  - DefaultValue: `DefaultValue`
```

## Parameters

DefaultValue

The value that `Fn::FindInMap` will resolve to if the
`TopLevelKey` and/or `SecondLevelKey` can not be
found from the `MapName` map. This field is optional.

All parameters `MapName`, `TopLevelKey`,
`SecondLevelKey`, and `DefaultValue` can be an intrinsic
function as long as it's able to resolve to a valid value during the transform.

## Examples

The following examples demonstrate how to define the fields of
`Fn::FindInMap` when you add the `AWS::LanguageExtensions`
transform.

### Using

a default value

The following is an example of using a default value in the
`Fn::FindInMap` function.

#### JSON

```
{
  //...
    "Transform": "AWS::LanguageExtensions",
    //...
    "Fn::FindInMap": [
      "RegionMap",
      { "Ref": "AWS::Region" },
      "InstanceType",
      { "DefaultValue": "t3.micro" }
    ]
  //...
}
```

#### YAML

```
Transform: 'AWS::LanguageExtensions'
#...
    !FindInMap
        - 'RegionMap'
        - !Ref 'AWS::Region'
        - 'InstanceType'
        - DefaultValue: t3.micro
#...
```

#### Using intrinsic functions to define the top level key

The following is an example of using a `Fn::FindInMap` function
with the `Fn::Select` and `Fn::Split` intrinsic functions
embedded inside it to define the top level key.

##### JSON

```
{
  //...
  "Transform": "AWS::LanguageExtensions",
  //...
      "Fn::FindInMap": [
        "MyMap",
        {
          "Fn::Select": [
            0,
            {
              "Fn::Split": [
                "|",
                { "Ref": "InputKeys" }
              ]
            }
          ]
        },
        "SecondKey"
      ]
//...
}
```

##### YAML

```
Transform: 'AWS::LanguageExtensions'
#...
    !FindInMap: [MyMap, !Select [0, !Split [|, !Ref InputKeys]], SecondKey]
#...
```

## Supported functions

You can use the following functions in the parameters of `Fn::FindInMap:`
enhancements:

- `Fn::FindInMap`
- `Fn::Join`
- `Fn::Sub`
- `Fn::If`
- `Fn::Select`
- `Fn::Length`
- `Fn::ToJsonString`
- `Fn::Split` - Unless it’s used
  for the default value, `Fn::Split` has to be used in conjunction with
  intrinsic functions that produce a string, such as `Fn::Join` or `Fn::Select`.
- `Ref`

## Related resources

For more information and examples that show how to use the `Fn::FindInMap`
intrinsic function, see [Fn::FindInMap](intrinsic-function-reference-findinmap.md "intrinsic-function-reference-findinmap.md").

For more information about the `AWS::LanguageExtensions` transform, see
[AWS::LanguageExtensions
transform](transform-aws-languageextensions.md "transform-aws-languageextensions.md").
