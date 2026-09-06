

# Actions, resources, and condition keys for AWS SimSpace Weaver
<a name="list_simspaceweaver"></a>

AWS SimSpace Weaver (service prefix: `simspaceweaver`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/simspaceweaver/simspaceweaver.json) for this service.

**Topics**
+ [Actions defined by AWS SimSpace Weaver](#list_simspaceweaver-actions-as-permissions)
+ [Resource types defined by AWS SimSpace Weaver](#list_simspaceweaver-resources-for-iam-policies)
+ [Condition keys for AWS SimSpace Weaver](#list_simspaceweaver-policy-keys)

## Actions defined by AWS SimSpace Weaver
<a name="list_simspaceweaver-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateSnapshot](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_CreateSnapshot.html)  **
  - **Description:** Grants permission to create a snapshot
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApp](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DeleteApp.html)  **
  - **Description:** Grants permission to delete an app
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSimulation](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DeleteSimulation.html)  **
  - **Description:** Grants permission to delete a simulation
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeApp](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DescribeApp.html)  **
  - **Description:** Grants permission to describe an app
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSimulation](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DescribeSimulation.html)  **
  - **Description:** Grants permission to describe a simulation
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApps](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_ListApps.html)  **
  - **Description:** Grants permission to list apps
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSimulations](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_ListSimulations.html)  **
  - **Description:** Grants permission to list simulations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartApp](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StartApp.html)  **
  - **Description:** Grants permission to start an app
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartClock](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StartClock.html)  **
  - **Description:** Grants permission to start a simulation clock
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSimulation](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StartSimulation.html)  **
  - **Description:** Grants permission to start a simulation
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_simspaceweaver-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_simspaceweaver-aws_TagKeys)
  - **Access level:** Write

- **   [StopApp](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StopApp.html)  **
  - **Description:** Grants permission to stop an app
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopClock](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StopClock.html)  **
  - **Description:** Grants permission to stop a simulation clock
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopSimulation](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_StopSimulation.html)  **
  - **Description:** Grants permission to stop a simulation
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_simspaceweaver-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_simspaceweaver-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [Simulation\*](#list_simspaceweaver-resource-Simulation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_simspaceweaver-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS SimSpace Weaver
<a name="list_simspaceweaver-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Simulation](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_configuring-simulation.html)  | arn:${Partition}:simspaceweaver:${Region}:${Account}:simulation/${SimulationName} | [aws:ResourceTag/${TagKey}](#list_simspaceweaver-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS SimSpace Weaver
<a name="list_simspaceweaver-policy-keys"></a>

AWS SimSpace Weaver defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 