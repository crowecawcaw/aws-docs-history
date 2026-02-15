# Authorizing your devices to securely use AWS IoT Jobs on the

data plane

To authorize your devices to interact securely with AWS IoT Jobs on the data plane, you
must use AWS IoT Core policies. AWS IoT Core policies for jobs are JSON documents containing
policy statements. These policies also use _Effect_,
_Action_, and _Resource_ elements, and follow a similar convention to IAM policies.
For more information about the elements, see [IAM
JSON Policy Elements Reference](../../../service-authorization/latest/reference/reference_policies_elements.md "../../../service-authorization/latest/reference/reference_policies_elements.md") in the _IAM user
Guide_.

The policies can be used with both MQTT and HTTPS protocols and must use TCP or TLS
mutual authentication to authenticate the devices. The following shows how to use these
policies across the different communication protocols.

###### Warning

We recommend that you don't use wildcard permissions, such as `"Action":
 ["iot:*"]` in your IAM policies or AWS IoT Core policies. Using wildcard
permissions is not a recommended security best practice. For more information, see
[AWS IoT
policy overly permissive](../../../iot-device-defender/latest/devguide/audit-chk-iot-policy-permissive.md "../../../iot-device-defender/latest/devguide/audit-chk-iot-policy-permissive.md").

## AWS IoT Core policies for MQTT protocol

AWS IoT Core policies for MQTT protocol grant you permissions to use the jobs device
MQTT API actions. The MQTT API operations are used to work with MQTT topics that are
reserved for jobs commands. For more information about these API operations, see
[Jobs device MQTT API operations](jobs-mqtt-api.md "jobs-mqtt-api.md").

MQTT policies use policy actions such as `iot:Connect`,
`iot:Publish`, `iot:Subscribe`, and
`iot:Receieve` to work with the jobs topics. These policies allow you
to connect to the message broker, subscribe to the jobs MQTT topics, and send and
receive MQTT messages between your devices and the cloud. For more information about
these actions, see [AWS IoT Core policy actions](iot-policy-actions.md "iot-policy-actions.md").

For information about topics for AWS IoT Jobs, see [Job topics](reserved-topics.md#reserved-topics-job "reserved-topics.md#reserved-topics-job").

The following example shows how you can use `iot:Publish` and
`iot:Subscribe` to publish and subscribe to jobs and job
executions.

In the example, replace:

- `region` with your AWS Region, such as
  `us-east-1`.
- `account-id` with your AWS account number,
  such as `57EXAMPLE833`.
- `thing-name` with the name of your IoT
  thing for which you're targeting jobs, such as
  `MyIoTThing`.

```
`{
 "Version":"2012-10-17",

 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish",
 "iot:Subscribe"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:topic/$aws/events/job/*",
 "arn:aws:iot:`us-east-1`:`123456789012`:topic/$aws/events/jobExecution/*",
 "arn:aws:iot:`us-east-1`:`123456789012`:topic/$aws/things/thing-123/jobs/*"
 ]
 }
 ]
}`

```

## AWS IoT Core policies for HTTPS protocol

AWS IoT Core policies on the data plane can also use the HTTPS protocol with the TLS
authentication mechanism to authorize your devices. On the data plane, policies use
the `iotjobsdata:` prefix to authorize jobs API operations that your
devices can perform. For example, the `iotjobsdata:DescribeJobExecution`
policy action grants the user permission to use the [`DescribeJobExecution`](../apireference/API_iot-jobs-data_DescribeJobExecution.md "../apireference/API_iot-jobs-data_DescribeJobExecution.md") API.

###### Note

The data plane policy actions must use the `iotjobsdata:` prefix.
On the control plane, the actions must use the `iot:` prefix. For an
example IAM policy when both control plane and data plane policy actions are
used, see [IAM policy example for both control
plane and data plane](iam-policy-users-jobs.md#iam-data-plane-example2 "iam-policy-users-jobs.md#iam-data-plane-example2").

The following table shows a list of AWS IoT Core policy actions and
permissions for authorizing devices to use the API actions.
For a list of API operations that you can perform in the data plane, see
[Jobs device HTTP API](jobs-http-device-api.md "jobs-http-device-api.md").

###### Note

These job execution policy actions apply only to the HTTP TLS
endpoint. If you use the MQTT endpoint, you must use the MQTT policy
actions defined previously.

| AWS IoT Core policy actions on data plane  | Policy action                                                                                                                                                 | API operation    | Resource types                                                                                                                                                                                                                                                                                                             | Description |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `iotjobsdata:DescribeJobExecution`         | [`DescribeJobExecution`](../apireference/API_iot-jobs-data_DescribeJobExecution.md "../apireference/API_iot-jobs-data_DescribeJobExecution.md")               | • job<br>• thing | Represents the permission to retrieve a job execution.<br>The `iotjobsdata:DescribeJobExecution` permission<br>is checked every time a request is made to retrieve a job<br>execution.                                                                                                                                     |
| `iotjobsdata:GetPendingJobExecutions`      | [`GetPendingJobExecutions`](../apireference/API_iot-jobs-data_GetPendingJobExecutions.md "../apireference/API_iot-jobs-data_GetPendingJobExecutions.md")      | thing            | Represents the permission to retrieve the list of jobs<br>that are not in a terminal status for a thing. The<br>`iotjobsdata:GetPendingJobExecutions`<br>permission is checked every time a request is made to<br>retrieve the list.                                                                                       |
| `iotjobsdata:StartNextPendingJobExecution` | [`StartNextPendingJobExecution`](../apireference/API_iot-jobs-data_GetPendingJobExecutions.md "../apireference/API_iot-jobs-data_GetPendingJobExecutions.md") | thing            | Represents the permission to get and start the next<br>pending job execution for a thing. That is, to update a job<br>execution with status `QUEUED` to `IN_PROGRESS`.<br>The `iotjobsdata:StartNextPendingJobExecution` permission<br>is checked every time a request is made to start the next<br>pending job execution. |
| `iotjobsdata:UpdateJobExecution`           | [`UpdateJobExecution`](../apireference/API_iot-jobs-data_UpdateJobExecution.md "../apireference/API_iot-jobs-data_UpdateJobExecution.md")                     | thing            | Represents the permission to update a job execution. The<br>`iotjobsdata:UpdateJobExecution` permission is checked every<br>time a request is made to update the state of a job execution.                                                                                                                                 |

The following shows an example of an AWS IoT Core policy that grants
permission to perform the actions on the data plane API operations for any
resource. You can scope your policy to a specific resource, such as an IoT
thing. In your example, replace:

- `region` with your AWS Region such as
  `us-east-1`.
- `account-id` with your AWS account number,
  such as `57EXAMPLE833`.
- `thing-name` with the name of the IoT thing,
  such as `MyIoTthing`.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iotjobsdata:GetPendingJobExecutions",
 "iotjobsdata:StartNextPendingJobExecution",
 "iotjobsdata:DescribeJobExecution",
 "iotjobsdata:UpdateJobExecution"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:thing/thing-123"
 }
 ]
}`

```

An example of when you must use these policies can be when your IoT devices use an
AWS IoT Core policy to access one of these API operations, such as the following example
of the `DescribeJobExecution` API:

```
GET /things/thingName/jobs/jobId?executionNumber=executionNumber&includeJobDocument=includeJobDocument&namespaceId=namespaceId HTTP/1.1
```
