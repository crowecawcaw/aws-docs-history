

# Intrinsic functions for AWS SAM
<a name="sam-specification-intrinsic-functions"></a>

Intrinsic functions are built-in functions that enable you to assign values to properties that are only available at runtime. AWS SAM has limited support for certain intrinsic function properties, so it is unable to resolve some intrinsic functions. Consequently, we recommend adding the `AWS::LanguageExtensions` transform to resolve this. The `AWS::LanguageExtensions` is a macro hosted by CloudFormation that lets you use intrinsic functions and other functionalities that are by default not included in CloudFormation.

```
Transform:
  - AWS::LanguageExtensions
  - AWS::Serverless-2016-10-31
```

**Note**  
If you use intrinsic functions in CodeUri property, AWS SAM will not be able to correctly parse the values. Consider using `AWS::LanguageExtensions` transform instead.  
For more information, refer to [Properties section of AWS::Serverless::Function](sam-resource-function.md#sam-resource-function-properties).

For details about how the AWS SAM CLI handles the `AWS::LanguageExtensions` transform, including using intrinsic functions in `CodeUri` and other packageable properties, see [CloudFormation language extensions support](sam-specification-language-extensions.md).

For more information about intrinsic functions, see [Intrinsic Function Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html) in the *AWS CloudFormation User Guide*.