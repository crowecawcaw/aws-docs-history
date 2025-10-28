This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `AWS::LanguageExtensions`

transform

This topic describes how to use the `AWS::LanguageExtensions` transform to
enable additional functions and capabilities that are not available by default.

The `AWS::LanguageExtensions` is a CloudFormation macro that, when referenced in
your stack template, updates any intrinsic function defined by the transform to its resolved
value within the template when you create or update a stack using a change set.

By including this transform in your CloudFormation template, you can access additional
features, such as `Fn::ForEach`, which allows for more advanced operations like
iteration. You can also use intrinsic functions in places where they're typically not
allowed, such as in `Ref` and `Fn::GetAtt` functions.

## Usage

To use the `AWS::LanguageExtensions` transform, you must declare it at the
top level of your CloudFormation template. You can't use
`AWS::LanguageExtensions` as a transform embedded in any other template
section.

The declaration must use the literal string `AWS::LanguageExtensions` as
its value. You can't use a parameter or function to specify a transform value.

### Syntax

To declare this transform in your CloudFormation template, use the following
syntax:

### JSON

```
{
  "Transform":"AWS::LanguageExtensions",
  "Resources":{
    `...`
  }
}
```

### YAML

```
Transform: AWS::LanguageExtensions
Resources:
  `...`
```

The `AWS::LanguageExtensions` transform is a standalone declaration with no
additional parameters.

## Support for additional

functions

The `AWS::LanguageExtensions` transform supports the following additional
functions:

- [Fn::ForEach](intrinsic-function-reference-foreach.md "intrinsic-function-reference-foreach.md")
- [Fn::Length](intrinsic-function-reference-length.md "intrinsic-function-reference-length.md")
- [Fn::ToJsonString](intrinsic-function-reference-ToJsonString.md "intrinsic-function-reference-ToJsonString.md")

## Considerations

When using the `AWS::LanguageExtensions` transform, keep the following
considerations in mind:

- When you update a stack that uses the `AWS::LanguageExtensions`
  transform, we recommend that you don't use the **Use existing template** option in
  the CloudFormation console, or the equivalent command line option
  `--use-previous-template`. The `AWS::LanguageExtensions`
  transform resolves parameters to literal values during processing. When you use
  `--use-previous-template`, CloudFormation uses this processed template
  with the old literal values, preventing new parameter values and Systems Manager parameter
  updates from being applied. Instead, provide the original template to ensure
  parameters are re-resolved with current values.
- Short-form YAML syntax isn't supported within a template for intrinsic
  functions that are only available in the `AWS::LanguageExtensions`
  transform. Use explicit references to these functions. For example, use
  `Fn::Length` instead of `!Length`.
- The AWS SAM CLI currently doesn't support the `Fn::ForEach` intrinsic
  function of the `AWS::LanguageExtensions` transform.
- If you're using multiple transforms, use a list format. If you're using custom
  macros, place AWS-provided transforms after your custom macros. If you're
  using both the `AWS::LanguageExtensions` and
  `AWS::Serverless` transforms, the
  `AWS::LanguageExtensions` transform must come before the
  `AWS::Serverless` transform in the list.
- Functions and attributes provided by the `AWS::LanguageExtensions`
  transform are only supported in the `Resources`,
  `Conditions`, and `Outputs` sections of your
  template.

## Examples

The following examples show how to use the `AWS::LanguageExtensions`
transform to use the `Fn::Length` intrinsic function, defined by the
transform.

### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Transform": "AWS::LanguageExtensions",
    "Parameters": {
        "QueueList": {
            "Type": "CommaDelimitedList"
        },
        "QueueNameParam": {
            "Description": "Name for your SQS queue",
            "Type": "String"
        }
    },
    "Resources": {
        "Queue": {
            "Type": "AWS::SQS::Queue",
            "Properties": {
                "QueueName": {
                    "Ref": "QueueNameParam"
                },
                "DelaySeconds": {
                    "Fn::Length": {
                        "Ref": "QueueList"
                    }
                }
            }
        }
    }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Parameters:
  QueueList:
    Type: CommaDelimitedList
  QueueNameParam:
    Description: Name for your SQS queue
    Type: String
Resources:
  Queue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: !Ref QueueNameParam
      DelaySeconds:
        'Fn::Length': !Ref QueueList
```

## Related resources

For more examples, see the following topics.

- [Fn::ForEach](intrinsic-function-reference-foreach.md "intrinsic-function-reference-foreach.md")
- [Fn::Length](intrinsic-function-reference-length.md "intrinsic-function-reference-length.md")
- [Fn::ToJsonString](intrinsic-function-reference-ToJsonString.md "intrinsic-function-reference-ToJsonString.md")
- [Ref](intrinsic-function-reference-ref.md "intrinsic-function-reference-ref.md")
- [Fn::GetAtt](intrinsic-function-reference-getatt.md "intrinsic-function-reference-getatt.md")
- [Fn::FindInMap
  enhancements](intrinsic-function-reference-findinmap-enhancements.md "intrinsic-function-reference-findinmap-enhancements.md")

For general information about using macros, see [Perform custom processing on CloudFormation
templates with template macros](../UserGuide/template-macros.md "../UserGuide/template-macros.md") in the
_AWS CloudFormation User Guide_.
