# DeploymentPreference

Specifies the configurations to enable gradual Lambda deployments. For more information about configuring gradual Lambda deployments, see [Deploying serverless applications
gradually with AWS SAM](automating-updates-to-serverless-apps.md "automating-updates-to-serverless-apps.md").

###### Note

You must specify an `AutoPublishAlias` in your [AWS::Serverless::Function](sam-resource-function.md "sam-resource-function.md") to use a `DeploymentPreference` object, otherwise an error will result.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Alarms: `List`
  Enabled: `Boolean`
  Hooks: `Hooks`
  PassthroughCondition: `Boolean`
  Role: `String`
  TriggerConfigurations: `List`
  Type: `String`

```

## Properties

`Alarms`

A list of CloudWatch alarms that you want to be triggered by any errors raised by the deployment.

This property accepts the `Fn::If` intrinsic function. See the Examples section at the bottom of this topic for an example template that uses `Fn::If`.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Enabled`

Whether this deployment preference is enabled.

_Type_: Boolean

_Required_: No

_Default_: True

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Hooks`

Validation Lambda functions that are run before and after traffic shifting.

_Type_: [Hooks](sam-property-function-hooks.md "sam-property-function-hooks.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`PassthroughCondition`

If True, and if this deployment preference is enabled, the function's Condition will be passed through to the generated CodeDeploy resource. Generally, you should set this to True. Otherwise, the CodeDeploy resource would be created even if the function's Condition resolves to False.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Role`

An IAM role ARN that CodeDeploy will use for traffic shifting. An IAM role will not be created if this is provided.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`TriggerConfigurations`

A list of trigger configurations you want to associate with the deployment group. Used to notify an SNS topic on lifecycle events.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `TriggerConfigurations` property of an `AWS::CodeDeploy::DeploymentGroup` resource.

`Type`

There are two categories of deployment types at the moment: Linear and Canary. For more information about available deployment types see [Deploying serverless applications
gradually with AWS SAM](automating-updates-to-serverless-apps.md "automating-updates-to-serverless-apps.md").

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### DeploymentPreference with pre- and post-traffic hooks.

Example deployment preference that contains pre- and post-traffic hooks.

#### YAML

```
DeploymentPreference:
  Enabled: true
  Type: Canary10Percent10Minutes
  Alarms:
    - !Ref: AliasErrorMetricGreaterThanZeroAlarm
    - !Ref: LatestVersionErrorMetricGreaterThanZeroAlarm
  Hooks:
    PreTraffic:
      !Ref: PreTrafficLambdaFunction
    PostTraffic:
      !Ref: PostTrafficLambdaFunction

```

### DeploymentPreference with Fn::If intrinsic function

Example deployment preference that uses `Fn::If` for configuring alarms. In this example, `Alarm1` will be configured if `MyCondition` is `true`, and `Alarm2` and `Alarm5` will be configured if `MyCondition` is `false`.

#### YAML

```
DeploymentPreference:
  Enabled: true
  Type: Canary10Percent10Minutes
  Alarms:
    Fn::If:
      - MyCondition
      - - Alarm1
      - - Alarm2
        - Alarm5

```
