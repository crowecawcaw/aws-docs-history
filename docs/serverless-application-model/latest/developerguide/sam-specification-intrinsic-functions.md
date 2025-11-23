# Intrinsic functions for AWS SAM

Intrinsic functions are built-in functions that enable you to assign values to properties
that are only available at runtime. AWS SAM has limited support for certain intrinsic function properties, so it is unable to resolve some intrinsic functions.
Consequently, we recommend adding the `AWS::LanguageExtensions` transform to resolve this. The `AWS::LanguageExtensions` is a macro hosted
by CloudFormation that lets you use intrinsic functions and other functionalities that are by default not included in CloudFormation.

```
Transform:
  - AWS::LanguageExtensions
  - AWS::Serverless-2016-10-31

```

###### Note

If you use intrinsic functions in CodeUri property, AWS SAM will not be able to correctly parse the values.
Consider using `AWS::LanguageExtensions` transform instead.

For more information, refer to [Properties section of AWS::Serverless::Function](sam-resource-function.md#sam-resource-function-properties "sam-resource-function.md#sam-resource-function-properties").

For more information about intrinsic functions, see
[Intrinsic Function Reference](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md") in the _AWS CloudFormation User Guide_.
