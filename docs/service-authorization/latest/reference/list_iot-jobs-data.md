

# Actions, resources, and condition keys for AWS IoT Jobs DataPlane
<a name="list_iot-jobs-data"></a>

AWS IoT Jobs DataPlane (service prefix: `iotjobsdata`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iot/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotjobsdata/iotjobsdata.json) for this service.

**Topics**
+ [API operations defined by AWS IoT Jobs DataPlane](#list_iot-jobs-data-operations)
+ [Actions defined by AWS IoT Jobs DataPlane](#list_iot-jobs-data-actions-as-permissions)
+ [Resource types defined by AWS IoT Jobs DataPlane](#list_iot-jobs-data-resources-for-iam-policies)
+ [Condition keys for AWS IoT Jobs DataPlane](#list_iot-jobs-data-policy-keys)

## API operations defined by AWS IoT Jobs DataPlane
<a name="list_iot-jobs-data-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iot-jobs-data-actions-as-permissions).




- **   DescribeJobExecution  **
  - **IAM action:**  [iotjobsdata:DescribeJobExecution](#list_iot-jobs-data-action-DescribeJobExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPendingJobExecutions  **
  - **IAM action:**  [iotjobsdata:GetPendingJobExecutions](#list_iot-jobs-data-action-GetPendingJobExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartCommandExecution  **
  - **IAM action:**  [iot:StartCommandExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_StartCommandExecution.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNextPendingJobExecution  **
  - **IAM action:**  [iotjobsdata:StartNextPendingJobExecution](#list_iot-jobs-data-action-StartNextPendingJobExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateJobExecution  **
  - **IAM action:**  [iotjobsdata:UpdateJobExecution](#list_iot-jobs-data-action-UpdateJobExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IoT Jobs DataPlane
<a name="list_iot-jobs-data-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [DescribeJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_DescribeJobExecution.html)  **
  - **Description:** Grants permission to describe a job execution
  - **Resource types (\*required):** [thing\*](#list_iot-jobs-data-resource-thing)
  - **Condition keys:** [iot:JobId](#list_iot-jobs-data-iot_JobId)
  - **Access level:** Read

- **   [GetPendingJobExecutions](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_GetPendingJobExecutions.html)  **
  - **Description:** Grants permission to get the list of all jobs for a thing that are not in a terminal state
  - **Resource types (\*required):** [thing\*](#list_iot-jobs-data-resource-thing)
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartNextPendingJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_StartNextPendingJobExecution.html)  **
  - **Description:** Grants permission to get and start the next pending job execution for a thing
  - **Resource types (\*required):** [thing\*](#list_iot-jobs-data-resource-thing)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateJobExecution](https://docs.aws.amazon.com/iot/latest/apireference/API_iot-jobs-data_UpdateJobExecution.html)  **
  - **Description:** Grants permission to update a job execution
  - **Resource types (\*required):** [thing\*](#list_iot-jobs-data-resource-thing)
  - **Condition keys:** [iot:JobId](#list_iot-jobs-data-iot_JobId)
  - **Access level:** Write



## Resource types defined by AWS IoT Jobs DataPlane
<a name="list_iot-jobs-data-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)  | arn:${Partition}:iot:${Region}:${Account}:thing/${ThingName} |   | 

## Condition keys for AWS IoT Jobs DataPlane
<a name="list_iot-jobs-data-policy-keys"></a>

AWS IoT Jobs DataPlane defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [iot:JobId](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html)  | Filters access by jobId for iotjobsdata:DescribeJobExecution and iotjobsdata:UpdateJobExecution APIs | String | 