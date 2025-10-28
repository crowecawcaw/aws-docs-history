# AWS::Serverless::StateMachine

Creates an AWS Step Functions state machine, which you can use to orchestrate AWS Lambda functions and
other AWS resources to form complex and robust workflows.

For more information about Step Functions, see the [AWS Step Functions Developer Guide](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md").

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into AWS CloudFormation resources.
For more information, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Type: AWS::Serverless::StateMachine
Properties:
  AutoPublishAlias: `String`
  UseAliasAsEventTarget: `Boolean`
  Definition: `Map`
  DefinitionSubstitutions: `Map`
  DefinitionUri: `String | S3Location`
  DeploymentPreference: `DeploymentPreference`
  Events: `EventSource`
  Logging: `LoggingConfiguration`
  Name: `String`
  PermissionsBoundary: `String`
  Policies: `String | List | Map`
  PropagateTags: `Boolean`
  RolePath: `String`
  Role: `String`
  Tags: `Map`
  Tracing: `TracingConfiguration`
  Type: `String`

```

## Properties

`AutoPublishAlias`

The name of the state machine alias. To learn more about using Step Functions state machine
aliases, see [Manage continuous
deployments with versions and aliases](../../../step-functions/latest/dg/concepts-cd-aliasing-versioning.md "../../../step-functions/latest/dg/concepts-cd-aliasing-versioning.md") in the
_AWS Step Functions Developer Guide_.

Use `DeploymentPreference` to configure deployment preferences for your
alias. If you don’t specify `DeploymentPreference`, AWS SAM will configure
traffic to shift to the newer state machine version all at once.

AWS SAM sets the version’s `DeletionPolicy` and
`UpdateReplacePolicy` to `Retain` by default. Previous versions
will not be deleted automatically.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Name` property of an
`AWS::StepFunctions::StateMachineAlias` resource.

`UseAliasAsEventTarget`

Indicate whether or not to pass the alias, created by using the `AutoPublishAlias` property, to the events source's target defined with [Events](#sam-statemachine-events "#sam-statemachine-events").

Specify `True` to use the alias as the events' target.

_Type_: Boolean

_Required_: No

_Default_: `False`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Definition`

The state machine definition is an object, where the format of the object matches
the format of your AWS SAM template file, for example, JSON or YAML. State machine
definitions adhere to the [Amazon States Language](../../../step-functions/latest/dg/concepts-amazon-states-language.md "../../../step-functions/latest/dg/concepts-amazon-states-language.md").

For an example of an inline state machine definition, see [Examples](#sam-resource-statemachine--examples "#sam-resource-statemachine--examples").

You must provide either a `Definition` or a
`DefinitionUri`.

_Type_: Map

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`DefinitionSubstitutions`

A string-to-string map that specifies the mappings for placeholder variables in the
state machine definition. This enables you to inject values obtained at runtime (for
example, from intrinsic functions) into the state machine definition.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`DefinitionSubstitutions` property of an
`AWS::StepFunctions::StateMachine` resource. If any intrinsic functions are
specified in an inline state machine definition, AWS SAM adds entries to this property to
inject them into the state machine definition.

`DefinitionUri`

The Amazon Simple Storage Service (Amazon S3) URI or local file path of the state machine definition written
in the [Amazon States Language](../../../step-functions/latest/dg/concepts-amazon-states-language.md "../../../step-functions/latest/dg/concepts-amazon-states-language.md").

If you provide a local file path, the template must go through the workflow that
includes the `sam deploy` or `sam package` command to correctly
transform the definition. To do this, you must use version 0.52.0 or later of the AWS SAM
CLI.

You must provide either a `Definition` or a
`DefinitionUri`.

_Type_: String | [S3Location](../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md#cfn-stepfunctions-statemachine-definitions3location "../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md#cfn-stepfunctions-statemachine-definitions3location")

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is passed directly to the
`DefinitionS3Location` property of an
`AWS::StepFunctions::StateMachine` resource.

`DeploymentPreference`

The settings that enable and configure gradual state machine deployments. To learn
more about Step Functions gradual deployments, see [Manage continuous
deployments with versions and aliases](../../../step-functions/latest/dg/concepts-cd-aliasing-versioning.md "../../../step-functions/latest/dg/concepts-cd-aliasing-versioning.md") in the
_AWS Step Functions Developer Guide_.

Specify `AutoPublishAlias` before configuring this property. Your
`DeploymentPreference` settings will be applied to the alias specified with
`AutoPublishAlias`.

When you specify `DeploymentPreference`, AWS SAM generates the
`StateMachineVersionArn` sub-property value automatically.

_Type_: [DeploymentPreference](../../../AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.md")

_Required_: No

_AWS CloudFormation compatibility_: AWS SAM generates and attaches the
`StateMachineVersionArn` property value to
`DeploymentPreference` and passes `DeploymentPreference` to the
`DeploymentPreference` property of an
`AWS::StepFunctions::StateMachineAlias` resource.

`Events`

Specifies the events that trigger this state machine. Events consist of a type and a
set of properties that depend on the type.

_Type_: [EventSource](sam-property-statemachine-statemachineeventsource.md "sam-property-statemachine-statemachineeventsource.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Logging`

Defines which execution history events are logged and where they are logged.

_Type_: [LoggingConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md#cfn-stepfunctions-statemachine-loggingconfiguration "../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md#cfn-stepfunctions-statemachine-loggingconfiguration")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`LoggingConfiguration` property of an
`AWS::StepFunctions::StateMachine` resource.

`Name`

The name of the state machine.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`StateMachineName` property of an
`AWS::StepFunctions::StateMachine` resource.

`PermissionsBoundary`

The ARN of a permissions boundary to use for this state machine's execution role.
This property only works if the role is generated for you.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`PermissionsBoundary` property of an `AWS::IAM::Role`
resource.

`Policies`

Permission policies for this state machine. Policies will be appended to the state
machine's default AWS Identity and Access Management (IAM) execution role.

This property accepts a single value or list of values. Allowed values
include:

- [AWS SAM policy templates](serverless-policy-templates.md "serverless-policy-templates.md").
- The ARN of an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies").
- The name of an AWS managed policy from the following [list](https://github.com/aws/serverless-application-model/blob/develop/samtranslator/internal/data/aws_managed_policies.json "https://github.com/aws/serverless-application-model/blob/develop/samtranslator/internal/data/aws_managed_policies.json").
- An [inline IAM policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") formatted in YAML as a map.

###### Note

If you set the `Role` property, this property is ignored.

_Type_: String | List | Map

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`PropagateTags`

Indicate whether or not to pass tags from the `Tags` property to your
[AWS::Serverless::StateMachine](sam-specification-generated-resources-statemachine.md "sam-specification-generated-resources-statemachine.md") generated
resources. Specify `True` to propagate tags in your generated
resources.

_Type_: Boolean

_Required_: No

_Default_: `False`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Role`

The ARN of an IAM role to use as this state machine's execution role.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is passed directly to the
`RoleArn` property of an
`AWS::StepFunctions::StateMachine` resource.

`RolePath`

The path to the state machine's IAM execution role.

Use this property when the role is generated for you. Do not use when the role is
specified with the `Role` property.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is passed directly to the
`Path` property of an `AWS::IAM::Role` resource.

`Tags`

A string-to-string map that specifies the tags added to the state machine and the
corresponding execution role. For information about valid keys and values for tags, see
the [Tags](../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md#cfn-stepfunctions-statemachine-tags "../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md#cfn-stepfunctions-statemachine-tags") property of an [AWS::StepFunctions::StateMachine](../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md") resource.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`Tags` property of an `AWS::StepFunctions::StateMachine`
resource. AWS SAM automatically adds a `stateMachine:createdBy:SAM` tag to this
resource, and to the default role that is generated for it.

`Tracing`

Selects whether or not AWS X-Ray is enabled for the state machine. For more
information about using X-Ray with Step Functions, see [AWS X-Ray
and Step Functions](../../../step-functions/latest/dg/concepts-xray-tracing.md "../../../step-functions/latest/dg/concepts-xray-tracing.md") in the _AWS Step Functions Developer Guide_.

_Type_: [TracingConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md#cfn-stepfunctions-statemachine-tracingconfiguration "../../../AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.md#cfn-stepfunctions-statemachine-tracingconfiguration")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`TracingConfiguration` property of an
`AWS::StepFunctions::StateMachine` resource.

`Type`

The type of the state machine.

_Valid values_: `STANDARD` or
`EXPRESS`

_Type_: String

_Required_: No

_Default_: `STANDARD`

_AWS CloudFormation compatibility_: This property is passed directly to the
`StateMachineType` property of an
`AWS::StepFunctions::StateMachine` resource.

## Return Values

### Ref

When you provide the logical ID of this resource to the Ref intrinsic function, Ref
returns the Amazon Resource Name (ARN) of the underlying
`AWS::StepFunctions::StateMachine` resource.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

### Fn::GetAtt

`Fn::GetAtt` returns a value for a specified attribute of this type. The
following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md") in the _AWS CloudFormation User Guide_.

`Name`

Returns the name of the state machine, such as
`HelloWorld-StateMachine`.

## Examples

### State

Machine Definition File

The following is an example of an inline state machine definition that allows a lambda function to invoke state machine.
Note that this example expects the `Role` property to configure proper policy to allow invocation.
The `my_state_machine.asl.json` file must be written in the [Amazon
States Language](../../../step-functions/latest/dg/concepts-amazon-states-language.md "../../../step-functions/latest/dg/concepts-amazon-states-language.md").

In this example, the `DefinitionSubstitution` entries allow the state machine
to include resources that are declared in the AWS SAM template file.

#### YAML

```
MySampleStateMachine:
  Type: AWS::Serverless::StateMachine
  Properties:
    DefinitionUri: statemachine/my_state_machine.asl.json
    Role: arn:aws:iam::123456123456:role/service-role/my-sample-role
    Tracing:
      Enabled: true
    DefinitionSubstitutions:
      MyFunctionArn: !GetAtt MyFunction.Arn
      MyDDBTable: !Ref TransactionTable

```

### Inline State Machine Definition

The following is an example of an inline state machine definition.

In this example, the AWS SAM template file is written in YAML, so the state machine
definition is also in YAML. To declare an inline state machine definition in JSON, write
your AWS SAM template file in JSON.

#### YAML

```
MySampleStateMachine:
  Type: AWS::Serverless::StateMachine
  Properties:
    Definition:
      StartAt: MyLambdaState
      States:
        MyLambdaState:
          Type: Task
          Resource: arn:aws:lambda:us-east-1:123456123456:function:my-sample-lambda-app
          End: true
    Role: arn:aws:iam::123456123456:role/service-role/my-sample-role
    Tracing:
      Enabled: true

```
