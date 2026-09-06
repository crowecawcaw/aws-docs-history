

# Working in the Amazon SWF console
<a name="swf-dg-using-console"></a>

The Amazon SWF console provides options to configure, initiate, and manage workflow executions.

With the Amazon SWF console, you can:
+ Register workflow domains.
+ Register workflow types, and activity types.
+ Start, view, signal, cancel, terminate, and restart workflow executions.

## Registering a domain
<a name="swf-dg-register-domain-console"></a>

Workflows run in an AWS resource called a *domain*, which controls the workflow's scope. An AWS account can have multiple domains, each of which can contain multiple workflows, but workflows in different domains can't interact.

Domain registration is the only functionality initially available in the console. After at least one domain is registered, you can perform the following actions for the domain:
+ Register workflow and activity types.
+ Initiate workflow executions.
+ Cancel, terminate, and send signals to running workflow executions.
+ Restart closed workflow executions.

You can also perform domain management actions, such as deprecating and undeprecating domains.

After you deprecate a domain, you can't use it to create new workflow executions or register new workflows. Deprecating a domain also deprecates all the activity and workflows registered in the domain. Executions that were started before the domain was deprecated continue to run.

After undeprecating a previously deprecated domain, you can resume using the domain to register workflow types and start new workflow executions.

For more information about these domain management actions, see [DeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateDomain.html) and [UndeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateDomain.html).

## Registering workflow types
<a name="dg-swf-register-workflow"></a>

You can register workflow types in the Amazon SWF console after you have registered at least one domain.

A workflow type is a set of activity types that carry out an objective and contain the logic that coordinates the activities. Workflow types coordinate and manage the execution of activities that can be run asynchronously across multiple computing devices and feature both sequential and parallel processing methods.

**To register an Amazon SWF workflow type using the console**

1. Open the domain in which you want to register a workflow.

1. Choose **Register**, and then choose **Register Workflow**.

