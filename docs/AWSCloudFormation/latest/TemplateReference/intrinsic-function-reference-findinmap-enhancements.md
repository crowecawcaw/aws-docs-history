

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Fn::FindInMap enhancements`
<a name="intrinsic-function-reference-findinmap-enhancements"></a>

The `AWS::LanguageExtensions` transform enhances the functionality of the `Fn::FindInMap` intrinsic function in CloudFormation templates.

The standard `Fn::FindInMap` function supports only `Fn::FindInMap` and `Ref` as nested intrinsic functions. The `AWS::LanguageExtensions` transform removes this limitation, allowing you to use a wider range of intrinsic functions to define the parameters of `Fn::FindInMap`.

**Note**  
The `DefaultValue` parameter for `Fn::FindInMap` no longer requires the `AWS::LanguageExtensions` transform. You can use `DefaultValue` in any CloudFormation template. For more information, see [`Fn::FindInMap`](intrinsic-function-reference-findinmap.md).

## Declaration
<a name="intrinsic-function-reference-findinmap-enhancements-declaration"></a>

### JSON
<a name="intrinsic-function-reference-findinmap-enhancements-syntax.json"></a>

```
{ "Fn::FindInMap" : [ "{{MapName}}", "{{TopLevelKey}}", "{{SecondLevelKey}}"] }
```

If you want to specify a fallback value for when a key isn't found in the mapping, include a `DefaultValue`:

```
{ "Fn::FindInMap" : [ "{{MapName}}", "{{TopLevelKey}}", "{{SecondLevelKey}}", {"DefaultValue": "{{DefaultValue}}"}] }
```

### YAML
<a name="intrinsic-function-reference-findinmap-enhancements-syntax.yaml"></a>

Syntax for the full function name:

```
Fn::FindInMap: [ {{MapName}}, {{TopLevelKey}}, {{SecondLevelKey}} ]
```

Syntax for the short form:

```
!FindInMap [ {{MapName}}, {{TopLevelKey}}, {{SecondLevelKey}} ]
```

If you want to specify a fallback value for when a key isn't found in the mapping, include a `DefaultValue`:

Syntax for the full function name:

```
Fn::FindInMap:
  - {{MapName}}
  - {{TopLevelKey}}
  - {{SecondLevelKey}}
  - DefaultValue: {{DefaultValue}}
```

Syntax for the short form:

```
!FindInMap
  - {{MapName}}
  - {{TopLevelKey}}
  - {{SecondLevelKey}}
  - DefaultValue: {{DefaultValue}}
```

## Parameters
<a name="intrinsic-function-reference-findinmap-enhancements-parameters"></a>

With the `AWS::LanguageExtensions` transform, the parameters `MapName`, `TopLevelKey`, `SecondLevelKey`, and `DefaultValue` can each be an intrinsic function, as long as it resolves to a valid value during the transform.

## Examples
<a name="w2aac28c16c20c13"></a>

The following examples demonstrate how to use intrinsic functions in the parameters of `Fn::FindInMap` when you add the `AWS::LanguageExtensions` transform.

### Using intrinsic functions to define the top level key
<a name="intrinsic-function-reference-findinmap-enhancements-example"></a>

The following is an example of using a `Fn::FindInMap` function with the `Fn::Select` and `Fn::Split` intrinsic functions embedded inside it to define the top level key.

#### JSON
<a name="intrinsic-function-reference-findinmap-enhancement-example.json"></a>

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

#### YAML
<a name="intrinsic-function-reference-findinmap-enhance-example.yaml"></a>

```
Transform: 'AWS::LanguageExtensions'
#...
    !FindInMap: [MyMap, !Select [0, !Split [|, !Ref InputKeys]], SecondKey]
#...
```

## Supported functions
<a name="intrinsic-function-reference-findinmap-enhancements-supported-functions"></a>

You can use the following functions in the parameters of `Fn::FindInMap` with the `AWS::LanguageExtensions` transform:
+ ``Fn::FindInMap``
+ ``Fn::Join``
+ ``Fn::Sub``
+ ``Fn::If``
+ ``Fn::Select``
+ ``Fn::Length``
+ ``Fn::ToJsonString``
+ ``Fn::Split`` – Unless it's used for the default value, `Fn::Split` must be used in conjunction with intrinsic functions that produce a string, such as ``Fn::Join`` or ``Fn::Select``.
+ ``Ref``

## Related resources
<a name="w2aac28c16c20c17"></a>

For more information and examples that show how to use the `Fn::FindInMap` intrinsic function, including the `DefaultValue` parameter, see [`Fn::FindInMap`](intrinsic-function-reference-findinmap.md).

For more information about the `AWS::LanguageExtensions` transform, see [`AWS::LanguageExtensions` transform](transform-aws-languageextensions.md).