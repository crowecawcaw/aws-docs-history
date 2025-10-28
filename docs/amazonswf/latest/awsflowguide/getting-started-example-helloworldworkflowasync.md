# HelloWorldWorkflowAsync

Application

Sometimes, it's preferable to have a workflow perform certain tasks locally instead of using
an activity. However, workflow tasks often involve processing the values represented by
`Promise<T>` objects. If you pass a `Promise<T>` object to a
synchronous workflow method, the method executes immediately but it can't access the
`Promise<T>` object's value until the object is ready. You could poll
`Promise<T>.isReady` until it returns `true`, but that's
inefficient and the method might block for a long time. A better approach is to use an
_asynchronous method_.

An asynchronous method is implemented much like a standard method—often as a member
of the workflow implementation class—and runs in the workflow implementation's context.
You designate it as an asynchronous method by applying an `@Asynchronous` annotation,
which directs the framework to treat it much like an activity.

- When a workflow implementation calls an asynchronous method, it returns immediately.
  Asynchronous methods typically return a `Promise<T>` object, which becomes
  ready when the method completes.
- If you pass an asynchronous method one or more `Promise<T>` objects, it
  defers execution until all the input objects are ready. An asynchronous method can therefore
  access its input `Promise<T>` values without risking an exception.

###### Note

Because of the way that the AWS Flow Framework for Java executes the workflow, asynchronous methods
typically execute multiple times, so you should use them only for quick low-overhead tasks.
You should use activities to perform lengthy tasks such as large computations. For details,
see [AWS Flow Framework Basic Concepts: Distributed Execution](awsflow-basics-distributed-execution.md "awsflow-basics-distributed-execution.md").

This topic is a walkthrough of HelloWorldWorkflowAsync, a modified version of
HelloWorldWorkflow that replaces one of the activities with an asynchronous method. To implement
the application, create a copy of the helloWorld.HelloWorldWorkflow package in your project
directory and name it helloWorld.HelloWorldWorkflowAsync.

###### Note

This topic builds on the concepts and files presented in the [HelloWorld Application](getting-started-example-helloworld.md "getting-started-example-helloworld.md") and [HelloWorldWorkflow Application](getting-started-example-helloworldworkflow.md "getting-started-example-helloworldworkflow.md") topics. Familiarize yourself
with the files and concepts presented in those topics before proceeding.

The following sections describe how to modify the original HelloWorldWorkflow code to use an
asynchronous method.

## HelloWorldWorkflowAsync Activities Implementation

HelloWorldWorkflowAsync implements its activities worker interface in
`GreeterActivities`, as follows:

```
import com.amazonaws.services.simpleworkflow.flow.annotations.Activities;
import com.amazonaws.services.simpleworkflow.flow.annotations.ActivityRegistrationOptions;

@Activities(version="2.0")
@ActivityRegistrationOptions(defaultTaskScheduleToStartTimeoutSeconds = 300,
                             defaultTaskStartToCloseTimeoutSeconds = 10)
public interface GreeterActivities {
   public String getName();
   public void say(String what);
}
```

This interface is similar to the one used by HelloWorldWorkflow, with the following
exceptions:

- It omits the `getGreeting` activity; that task is now handled by an
  asynchronous method.
- The version number is set to 2.0. After you have registered an activities interface
  with Amazon SWF, you can't modify it unless you change the version number.

The remaining activity method implementations are identical to HelloWorldWorkflow. Just
delete `getGreeting` from `GreeterActivitiesImpl`.

## HelloWorldWorkflowAsync Workflow Implementation

HelloWorldWorkflowAsync defines the workflow interface as follows:

```
import com.amazonaws.services.simpleworkflow.flow.annotations.Execute;
import com.amazonaws.services.simpleworkflow.flow.annotations.Workflow;
import com.amazonaws.services.simpleworkflow.flow.annotations.WorkflowRegistrationOptions;

@Workflow
@WorkflowRegistrationOptions(defaultExecutionStartToCloseTimeoutSeconds = 3600)
public interface GreeterWorkflow {

   @Execute(version = "2.0")
   public void greet();
}
```

The interface is identical to HelloWorldWorkflow apart from a new version number. As with
activities, if you want to change a registered workflow, you must change its version.

HelloWorldWorkflowAsync implements the workflow as follows:

