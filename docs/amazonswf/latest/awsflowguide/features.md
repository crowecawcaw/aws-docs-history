# Workflow and Activity Contracts

Java interfaces are used to declare the signatures of workflows and activities. The interface forms the
contract between the implementation of the workflow (or activity) and the client of that workflow (or activity).
For example, a workflow type `MyWorkflow` is defined using an interface that is annotated with the
`@Workflow` annotation:

```
@Workflow
@WorkflowRegistrationOptions(
   defaultExecutionStartToCloseTimeoutSeconds = 60,
   defaultTaskStartToCloseTimeoutSeconds = 10)
public interface MyWorkflow
{
    @Execute(version = "1.0")
    void startMyWF(int a, String b);

    @Signal
    void signal1(int a, int b, String c);

    @GetState
    MyWorkflowState getState();
}
```

The contract has no implementation-specific settings. This use of implementation-neutral contracts allows
clients to be decoupled from the implementation and hence provides the flexibility to change the implementation
details without breaking the client. Conversely, you may also change the client without necessitating changes to
the workflow or activity being consumed. For example, the client may be modified to call an activity
asynchronously using promises (`Promise<T>`) without requiring a change to the activity
implementation. Similarly, the activity implementation may be changed so that it is completed asynchronously, for
example, by a person sending an email—without requiring the clients of the activity to be changed.

In the example above, the workflow interface `MyWorkflow` contains a method,
`startMyWF`, for starting a new execution. This method is annotated with the `@Execute`
annotation and must have a return type of `void` or `Promise<>`. In a given workflow
interface, at most one method can be annotated with this annotation. This method is the entry point of the
workflow logic, and the framework calls this method to execute the workflow logic when a decision task is
received.

The workflow interface also defines the signals that may be sent to the workflow. The signal method gets
invoked when a signal with a matching name is received by the workflow execution. For example, the
`MyWorkflow` interface declares a signal method, `signal1`, annotated with the
`@Signal` annotation.

The `@Signal` annotation is required on signal methods. The return type of a signal method must
be `void`. A workflow interface may have zero or more signal methods defined in it. You may declare a
workflow interface without an `@Execute` method and some `@Signal` methods to generate
clients that can't start their execution but can send signals to running executions.

Methods annotated with `@Execute` and `@Signal` annotations may have any number of
parameters of any type other than `Promise<T>` or its derivatives. This allows you to pass strongly
typed inputs to a workflow execution at start and while it is running. The return type of the
`@Execute` method must be `void` or `Promise<>`.

Additionally, you may also declare a method in the workflow interface to report the latest state of a
workflow execution, for instance, the `getState` method in the previous example. This state isn't the
entire application state of the workflow. The intended use of this feature is to allow you to store up to 32 KB of
data to indicate the latest status of the execution. For example, in an order processing workflow, you may store a
string that indicates that the order has been received, processed, or canceled. This method is called by the
framework every time a decision task is completed to get the latest state. The state is stored in Amazon Simple Workflow Service
(Amazon SWF) and can be retrieved using the generated external client. This allows you to check the latest state of a
workflow execution. Methods annotated with `@GetState` must not take any arguments and must not have a
`void` return type. You can return any type, which fits your needs, from this method. In the above
example, an object of `MyWorkflowState` (see definition below) is returned by the method that is used
to store a string state and a numeric percent complete. The method is expected to perform read-only access of the
workflow implementation object and is invoked synchronously, which disallows use of any asynchronous operations
like calling methods annotated with `@Asynchronous`. At most one method in a workflow interface can be
annotated with `@GetState` annotation.

```
public class MyWorkflowState {
   public String status;
   public int percentComplete;
}
```

Similarly, a set of activities are defined using an interface annotated with `@Activities`
annotation. Each method in the interface corresponds to an activity—for example:

```
@Activities(version = "1.0")
@ActivityRegistrationOptions(
     defaultTaskScheduleToStartTimeoutSeconds = 300,
     defaultTaskStartToCloseTimeoutSeconds = 3600)
public interface MyActivities {
    // Overrides values from annotation found on the interface
    @ActivityRegistrationOptions(description = "This is a sample activity",
         defaultTaskScheduleToStartTimeoutSeconds = 100,
         defaultTaskStartToCloseTimeoutSeconds = 60)
    int activity1();

    void activity2(int a);
}
```

The interface allows you to group together a set of related activities. You can define any number of
activities within an activities interface, and you can define as many activities interfaces as you want. Similar
to `@Execute` and `@Signal` methods, activity methods can take any number of arguments of
any type other than `Promise<T>` or its derivatives. The return type of an activity must not be
`Promise<T>` or its derivatives.
