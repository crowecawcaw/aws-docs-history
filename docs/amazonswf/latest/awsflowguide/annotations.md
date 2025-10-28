# AWS Flow Framework for Java Annotations

###### Topics

- [@Activities](#annotations-activities "#annotations-activities")
- [@Activity](#annotations-activity "#annotations-activity")
- [@ActivityRegistrationOptions](#annotations-activityregistration "#annotations-activityregistration")
- [@Asynchronous](#annotations-asynchronous "#annotations-asynchronous")
- [@Execute](#annotations-execute "#annotations-execute")
- [@ExponentialRetry](#annotations-exponentialretry "#annotations-exponentialretry")
- [@GetState](#annotations-getstate "#annotations-getstate")
- [@ManualActivityCompletion](#annotations-manualactivitycompletion "#annotations-manualactivitycompletion")
- [@Signal](#annotations-signal "#annotations-signal")
- [@SkipRegistration](#annotations-skipregistration "#annotations-skipregistration")
- [@Wait and @NoWait](#annotations-waitnowait "#annotations-waitnowait")
- [@Workflow](#annotations-workflow "#annotations-workflow")
- [@WorkflowRegistrationOptions](#annotations-workflowregistrationoptions "#annotations-workflowregistrationoptions")

## @Activities

This annotation can be used on an interface to declare a set of activity types. Each
method in an interface annotated with this annotation represents an activity type. An
interface can't have both `@Workflow` and `@Activities`
annotations-

The following parameters can be specified on this annotation:

`activityNamePrefix`

Specifies the prefix of the name of the activity types declared in the interface. If
set to an empty string (which is the default), the name of the interface followed by '.'
is used as the prefix.

`version`

Specifies the default version of the activity types declared in the interface. The
default value is `1.0`.

`dataConverter`

Specifies the type of the `DataConverter` to use for
serializing/deserializing data when creating tasks of this activity type and its
results. Set to `NullDataConverter` by default, which indicates that the
`JsonDataConverter` should be used.

## @Activity

This annotation can be used on methods within an interface annotated with
`@Activities`.

The following parameters can be specified on this annotation:

`name`

Specifies the name of the activity type. The default is an empty string, which
indicates that the default prefix and the activity method name should be used to
determine the name of the activity type (which is of the form
{_prefix_}{_name_}). Note that when you specify
a name in an `@Activity` annotation, the framework will not automatically
prepend a prefix to it. You are free to use your own naming scheme.

`version`

Specifies the version of the activity type. This overrides the default version
specified in the `@Activities` annotation on the containing interface. The
default is an empty string.

## @ActivityRegistrationOptions

Specifies the registration options of an activity type. This annotation can be used on an
interface annotated with `@Activities` or the methods within. If specified in both
places, then the annotation used on the method takes effect.

The following parameters can be specified on this annotation:

`defaultTasklist`

Specifies the default task list to be registered with Amazon SWF for this activity type.
This default can be overridden when calling the activity method on the generated client
using the `ActivitySchedulingOptions` parameter. Set to
`USE_WORKER_TASK_LIST` by default. This is a special value which indicates
that the task list used by the worker, which is performing the registration, should be
used.

`defaultTaskScheduleToStartTimeoutSeconds`

Specifies the defaultTaskScheduleToStartTimeout registered with Amazon SWF for this
activity type. This is the maximum time a task of this activity type is allowed to wait
before it is assigned to a worker. See the _Amazon Simple Workflow Service API Reference_ for more
details.

`defaultTaskHeartbeatTimeoutSeconds`

Specifies the `defaultTaskHeartbeatTimeout` registered with Amazon SWF for
this activity type. Activity workers must provide heartbeat within this duration;
otherwise, the task will be timed out. Set to -1 by default, which is a special value
that indicates this timeout should be disabled. See the
_Amazon Simple Workflow Service API Reference_ for more details.

`defaultTaskStartToCloseTimeoutSeconds`

Specifies the defaultTaskStartToCloseTimeout registered with Amazon SWF for this activity
type. This timeout determines the maximum time a worker can take to process an activity
task of this type. See the _Amazon Simple Workflow Service API Reference_ for more details.

`defaultTaskScheduleToCloseTimeoutSeconds`

Specifies the `defaultScheduleToCloseTimeout` registered with Amazon SWF for
this activity type. This timeout determines the total duration that the task can stay in
open state. Set to -1 by default, which is a special value that indicates this timeout
should be disabled. See the _Amazon Simple Workflow Service API Reference_ for more
details.

## @Asynchronous

When used on a method in the workflow coordination logic, indicates that the method should
be executed asynchronously. A call to the method will return immediately, but the actual
execution will happen asynchronously when all Promise<> parameters passed to the methods
become ready. Methods annotated with @Asynchronous must have a return type of Promise<>
or void.

`daemon`

Indicates if the task created for the asynchronous method should be a daemon task.
`False` by default.

## @Execute

When used on a method in an interface annotated with the `@Workflow`
annotation, identifies the entry point of the workflow.

###### Important

Only one method in the interface can be decorated with `@Execute`.

The following parameters can be specified on this annotation:

`name`

Specifies the name of the workflow type. If not set, the name defaults to
{_prefix_}{_name_}, where
{_prefix_} is the name of the workflow interface followed by a '.'
and {_name_} is the name of the `@Execute`-decorated
method in the workflow.

`version`

Specifies the version of the workflow type.

## @ExponentialRetry

When used on an activity or asynchronous method, sets an exponential retry policy if the
method throws an unhandled exception. A retry attempt is made after a back-off period, which
is calculated by the power of the number of attempts.

The following parameters can be specified on this annotation:

`intialRetryIntervalSeconds`

Specifies the duration to wait before the first retry attempt. This value should not
be greater than `maximumRetryIntervalSeconds` and
`retryExpirationSeconds`.

`maximumRetryIntervalSeconds`

Specifies the maximum duration between retry attempts. Once reached, the retry
interval is capped to this value. Set to -1 by default, which means unlimited
duration.

`retryExpirationSeconds`

Specifies the duration after which exponential retry will stop. Set to -1 by
default, which means there is no expiration.

`backoffCoefficient`

Specifies the coefficient used to calculate the retry interval. See [Exponential Retry Strategy](features-retry.md#features-retry-exponential "features-retry.md#features-retry-exponential").

`maximumAttempts`

Specifies the number of attempts after which exponential retry will stop. Set to -1
by default, which means there is no limit on the number of retry attempts.

`exceptionsToRetry`

Specifies the list of exception types that should trigger a retry. Unhandled
exception of these types will not propagate further and the method will be retried after
the calculated retry interval. By default, the list contains
`Throwable`.

`excludeExceptions`

Specifies the list of exception types that should not trigger a retry. Unhandled
exceptions of this type will be allowed to propagate. The list is empty by
default.

## @GetState

When used on a method in an interface annotated with the `@Workflow`
annotation, identifies that the method is used to retrieve the latest workflow execution
state. There can be at most one method with this annotation in an interface with the
`@Workflow` annotation. Methods with this annotation must not take any parameters
and must have a return type other than `void`.

## @ManualActivityCompletion

This annotation can be used on an activity method to indicate that the activity task
should not be completed when the method returns. The activity task will not be automatically
completed and would need to be completed manually directly using the Amazon SWF API. This is useful
for use cases where the activity task is delegated to some external system that isn't
automated or requires human intervention to be completed.

## @Signal

When used on a method in an interface annotated with the `@Workflow`
annotation, identifies a signal that can be received by executions of the workflow type
declared by the interface. Use of this annotation is required to define a signal method.

The following parameters can be specified on this annotation:

`name`

Specifies the name portion of the signal name. If not set, the name of the method is
used.

## @SkipRegistration

When used on an interface annotated with the `@Workflow` annotation, indicates
that the workflow type should not be registered with Amazon SWF. One of
`@WorkflowRegistrationOptions` and `@SkipRegistrationOptions`
annotations must be used on an interface annotated with `@Workflow`, but not
both.

## @Wait and @NoWait

These annotations can be used on a parameter of type `Promise<>` to
indicate whether the AWS Flow Framework for Java should wait for it to become ready before executing the
method. By default, `Promise<>` parameters passed into
`@Asynchronous` methods must become ready before method execution occurs. In
certain scenarios, it is necessary to override this default behavior.
`Promise<>` parameters passed into `@Asynchronous` methods and
annotated with `@NoWait` are not waited for.

Collections parameters (or subclasses of) that contain promises, such as
`List<Promise<Int>>`, must be annotated with `@Wait`
annotation. By default, the framework doesn't wait for the members of a collection.

## @Workflow

This annotation is used on an interface to declare a _workflow_ type.
An interface decorated with this annotation should contain exactly one method that is
decorated with the [@Execute](#annotations-execute "#annotations-execute")
annotation to declare an entry point for your workflow.

###### Note

An interface can't have both `@Workflow` and `@Activities`
annotations declared at once; they are mutually exclusive.

The following parameters can be specified on this annotation:

`dataConverter`

Specifies which `DataConverter` to use when sending requests to, and
receiving results from, workflow executions of this workflow type.

The default is `NullDataConverter` which, in turn, falls back to
`JsonDataConverter` to process all request and response data as JavaScript
Object Notation (JSON).

### Example

```
import com.amazonaws.services.simpleworkflow.flow.annotations.Execute;
import com.amazonaws.services.simpleworkflow.flow.annotations.Workflow;
import com.amazonaws.services.simpleworkflow.flow.annotations.WorkflowRegistrationOptions;

@Workflow
@WorkflowRegistrationOptions(defaultExecutionStartToCloseTimeoutSeconds = 3600)
public interface GreeterWorkflow {
   @Execute(version = "1.0")
   public void greet();
}
```

## @WorkflowRegistrationOptions

When used on an interface annotated with `@Workflow`, provides default settings
used by Amazon SWF when registering the workflow type.

###### Note

Either `@WorkflowRegistrationOptions` or
`@SkipRegistrationOptions` must be used on an interface annotated with
`@Workflow`, but you can't specify both.

The following parameters can be specified on this annotation:

Description

An optional text description of the workflow type.

`defaultExecutionStartToCloseTimeoutSeconds`

Specifies the `defaultExecutionStartToCloseTimeout` registered with Amazon SWF
for the workflow type. This is the total time that a workflow execution of this type can
take to complete.

For more information about workflow timeouts, see [Amazon SWF Timeout Types](swf-timeout-types.md "swf-timeout-types.md") .

`defaultTaskStartToCloseTimeoutSeconds`

Specifies the `defaultTaskStartToCloseTimeout` registered with Amazon SWF for
the workflow type. This specifies the time a single decision task for a workflow
execution of this type can take to complete.

If you don't specify `defaultTaskStartToCloseTimeout`, it will default to
30 seconds.

For more information about workflow timeouts, see [Amazon SWF Timeout Types](swf-timeout-types.md "swf-timeout-types.md") .

`defaultTaskList`

The default task list used for decision tasks for executions of this workflow type.
The default set here can be overridden by using `StartWorkflowOptions` when
starting a workflow execution.

If you don't specify `defaultTaskList`, it will be set to
`USE_WORKER_TASK_LIST` by default. This indicates that the task list used
by the worker that is performing the workflow registration should be used.

`defaultChildPolicy`

Specifies the policy to use for child workflows if an execution of this type is
terminated. The default value is `ABANDON`. The possible values are:

- `ABANDON` – Allow the child workflow executions to keep
  running
- `TERMINATE` – Terminate child workflow executions
- `REQUEST_CANCEL` – Request cancellation of the child workflow
  executions
