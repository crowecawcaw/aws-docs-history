# ApiUsagePlan

Configures a usage plan for an API Gateway API. For more information about usage plans, see [Create and Use Usage Plans with API Keys](../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md "../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md") in the _API Gateway Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  CreateUsagePlan: `String`
  Description: `String`
  Quota: `QuotaSettings`
  Tags: `List`
  Throttle: `ThrottleSettings`
  UsagePlanName: `String`

```

## Properties

`CreateUsagePlan`

Determines how this usage plan is configured. Valid values are `PER_API`, `SHARED`, and `NONE`.

`PER_API` creates [AWS::ApiGateway::UsagePlan](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md"), [AWS::ApiGateway::ApiKey](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.md"), and [AWS::ApiGateway::UsagePlanKey](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.md") resources that are specific to this API. These resources have logical IDs of ``<api-logical-id>`UsagePlan`, ``<api-logical-id>`ApiKey`, and ``<api-logical-id>`UsagePlanKey`, respectively.

`SHARED` creates [AWS::ApiGateway::UsagePlan](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md"), [AWS::ApiGateway::ApiKey](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.md"), and [AWS::ApiGateway::UsagePlanKey](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.md") resources that are shared across any API that also has `CreateUsagePlan: SHARED` in the same AWS SAM template. These resources have logical IDs of `ServerlessUsagePlan`, `ServerlessApiKey`, and `ServerlessUsagePlanKey`, respectively. If you use this option, we recommend that you add additional configuration for this usage plan on only one API resource to avoid conflicting definitions and an uncertain state.

`NONE` disables the creation or association of a usage plan with this API. This is only necessary if `SHARED` or `PER_API` is specified in the [Globals section of the AWS SAM
template](sam-specification-template-anatomy-globals.md "sam-specification-template-anatomy-globals.md").

_Valid values_: `PER_API`, `SHARED`, and `NONE`

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Description`

A description of the usage plan.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Description` property of an `AWS::ApiGateway::UsagePlan` resource.

`Quota`

Configures the number of requests that users can make within a given interval.

_Type_: [QuotaSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md#cfn-apigateway-usageplan-quota "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md#cfn-apigateway-usageplan-quota")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Quota` property of an `AWS::ApiGateway::UsagePlan` resource.

`Tags`

An array of arbitrary tags (key-value pairs) to associate with the usage plan.

This property uses the [CloudFormation Tag Type](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md").

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Tags` property of an `AWS::ApiGateway::UsagePlan` resource.

`Throttle`

Configures the overall request rate (average requests per second) and burst capacity.

_Type_: [ThrottleSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md#cfn-apigateway-usageplan-throttle "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md#cfn-apigateway-usageplan-throttle")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Throttle` property of an `AWS::ApiGateway::UsagePlan` resource.

`UsagePlanName`

A name for the usage plan.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `UsagePlanName` property of an `AWS::ApiGateway::UsagePlan` resource.

## Examples

### UsagePlan

The following is a usage plan example.

#### YAML

```
Auth:
  UsagePlan:
    CreateUsagePlan: PER_API
    Description: Usage plan for this API
    Quota:
      Limit: 500
      Period: MONTH
    Throttle:
      BurstLimit: 100
      RateLimit: 50
    Tags:
      - Key: TagName
        Value: TagValue

```
