# Execution Context

###### Topics

- [Decision Context](#executioncontext.decision "#executioncontext.decision")
- [Activity Execution Context](#activitycontext "#activitycontext")
  The framework provides an ambient context to workflow and activity implementations. This context is
  specific to the task being processed and provides some utilities that you can use in your
  implementation. A context object is created every time a new task is processed by the
  worker.

## Decision Context

When a decision task is executed, the framework provides the context to workflow implementation
through the `DecisionContext` class. `DecisionContext` provides context-sensitive information like
workflow execution run Id and clock and timer functionality.

### Accessing DecisionContext in Workflow Implementation

You can access the `DecisionContext` in your workflow implementation using the
`DecisionContextProviderImpl` class. Alternatively, you can inject the context in a field or
property of your workflow implementation using Spring as shown in the Testability and
Dependency Injection section.

```
DecisionContextProvider contextProvider
    = new DecisionContextProviderImpl();
DecisionContext context = contextProvider.getDecisionContext();
```

### Creating a Clock and Timer

The `DecisionContext` contains a property of type
`WorkflowClock` that provides timer and clock functionality. Because the
workflow logic needs to be deterministic, you should not directly use the system clock in
your workflow implementation. The `currentTimeMills` method on the
`WorkflowClock` returns the time of the start event of the decision being
processed. This ensures that you get the same time value during replay, hence, making your
workflow logic deterministic.

`WorkflowClock` also has a `createTimer` method which returns a
`Promise` object that becomes ready after the specified interval. You can use
this value as a parameter to other asynchronous methods to delay their execution by the
specified period of time. This way you can effectively schedule an asynchronous method or activity for execution at a later
time.

The example in the following listing demonstrates how to periodically call an activity.

```
@Workflow
@WorkflowRegistrationOptions(defaultExecutionStartToCloseTimeoutSeconds = 60,
               defaultTaskStartToCloseTimeoutSeconds = 10)
public interface PeriodicWorkflow {

    @Execute(version = "1.0")
    void periodicWorkflow();
}

@Activities(version = "1.0")
@ActivityRegistrationOptions(defaultTaskScheduleToStartTimeoutSeconds = 300,
                             defaultTaskStartToCloseTimeoutSeconds = 3600)
public interface PeriodicActivity {
    void activity1();
}

public class PeriodicWorkflowImpl implements PeriodicWorkflow {

    private DecisionContextProvider contextProvider
         = new DecisionContextProviderImpl();

    private WorkflowClock clock
         = contextProvider.getDecisionContext().getWorkflowClock();

    @Override
    public void periodicWorkflow() {
        callPeriodicActivity(0);
    }

    @Asynchronous
    private void callPeriodicActivity(int count,
                                      Promise<?>... waitFor) {
        if (count == 100) {
            return;
        }
        PeriodicActivityClient client = new PeriodicActivityClientImpl();
        // call activity
        Promise<Void> activityCompletion = client.activity1();

        Promise<Void> timer = clock.createTimer(3600);

        // Repeat the activity either after 1 hour or after previous activity run
        // if it takes longer than 1 hour
        callPeriodicActivity(count + 1, timer, activityCompletion);
    }
}


public class PeriodicActivityImpl implements PeriodicActivity
{
@Override
   public void activity1() {
      ...
      }
}
```

In the above listing, the `callPeriodicActivity` asynchronous method calls
`activity1` and then creates a timer using the current
`AsyncDecisionContext`. It passes the returned `Promise` as an
argument to a recursive call to itself. This recursive call waits until the timer fires (1
hour in this example) before executing.

## Activity Execution Context

Just as the `DecisionContext` provides context information when a decision
task is being processed, `ActivityExecutionContext` provides similar context
information when an activity task is being processed. This context is available to your
activity code through `ActivityExecutionContextProviderImpl` class.

```
ActivityExecutionContextProvider provider
    = new ActivityExecutionContextProviderImpl();
ActivityExecutionContext aec = provider.getActivityExecutionContext();
```

Using `ActivityExecutionContext`, you can perform the following:

### Heartbeat a Long Running Activity

If the activity is long running, it must periodically report its progress to Amazon SWF to
let it know that the task is still making progress. In the absence of such a heartbeat, the
task may timeout if a task heartbeat timeout was set at activity type registration or
while scheduling the activity. In order to send a heartbeat, you can use the `recordActivityHeartbeat`
method on `ActivityExecutionContext`. Heartbeat also provides a mechanism for canceling
ongoing activities. See the [Error Handling](errorhandling.md "errorhandling.md") section for more details and an example.

### Get Details of the Activity Task

If you want, you can get all the details of the activity task that were passed by
Amazon SWF when the executor got the task. This includes information regarding the inputs to
the task, task type, task token, etc. If you want to implement an activity that is
manually completed—for example, by a human action—then you must use the
`ActivityExecutionContext` to retrieve the task token and pass it to the
process that will eventually complete the activity task. See the section on [Manually Completing Activities](activityimpl.md#activityimpl.complete "activityimpl.md#activityimpl.complete") for more
details.

### Get the Amazon SWF Client Object that is Being Used by the Executor

The Amazon SWF client object being used by the executor can be retrieved by calling
`getService` method on `ActivityExecutionContext`. This is useful
if you want to make a direct call to the Amazon SWF service.
