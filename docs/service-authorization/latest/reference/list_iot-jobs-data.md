# Actions, resources, and condition keys for AWS IoT Jobs DataPlane

AWS IoT Jobs DataPlane (service prefix: `iotjobsdata`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../iot/latest/developerguide/what-is-aws-iot.md "../../../iot/latest/developerguide/what-is-aws-iot.md").
- View a list of the [API operations available for
  this service](../../../iot/latest/apireference.md "../../../iot/latest/apireference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../iot/latest/developerguide/authorization.md "../../../iot/latest/developerguide/authorization.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/iotjobsdata/iotjobsdata.json "https://servicereference.us-east-1.amazonaws.com/v1/iotjobsdata/iotjobsdata.json") for this service.

###### Topics

- [API operations defined by AWS IoT Jobs DataPlane](#list_iot-jobs-data-operations "#list_iot-jobs-data-operations")
- [Actions defined by AWS IoT Jobs DataPlane](#list_iot-jobs-data-actions-as-permissions "#list_iot-jobs-data-actions-as-permissions")
- [Resource types defined by AWS IoT Jobs DataPlane](#list_iot-jobs-data-resources-for-iam-policies "#list_iot-jobs-data-resources-for-iam-policies")
- [Condition keys for AWS IoT Jobs DataPlane](#list_iot-jobs-data-policy-keys "#list_iot-jobs-data-policy-keys")

## API operations defined by AWS IoT Jobs DataPlane

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iot-jobs-data-actions-as-permissions "#list_iot-jobs-data-actions-as-permissions").

| Operation                    | IAM action                                                                                                                                                                             | Condition key | Possible value(s) | Access level |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| DescribeJobExecution         | [iotjobsdata:DescribeJobExecution](#list_iot-jobs-data-action-DescribeJobExecution "#list_iot-jobs-data-action-DescribeJobExecution")                                                  |               |                   | Read         |
| GetPendingJobExecutions      | [iotjobsdata:GetPendingJobExecutions](#list_iot-jobs-data-action-GetPendingJobExecutions "#list_iot-jobs-data-action-GetPendingJobExecutions")                                         |               |                   | Read         |
| StartCommandExecution        | [iot:StartCommandExecution](../../../iot/latest/apireference/API_iot-jobs-data_StartCommandExecution.md "../../../iot/latest/apireference/API_iot-jobs-data_StartCommandExecution.md") |               |                   | Write        |
| StartNextPendingJobExecution | [iotjobsdata:StartNextPendingJobExecution](#list_iot-jobs-data-action-StartNextPendingJobExecution "#list_iot-jobs-data-action-StartNextPendingJobExecution")                          |               |                   | Write        |
| UpdateJobExecution           | [iotjobsdata:UpdateJobExecution](#list_iot-jobs-data-action-UpdateJobExecution "#list_iot-jobs-data-action-UpdateJobExecution")                                                        |               |                   | Write        |

## Actions defined by AWS IoT Jobs DataPlane

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                 | Description                                                                                | Resource types (\*required)                                                        | Condition keys                                                             | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------ |
| [DescribeJobExecution](../../../iot/latest/apireference/API_iot-jobs-data_DescribeJobExecution.md "../../../iot/latest/apireference/API_iot-jobs-data_DescribeJobExecution.md")                         | Grants permission to describe a job execution                                              | [thing\*](#list_iot-jobs-data-resource-thing "#list_iot-jobs-data-resource-thing") | [iot:JobId](#list_iot-jobs-data-iot_JobId "#list_iot-jobs-data-iot_JobId") | Read         |
| [GetPendingJobExecutions](../../../iot/latest/apireference/API_iot-jobs-data_GetPendingJobExecutions.md "../../../iot/latest/apireference/API_iot-jobs-data_GetPendingJobExecutions.md")                | Grants permission to get the list of all jobs for a thing that are not in a terminal state | [thing\*](#list_iot-jobs-data-resource-thing "#list_iot-jobs-data-resource-thing") |                                                                            | Read         |
| [StartNextPendingJobExecution](../../../iot/latest/apireference/API_iot-jobs-data_StartNextPendingJobExecution.md "../../../iot/latest/apireference/API_iot-jobs-data_StartNextPendingJobExecution.md") | Grants permission to get and start the next pending job execution for a thing              | [thing\*](#list_iot-jobs-data-resource-thing "#list_iot-jobs-data-resource-thing") |                                                                            | Write        |
| [UpdateJobExecution](../../../iot/latest/apireference/API_iot-jobs-data_UpdateJobExecution.md "../../../iot/latest/apireference/API_iot-jobs-data_UpdateJobExecution.md")                               | Grants permission to update a job execution                                                | [thing\*](#list_iot-jobs-data-resource-thing "#list_iot-jobs-data-resource-thing") | [iot:JobId](#list_iot-jobs-data-iot_JobId "#list_iot-jobs-data-iot_JobId") | Write        |

## Resource types defined by AWS IoT Jobs DataPlane

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                       | ARN                                                          | Condition keys |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------- |
| [thing](../../../iot/latest/developerguide/thing-registry.md "../../../iot/latest/developerguide/thing-registry.md") | arn:${Partition}:iot:${Region}:${Account}:thing/${ThingName} |                |

## Condition keys for AWS IoT Jobs DataPlane

AWS IoT Jobs DataPlane defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                               | Description                                                                                          | Type   |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------ |
| [iot:JobId](list_awsiot.md "list_awsiot.md") | Filters access by jobId for iotjobsdata:DescribeJobExecution and iotjobsdata:UpdateJobExecution APIs | String |
