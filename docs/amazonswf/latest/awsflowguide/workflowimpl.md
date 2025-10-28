# Workflow Implementation

In order to implement a workflow, you write a class that implements the desired
`@Workflow` interface. For instance, the example workflow interface
(`MyWorkflow`) can be implemented like so:

```
public class MyWFImpl implements MyWorkflow
{
  MyActivitiesClient client = new MyActivitiesClientImpl();
  @Override
  public void startMyWF(int a, String b){
    Promise<Integer> result = client.activity1();
    client.activity2(result);
  }
  @Override
  public void signal1(int a, int b, String c){
    //Process signal
     client.activity2(a + b);
  }
}
```

The `@Execute` method in this class is the entry point of the workflow logic. Because the framework uses replay to reconstruct
the object state when a decision task is to be processed, a new object is created for each decision task.

The use of `Promise<`T`>` as a parameter is
disallowed in the `@Execute` method within a `@Workflow` interface. This
is done because making an asynchronous call is purely a decision of the caller. The workflow
implementation itself doesn't depend on whether the invocation was synchronous or
asynchronous. Therefore, the generated client interface has overloads that take
`Promise<`T`>` parameters so that these methods can
be called asynchronously.

The return type of an `@Execute` method can only be `void` or
`Promise<`T`>`. Note that a return type of the
corresponding external client is `void` and not `Promise<>`. Because
the external client isn't intended to be used from the asynchronous code, the external client
doesn't return `Promise` objects. For getting results of workflow executions
stated externally, you can design the workflow to update state in an external data store
through an activity. Amazon SWF's visibility APIs can also be used to retrieve the result of a
workflow for diagnostic purposes. It isn't recommended that you use the visibility APIs to
retrieve results of workflow executions as a general practice because these API calls may get
throttled by Amazon SWF. The visibility APIs require you to identify the workflow execution using a
`WorkflowExecution` structure. You can get this structure from the generated
workflow client by calling the `getWorkflowExecution` method. This method will
return the `WorkflowExecution` structure corresponding to the workflow execution
that the client is bound to. See the [Amazon Simple Workflow Service API Reference](../apireference.md "../apireference.md") for more details about the visibility APIs.

When calling activities from your workflow implementation, you should use the generated
activities client. Similarly, to send signals, use the generated workflow clients.

## Decision Context

The framework provides an ambient context anytime workflow code is executed by the framework. This context provides
context-specific functionality that you may access in your workflow implementation, such as creating a timer.
See the section on [Execution Context](executioncontext.md "executioncontext.md") for more information.

## Exposing Execution State

Amazon SWF allows you to add custom state in the workflow history. The latest state reported by
the workflow execution is returned to you through visibility calls to the Amazon SWF service and
in the Amazon SWF console. For example, in an order processing workflow, you may report the order
status at different stages like 'order received', 'order shipped', and so on. In the
AWS Flow Framework for Java, this is accomplished through a method on your workflow interface that is annotated
with the `@GetState` annotation. When the decider is done processing a decision task, it
calls this method to get the latest state from the workflow implementation. Besides
visibility calls, the state can also be retrieved using the generated external client
(which uses the visibility API calls internally).

The following example demonstrates how to set the execution context.

```
@Workflow
@WorkflowRegistrationOptions(defaultExecutionStartToCloseTimeoutSeconds = 60,
               defaultTaskStartToCloseTimeoutSeconds = 10)
public interface PeriodicWorkflow {

    @Execute(version = "1.0")
    void periodicWorkflow();

    @GetState
    String getState();
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

    private PeriodicActivityClient activityClient
               = new PeriodicActivityClientImpl();

    private String state;

    @Override
    public void periodicWorkflow() {
        state = "Just Started";
        callPeriodicActivity(0);
    }

    @Asynchronous
    private void callPeriodicActivity(int count,
                                      Promise<?>... waitFor)
    {
        if(count == 100) {
            state = "Finished Processing";
            return;
        }

        // call activity
        activityClient.activity1();

        // Repeat the activity after 1 hour.
        Promise<Void> timer = clock.createTimer(3600);
        state = "Waiting for timer to fire. Count = "+count;
        callPeriodicActivity(count+1, timer);
    }

    @Override
    public String getState() {
        return state;
    }
}

public class PeriodicActivityImpl implements PeriodicActivity
{
@Override
      public static void activity1()
   {
      ...
    }
}
```

The generated external client can be used to retrieve the latest state of the workflow
execution at any time.

```

PeriodicWorkflowClientExternal client
        = new PeriodicWorkflowClientExternalFactoryImpl().getClient();
System.out.println(client.getState());
```

In the above example, the execution state is reported at various stages. When the
workflow instance starts, `periodicWorkflow` reports the initial state as 'Just Started'.
Each call to `callPeriodicActivity` then updates the workflow state. Once `activity1` has been
called 100 times, the method returns and the workflow instance completes.

## Workflow Locals

Sometimes, you may have a need for the use of static variables in your workflow
implementation. For example, you may want to store a counter that is to be accessed from
various places (possibly different classes) in the implementation of the workflow. However,
you can't rely on static variables in your workflows because static variables are shared
across threads, which is problematic because a worker may process different decision tasks
on different threads at the same time. Alternatively, you may store such state in a field on
the workflow implementation, but then you will need to pass the implementation object
around. To address this need, the framework provides a
`WorkflowExecutionLocal<?>` class. Any state that needs to have static
variable like semantics should be kept as an instance local using
`WorkflowExecutionLocal<?>`. You can declare and use a static variable of
this type. For example, in the following snippet, a
`WorkflowExecutionLocal<String>` is used to store a user name.

```
public class MyWFImpl implements MyWF {
  public static WorkflowExecutionLocal<String> username
      = new WorkflowExecutionLocal<String>();

  @Override
  public void start(String username){
    this.username.set(username);
    Processor p = new Processor();
    p.updateLastLogin();
    p.greetUser();
   }

  public static WorkflowExecutionLocal<String> getUsername() {
    return username;
  }

  public static void setUsername(WorkflowExecutionLocal<String> username) {
    MyWFImpl.username = username;
  }
}

public class Processor {
  void updateLastLogin(){
    UserActivitiesClient c = new UserActivitiesClientImpl();
    c.refreshLastLogin(MyWFImpl.getUsername().get());
  }
   void greetUser(){
    GreetingActivitiesClient c = new GreetingActivitiesClientImpl();
    c.greetUser(MyWFImpl.getUsername().get());
  }
}
```
