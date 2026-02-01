• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# `aws:createStack` –

Create an CloudFormation stack

Creates an AWS CloudFormation stack from a template.

###### Note

The `aws:createStack` action supports automatic throttling retry. For
more information, see [Configuring automatic retry for
throttled operations](automation-throttling-retry.md "automation-throttling-retry.md").

For supplemental information about creating CloudFormation stacks, see [CreateStack](../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md "../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md") in the
_AWS CloudFormation API Reference_.

**Input**

YAML

```
name: makeStack
action: aws:createStack
maxAttempts: 1
onFailure: Abort
inputs:
  Capabilities:
  - CAPABILITY_IAM
  StackName: myStack
  TemplateURL: http://s3.amazonaws.com/amzn-s3-demo-bucket/myStackTemplate
  TimeoutInMinutes: 5
  Parameters:
    - ParameterKey: LambdaRoleArn
      ParameterValue: "{{LambdaAssumeRole}}"
    - ParameterKey: createdResource
      ParameterValue: createdResource-{{automation:EXECUTION_ID}}
```

JSON

```
{
    "name": "makeStack",
    "action": "aws:createStack",
    "maxAttempts": 1,
    "onFailure": "Abort",
    "inputs": {
        "Capabilities": [
            "CAPABILITY_IAM"
        ],
        "StackName": "myStack",
        "TemplateURL": "http://s3.amazonaws.com/amzn-s3-demo-bucket/myStackTemplate",
        "TimeoutInMinutes": 5,
        "Parameters": [
          {
            "ParameterKey": "LambdaRoleArn",
            "ParameterValue": "{{LambdaAssumeRole}}"
          },
          {
            "ParameterKey": "createdResource",
            "ParameterValue": "createdResource-{{automation:EXECUTION_ID}}"
          }
    }
}
```

Capabilities

A list of values that you specify before CloudFormation can create certain
stacks. Some stack templates include resources that can affect permissions
in your AWS account. For those stacks, you must explicitly acknowledge
their capabilities by specifying this parameter.

Valid values include `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, and `CAPABILITY_AUTO_EXPAND`.

###### CAPABILITY_IAM and CAPABILITY_NAMED_IAM

If you have IAM resources, you can specify either capability. If you
have IAM resources with custom names, you must specify `CAPABILITY_NAMED_IAM`. If you don't specify this
parameter, this action returns an `InsufficientCapabilities` error. The following resources
require you to specify either `CAPABILITY_IAM`
or `CAPABILITY_NAMED_IAM`.

- [`AWS::IAM::AccessKey`](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.md")
- [`AWS::IAM::Group`](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.md")
- [`AWS::IAM::InstanceProfile`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.md")
- [`AWS::IAM::Policy`](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.md")
- [`AWS::IAM::Role`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md")
- [`AWS::IAM::User`](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.md")
- [`AWS::IAM::UserToGroupAddition`](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.md")

If your stack template contains these resources, we recommend that you
review all permissions associated with them and edit their permissions, if
necessary.

For more information, see [Acknowledging
IAM Resources in CloudFormation Templates](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md#capabilities "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md#capabilities").

###### CAPABILITY_AUTO_EXPAND

Some template contain macros. Macros perform custom processing on
templates; this can include simple actions like find-and-replace
operations, all the way to extensive transformations of entire
templates. Because of this, users typically create a change set from the
processed template, so that they can review the changes resulting from
the macros before actually creating the stack. If your stack template
contains one or more macros, and you choose to create a stack directly
from the processed template, without first reviewing the resulting
changes in a change set, you must acknowledge this capability.

For more information, see [Using AWS CloudFormation Macros to Perform Custom Processing on
Templates](../../../AWSCloudFormation/latest/UserGuide/template-macros.md "../../../AWSCloudFormation/latest/UserGuide/template-macros.md") in the _AWS CloudFormation User Guide_.

Type: array of Strings

Valid Values: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM |
 CAPABILITY_AUTO_EXPAND`

Required: No

ClientRequestToken

A unique identifier for this CreateStack request. Specify this token if
you set maxAttempts in this step to a value greater than 1. By specifying
this token, CloudFormation knows that you aren't attempting to create a new
stack with the same name.

Type: String

Required: No

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: [a-zA-Z0-9][-a-zA-Z0-9]\*

DisableRollback

Set to `true` to turn off rollback of the stack
if stack creation failed.

Conditional: You can specify either the `DisableRollback` parameter or the `OnFailure` parameter, but not both.

Default: `false`

Type: Boolean

Required: No

NotificationARNs

