# Create a CloudFormation macro definition

When you create a macro definition, the macro definition makes the underlying Lambda
function available in the specified account so that CloudFormation invokes it to process the
templates.

## Event mapping

When CloudFormation invokes a macro's Lambda function, it sends a request in JSON
format with the following structure:

```
{
    "region" : "`us-east-1`",
    "accountId" : "`$ACCOUNT_ID`",
    "fragment" : { `...` },
    "transformId" : "`$TRANSFORM_ID`",
    "params" : { `...` },
    "requestId" : "`$REQUEST_ID`",
    "templateParameterValues" : { `...` }
}
```

- `region`

The Region in which the macro resides.

- `accountId`

The account ID of the account from which the macro is invoking the Lambda
function.

- `fragment`

The template content available for custom processing, in JSON
format.

    + For macros included in the `Transform` template
     section, this is the entire template except for the
     `Transform` section.
    + For macros included in an `Fn::Transform` intrinsic
     function call, this includes all sibling nodes (and their children)
     based on the location of the intrinsic function within the template
     except for the `Fn::Transform` function. For more
     information, see [Macro template scope](#template-macros-scope "#template-macros-scope").

- `transformId`

The name of the macro invoking this function.

- `params`

For `Fn::Transform` function calls, any specified parameters
for the function. CloudFormation doesn't evaluate these parameters before
passing them to the function.

For macros included in the `Transform` template section, this
section is empty.

- `requestId`

The ID of the request invoking this function.

- `templateParameterValues`

Any parameters specified in the [Parameters](parameters-section-structure.md "parameters-section-structure.md") section of the
template. CloudFormation evaluates these parameters before passing them to the
function.

## Response format

CloudFormation expects the Lambda function to return a response in the following JSON
format:

```
{
    "requestId" : "`$REQUEST_ID`",
    "status" : "`$STATUS`",
    "fragment" : { `...` },
    "errorMessage": "optional error message for failures"
}
```

- `requestId`

The ID of the request invoking this function. This must match the request
ID provided by CloudFormation when invoking the function.

- `status`

The status of the request (case-insensitive). Should be set to
`success`. CloudFormation treats any other response as a
failure.

- `fragment`

The processed template content for CloudFormation to include in the processed
template, including siblings. CloudFormation replaces the template content that
is passed to the Lambda function with the template fragment it receives in
the Lambda response.

The processed template content must be valid JSON, and its inclusion in
the processed template must result in a valid template.

If your function doesn't actually change the template content that
CloudFormation passes to it, but you still need to include that content in the
processed template, your function needs to return that template content to
CloudFormation in its response.

- `errorMessage`

The error message that explains why the transform failed. CloudFormation
displays this error message in the **Events** pane of the
**Stack details** page for your stack.

For example:

```
Error creating change set: Transform
                            AWS account account
                            number::macro name failed with:
                            error message string.
```

## Create a macro definition

###### To create a CloudFormation macro

definition

1. [Build a Lambda function](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") that will handle the processing of
   template contents. It can process any part of a template, up to the entire
   template.
2. Create a CloudFormation template containing an
   `AWS::CloudFormation::Macro` resource type and specify the
   `Name` and `FunctionName` properties. The
   `FunctionName` property must contain the ARN of the Lambda
   function to invoke when CloudFormation runs the macro.
3. (Optional) To aid in debugging, you can also specify the
   `LogGroupName` and `LogRoleArn` properties when
   creating the `AWS::CloudFormation::Macro` resource type for your
   macro. These properties enable you to specify the CloudWatch Logs log group to which
   CloudFormation sends error logging information when invoking the macro's
   underlying Lambda function, and the role CloudFormation should assume when
   sending log entries to those logs.
4. [Create a stack](cfn-console-create-stack.md "cfn-console-create-stack.md") using the
   template with the macro in the account you want to use it in. Or, [create a stack
   set with self-managed permissions](stacksets-getting-started-create-self-managed.md "stacksets-getting-started-create-self-managed.md") using the template with the
   macro in the administrator account, and then create stack instances in the
   target accounts.
5. After CloudFormation has successfully created the stacks that contain the
   macro definition, the macro is available for use within those accounts. You
   use a macro by referencing it in a template, at the appropriate location
   relevant to the template contents you want to process.

## Macro template scope

Macros referenced in the `Transform` section of a template can process
the entire contents of that template.

Macros referenced in an `Fn::Transform` function can process the
contents of any of the sibling elements (including children) of that
`Fn::Transform` function in the template.

For example, in the template sample below, `AWS::Include` can process
the `MyBucket` properties, based on the location of the
`Fn::Transform` function that contains it. `MyMacro` can
process the contents of the entire template because of its inclusion in the
`Transform` section.

```
# Start of processable content for MyMacro
AWSTemplateFormatVersion: 2010-09-09
 Transform: [MyMacro]
 Resources:
    WaitCondition:
      Type: AWS::CloudFormation::WaitCondition
    MyBucket:
      Type: AWS::S3::Bucket
      # Start of processable content for AWS::Include
      Properties:
        BucketName: `amzn-s3-demo-bucket1`
        Tags: `[{"key":"value"}]`
        'Fn::Transform':
          - Name: 'AWS::Include'
              Parameters:
                Location: `s3://amzn-s3-demo-bucket2/MyFileName.yaml`
        CorsConfiguration: `[]`
        # End of processable content for AWS::Include
    MyEc2Instance:
      Type: AWS::EC2::Instance
      Properties:
        ImageID: `ami-1234567890abcdef0`
# End of processable content for MyMacro
```

## Macro evaluation order

You can reference multiple macros in a given template, including transforms hosted
by CloudFormation, such as [AWS::Include](../TemplateReference/transform-aws-include.md "../TemplateReference/transform-aws-include.md") and [AWS::Serverless](../TemplateReference/transform-aws-serverless.md "../TemplateReference/transform-aws-serverless.md").

Macros are evaluated in order, based on their location in the template, from the
most deeply nested outward to the most general. Macros at the same location in the
template are evaluated serially based on the order in which they're listed.

Transforms such as `AWS::Include` and `AWS::Transform` are
treated the same as any other macros in terms of action order and scope.

For example, in the template sample below, CloudFormation evaluates the
`PolicyAdder` macro first, because it's the most deeply-nested macro
in the template. CloudFormation then evaluates `MyMacro` before evaluating
`AWS::Serverless` because it's listed before
`AWS::Serverless` in the `Transform` section.

```
AWSTemplateFormatVersion: 2010-09-09
 Transform: [MyMacro, AWS::Serverless]
 Resources:
    WaitCondition:
      Type: AWS::CloudFormation::WaitCondition
    MyBucket:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: `amzn-s3-demo-bucket`
        Tags: `[{"key":"value"}]`
        'Fn::Transform':
          - Name: PolicyAdder
        CorsConfiguration: `[]`
    MyEc2Instance:
      Type: AWS::EC2::Instance
      Properties:
        ImageID: `ami-1234567890abcdef0`
```
