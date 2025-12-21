# Security Hub CSPM controls for AWS Lambda

These AWS Security Hub CSPM controls evaluate the AWS Lambda service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Lambda.1] Lambda function policies should prohibit public

access

**Related requirements:** NIST.800-53.r5 AC-21,
NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5
AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11),
NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21),
NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS
v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, PCI DSS
v3.2.1/7.2.1, PCI DSS v4.0.1/7.2.1

**Category:** Protect > Secure network
configuration

**Severity:** Critical

**Resource type:**
`AWS::Lambda::Function`

**AWS Config rule:**
[lambda-function-public-access-prohibited](../../../config/latest/developerguide/lambda-function-public-access-prohibited.md "../../../config/latest/developerguide/lambda-function-public-access-prohibited.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the Lambda function resource-based policy prohibits public
access outside of your account. The control fails if public access is permitted. The
control also fails if a Lambda function is invoked from Amazon S3, and the policy doesn't
include a condition to limit public access, such as `AWS:SourceAccount`. We
recommend using other S3 conditions along with `AWS:SourceAccount` in your
bucket policy for more refined access.

###### Note

This control doesn't evaluate policy conditions that use wildcard characters or
variables. To produce a `PASSED` finding, conditions in the policy for
the Lambda function must only use fixed values, which are values that don't contain
wildcard characters or policy variables. For information about policy variables, see
[Variables and
tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _AWS Identity and Access Management User
Guide_.

The Lambda function should not be publicly accessible, as this may allow unintended
access to your function code.

### Remediation

To remediate this issue, you must update your function's resource-based policy to
remove permissions or to add the `AWS:SourceAccount` condition. You can
only update the resource-based policy from the Lambda API or AWS CLI.

To start, [review the
resource-based policy](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md") on the Lambda console. Identify the policy statement
that has `Principal` field values that make the policy public, such as
`"*"` or `{ "AWS": "*" }`.

You cannot edit the policy from the console. To remove permissions from the
function, run the [remove-permission](../../../cli/latest/reference/lambda/remove-permission.md "../../../cli/latest/reference/lambda/remove-permission.md") command from the AWS CLI.

```
$ aws lambda remove-permission --function-name `<function-name>` --statement-id `<statement-id>`
```

Replace `<function-name>` with the name
of the Lambda function, and `<statement-id>`
with the statement ID (`Sid`) of the statement that you want to
remove.

## [Lambda.2] Lambda functions should use supported

runtimes

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2, NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5
SI-2(4), NIST.800-53.r5 SI-2(5), PCI DSS v4.0.1/12.3.4

**Category:** Protect > Secure development

**Severity:** Medium

**Resource type:**
`AWS::Lambda::Function`

**AWS Config rule:**
[lambda-function-settings-check](../../../config/latest/developerguide/lambda-function-settings-check.md "../../../config/latest/developerguide/lambda-function-settings-check.md")

**Schedule type:** Change triggered

**Parameters:**

- `runtime`: `dotnet8, java25, java21, java17, java11,
java8.al2, nodejs24.x, nodejs22.x, nodejs20.x, python3.14, python3.13, python3.12, python3.11,
python3.10, ruby3.4, ruby3.3, ruby3.2` (not
  customizable)

This control checks whether AWS Lambda function runtime settings match the expected
values set for the supported runtimes in each language. The control fails if the Lambda
function doesn't use a supported runtime, as noted in the Parameters section. Security Hub CSPM
ignores functions that have a package type of `Image`.

Lambda runtimes are built around a combination of operating system, programming
language, and software libraries that are subject to maintenance and security updates.
When a runtime component is no longer supported for security updates, Lambda deprecates
the runtime. Even though you can't create functions that use the deprecated runtime, the
function is still available to process invocation events. We recommend ensuring that
your Lambda functions are current and don't use deprecated runtime environments. For a
list of supported runtimes, see [Lambda runtimes](../../../lambda/latest/dg/lambda-runtimes.md "../../../lambda/latest/dg/lambda-runtimes.md") in the _AWS Lambda Developer Guide_.

### Remediation

For more information about supported runtimes and deprecation schedules, see
[Runtime deprecation policy](../../../lambda/latest/dg/runtime-support-policy.md "../../../lambda/latest/dg/runtime-support-policy.md") in the _AWS Lambda Developer Guide_. When you migrate your runtimes to the latest
version, follow the syntax and guidance from the publishers of the language. We also
recommend applying [runtime
updates](../../../lambda/latest/dg/runtimes-update.md#runtime-management-controls "../../../lambda/latest/dg/runtimes-update.md#runtime-management-controls") to help reduce the risk of impact to your workloads in the rare
event of a runtime version incompatibility.

## [Lambda.3] Lambda functions should be in a VPC

**Related requirements:** PCI DSS v3.2.1/1.2.1, PCI DSS
v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, NIST.800-53.r5 AC-21,
NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5
AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11),
NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21),
NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network
configuration

**Severity:** Low

**Resource type:**
`AWS::Lambda::Function`

**AWS Config rule:**
[lambda-inside-vpc](../../../config/latest/developerguide/lambda-inside-vpc.md "../../../config/latest/developerguide/lambda-inside-vpc.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a Lambda function is deployed in a virtual private cloud
(VPC). The control fails if the Lambda function isn't deployed in a VPC. Security Hub CSPM doesn't
evaluate the VPC subnet routing configuration to determine public reachability. You
might see failed findings for Lambda@Edge resources.

Deploying resources in a VPC strengthens security and control over network
configurations. Such deployments also offer scalability and high fault tolerance across
multiple Availability Zones. You can customize VPC deployments to meet diverse
application requirements.

### Remediation

To configure an existing function to connect to private subnets in your VPC, see
[Configuring VPC access](../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring "../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring") in the
_AWS Lambda Developer Guide_. We recommend choosing at least two private
subnets for high availability and at least one security group that meets the
connectivity requirements of the function.

## [Lambda.5] VPC Lambda functions should operate in multiple

Availability Zones

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5
SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::Lambda::Function`

**AWS Config rule:**
[lambda-vpc-multi-az-check](../../../config/latest/developerguide/lambda-vpc-multi-az-check.md "../../../config/latest/developerguide/lambda-vpc-multi-az-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter           | Description                          | Type | Allowed custom values | Security Hub CSPM default value |
| ------------------- | ------------------------------------ | ---- | --------------------- | ------------------------------- |
| `availabilityZones` | Minimum number of Availability Zones | Enum | `2, 3, 4, 5, 6`       | `2`                             |

This control checks if an AWS Lambda function that connects to a virtual private cloud
(VPC) operates in at least the specified number of Availability Zone (AZs). The control
fails if the function doesn't operate in at least the specified number of AZs. Unless
you provide a custom parameter value for the minimum number of AZs, Security Hub CSPM uses a default
value of two AZs.

Deploying resources across multiple AZs is an AWS best practice to ensure high
availability within your architecture. Availability is a core pillar in the
confidentiality, integrity, and availability triad security model. All Lambda functions
that connect to a VPC should have a multi-AZ deployment to ensure that a single zone of
failure doesn't cause a total disruption of operations.

### Remediation

If you configure your function to connect to a VPC in your account, specify
subnets in multiple AZs to ensure high availability. For instructions, see [Configuring VPC access](../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring "../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring") in the
_AWS Lambda Developer Guide_.

Lambda automatically runs other functions in multiple AZs to ensure that it is
available to process events in case of a service interruption in a single
zone.

## [Lambda.6] Lambda functions should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Lambda::Function`

**AWS Config rule:**
`tagged-lambda-function` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`              |

This control checks whether an AWS Lambda function has tags with the specific keys
defined in the parameter `requiredTagKeys`. The control fails if the function
doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter
`requiredTagKeys`. If the parameter `requiredTagKeys` isn't
provided, the control only checks for the existence of a tag key and fails if the
function isn't tagged with any key. System tags, which are automatically applied and
begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an
optional value. You can create tags to categorize resources by purpose, owner,
environment, or other criteria. Tags can help you identify, organize, search for, and
filter resources. Tagging also helps you track accountable resource owners for actions
and notifications. When you use tagging, you can implement attribute-based access
control (ABAC) as an authorization strategy, which defines permissions based on tags.
You can attach tags to IAM entities (users or roles) and to AWS resources. You can
create a single ABAC policy or a separate set of policies for your IAM principals. You
can design these ABAC policies to allow operations when the principal's tag matches the
resource tag. For more information, see [What is
ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or
sensitive information in tags. Tags are accessible to many AWS services, including
AWS Billing. For more tagging best practices, see [Tagging your
AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the _AWS General Reference_.

### Remediation

To add tags to a Lambda function, see [Using tags
on Lambda functions](../../../lambda/latest/dg/configuration-tags.md "../../../lambda/latest/dg/configuration-tags.md") in the _AWS Lambda Developer Guide_.

## [Lambda.7] Lambda functions should have AWS X-Ray active

tracing enabled

**Related requirements:** NIST.800-53.r5 CA-7

**Category:** Identify > Logging

**Severity:** Low

**Resource type:**
`AWS::Lambda::Function`

**AWS Config rule:**
[lambda-function-xray-enabled](../../../config/latest/developerguide/lambda-function-xray-enabled.md "../../../config/latest/developerguide/lambda-function-xray-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether active tracing with AWS X-Ray is enabled for an AWS Lambda
function. The control fails if active tracing with X-Ray is disabled for the Lambda
function.

AWS X-Ray can provide tracing and monitoring capabilities for AWS Lambda functions,
which can save time and effort debugging and operating Lambda functions. It can help you
diagnose errors and identify performance bottlenecks, slowdowns, and timeouts by
breaking down latency for Lambda functions. It can also help with data privacy and
compliance requirements. If you enable active tracing for a Lambda function, X-Ray
provides a holistic view of data flow and processing within the Lambda function, which
can help you identify potential security vulnerabilities or non-compliant data handling
practices. This visibility can help you maintain data integrity, confidentiality, and
compliance with relevant regulations.

###### Note

AWS X-Ray tracing is currently not supported for Lambda functions with Amazon Managed Streaming for Apache Kafka
(Amazon MSK), self-managed Apache Kafka, Amazon MQ with ActiveMQ and RabbitMQ, or Amazon DocumentDB
event source mappings.

### Remediation

For information about enabling active tracing for an AWS Lambda function, see
[Visualize
Lambda function invocations using AWS X-Ray](../../../lambda/latest/dg/services-xray.md "../../../lambda/latest/dg/services-xray.md") in the _AWS Lambda Developer Guide_.
