

# Actions, resources, and condition keys for AWS RoboMaker
<a name="list_robomaker"></a>

AWS RoboMaker (service prefix: `robomaker`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/robomaker/how-it-works.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/robomaker/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/robomaker/latest/dg/what-is-robomaker.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/robomaker/robomaker.json) for this service.

**Topics**
+ [Actions defined by AWS RoboMaker](#list_robomaker-actions-as-permissions)
+ [Permission-only actions for AWS RoboMaker](#list_robomaker-permission-only-actions)
+ [Resource types defined by AWS RoboMaker](#list_robomaker-resources-for-iam-policies)
+ [Condition keys for AWS RoboMaker](#list_robomaker-policy-keys)

## Actions defined by AWS RoboMaker
<a name="list_robomaker-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchDeleteWorlds](https://docs.aws.amazon.com/robomaker/latest/dg/API_BatchDeleteWorlds.html)  **
  - **Description:** Delete one or more worlds in a batch operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDescribeSimulationJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_BatchDescribeSimulationJob.html)  **
  - **Description:** Describe multiple simulation jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CancelDeploymentJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_CancelDeploymentJob.html)  **
  - **Description:** Cancel a deployment job
  - **Resource types (\*required):** [deploymentJob\*](#list_robomaker-resource-deploymentJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelSimulationJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_CancelSimulationJob.html)  **
  - **Description:** Cancel a simulation job
  - **Resource types (\*required):** [simulationJob\*](#list_robomaker-resource-simulationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelSimulationJobBatch](https://docs.aws.amazon.com/robomaker/latest/dg/API_CancelSimulationJobBatch.html)  **
  - **Description:** Cancel a simulation job batch
  - **Resource types (\*required):** [simulationJobBatch\*](#list_robomaker-resource-simulationJobBatch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelWorldExportJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_CancelWorldExportJob.html)  **
  - **Description:** Cancel a world export job
  - **Resource types (\*required):** [worldExportJob\*](#list_robomaker-resource-worldExportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelWorldGenerationJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_CancelWorldGenerationJob.html)  **
  - **Description:** Cancel a world generation job
  - **Resource types (\*required):** [worldGenerationJob\*](#list_robomaker-resource-worldGenerationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDeploymentJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateDeploymentJob.html)  **
  - **Description:** Create a deployment job
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFleet](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateFleet.html)  **
  - **Description:** Create a deployment fleet that represents a logical group of robots running the same robot application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRobot](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateRobot.html)  **
  - **Description:** Create a robot that can be registered to a fleet
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRobotApplication](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateRobotApplication.html)  **
  - **Description:** Create a robot application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRobotApplicationVersion](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateRobotApplicationVersion.html)  **
  - **Description:** Create a snapshot of a robot application
  - **Resource types (\*required):** [robotApplication\*](#list_robomaker-resource-robotApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSimulationApplication](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateSimulationApplication.html)  **
  - **Description:** Create a simulation application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSimulationApplicationVersion](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateSimulationApplicationVersion.html)  **
  - **Description:** Create a snapshot of a simulation application
  - **Resource types (\*required):** [simulationApplication\*](#list_robomaker-resource-simulationApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSimulationJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateSimulationJob.html)  **
  - **Description:** Create a simulation job
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorldExportJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateWorldExportJob.html)  **
  - **Description:** Create a world export job
  - **Resource types (\*required):** [world\*](#list_robomaker-resource-world)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorldGenerationJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateWorldGenerationJob.html)  **
  - **Description:** Create a world generation job
  - **Resource types (\*required):** [worldTemplate\*](#list_robomaker-resource-worldTemplate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorldTemplate](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateWorldTemplate.html)  **
  - **Description:** Create a world template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteFleet](https://docs.aws.amazon.com/robomaker/latest/dg/API_DeleteFleet.html)  **
  - **Description:** Delete a deployment fleet
  - **Resource types (\*required):** [deploymentFleet\*](#list_robomaker-resource-deploymentFleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRobot](https://docs.aws.amazon.com/robomaker/latest/dg/API_DeleteRobot.html)  **
  - **Description:** Delete a robot
  - **Resource types (\*required):** [robot\*](#list_robomaker-resource-robot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRobotApplication](https://docs.aws.amazon.com/robomaker/latest/dg/API_DeleteRobotApplication.html)  **
  - **Description:** Delete a robot application
  - **Resource types (\*required):** [robotApplication\*](#list_robomaker-resource-robotApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSimulationApplication](https://docs.aws.amazon.com/robomaker/latest/dg/API_DeleteSimulationApplication.html)  **
  - **Description:** Delete a simulation application
  - **Resource types (\*required):** [simulationApplication\*](#list_robomaker-resource-simulationApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorldTemplate](https://docs.aws.amazon.com/robomaker/latest/dg/API_DeleteWorldTemplate.html)  **
  - **Description:** Delete a world template
  - **Resource types (\*required):** [worldTemplate\*](#list_robomaker-resource-worldTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterRobot](https://docs.aws.amazon.com/robomaker/latest/dg/API_DeregisterRobot.html)  **
  - **Description:** Deregister a robot from a fleet
  - **Resource types (\*required):** [deploymentFleet\*](#list_robomaker-resource-deploymentFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [robot\*](#list_robomaker-resource-robot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDeploymentJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeDeploymentJob.html)  **
  - **Description:** Describe a deployment job
  - **Resource types (\*required):** [deploymentJob\*](#list_robomaker-resource-deploymentJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFleet](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeFleet.html)  **
  - **Description:** Describe a deployment fleet
  - **Resource types (\*required):** [deploymentFleet\*](#list_robomaker-resource-deploymentFleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRobot](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeRobot.html)  **
  - **Description:** Describe a robot
  - **Resource types (\*required):** [robot\*](#list_robomaker-resource-robot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRobotApplication](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeRobotApplication.html)  **
  - **Description:** Describe a robot application
  - **Resource types (\*required):** [robotApplication\*](#list_robomaker-resource-robotApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSimulationApplication](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeSimulationApplication.html)  **
  - **Description:** Describe a simulation application
  - **Resource types (\*required):** [simulationApplication\*](#list_robomaker-resource-simulationApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSimulationJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeSimulationJob.html)  **
  - **Description:** Describe a simulation job
  - **Resource types (\*required):** [simulationJob\*](#list_robomaker-resource-simulationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSimulationJobBatch](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeSimulationJobBatch.html)  **
  - **Description:** Describe a simulation job batch
  - **Resource types (\*required):** [simulationJobBatch\*](#list_robomaker-resource-simulationJobBatch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorld](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeWorld.html)  **
  - **Description:** Describe a world
  - **Resource types (\*required):** [world\*](#list_robomaker-resource-world)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorldExportJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeWorldExportJob.html)  **
  - **Description:** Describe a world export job
  - **Resource types (\*required):** [worldExportJob\*](#list_robomaker-resource-worldExportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorldGenerationJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeWorldGenerationJob.html)  **
  - **Description:** Describe a world generation job
  - **Resource types (\*required):** [worldGenerationJob\*](#list_robomaker-resource-worldGenerationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorldTemplate](https://docs.aws.amazon.com/robomaker/latest/dg/API_DescribeWorldTemplate.html)  **
  - **Description:** Describe a world template
  - **Resource types (\*required):** [worldTemplate\*](#list_robomaker-resource-worldTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorldTemplateBody](https://docs.aws.amazon.com/robomaker/latest/dg/API_GetWorldTemplateBody.html)  **
  - **Description:** Get the body of a world template
  - **Resource types (\*required):** [worldTemplate\*](#list_robomaker-resource-worldTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDeploymentJobs](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListDeploymentJobs.html)  **
  - **Description:** List deployment jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFleets](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListFleets.html)  **
  - **Description:** List fleets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRobotApplications](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListRobotApplications.html)  **
  - **Description:** List robot applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRobots](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListRobots.html)  **
  - **Description:** List robots
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSimulationApplications](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListSimulationApplications.html)  **
  - **Description:** List simulation applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSimulationJobBatches](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListSimulationJobBatches.html)  **
  - **Description:** List simulation job batches
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSimulationJobs](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListSimulationJobs.html)  **
  - **Description:** List simulation jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** List tags for a RoboMaker resource
  - **Resource types (\*required):** [deploymentFleet](#list_robomaker-resource-deploymentFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deploymentJob](#list_robomaker-resource-deploymentJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [robot](#list_robomaker-resource-robot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [robotApplication](#list_robomaker-resource-robotApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [simulationApplication](#list_robomaker-resource-simulationApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [simulationJob](#list_robomaker-resource-simulationJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [simulationJobBatch](#list_robomaker-resource-simulationJobBatch) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [world](#list_robomaker-resource-world) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [worldExportJob](#list_robomaker-resource-worldExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [worldGenerationJob](#list_robomaker-resource-worldGenerationJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [worldTemplate](#list_robomaker-resource-worldTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorldExportJobs](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListWorldExportJobs.html)  **
  - **Description:** List world export jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorldGenerationJobs](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListWorldGenerationJobs.html)  **
  - **Description:** List world generation jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorldTemplates](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListWorldTemplates.html)  **
  - **Description:** List world templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorlds](https://docs.aws.amazon.com/robomaker/latest/dg/API_ListWorlds.html)  **
  - **Description:** List worlds
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RegisterRobot](https://docs.aws.amazon.com/robomaker/latest/dg/API_RegisterRobot.html)  **
  - **Description:** Register a robot to a fleet
  - **Resource types (\*required):** [deploymentFleet\*](#list_robomaker-resource-deploymentFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [robot\*](#list_robomaker-resource-robot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestartSimulationJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_RestartSimulationJob.html)  **
  - **Description:** Restart a running simulation job
  - **Resource types (\*required):** [simulationJob\*](#list_robomaker-resource-simulationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSimulationJobBatch](https://docs.aws.amazon.com/robomaker/latest/dg/API_StartSimulationJobBatch.html)  **
  - **Description:** Create a simulation job batch
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Write

- **   [SyncDeploymentJob](https://docs.aws.amazon.com/robomaker/latest/dg/API_SyncDeploymentJob.html)  **
  - **Description:** Ensures the most recently deployed robot application is deployed to all robots in the fleet
  - **Resource types (\*required):** [deploymentFleet\*](#list_robomaker-resource-deploymentFleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/robomaker/latest/dg/API_TagResource.html)  **
  - **Description:** Add tags to a RoboMaker resource
  - **Resource types (\*required):** [deploymentFleet](#list_robomaker-resource-deploymentFleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [deploymentJob](#list_robomaker-resource-deploymentJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [robot](#list_robomaker-resource-robot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [robotApplication](#list_robomaker-resource-robotApplication) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [simulationApplication](#list_robomaker-resource-simulationApplication) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [simulationJob](#list_robomaker-resource-simulationJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [simulationJobBatch](#list_robomaker-resource-simulationJobBatch) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [world](#list_robomaker-resource-world) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [worldExportJob](#list_robomaker-resource-worldExportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [worldGenerationJob](#list_robomaker-resource-worldGenerationJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [worldTemplate](#list_robomaker-resource-worldTemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_robomaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/robomaker/latest/dg/API_UntagResource.html)  **
  - **Description:** Remove tags from a RoboMaker resource
  - **Resource types (\*required):** [deploymentFleet](#list_robomaker-resource-deploymentFleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [deploymentJob](#list_robomaker-resource-deploymentJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [robot](#list_robomaker-resource-robot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [robotApplication](#list_robomaker-resource-robotApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [simulationApplication](#list_robomaker-resource-simulationApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [simulationJob](#list_robomaker-resource-simulationJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [simulationJobBatch](#list_robomaker-resource-simulationJobBatch) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [world](#list_robomaker-resource-world) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [worldExportJob](#list_robomaker-resource-worldExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [worldGenerationJob](#list_robomaker-resource-worldGenerationJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Resource types (\*required):** [worldTemplate](#list_robomaker-resource-worldTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_robomaker-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateRobotApplication](https://docs.aws.amazon.com/robomaker/latest/dg/API_UpdateRobotApplication.html)  **
  - **Description:** Update a robot application
  - **Resource types (\*required):** [robotApplication\*](#list_robomaker-resource-robotApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSimulationApplication](https://docs.aws.amazon.com/robomaker/latest/dg/API_UpdateSimulationApplication.html)  **
  - **Description:** Update a simulation application
  - **Resource types (\*required):** [simulationApplication\*](#list_robomaker-resource-simulationApplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorldTemplate](https://docs.aws.amazon.com/robomaker/latest/dg/API_UpdateWorldTemplate.html)  **
  - **Description:** Update a world template
  - **Resource types (\*required):** [worldTemplate\*](#list_robomaker-resource-worldTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS RoboMaker
<a name="list_robomaker-permission-only-actions"></a>

The following actions are defined by AWS RoboMaker but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   ListSupportedAvailabilityZones  | Lists supported availability zones |  |   | List | 
|   UpdateRobotDeployment  | Report the deployment status for an individual robot |  |   | Write | 

## Resource types defined by AWS RoboMaker
<a name="list_robomaker-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [deploymentFleet](https://docs.aws.amazon.com/robomaker/latest/dg/managing-simulation-applications.html)  | arn:${Partition}:robomaker:${Region}:${Account}:deployment-fleet/${FleetName}/${CreatedOnEpoch} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [deploymentJob](https://docs.aws.amazon.com/robomaker/latest/dg/deployment.html)  | arn:${Partition}:robomaker:${Region}:${Account}:deployment-job/${DeploymentJobId} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [robot](https://docs.aws.amazon.com/robomaker/latest/dg/fleets.html)  | arn:${Partition}:robomaker:${Region}:${Account}:robot/${RobotName}/${CreatedOnEpoch} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [robotApplication](https://docs.aws.amazon.com/robomaker/latest/dg/managing-robot-applications.html)  | arn:${Partition}:robomaker:${Region}:${Account}:robot-application/${ApplicationName}/${CreatedOnEpoch} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [simulationApplication](https://docs.aws.amazon.com/robomaker/latest/dg/managing-simulation-applications.html)  | arn:${Partition}:robomaker:${Region}:${Account}:simulation-application/${ApplicationName}/${CreatedOnEpoch} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [simulationJob](https://docs.aws.amazon.com/robomaker/latest/dg/simulation.html)  | arn:${Partition}:robomaker:${Region}:${Account}:simulation-job/${SimulationJobId} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [simulationJobBatch](https://docs.aws.amazon.com/robomaker/latest/dg/simulation-job-batch.html)  | arn:${Partition}:robomaker:${Region}:${Account}:simulation-job-batch/${SimulationJobBatchId} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [world](https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-generated-worlds.html)  | arn:${Partition}:robomaker:${Region}:${Account}:world/${WorldId} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [worldExportJob](https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-export-jobs.html)  | arn:${Partition}:robomaker:${Region}:${Account}:world-export-job/${WorldExportJobId} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [worldGenerationJob](https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-generation-jobs.html)  | arn:${Partition}:robomaker:${Region}:${Account}:world-generation-job/${WorldGenerationJobId} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 
|  [worldTemplate](https://docs.aws.amazon.com/robomaker/latest/dg/worlds-managing-simworld-templates.html)  | arn:${Partition}:robomaker:${Region}:${Account}:world-template/${WorldTemplateJobId} | [aws:ResourceTag/${TagKey}](#list_robomaker-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS RoboMaker
<a name="list_robomaker-policy-keys"></a>

AWS RoboMaker defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/robomaker/latest/dg/tagging-resources-iam-policies.html)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/robomaker/latest/dg/tagging-resources-iam-policies.html)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/robomaker/latest/dg/tagging-resources-iam-policies.html)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 