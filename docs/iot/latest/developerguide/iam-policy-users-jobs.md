# Authorizing users and cloud services to use

AWS IoT Jobs

To authorize your users and cloud services, you must use IAM policies on both the
control plane and data plane. The policies must be used with HTTPS protocol and must use
AWS Signature Version 4 authentication (port 443) to authenticate users.

###### Note

AWS IoT Core policies must not be used on the control plane. Only IAM policies are
used for authorizing users or Cloud Services. For more information about using the
required policy type, see [Required policy type for AWS IoT Jobs](iot-jobs-security.md#jobs-required-policy "iot-jobs-security.md#jobs-required-policy").

IAM policies are JSON documents that contain policy statements. Policy statements
use _Effect_, _Action_, and _Resource_ elements to specify
resources, allowed or denied actions, and conditions under which actions are allowed or
denied. For more information, see [IAM
JSON Policy Elements Reference](../../../service-authorization/latest/reference/reference_policies_elements.md "../../../service-authorization/latest/reference/reference_policies_elements.md") in the
_IAM user Guide_.

###### Warning

We recommend that you don't use wildcard permissions, such as `"Action":
 ["iot:*"]` in your IAM policies or AWS IoT Core policies. Using wildcard
permissions is not a recommended security best practice. For more information, see
[AWS IoT
policy overly permissive](../../../iot-device-defender/latest/devguide/audit-chk-iot-policy-permissive.md "../../../iot-device-defender/latest/devguide/audit-chk-iot-policy-permissive.md").

## IAM policies on the control plane

On the control plane, IAM policies use the `iot:` prefix with the
action to authorize the corresponding jobs API operation. For example, the
`iot:CreateJob` policy action grants the user permission to use the
[`CreateJob`](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md")
API.

The following table shows a list of IAM policy actions and permissions to
use the API actions. For information about resource types, see [Resource types defined by AWS IoT](../../../service-authorization/latest/reference/list_awsiot.md#awsiot-job "../../../service-authorization/latest/reference/list_awsiot.md#awsiot-job"). For more information about AWS IoT
actions, see [Actions
defined by AWS IoT](../../../service-authorization/latest/reference/list_awsiot.md "../../../service-authorization/latest/reference/list_awsiot.md").

| IAM policy actions on control plane | Policy action                                                                                                                         | API operation                                                  | Resource types                                                                                                                                                                                          | Description |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `iot:AssociateTargetsWithJob`       | [`AssociateTargetsWithJob`](../apireference/API_AssociateTargetsWithJob.md "../apireference/API_AssociateTargetsWithJob.md")          | • job<br>• thing<br>• thinggroup                               | Represents the permission to associate a group with a<br>continuous job. The `iot:AssociateTargetsWithJob`<br>permission is checked every time a request is made to associate<br>targets.               |
| `iot:CancelJob`                     | [`CancelJob`](../apireference/API_CancelJob.md "../apireference/API_CancelJob.md")                                                    | job                                                            | Represents the permission to cancel a job. The<br>`iot:CancelJob` permission is checked every time<br>a request is made to cancel a job.                                                                |
| `iot:CancelJobExecution`            | [`CancelJobExecution`](../apireference/API_CancelJobExecution.md "../apireference/API_CancelJobExecution.md")                         | • job<br>• thing                                               | Represents the permission to cancel a job execution. The<br>`iot: CancelJobExecution` permission is checked<br>every time a request is made to cancel a job execution.                                  |
| `iot:CreateJob`                     | [`CreateJob`](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md")                                                    | • job<br>• thing<br>• thinggroup<br>• jobtemplate<br>• package | Represents the permission to create a job. The `iot:<br>CreateJob` permission is checked every time a request<br>is made to create a job.                                                               |
| `iot:CreateJobTemplate`             | [`CreateJobTemplate`](../apireference/API_CreateJobTemplate.md "../apireference/API_CreateJobTemplate.md")                            | • job<br>• jobtemplate<br>• package                            | Represents the permission to create a job template. The<br>`iot: CreateJobTemplate` permission is checked<br>every time a request is made to create a job template.                                     |
| `iot:DeleteJob`                     | [`DeleteJob`](../apireference/API_DeleteJob.md "../apireference/API_DeleteJob.md")                                                    | job                                                            | Represents the permission to delete a job. The `iot:<br>DeleteJob` permission is checked every time a request<br>is made to delete a job.                                                               |
| `iot:DeleteJobTemplate`             | [`DeleteJobTemplate`](../apireference/API_DeleteJobTemplate.md "../apireference/API_DeleteJobTemplate.md")                            | jobtemplate                                                    | Represents the permission to delete a job template. The<br>`iot: CreateJobTemplate` permission is checked<br>every time a request is made to delete a job template.                                     |
| `iot:DeleteJobExecution`            | [`DeleteJobTemplate`](../apireference/API_DeleteJobExecution.md "../apireference/API_DeleteJobExecution.md")                          | • job<br>• thing                                               | Represents the permission to delete a job execution. The<br>`iot: DeleteJobExecution` permission is checked<br>every time a request is made to delete a job execution.                                  |
| `iot:DescribeJob`                   | [`DescribeJob`](../apireference/API_DescribeJob.md "../apireference/API_DescribeJob.md")                                              | job                                                            | Represents the permission to describe a job. The `iot:<br>DescribeJob` permission is checked every time a<br>request is made to describe a job.                                                         |
| `iot:DescribeJobExecution`          | [`DescribeJobExecution`](../apireference/API_DescribeJobExecution.md "../apireference/API_DescribeJobExecution.md")                   | • job<br>• thing                                               | Represents the permission to describe a job execution. The<br>`iot: DescribeJobExecution` permission is checked<br>every time a request is made to describe a job<br>execution.                         |
| `iot:DescribeJobTemplate`           | [`DescribeJobTemplate`](../apireference/API_DescribeJobTemplate.md "../apireference/API_DescribeJobTemplate.md")                      | jobtemplate                                                    | Represents the permission to describe a job template. The<br>`iot: DescribeJobTemplate` permission is checked<br>every time a request is made to describe a job template.                               |
| `iot:DescribeManagedJobTemplate`    | [`DescribeManagedJobTemplate`](../apireference/API_DescribeManagedJobTemplate.md "../apireference/API_DescribeManagedJobTemplate.md") | jobtemplate                                                    | Represents the permission to describe a managed job template.<br>The `iot: DescribeManagedJobTemplate` permission is<br>checked every time a request is made to describe a managed job<br>template.     |
| `iot:GetJobDocument`                | [`GetJobDocument`](../apireference/API_GetJobDocument.md "../apireference/API_GetJobDocument.md")                                     | job                                                            | Represents the permission to get the job document for a job.<br>The `iot:GetJobDocument` permission is checked<br>every time a request is made to get a job document.                                   |
| `iot:ListJobExecutionsForJob`       | [`ListJobExecutionsForJob`](../apireference/API_ListJobExecutionsForJob.md "../apireference/API_ListJobExecutionsForJob.md")          | job                                                            | Represents the permission to list the job executions for a<br>job. The `iot:ListJobExecutionsForJob` permission is<br>checked every time a request is made to list the job executions<br>for a job.     |
| `iot:ListJobExecutionsForThing`     | [`ListJobExecutionsForThing`](../apireference/API_ListJobExecutionsForThing.md "../apireference/API_ListJobExecutionsForThing.md")    | thing                                                          | Represents the permission to list the job executions for a<br>job. The `iot:ListJobExecutionsForThing` permission<br>is checked every time a request is made to list the job<br>executions for a thing. |
| `iot:ListJobs`                      | [`ListJobs`](../apireference/API_ListJobs.md "../apireference/API_ListJobs.md")                                                       | none                                                           | Represents the permission to list the jobs. The<br>`iot:ListJobs` permission is checked every time a<br>request is made to list the jobs.                                                               |
| `iot:ListJobTemplates`              | [`ListJobTemplates`](../apireference/API_ListJobTemplates.md "../apireference/API_ListJobTemplates.md")                               | none                                                           | Represents the permission to list the job templates. The<br>`iot:ListJobTemplates` permission is checked<br>every time a request is made to list the job<br>templates.                                  |
| `iot:ListManagedJobTemplates`       | [`ListManagedJobTemplates`](../apireference/API_ListManagedJobTemplates.md "../apireference/API_ListManagedJobTemplates.md")          | none                                                           | Represents the permission to list the managed job templates.<br>The `iot:ListManagedJobTemplates` permission is<br>checked every time a request is made to list the managed job<br>templates.           |
| `iot:UpdateJob`                     | [`UpdateJob`](../apireference/API_UpdateJob.md "../apireference/API_UpdateJob.md")                                                    | job                                                            | Represents the permission to update a job. The<br>`iot:UpdateJob` permission is checked every time<br>a request is made to update a job.                                                                |
| `iot:TagResource`                   | [`TagResource`](../apireference/API_TagResource.md "../apireference/API_TagResource.md")                                              | • job<br>• jobtemplate<br>• thing                              | Grants permission to tag a specific resource.                                                                                                                                                           |
| `iot:UntagResource`                 | [`UntagResource`](../apireference/API_UntagResource.md "../apireference/API_UntagResource.md")                                        | • job<br>• jobtemplate<br>• thing                              | Grants permission to untag a specific resource.                                                                                                                                                         |

The following example shows an IAM policy that allows the user permission to
perform the following actions for your IoT thing and thing group.

In the example, replace:

- `region` with your AWS Region, such as
  `us-east-1`.
- `account-id` with your AWS account number,
  such as `57EXAMPLE833`.
- `thing-group-name` with the name of your
  IoT thing group for which you're targeting jobs, such as
  `FirmwareUpdateGroup`.
- `thing-name` with the name of your IoT thing
  for which you're targeting jobs, such as
  `MyIoTThing`.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iot:CreateJobTemplate",
 "iot:CreateJob"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:thinggroup/`thing-group-name`"
 },
 {
 "Action": [
 "iot:DescribeJob",
 "iot:CancelJob",
 "iot:DeleteJob"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:job/*"
 },
 {
 "Action": [
 "iot:DescribeJobExecution",
 "iot:CancelJobExecution",
 "iot:DeleteJobExecution"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:thing/thing-123",
 "arn:aws:iot:`us-east-1`:`123456789012`:job/*"
 ]
 }
 ]
}`

```

You can restrict _principals_ from making
API calls to your control plane endpoint from specific IP addresses. To
specify the IP addresses that can be allowed, in the Condition element of
your IAM policy, use the [`aws:SourceIp`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip") global condition key.

Using this condition key can also deny access to other AWS services from
making these API calls on your behalf, such as AWS CloudFormation. To allow access to
these services, use the [`aws:ViaAWSService`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-viaawsservice "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-viaawsservice") global condition key with the
aws:SourceIp key. This
makes
sure that the source IP address access restriction
applies only to requests that are made directly by a principal. For more
information, see [AWS: Denies access to AWS based on the source IP](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md").

The following example shows how to allow only a specific IP address that
can make API calls to the control plane endpoint. The
`aws:ViaAWSService` key is set to `true`, which
allows other services to make API calls on your behalf.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:CreateJobTemplate",
 "iot:CreateJob"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": "`123.45.167.89`"
 },
 "Bool": {
 "aws:ViaAWSService": "false"
 }
 }
 }]
}`

```

## IAM policies on the data plane

IAM policies on the data plane use the `iotjobsdata:` prefix to
authorize jobs API operations that users can perform. On the data plane, you can
grant a user permission to use the [`DescribeJobExecution`](../apireference/API_iot-jobs-data_DescribeJobExecution.md "../apireference/API_iot-jobs-data_DescribeJobExecution.md") API by using the
`iotjobsdata:DescribeJobExecution` policy action.

###### Warning

Using IAM policies on the data plane is not recommended when targeting AWS IoT
Jobs for your devices. We recommend that you use IAM policies on the control
plane for users to create and manage jobs. On the data plane, for authorizing
devices to retrieve job executions and update the execution status, use
[AWS IoT Core policies for HTTPS protocol](iot-data-plane-jobs.md#iot-jobs-data-http "iot-data-plane-jobs.md#iot-jobs-data-http").

The API operations that must be authorized are usually performed by
you
typing CLI commands. The following shows an example of a user performing a
`DescribeJobExecution` operation.

In the example, replace:

- `region` with your AWS Region, such as
  `us-east-1`.
- `account-id` with your AWS account number,
  such as `57EXAMPLE833`.
- `thing-name` with the name of your IoT thing
  for which you're targeting jobs, such as
  `myRegisteredThing`.
- `job-id` is the unique
  identifier for the job that's targeted using the API.

```
aws iot-jobs-data describe-job-execution \
    --endpoint-url "https://`account-id`.jobs.iot.`region`.amazonaws.com" \
    --job-id `jobID` --thing-name `thing-name`

```

The following shows a sample IAM policy that authorizes this action:

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": [
 "iotjobsdata:DescribeJobExecution"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:thing/thing-123"
 }
}`

```

You can restrict _principals_ from making
API calls to your data plane endpoint from specific IP addresses. To specify
the IP addresses that can be allowed, in the Condition element of your IAM
policy, use the [`aws:SourceIp`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip") global condition key.

Using this condition key can also deny access to other AWS services from
making these API calls on your behalf, such as AWS CloudFormation. To allow access to
these services, use the [`aws:ViaAWSService`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-viaawsservice "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-viaawsservice") global condition key with the
`aws:SourceIp` condition key. This makes sure that the IP
address access restriction only applies to requests that are directly made
by the principal. For more information, see [AWS: Denies access to AWS based on the source IP](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md").

The following example shows how to allow only a specific IP address that
can make API calls to the data plane endpoint.

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "iotjobsdata:*"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": "`123.45.167.89`"
 },
 "Bool": {
 "aws:ViaAWSService": "false"
 }
 }
 }]
}`

```

The following example shows how to restrict specific IP addresses or
address ranges from making API calls to the data plane endpoint.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "iotjobsdata:*"
 ],
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "`123.45.167.89`",
 "`192.0.2.0/24`",
 "`203.0.113.0/24`"
 ]
 }
 },
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

If you perform an API operation on both the control plane and data plane,
your control plane policy action must use the `iot:` prefix, and
your data plane policy action must use the `iotjobsdata:` prefix.

For example, the `DescribeJobExecution` API can be used in both
the control plane and data plane. On the control plane, the [DescribeJobExecution](../apireference/API_DescribeJobExecution.md "../apireference/API_DescribeJobExecution.md")
API is used to describe a job execution. On the data plane, the [DescribeJobExecution](../apireference/API_iot-jobs-data_DescribeJobExecution.md "../apireference/API_iot-jobs-data_DescribeJobExecution.md") API is used to get details of a job execution.

The following IAM policy authorizes a user permission to use the
`DescribeJobExecution` API on both the control plane and data
plane.

In the example, replace:

- `region` with your AWS Region, such as
  `us-east-1`.
- `account-id` with your AWS account number,
  such as `57EXAMPLE833`.
- `thing-name` with the name of your IoT thing
  for which you're targeting jobs, such as
  `MyIoTThing`.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iotjobsdata:DescribeJobExecution"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:thing/thing-123"
 },
 {
 "Action": [
 "iot:DescribeJobExecution",
 "iot:CancelJobExecution",
 "iot:DeleteJobExecution"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:thing/thing-123",
 "arn:aws:iot:`us-east-1`:`123456789012`:job/*"
 ]
 }
 ]
}`

```

## Authorize tagging of IoT resources

For better control over jobs and job templates that you can create, modify, or
use, you can attach tags to the jobs or job templates. Tags also help you discern
ownership and assign and allocate costs by placing them in billing groups and
attaching tags to them.

When a user wants to tag their jobs or job templates that they created by using
the AWS Management Console or the AWS CLI, your IAM policy must grant the user permissions to tag
them. To grant permissions, your IAM policy must use the
`iot:TagResource` action.

###### Note

If your IAM policy doesn't include the `iot:TagResource` action,
then any [`CreateJob`](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md") or [`CreateJobTemplate`](../apireference/API_CreateJobTemplate.md "../apireference/API_CreateJobTemplate.md") with a tag will return an
`AccessDeniedException` error.

When you want to tag your jobs or job templates that you created by using the
AWS Management Console or the AWS CLI, your IAM policy must grant permission to tag them. To
grant permissions, your IAM policy must use the `iot:TagResource`
action.

For general information about tagging your resources, see [Tagging your AWS IoT resources](tagging-iot.md "tagging-iot.md").

Refer to the following IAM policy examples granting tagging
permissions:

_Example 1_

A user that runs the following command to create a job and tag it to a
specific environment.

In this example, replace:

- `region` with your AWS Region, such as
  `us-east-1`.
- `account-id` with your AWS account number,
  such as `57EXAMPLE833`.
- `thing-name` with the name of your IoT thing
  for which you're targeting jobs, such as
  `MyIoTThing`.

```
aws iot create-job
    --job-id `test_job`
    --targets "arn:aws:iot:`region`:`account-id`:thing/`thingOne`"
    --document-source "https://s3.amazonaws.com/amzn-s3-demo-bucket/job-document.json"
    --description "test job description"
    --tags Key=environment,Value=beta
```

For this example, you must use the following IAM policy:

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": [
 "iot:CreateJob",
 "iot:CreateJobTemplate",
 "iot:TagResource"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:job/*",
 "arn:aws:iot:`us-east-1`:`123456789012`:jobtemplate/*"
 ]
 }
}`

```