```
import com.amazonaws.services.simpleworkflow.flow.annotations.Asynchronous;
import com.amazonaws.services.simpleworkflow.flow.core.Promise;

public class GreeterWorkflowImpl implements GreeterWorkflow {
   private GreeterActivitiesClient operations = new GreeterActivitiesClientImpl();

   @Override
   public void greet() {
      Promise<String> name = operations.getName();
      Promise<String> greeting = getGreeting(name);
      operations.say(greeting);
   }

   @Asynchronous
   private Promise<String> getGreeting(Promise<String> name) {
      String returnString = "Hello " + name.get() + "!";
      return Promise.asPromise(returnString);
   }
}
```

HelloWorldWorkflowAsync replaces the `getGreeting` activity with a
`getGreeting` asynchronous method but the `greet` method works in much
the same way:

1. Execute the `getName` activity, which immediately returns a
   `Promise<String>` object, `name`, that represents the
   name.
2. Call the `getGreeting` asynchronous method and pass it the
   `name` object. `getGreeting` immediately returns a
   `Promise<String>` object, `greeting`, that represents the
   greeting.
3. Execute the `say` activity and pass it the `greeting`
   object.
4. When `getName` completes, `name` becomes ready and
   `getGreeting` uses its value to construct the greeting.
5. When `getGreeting` completes, `greeting` becomes ready and
   `say` prints the string to the console.

The difference is that, instead of calling the activities client to execute a
`getGreeting` activity, greet calls the asynchronous `getGreeting`
method. The net result is the same, but the `getGreeting` method works somewhat
differently than the `getGreeting` activity.

- The workflow worker uses standard function call semantics to execute
  `getGreeting`. However, the asynchronous execution of the activity is
  mediated by Amazon SWF.
- `getGreeting` runs in the workflow implementation's process.
- `getGreeting` returns a `Promise<String>` object rather
  than a `String` object. To get the String value held by the
  `Promise`, you call its `get()` method. However, because the
  activity is being run asynchronously, its return value might not be ready immediately;
  `get()` will raise an exception until the return value of the asynchronous
  method is available.

For more information about how `Promise` works, see [AWS Flow Framework Basic Concepts: Data Exchange Between Activities and Workflows](awsflow-basics-data-exchange-activities-workflows.md "awsflow-basics-data-exchange-activities-workflows.md").

`getGreeting` creates a return value by passing the greeting string to the
static `Promise.asPromise` method. This method creates a
`Promise<T>` object of the appropriate type, sets the value, and puts it in
the ready state.

## HelloWorldWorkflowAsync

Workflow and Activities Host and Starter

HelloWorldWorkflowAsync implements `GreeterWorker` as the host class for the
workflow and activity implementations. It is identical to the HelloWorldWorkflow
implementation except for the `taskListToPoll` name, which is set to
"`HelloWorldAsyncList`".

```
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflow;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient;
import com.amazonaws.services.simpleworkflow.flow.ActivityWorker;
import com.amazonaws.services.simpleworkflow.flow.WorkflowWorker;

public class GreeterWorker {
    public static void main(String[] args) throws Exception {
        ClientConfiguration config = new ClientConfiguration().withSocketTimeout(70*1000);

        String swfAccessId = System.getenv("AWS_ACCESS_KEY_ID");
        String swfSecretKey = System.getenv("AWS_SECRET_KEY");
        AWSCredentials awsCredentials = new BasicAWSCredentials(swfAccessId, swfSecretKey);

        AmazonSimpleWorkflow service = new AmazonSimpleWorkflowClient(awsCredentials, config);
        service.setEndpoint("https://swf.us-east-1.amazonaws.com");

        String domain = "helloWorldWalkthrough";
        String taskListToPoll = "HelloWorldAsyncList";

        ActivityWorker aw = new ActivityWorker(service, domain, taskListToPoll);
        aw.addActivitiesImplementation(new GreeterActivitiesImpl());
        aw.start();

        WorkflowWorker wfw = new WorkflowWorker(service, domain, taskListToPoll);
        wfw.addWorkflowImplementationType(GreeterWorkflowImpl.class);
        wfw.start();
    }
}
```

HelloWorldWorkflowAsync implements the workflow starter in `GreeterMain`; it is
identical to the HelloWorldWorkflow implementation.

To execute the workflow, run `GreeterWorker` and `GreeterMain`, just
as with HelloWorldWorkflow.
