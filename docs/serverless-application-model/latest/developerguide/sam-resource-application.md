# AWS::Serverless::Application

Embeds a serverless application from the [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications "https://serverlessrepo.aws.amazon.com/applications") or from an Amazon S3 bucket as a nested application. Nested applications are deployed as nested [AWS::CloudFormation::Stack](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.md") resources, which can contain multiple other resources including other AWS::Serverless::Application resources.

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into AWS CloudFormation resources. For more information,
see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
Type: AWS::Serverless::Application
Properties:
  Location: `String | ApplicationLocationObject`
  NotificationARNs: `List`
  Parameters: `Map`
  Tags: `Map`
  TimeoutInMinutes: `Integer`

```

## Properties

`Location`

Template URL, file path, or location object of a nested application.

If a template URL is provided, it must follow the format specified in the [CloudFormation TemplateUrl documentation](../../../AWSCloudFormation/latest/UserGuide/aws-properties-stack.md#cfn-cloudformation-stack-templateurl "../../../AWSCloudFormation/latest/UserGuide/aws-properties-stack.md#cfn-cloudformation-stack-templateurl") and contain a valid CloudFormation or SAM template. An [ApplicationLocationObject](sam-property-application-applicationlocationobject.md "sam-property-application-applicationlocationobject.md") can be used to specify an application that has been published to the [AWS Serverless Application Repository](../../../serverlessrepo/latest/devguide/what-is-serverlessrepo.md "../../../serverlessrepo/latest/devguide/what-is-serverlessrepo.md").

If a local file path is provided, the template must go through the workflow that includes the `sam deploy` or `sam package` command, in order for the application to be transformed properly.

_Type_: String | [ApplicationLocationObject](sam-property-application-applicationlocationobject.md "sam-property-application-applicationlocationobject.md")

_Required_: Yes

_AWS CloudFormation compatibility_: This property is similar to the `TemplateURL` property of an `AWS::CloudFormation::Stack` resource. The CloudFormation version does not take an [ApplicationLocationObject](sam-property-application-applicationlocationobject.md "sam-property-application-applicationlocationobject.md") to retrieve an application from the AWS Serverless Application Repository.

`NotificationARNs`

A list of existing Amazon SNS topics where notifications about stack events are sent.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `NotificationARNs` property of an `AWS::CloudFormation::Stack` resource.

`Parameters`

Application parameter values.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Parameters` property of an `AWS::CloudFormation::Stack` resource.

`Tags`

A map (string to string) that specifies the tags to be added to this application. Keys and values are limited to alphanumeric characters. Keys can be 1 to 127 Unicode characters in length and cannot be prefixed with aws:. Values can be 1 to 255 Unicode characters in length.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the `Tags` property of an `AWS::CloudFormation::Stack` resource. The Tags property in SAM consists of Key:Value pairs; in CloudFormation it consists of a list of Tag objects. When the stack is created, SAM will automatically add a `lambda:createdBy:SAM` tag to this application. In addition, if this application is from the AWS Serverless Application Repository, then SAM will also automatically the two additional tags `serverlessrepo:applicationId:`ApplicationId`` and `serverlessrepo:semanticVersion:`SemanticVersion``.

`TimeoutInMinutes`

The length of time, in minutes, that AWS CloudFormation waits for the nested stack to reach the `CREATE_COMPLETE` state. The default is no timeout. When AWS CloudFormation detects that the nested stack has reached the `CREATE_COMPLETE` state, it marks the nested stack resource as `CREATE_COMPLETE` in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches `CREATE_COMPLETE`, AWS CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `TimeoutInMinutes` property of an `AWS::CloudFormation::Stack` resource.

## Return Values

### Ref

When the logical ID of this resource is provided to the `Ref` intrinsic function, it returns the resource name of the underlying `AWS::CloudFormation::Stack` resource.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

### Fn::GetAtt

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are
the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md") in the _AWS CloudFormation User Guide_.

`Outputs.ApplicationOutputName`

The value of the stack output with name `ApplicationOutputName`.

## Examples

### SAR Application

Application that uses a template from the Serverless Application Repository

#### YAML

```
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: 'arn:aws:serverlessrepo:us-east-1:012345678901:applications/my-application'
    SemanticVersion: 1.0.0
  Parameters:
    StringParameter: parameter-value
    IntegerParameter: 2

```

### Normal-Application

Application from an S3 url

#### YAML

```
Type: AWS::Serverless::Application
Properties:
  Location: https://s3.amazonaws.com/sam-s3-demo-bucket/template.yaml

```
