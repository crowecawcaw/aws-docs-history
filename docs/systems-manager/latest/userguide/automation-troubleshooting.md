# Troubleshooting Systems Manager Automation

Use the following information to help you troubleshoot problems with AWS Systems Manager
Automation, a tool in AWS Systems Manager. This topic includes specific tasks to resolve issues
based on Automation error messages.

###### Topics

- [Common Automation errors](#automation-trbl-common "#automation-trbl-common")
- [Automation execution failed to
  start](#automation-trbl-access "#automation-trbl-access")
- [Execution started, but status is
  failed](#automation-trbl-exstrt "#automation-trbl-exstrt")
- [Execution started, but timed out](#automation-trbl-to "#automation-trbl-to")

## Common Automation errors

This section includes information about common Automation errors.

### VPC not defined 400

By default, when Automation runs either the `AWS-UpdateLinuxAmi`
runbook or the `AWS-UpdateWindowsAmi` runbook, the system creates a
temporary instance in the default VPC (172.30.0.0/16). If you deleted the
default VPC, you will receive the following error:

`VPC not defined 400`

To solve this problem, you must specify a value for the `SubnetId`
input parameter.

## Automation execution failed to

start

An automation can fail with an access denied error or an invalid assume role error
if you haven't properly configured AWS Identity and Access Management (IAM) roles, and policies for
Automation.

### Access denied

The following examples describe situations when an automation failed to start
with an access denied error.

###### Access Denied to Systems Manager API

**Error message**: `User:
 user arn isn't authorized to perform: ssm:StartAutomationExecution on
 resource: document arn (Service: AWSSimpleSystemsManagement; Status
 Code: 400; Error Code: AccessDeniedException; Request ID:
 xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)`

- Possible cause 1: The user attempting to start the automation doesn't
  have permission to invoke the `StartAutomationExecution` API. To resolve this issue, attach
  the required IAM policy to the user that was used to start the
  automation.
- Possible cause 2: The user attempting to start the automation has
  permission to invoke the `StartAutomationExecution` API but doesn't have permission to
  invoke the API by using the specific runbook. To resolve this issue,
  attach the required IAM policy to the user that was used to start the
  automation.

###### Access denied due to missing PassRole permissions

**Error message**: `User:
 user arn isn't authorized to perform: iam:PassRole on resource:
 automation assume role arn (Service: AWSSimpleSystemsManagement; Status
 Code: 400; Error Code: AccessDeniedException; Request ID:
 xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)`

The user attempting to start the automation doesn't have PassRole permission
for the assume role. To resolve this issue, attach the iam:PassRole policy to
the role of the user attempting to start the automation. For more information,
see [Task 2: Attach the iam:PassRole policy
to your Automation role](automation-setup-iam.md#attach-passrole-policy "automation-setup-iam.md#attach-passrole-policy").

### Invalid assume role

When you run an Automation, an assume role is either provided in the runbook
or passed as a parameter value for the runbook. Different types of errors can
occur if the assume role isn't specified or configured properly.

###### Malformed Assume Role

**Error message**: `The
 format of the supplied assume role ARN isn't valid.` The assume
role is improperly formatted. To resolve this issue, verify that a valid
assume role is specified in your runbook or as a runtime parameter when
starting the automation.

###### Assume role can't be assumed

**Error message**: `The
 defined assume role is unable to be assumed. (Service:
 AWSSimpleSystemsManagement; Status Code: 400; Error Code:
 InvalidAutomationExecutionParametersException; Request ID:
 xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)`

- Possible cause 1: The assume role doesn't exist. To resolve this
  issue, create the role. For more information, see [Setting up Automation](automation-setup.md "automation-setup.md"). Specific details for creating this
  role are described in the following topic, [Task 1: Create a service role for
  Automation](automation-setup-iam.md#create-service-role "automation-setup-iam.md#create-service-role").
- Possible cause 2: The assume role doesn't have a trust relationship
  with the Systems Manager service. To resolve this issue, create the trust
  relationship. For more information, see [I Can't Assume A Role](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_cant-assume-role "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_cant-assume-role") in the
  _IAM User Guide_.

## Execution started, but status is

failed

### Action-specific failures

Runbooks contain steps and steps run in order. Each step invokes one or more
AWS service APIs. The APIs determine the inputs, behavior, and outputs of the
step. There are multiple places where an error can cause a step to fail. Failure
messages indicate when and where an error occurred.

To see a failure message in the Amazon Elastic Compute Cloud (Amazon EC2) console, choose the
**View Outputs** link of the failed step. To see a failure
message from the AWS CLI, call `get-automation-execution`
and look for the `FailureMessage` attribute in a failed
`StepExecution`.

In the following examples, a step associated with the `aws:runInstance` action failed. Each example explores a different
type of error.

###### Missing Image

**Error message**: `Automation Step Execution fails when it's launching the instance(s).
 Get Exception from RunInstances API of ec2 Service. Exception Message
 from RunInstances API: [The image id '[ami id]' doesn't exist (Service:
 AmazonEC2; Status Code: 400; Error Code: InvalidAMIID.NotFound; Request
 ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)]. Please refer to Automation
 Service Troubleshooting Guide for more diagnosis details.`

The `aws:runInstances` action received input for an
`ImageId` that doesn't exist. To resolve this
problem, update the runbook or parameter values with the correct AMI
ID.

###### Assume role policy lacks sufficient permissions

**Error message**: `Automation Step Execution fails when it's launching the instance(s).
 Get Exception from RunInstances API of ec2 Service. Exception Message
 from RunInstances API: [You aren't authorized to perform this operation.
 Encoded authorization failure message: xxxxxxx (Service: AmazonEC2;
 Status Code: 403; Error Code: UnauthorizedOperation; Request ID:
 xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)]. Please refer to Automation
 Service Troubleshooting Guide for more diagnosis details.`

The assume role doesn't have sufficient permission to invoke the `RunInstances` API on EC2 instances. To resolve this
problem, attach an IAM policy to the assume role that has permission to invoke
the `RunInstances` API. For more information, see the
[Create the service roles for Automation using
the console](automation-setup-iam.md "automation-setup-iam.md").

###### Unexpected State

**Error message**: `Step
 fails when it's verifying launched instance(s) are ready to be used.
 Instance i-xxxxxxxxx entered unexpected state: shutting-down. Please
 refer to Automation Service Troubleshooting Guide for more diagnosis
 details.`

- Possible cause 1: There is a problem with the instance or the Amazon EC2
  service. To resolve this problem, login to the instance or review the
  instance system log to understand why the instance started shutting
  down.
- Possible cause 2: The user data script specified for the `aws:runInstances` action has a problem or
  incorrect syntax. Verify the syntax of the user data script. Also,
  verify that the user data scripts doesn't shut down the instance, or
  invoke other scripts that shut down the instance.

###### Action-Specific Failures Reference

When a step fails, the failure message might indicate which service was
being invoked when the failure occurred. The following table lists the
services invoked by each action. The table also provides links to
information about each service.

| Action                     | AWS services invoked by this action | For information about this service                                                                                                               | Troubleshooting content                                                                                                                                               |
| -------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws:runInstances`         | Amazon EC2                          | [Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide.md "../../../AWSEC2/latest/UserGuide.md")                                               | [Troubleshooting EC2 Instances](../../../AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.md "../../../AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.md")        |
| `aws:changeInstanceState`  | Amazon EC2                          | [Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide.md "../../../AWSEC2/latest/UserGuide.md")                                               | [Troubleshooting EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.md "../../../AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.md")        |
| `aws:runCommand`           | Systems Manager                     | [AWS Systems Manager Run Command](run-command.md "run-command.md")                                                                               | [Troubleshooting Systems Manager Run Command](troubleshooting-remote-commands.md "troubleshooting-remote-commands.md")                                                |
| `aws:createImage`          | Amazon EC2                          | [Amazon Machine Images](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md")                                     |                                                                                                                                                                       |
| `aws:createStack`          | AWS CloudFormation                  | [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") | [Troubleshooting AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md") |
| `aws:deleteStack`          | AWS CloudFormation                  | [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") | [Troubleshooting AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md") |
| `aws:deleteImage`          | Amazon EC2                          | [Amazon Machines Images](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md")                                    |                                                                                                                                                                       |
| `aws:copyImage`            | Amazon EC2                          | [Amazon Machine Images](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md")                                     |                                                                                                                                                                       |
| `aws:createTag`            | Amazon EC2, Systems Manager         | [EC2 Resource and Tags](../../../AWSEC2/latest/UserGuide/EC2_Resources.md "../../../AWSEC2/latest/UserGuide/EC2_Resources.md")                   |                                                                                                                                                                       |
| `aws:invokeLambdaFunction` | AWS Lambda                          | [AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md")                                                        | [Troubleshooting Lambda](../../../lambda/latest/dg/monitoring-functions.md "../../../lambda/latest/dg/monitoring-functions.md")                                       | ### Automation service internal error **Error message**: `Internal Server Error. Please refer to Automation Service Troubleshooting Guide for more diagnosis details.` A problem with the Automation service is preventing the specified runbook from running correctly. To resolve this issue, contact AWS Support. Provide the execution ID and customer ID, if available. ## Execution started, but timed out **Error message**: `Step timed out while step is verifying launched instance(s) are ready to be used. Please refer to Automation Service Troubleshooting Guide for more diagnosis details.` A step in the `aws:runInstances` action timed out. This can happen if the step action takes longer to run than the value specified for `timeoutSeconds` in the step. To resolve this issue, specify a longer value for the `timeoutSeconds` parameter in the `aws:runInstances` action. If that doesn't solve the problem, investigate why the step takes longer to run than expected |