1. On the **Register Workflow** page, enter the **Workflow name** and **Workflow version**. Optionally, you can also specify a **[Default task list](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html#SWF-RegisterWorkflowType-request-defaultTaskList)** that will be used to schedule decision tasks for executions of this workflow.

1. (Optional) Choose **Advanced options** to specify the following details for your workflow:
   + **[Default Task priority](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html#SWF-RegisterWorkflowType-request-defaultTaskPriority)** – The default task priority to assign to the workflow.
   + **[Default Execution start to close timeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html#SWF-RegisterWorkflowType-request-defaultExecutionStartToCloseTimeout)** – The default maximum duration for executions of this workflow.
   + **[Default Task start to close timeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html#SWF-RegisterWorkflowType-request-defaultTaskStartToCloseTimeout)** – The default maximum duration of decision tasks for this workflow.
   + **[Default Child policy](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html#SWF-RegisterWorkflowType-request-defaultChildPolicy)** – The default policy to use for the child workflow executions.
   + **[Default Lambda role](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html#SWF-RegisterWorkflowType-request-defaultLambdaRole)** – The default IAM role attached to this workflow.

1. Choose **Register workflow**.

## Registering activity types
<a name="dg-swf-register-activity"></a>

Activities are tasks which you want your workflow type to coordinate and execute (for example: verify customer's order, charge credit card etc.). The order in which activities are performed is determined by the workflow type's coordination logic.

You can register activity types after at least one domain is registered.

**To register an Amazon SWF activity type using the console**

1. Open the domain in which you want to register an activity.

1. Choose **Register**, and then choose **Register Activity**.

1. On the **Register activity** page, enter the **[Activity name](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-name)** and **[Activity version](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-version)**. Optionally, you can also specify a **[Default task list](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskList)** that will be used to schedule tasks of this activity.

1. (Optional) Choose **Advanced options** to specify the following details for your activity:
   + **[Default Task priority](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskPriority)** – The default task priority to assign to the activity.
   + **[Default task schedule to start timeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskScheduleToStartTimeout)** – The default maximum duration that a task of this activity can wait before being assigned to a worker.
   + **[Default Task start to close timeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskStartToCloseTimeout)** – The default maximum duration that a worker can take to process tasks of this activity.
   + **[Default task schedule to close timeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskScheduleToCloseTimeout)** – The default maximum duration for a task of this activity.
   + **[Default task heartbeat timeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskHeartbeatTimeout)** – The default maximum time before which a worker processing a task of this type must report progress by calling [RecordActivityTaskHeartbeat](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RecordActivityTaskHeartbeat.html).

1. Choose **Register activity**.

## Starting a workflow
<a name="dg-swf-execution-start"></a>

You can start a workflow execution from the Amazon SWF console. You cannot start a workflow execution until you have registered at least one workflow.

### To start a workflow execution using the console
<a name="start-workflow-execution-console"></a>

1. Open the Amazon SWF console, and in the left navigation pane, choose **Domains**.

1. Below the domain name, choose **Workflows**.

1. On the **Workflows** page, choose the workflow that you want to execute.

1. Choose **Start execution**.

1. On the **Start execution** page, enter the **[Workflow name](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowType.html#SWF-Type-WorkflowType-name)** and **Execution ID** to identify your execution by a name. Optionally, you can also specify a **[Task list](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html#SWF-StartWorkflowExecution-request-taskList)** that will be used for the decision tasks generated for this workflow execution.

1. (Optional) Choose **Advanced options** to specify the following details for your workflow execution:
   + ** [Task priority](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html#SWF-StartWorkflowExecution-request-taskPriority)** – The task priority to use for this workflow execution.
   + **[Execution start to close timeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html#SWF-StartWorkflowExecution-request-executionStartToCloseTimeout)** – The total duration for this workflow execution.
   + **[Task start to close timeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html#SWF-StartWorkflowExecution-request-taskStartToCloseTimeout)** – The maximum duration of decision tasks for this workflow execution.
   + **[Child policy](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html#SWF-StartWorkflowExecution-request-childPolicy)** – The policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the [TerminateWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TerminateWorkflowExecution.html) action explicitly or due to an expired timeout.
   + **[Lambda role](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html#SWF-StartWorkflowExecution-request-lambdaRole)** – The IAM role to attach to this workflow execution.

1. Choose **Start execution**.

## Managing workflow executions
<a name="swf-dg-console-manage-workflow-executions"></a>

You can filter your workflow executions by name, status, ID, and tag. You can send signals with inputs into active workflow executions. If you need to cancel or terminate a workflow, you can use the **Try-cancel** option. Cancelling is preferable over terminating a workflow execution because canceling gives the workflow an opportunity to perform any clean-up tasks and then close properly.

In the console, you can manage the workflow executions that are currently running and/or closed.

**To manage your workflow executions**

1. Open a domain to manage its workflow executions.

1. Choose **Find Execution**.

1. On the **Workflow executions** page, choose **Filter executions by property**, and then under **Properties** choose one of the following filters:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-using-console.html)

1. (Optional) After applying the required filter to list workflow executions, you can perform the following operations to an **Active** execution:
   + **Signal** – Use this option to send a running workflow execution additional data. To do this:

     1. Choose the execution to which you want to send additional data.

     1. Choose **Signal**, and then specify the data in the **Signal execution** dialog box.

     1. Choose **Signal**.
   + **Try-cancel** – Use this option to try to cancel a workflow execution. It is preferable to cancel a workflow execution rather than terminate it. Canceling provides the workflow execution an opportunity to perform any clean-up tasks and then close properly.

     1. Choose the execution which you want to cancel.

     1. Choose **Try-cancel**.
   + **Terminate** – Use this option to terminate a workflow execution. Note that it is preferable to cancel a workflow execution rather than terminate it.

     1. Choose the execution which you want to terminate.

     1. For **Child policy**, make sure **Terminate** is selected.

     1. (Optional) Specify the **Reason** and **Details** for terminating the execution.

     1. Choose **Terminate**.

1. (Optional) **Re-run** – Use this option to re-run a closed workflow execution.

   1. In the list of workflow executions, select the closed execution to re-run. When you select a closed execution, the **Re-run** button becomes enabled. Choose **Re-run**.

   1. On the **Re-run execution** page, specify the details for workflow execution as mentioned in [Starting a workflow](#dg-swf-execution-start).