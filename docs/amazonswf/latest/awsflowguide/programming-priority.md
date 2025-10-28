# Setting task priority in Amazon SWF

By default, tasks on a task list are delivered based upon their _arrival time_: tasks that
are scheduled first are generally run first, as far as possible. By setting an optional _task priority_,
you can give priority to certain tasks: Amazon SWF will attempt to deliver higher-priority tasks on a task list before those
with lower priority.

You can set task priorities for both workflows and activities. A workflow's task priority doesn't affect the
priority of any activity tasks it schedules, nor does it affect any child workflows it starts. The default priority
for an activity or workflow is set (either by you or by Amazon SWF) during registration, and the registered task
priority is always used unless it is overridden while scheduling the activity or starting a workflow
execution.

Task priority values can range from "-2147483648" to "2147483647", with higher numbers indicating higher
priority. If you don't set the task priority for an activity or workflow, it will be assigned a priority of zero
("0").

###### Topics

- [Setting Task Priority for Workflows](#task-priority-workflows "#task-priority-workflows")
- [Setting Task Priority for Activities](#task-priority-activities "#task-priority-activities")

## Setting Task Priority for Workflows

You can set the task priority for a workflow when you register it or start it. The task priority that is set when the
workflow type is registered is used as the default for any workflow executions of that type, unless it is overridden
when starting the workflow execution.

To register a workflow type with a default task priority, set the _defaultTaskPriority_ option in
[WorkflowRegistrationOptions](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/annotations/WorkflowRegistrationOptions.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/annotations/WorkflowRegistrationOptions.md") when declaring it:

```
@Workflow
@WorkflowRegistrationOptions(
    defaultTaskPriority = 10,
    defaultTaskStartToCloseTimeoutSeconds = 240)
public interface PriorityWorkflow
{
    @Execute(version = "1.0")
    void startWorkflow(int a);
}

```

You can also set the _taskPriority_ for a workflow when you start it, overriding the registered (default)
task priority.

```
StartWorkflowOptions priorityWorkflowOptions
    = new StartWorkflowOptions().withTaskPriority(10);

PriorityWorkflowClientExternalFactory cf
    = new PriorityWorkflowClientExternalFactoryImpl(swfService, domain);

priority_workflow_client = cf.getClient();

priority_workflow_client.startWorkflow(
        "Smith, John", priorityWorkflowOptions);

```

Additionally, you can set the task priority when starting a child workflow or continuing a workflow as new. For example,
you can set the _taskPriority_ option in [ContinueAsNewWorkflowExecutionParameters](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/generic/ContinueAsNewWorkflowExecutionParameters.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/generic/ContinueAsNewWorkflowExecutionParameters.md") or in
[StartChildWorkflowExecutionParameters](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/generic/StartChildWorkflowExecutionParameters.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/generic/StartChildWorkflowExecutionParameters.md").

## Setting Task Priority for Activities

You can set the task priority for an activity either when registering it or when scheduling it. The task priority that
is set when registering an activity type is used as the default priority when the activity is run, unless it is
overridden when scheduling the activity.

To register an activity type with a default task priority, set the _defaultTaskPriority_ option in
[ActivityRegistrationOptions](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/annotations/ActivityRegistrationOptions.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/annotations/ActivityRegistrationOptions.md") when declaring it:

```
@Activities(version = "1.0")
@ActivityRegistrationOptions(
    defaultTaskPriority = 10,
    defaultTaskStartToCloseTimeoutSeconds = 120)
public interface ImportantActivities {
    int doSomethingImportant();
}

```

You can also set the _taskPriority_ for an activity when you schedule it, overriding the registered (default)
task priority.

```
ActivitySchedulingOptions activityOptions = new ActivitySchedulingOptions.withTaskPriority(10);

ImportantActivitiesClient activityClient = new ImportantActivitiesClientImpl();

activityClient.doSomethingImportant(activityOptions);

```