The Amazon Simple Notification Service (Amazon SNS) topic ARNs for publishing stack-related events. You
can find SNS topic ARNs using the Amazon SNS console, [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").

Type: array of Strings

Array Members: Maximum number of 5 items.

Required: No

OnFailure

Determines the action to take if stack creation failed. You must specify
`DO_NOTHING`, `ROLLBACK`, or `DELETE`.

Conditional: You can specify either the `OnFailure` parameter or the `DisableRollback` parameter, but not both.

Default: `ROLLBACK`

Type: String

Valid Values: `DO_NOTHING | ROLLBACK |
 DELETE`

Required: No

Parameters

A list of `Parameter` structures that specify
input parameters for the stack. For more information, see the [Parameter](../../../AWSCloudFormation/latest/APIReference/API_Parameter.md "../../../AWSCloudFormation/latest/APIReference/API_Parameter.md") data type.

Type: array of [Parameter](../../../AWSCloudFormation/latest/APIReference/API_Parameter.md "../../../AWSCloudFormation/latest/APIReference/API_Parameter.md") objects

Required: No

ResourceTypes

The template resource types that you have permissions to work with for
this create stack action. For example: `AWS::EC2::Instance`, `AWS::EC2::*`, or
`Custom::`MyCustomInstance``. Use the
following syntax to describe template resource types.

- For all AWS resources:

```
AWS::*
```

- For all custom resources:

```
Custom::*
```

- For a specific custom resource:

```
Custom::`logical_ID`
```

- For all resources of a particular AWS service:

```
AWS::`service_name`::*
```

- For a specific AWS resource:

```
AWS::`service_name`::`resource_logical_ID`
```

If the list of resource types doesn't include a resource that you're
creating, the stack creation fails. By default, CloudFormation grants
permissions to all resource types. IAM uses this parameter for
CloudFormation-specific condition keys in IAM policies. For more information,
see [Controlling Access
with AWS Identity and Access Management](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md").

Type: array of Strings

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

RoleARN

The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to
create the stack. CloudFormation uses the role's credentials to make calls on
your behalf. CloudFormation always uses this role for all future operations on
the stack. As long as users have permission to operate on the stack,
CloudFormation uses this role even if the users don't have permission to pass
it. Ensure that the role grants the least amount of privileges.

If you don't specify a value, CloudFormation uses the role that was previously
associated with the stack. If no role is available, CloudFormation uses a
temporary session that is generated from your user credentials.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

StackName

The name that is associated with the stack. The name must be unique in the
Region in which you're creating the stack.

###### Note

A stack name can contain only alphanumeric characters (case sensitive)
and hyphens. It must start with an alphabetic character and can't be
longer than 128 characters.

Type: String

Required: Yes

StackPolicyBody

Structure containing the stack policy body. For more information, see
[Prevent Updates
to Stack Resources](../../../AWSCloudFormation/latest/UserGuide/protect-stack-resources.md "../../../AWSCloudFormation/latest/UserGuide/protect-stack-resources.md").

Conditional: You can specify either the `StackPolicyBody` parameter or the `StackPolicyURL` parameter, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 16384.

Required: No

StackPolicyURL

Location of a file containing the stack policy. The URL must point to a
policy located in an S3 bucket in the same region as the stack. The maximum
file size allowed for the stack policy is 16 KB.

Conditional: You can specify either the `StackPolicyBody` parameter or the `StackPolicyURL` parameter, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1350.

Required: No

Tags

Key-value pairs to associate with this stack. CloudFormation also propagates
these tags to the resources created in the stack. You can specify a maximum
number of 10 tags.

Type: array of [Tag](../../../AWSCloudFormation/latest/APIReference/API_Tag.md "../../../AWSCloudFormation/latest/APIReference/API_Tag.md") objects

Required: No

TemplateBody

Structure containing the template body with a minimum length of 1 byte and
a maximum length of 51,200 bytes. For more information, see [Template Anatomy](../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md "../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md").

Conditional: You can specify either the `TemplateBody` parameter or the `TemplateURL` parameter, but not both.

Type: String

Length Constraints: Minimum length of 1.

Required: No

TemplateURL

Location of a file containing the template body. The URL must point to a
template that is located in an S3 bucket. The maximum size allowed for the
template is 460,800 bytes. For more information, see [Template Anatomy](../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md "../../../AWSCloudFormation/latest/UserGuide/template-anatomy.md").

Conditional: You can specify either the `TemplateBody` parameter or the `TemplateURL` parameter, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: No

TimeoutInMinutes

The amount of time that can pass before the stack status becomes `CREATE_FAILED`. If `DisableRollback` isn't set or is set to `false`, the stack will be rolled back.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

## Outputs

StackId

Unique identifier of the stack.

Type: String

StackStatus

Current status of the stack.

Type: String

Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED |
 CREATE_COMPLETE | ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED |
 ROLLBACK_COMPLETE | DELETE_IN_PROGRESS | DELETE_FAILED |
 DELETE_COMPLETE | UPDATE_IN_PROGRESS |
 UPDATE_COMPLETE_CLEANUP_IN_PROGRESS | UPDATE_COMPLETE |
 UPDATE_ROLLBACK_IN_PROGRESS | UPDATE_ROLLBACK_FAILED |
 UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS |
 UPDATE_ROLLBACK_COMPLETE | REVIEW_IN_PROGRESS`

Required: Yes

StackStatusReason

Success or failure message associated with the stack status.

Type: String

Required: No

For more information, see [CreateStack](../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md "../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md").

## Security

considerations

Before you can use the `aws:createStack` action, you must
assign the following policy to the IAM Automation assume role. For more
information about the assume role, see [Task 1: Create a service role for
Automation](automation-setup-iam.md#create-service-role "automation-setup-iam.md#create-service-role").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "sqs:*",
 "cloudformation:CreateStack",
 "cloudformation:DescribeStacks"
 ],
 "Resource":"*"
 }
 ]
}`

```
