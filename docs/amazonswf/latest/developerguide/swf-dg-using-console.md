# Working in the Amazon SWF console

The Amazon SWF console provides options to configure, initiate, and manage workflow executions.

With the Amazon SWF console, you can:

- Register workflow domains.
- Register workflow types, and activity types.
- Start, view, signal, cancel, terminate, and restart workflow executions.

## Registering a domain

Workflows run in an AWS resource called a _domain_, which controls the workflow's scope. An AWS account can have multiple domains, each of which can contain multiple workflows, but workflows in different domains
can't interact.

Domain registration is the only functionality initially available in the console. After at least one domain is registered, you can perform the following actions for the domain:

- Register workflow and activity types.
- Initiate workflow executions.
- Cancel, terminate, and send signals to running workflow executions.
- Restart closed workflow executions.

You can also perform domain management actions, such as deprecating and undeprecating domains.

After you deprecate a domain, you can't use it to create new workflow executions or register new workflows. Deprecating a domain also deprecates all the activity and workflows registered in the domain. Executions that
were started before the domain was deprecated continue to run.

After undeprecating a previously deprecated domain, you can resume using the domain to register workflow types and start new workflow executions.

For more information about these domain management actions, see
[DeprecateDomain](../apireference/API_DeprecateDomain.md "../apireference/API_DeprecateDomain.md") and
[UndeprecateDomain](../apireference/API_UndeprecateDomain.md "../apireference/API_UndeprecateDomain.md").

## Registering workflow types

You can register workflow types in the Amazon SWF console after you have registered at least one domain.

A workflow type is a set of activity types that carry out an objective and contain the logic that coordinates the activities. Workflow types coordinate and manage the execution of activities that can be run asynchronously across multiple computing devices and feature both sequential and parallel processing methods.

###### To register an Amazon SWF workflow type using the console

1. Open the domain in which you want to register a workflow.
2. Choose **Register**, and then choose **Register Workflow**.
3. On the **Register Workflow** page, enter the **Workflow name** and **Workflow version**. Optionally, you
   can also specify a
   **[Default
   task list](../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultTaskList "../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultTaskList")** that will be used to schedule decision tasks for executions of this workflow.
4. (Optional) Choose **Advanced options** to specify the following details for your workflow:
   - **[Default Task
     priority](../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultTaskPriority "../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultTaskPriority")** – The default task priority to assign to the workflow.
   - **[Default Execution start
     to close timeout](../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultExecutionStartToCloseTimeout "../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultExecutionStartToCloseTimeout")** – The default maximum duration for executions of this workflow.
   - **[Default Task start to close
     timeout](../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultTaskStartToCloseTimeout "../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultTaskStartToCloseTimeout")** – The default maximum duration of decision tasks for this workflow.
   - **[Default Child policy](../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultChildPolicy "../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultChildPolicy")**
     – The default policy to use for the child workflow executions.
   - **[Default Lambda role](../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultLambdaRole "../apireference/API_RegisterWorkflowType.md#SWF-RegisterWorkflowType-request-defaultLambdaRole")**
     – The default IAM role attached to this workflow.

5. Choose **Register workflow**.

## Registering activity types

