# HelloWorldWorkflowParallel Application

The preceding versions of Hello World! all use a linear workflow topology. However, Amazon SWF
isn't limited to linear topologies. The HelloWorldWorkflowParallel application is a modified
version of HelloWorldWorkflow that uses a parallel topology, as shown in the following
figure.

![HelloWorldWorkflowParallel workflow topology](images/helloworld_parallel_topology.png)
With HelloWorldWorkflowParallel, `getName` and `getGreeting`
run in parallel and each return part of the greeting. `say` then merges the two strings
into a greeting, and prints it to the console.

To implement the application, create a copy of the helloWorld.HelloWorldWorkflow package
in your project directory and name it helloWorld.HelloWorldWorkflowParallel. The following
sections describe how to modify the original HelloWorldWorkflow code to run `getName`
and `getGreeting` in parallel.

## HelloWorldWorkflowParallel Activities Worker

The HelloWorldWorkflowParallel activities interface is implemented in
`GreeterActivities`, as shown in the following example.

```
import com.amazonaws.services.simpleworkflow.flow.annotations.Activities;
import com.amazonaws.services.simpleworkflow.flow.annotations.ActivityRegistrationOptions;

@Activities(version="5.0")
@ActivityRegistrationOptions(defaultTaskScheduleToStartTimeoutSeconds = 300,
                             defaultTaskStartToCloseTimeoutSeconds = 10)
public interface GreeterActivities {
   public String getName();
   public String getGreeting();
   public void say(String greeting, String name);
}
```

The interface is similar to HelloWorldWorkflow, with the following exceptions:

- `getGreeting` doesn't take any input; it simply
  returns a greeting string.
- `say` takes two input strings, the greeting and the
  name.
- The interface has a new version number, which is required any time that you change a
  registered interface.

HelloWorldWorkflowParallel implements the activities in
`GreeterActivitiesImpl`, as follows:

```
public class GreeterActivitiesImpl implements GreeterActivities {

   @Override
   public String getName() {
      return "World!";
   }

   @Override
   public String getGreeting() {
      return "Hello ";
   }

   @Override
   public void say(String greeting, String name) {
      System.out.println(greeting + name);
   }
}
```

`getName` and `getGreeting` now simply return half of the greeting string.
`say` concatenates the two pieces to produce the complete phrase,
and prints it to the console.

## HelloWorldWorkflowParallel Workflow Worker

The HelloWorldWorkflowParallel workflow interface is implemented in
`GreeterWorkflow`, as follows:

```
import com.amazonaws.services.simpleworkflow.flow.annotations.Execute;
import com.amazonaws.services.simpleworkflow.flow.annotations.Workflow;
import com.amazonaws.services.simpleworkflow.flow.annotations.WorkflowRegistrationOptions;

@Workflow
@WorkflowRegistrationOptions(defaultExecutionStartToCloseTimeoutSeconds = 3600)
public interface GreeterWorkflow {

   @Execute(version = "5.0")
   public void greet();
}
```

The class is identical to the HelloWorldWorkflow version, except that the version
number has been changed to match the activities worker.

The workflow is implemented in `GreeterWorkflowImpl`, as follows:

```
import com.amazonaws.services.simpleworkflow.flow.core.Promise;

public class GreeterWorkflowImpl implements GreeterWorkflow {
   private GreeterActivitiesClient operations = new GreeterActivitiesClientImpl();

   public void greet() {
      Promise<String> name = operations.getName();
      Promise<String> greeting = operations.getGreeting();
      operations.say(greeting, name);
   }
}
```

At a glance, this implementation looks very similar to HelloWorldWorkflow; the three activities client
methods execute in sequence. However, the activities don't.

- HelloWorldWorkflow passed `name` to `getGreeting`. Because `name` was a
  `Promise<T>` object, `getGreeting` deferred executing the activity until
  `getName` completed, so the two activities executed in sequence.
- HelloWorldWorkflowParallel doesn't pass any input `getName` or `getGreeting`.
  Neither method defers execution and the associated activity methods execute immediately, in parallel.

The `say` activity takes both `greeting` and `name` as input parameters.
Because they are `Promise<T>` objects, `say` defers execution until both activities
complete, and then constructs and prints the greeting.

Notice that HelloWorldWorkflowParallel doesn't use any special modeling code to define the workflow
topology. It does it implicitly by using standard Java flow control and taking advantage of the properties of
`Promise<T>` objects. AWS Flow Framework for Java applications can implement even complex topologies simply by
using `Promise<T>` objects in conjunction with conventional Java control flow constructs.

## HelloWorldWorkflowParallel Workflow and Activities Host and Starter

HelloWorldWorkflowParallel implements `GreeterWorker` as the host class for the workflow and
activity implementations. It is identical to the HelloWorldWorkflow implementation except for the
`taskListToPoll` name, which is set to "HelloWorldParallelList".

`HelloWorldWorkflowParallel` implements the workflow starter in `GreeterMain`, and it
is identical to the HelloWorldWorkflow implementation.

To execute the workflow, run `GreeterWorker` and `GreeterMain`, just as with
`HelloWorldWorkflow`.
