

# AWS Flow Framework for Java Exceptions
<a name="errorhandling.exceptions"></a>

The following exceptions are used by the AWS Flow Framework for Java. This section provides an overview of the exception. For more details, see the AWS SDK for Java documentation of the individual exceptions.

**Topics**
+ [ActivityFailureException](#errorhandling.exceptions.ActivityFailureException)
+ [ActivityTaskException](#errorhandling.exceptions.ActivityTaskException)
+ [ActivityTaskFailedException](#errorhandling.exceptions.ActivityTaskFailedException)
+ [ActivityTaskTimedOutException](#errorhandling.exceptions.ActivityTaskTimedOutException)
+ [ChildWorkflowException](#errorhandling.exceptions.ChildWorkflowException)
+ [ChildWorkflowFailedException](#errorhandling.exceptions.ChildWorkflowFailedException)
+ [ChildWorkflowTerminatedException](#errorhandling.exceptions.ChildWorkflowTerminatedException)
+ [ChildWorkflowTimedOutException](#errorhandling.exceptions.ChildWorkflowTimedOutException)
+ [DataConverterException](#errorhandling.exceptions.DataConverterException)
+ [DecisionException](#errorhandling.exceptions.DecisionException)
+ [ScheduleActivityTaskFailedException](#errorhandling.exceptions.ScheduleActivityTaskFailedException)
+ [SignalExternalWorkflowException](#errorhandling.exceptions.SignalExternalWorkflowException)
+ [StartChildWorkflowFailedException](#errorhandling.exceptions.StartChildWorkflowFailedException)
+ [StartTimerFailedException](#errorhandling.exceptions.StartTimerFailedException)
+ [TimerException](#errorhandling.exceptions.TimerException)
+ [WorkflowException](#errorhandling.exceptions.WorkflowException)

## ActivityFailureException
<a name="errorhandling.exceptions.ActivityFailureException"></a>

This exception is used by the framework internally to communicate activity failure. When an activity fails due to an unhandled exception, it is wrapped in `ActivityFailureException` and reported to Amazon SWF. You need to deal with this exception only if you use the activity worker extensibility points. Your application code will never need to deal with this exception.

## ActivityTaskException
<a name="errorhandling.exceptions.ActivityTaskException"></a>

This is the base class for activity task failure exceptions: `ScheduleActivityTaskFailedException`, `ActivityTaskFailedException`, `ActivityTaskTimedoutException`. It contains the task Id and activity type of the failed task. You can catch this exception in your workflow implementation to deal with activity failures in a generic way.

## ActivityTaskFailedException
<a name="errorhandling.exceptions.ActivityTaskFailedException"></a>

Unhandled exceptions in activities are reported back to the workflow implementation by throwing an `ActivityTaskFailedException`. The original exception can be retrieved from the cause property of this exception. The exception also provides other information that is useful for debugging purposes, such as the unique activity identifier in the history.

The framework is able to provide the remote exception by serializing the original exception from the activity worker.

## ActivityTaskTimedOutException
<a name="errorhandling.exceptions.ActivityTaskTimedOutException"></a>

This exception is thrown if an activity was timed out by Amazon SWF. This could happen if the activity task could not be assigned to the worker within the require time period or could not be completed by the worker in the required time. You can set these timeouts on the activity using the `@ActivityRegistrationOptions` annotation or using the `ActivitySchedulingOptions` parameter when calling the activity method.

## ChildWorkflowException
<a name="errorhandling.exceptions.ChildWorkflowException"></a>

Base class for exceptions used to report failure of child workflow execution. The exception contains the Ids of the child workflow execution as well as its workflow type. You can catch this exception to deal with child workflow execution failures in a generic way.

## ChildWorkflowFailedException
<a name="errorhandling.exceptions.ChildWorkflowFailedException"></a>

Unhandled exceptions in child workflows are reported back to the parent workflow implementation by throwing a `ChildWorkflowFailedException`. The original exception can be retrieved from the `cause` property of this exception. The exception also provides other information that is useful for debugging purposes, such as the unique identifiers of the child execution.

## ChildWorkflowTerminatedException
<a name="errorhandling.exceptions.ChildWorkflowTerminatedException"></a>

This exception is thrown in parent workflow execution to report the termination of a child workflow execution. You should catch this exception if you want to deal with the termination of the child workflow, for example, to perform cleanup or compensation.

## ChildWorkflowTimedOutException
<a name="errorhandling.exceptions.ChildWorkflowTimedOutException"></a>

This exception is thrown in parent workflow execution to report that a child workflow execution was timed out and closed by Amazon SWF. You should catch this exception if you want to deal with the forced closure of the child workflow, for example, to perform cleanup or compensation.

## DataConverterException
<a name="errorhandling.exceptions.DataConverterException"></a>

The framework uses the `DataConverter` component to marshal and unmarshal data that is sent over the wire. This exception is thrown if the `DataConverter` fails to marshal or unmarshal data. This could happen for various reasons, for example, due to a mismatch in the `DataConverter` components being used to marshal and unmarshal the data.

## DecisionException
<a name="errorhandling.exceptions.DecisionException"></a>

This is the base class for exceptions that represent failures to enact a decision by Amazon SWF. You can catch this exception to generically deal with such exceptions.

## ScheduleActivityTaskFailedException
<a name="errorhandling.exceptions.ScheduleActivityTaskFailedException"></a>

This exception is thrown if Amazon SWF fails to schedule an activity task. This could happen due to various reasons—for example, the activity was deprecated, or an Amazon SWF limit on your account has been reached. The `failureCause` property in the exception specifies the exact cause of failure to schedule the activity.

## SignalExternalWorkflowException
<a name="errorhandling.exceptions.SignalExternalWorkflowException"></a>

This exception is thrown if Amazon SWF fails to process a request by the workflow execution to signal another workflow execution. This happens if the target workflow execution could not be found—that is, the workflow execution you specified doesn't exist or is in closed state.

## StartChildWorkflowFailedException
<a name="errorhandling.exceptions.StartChildWorkflowFailedException"></a>

This exception is thrown if Amazon SWF fails to start a child workflow execution. This could happen due to various reasons—for example, the type of child workflow specified was deprecated, or a Amazon SWF limit on your account has been reached. The `failureCause` property in the exception specifies the exact cause of failure to start the child workflow execution.

## StartTimerFailedException
<a name="errorhandling.exceptions.StartTimerFailedException"></a>

This exception is thrown if Amazon SWF fails to start a timer requested by the workflow execution. This could happen if the specified timer ID is already in use, or an Amazon SWF limit on your account has been reached. The `failureCause` property in the exception specifies the exact cause of failure.

## TimerException
<a name="errorhandling.exceptions.TimerException"></a>

This is the base class for exceptions related to timers.

## WorkflowException
<a name="errorhandling.exceptions.WorkflowException"></a>

This exception is used internally by the framework to report failures in workflow execution. You need to deal with this exception only if you are using a workflow worker extensibility point.