Activities are tasks which you want your workflow type to coordinate and execute (for example: verify customer's order, charge credit card etc.). The order in which activities are performed is determined by the workflow type's coordination logic.

You can register activity types after at least one domain is registered.

###### To register an Amazon SWF activity type using the console

1. Open the domain in which you want to register an activity.
2. Choose **Register**, and then choose **Register Activity**.
3. On the **Register activity** page, enter the
   **[Activity
   name](../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-name "../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-name")** and
   **[Activity
   version](../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-version "../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-version")**. Optionally, you
   can also specify a
   **[Default
   task list](../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskList "../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskList")** that will be used to schedule tasks of this activity.
4. (Optional) Choose **Advanced options** to specify the following details for your activity:
   - **[Default Task
     priority](../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskPriority "../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskPriority")** – The default task priority to assign to the activity.
   - **[Default task schedule to start timeout](../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskScheduleToStartTimeout "../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskScheduleToStartTimeout")** – The default maximum duration that a task of this activity can wait before being assigned to a worker.
   - **[Default Task start to close timeout](../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskStartToCloseTimeout "../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskStartToCloseTimeout")** – The default maximum duration that a worker can take to process tasks of this activity.
   - **[Default task schedule to close timeout](../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskScheduleToCloseTimeout "../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskScheduleToCloseTimeout")** – The default maximum duration for a task of this activity.
   - **[Default task heartbeat timeout](../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskHeartbeatTimeout "../apireference/API_RegisterActivityType.md#SWF-RegisterActivityType-request-defaultTaskHeartbeatTimeout")** – The default maximum time before which a worker processing a task of this type must report progress by calling
     [RecordActivityTaskHeartbeat](../apireference/API_RecordActivityTaskHeartbeat.md "../apireference/API_RecordActivityTaskHeartbeat.md").

5. Choose **Register activity**.

## Starting a workflow

You can start a workflow execution from the Amazon SWF console. You cannot start a workflow execution until you have registered at least one workflow.

### To start a workflow execution using the console

1. Open the Amazon SWF console, and in the left navigation pane, choose **Domains**.
2. Below the domain name, choose **Workflows**.
3. On the **Workflows** page, choose the workflow that you want to execute.
4. Choose **Start execution**.
5. On the **Start execution** page, enter the
   **[Workflow name](../apireference/API_WorkflowType.md#SWF-Type-WorkflowType-name "../apireference/API_WorkflowType.md#SWF-Type-WorkflowType-name")** and
   **Execution ID** to identify your execution by a name. Optionally, you
   can also specify a
   **[Task
   list](../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-taskList "../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-taskList")** that will be used for the decision tasks generated for this workflow execution.
6. (Optional) Choose **Advanced options** to specify the following details for your workflow execution:
   - **[Task
     priority](../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-taskPriority "../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-taskPriority")** – The task priority to use for this workflow execution.
   - **[Execution start to close timeout](../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-executionStartToCloseTimeout "../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-executionStartToCloseTimeout")** – The total duration for this workflow execution.
   - **[Task start to close timeout](../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-taskStartToCloseTimeout "../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-taskStartToCloseTimeout")** – The maximum duration of decision tasks for this workflow execution.
   - **[Child policy](../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-childPolicy "../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-childPolicy")** – The policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the [TerminateWorkflowExecution](../apireference/API_TerminateWorkflowExecution.md "../apireference/API_TerminateWorkflowExecution.md") action explicitly or due to an expired timeout.
   - **[Lambda role](../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-lambdaRole "../apireference/API_StartWorkflowExecution.md#SWF-StartWorkflowExecution-request-lambdaRole")** – The IAM role to attach to this workflow execution.

7. Choose **Start execution**.

## Managing workflow executions

You can filter your workflow executions by name, status, ID, and tag. You can send signals with inputs into active workflow executions. If you need to cancel or terminate a workflow, you can use the **Try-cancel** option. Cancelling is preferable over terminating a workflow execution because canceling gives the workflow an opportunity to perform any clean-up tasks and then close properly.

In the console, you can manage the workflow executions that are currently running and/or closed.

###### To manage your workflow executions

1. Open a domain to manage its workflow executions.
2. Choose **Find Execution**.
3. On the **Workflow executions** page, choose **Filter executions by property**, and then under **Properties**
   choose one of the following filters:

| Choose           | To apply this filter                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Workflow**     | Choose this filter to list executions of a specific workflow. For example, to view executions of the `fiction-books-order-workflow`, do the<br>following:<br>1. Choose **Workflow**.<br>2. Under **Operators**, choose **Equals**.<br>3. Under **Workflows**, choose **fiction-books-order-workflow**.<br>4. (Optional) Choose \*_Clear filters_<br>• to remove the filter and start a new search for executions.                  |
| **Status**       | Choose this filter to list executions with a specific status. For example, to view executions with the status **Failed**, do the<br>following:<br>1. Choose **Status**.<br>2. Under **Operators**, choose **Equals**.<br>3. Under **Statuses**, choose **Failed**.<br>4. (Optional) Choose \*_Clear filters_<br>• to remove the filter and start a new search for executions.                                                      |
| **Execution ID** | Choose this filter to view a workflow execution based on its ID. For example, to view the execution with ID `fiction-books-order-category1`, do the<br>following:<br>1. Choose **Execution ID**.<br>2. Under **Operators**, choose **Equals**.<br>3. Under **Execution IDs**, choose **fiction-books-order-category1**.<br>4. (Optional) Choose \*_Clear filters_<br>• to remove the filter and start a new search for executions. |
| **Tag**          | Choose this filter to list executions with a specific tag. For example, to view executions with the status `purchaseOrder`, do the<br>following:<br>1. Choose **Tag**.<br>2. Under **Operators**, choose **Equals**.<br>3. Under **Tag**, choose **purchaseOrder**.<br>4. (Optional) Choose \*_Clear filters_<br>• to remove the filter and start a new search for executions.                                                     |

4. (Optional) After applying the required filter to list workflow executions, you can perform the following operations to an **Active** execution:
   - **Signal** – Use this option to send a running workflow execution additional data. To do this:
     1. Choose the execution to which you want to send additional data.
     2. Choose **Signal**, and then specify the data in the **Signal execution** dialog box.
     3. Choose **Signal**.

   - **Try-cancel** – Use this option to try to cancel a workflow execution. It is preferable to cancel a workflow execution rather than terminate it.
     Canceling provides the workflow execution an opportunity to perform any clean-up tasks and then close properly.
     1. Choose the execution which you want to cancel.
     2. Choose **Try-cancel**.

   - **Terminate** – Use this option to terminate a workflow execution. Note that it is preferable to cancel a workflow execution rather than
     terminate it.
     1. Choose the execution which you want to terminate.
     2. For **Child policy**, make sure **Terminate** is selected.
     3. (Optional) Specify the **Reason** and **Details** for terminating the execution.
     4. Choose **Terminate**.

5. (Optional) **Re-run** – Use this option to re-run a closed workflow execution.
   1. In the list of workflow executions, select the closed execution to re-run. When you select a closed execution, the **Re-run** button becomes enabled.
      Choose **Re-run**.
   2. On the **Re-run execution** page, specify the details for workflow execution as mentioned in
      [Starting a workflow](#dg-swf-execution-start "#dg-swf-execution-start").
