# HelloWorldWorkflow Application

Although the basic [HelloWorld](getting-started-example-helloworld.md "getting-started-example-helloworld.md") example is structured
like a workflow, it differs from an Amazon SWF workflow in several key respects:

| Conventional and Amazon SWF Workflow Applications                                          | HelloWorld                                                                                                                                                                                                                  | Amazon SWF Workflow |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Runs locally as a single process.                                                          | Runs as multiple processes that can be distributed across multiple systems, including Amazon EC2<br>instances, private data centers, client computers, and so on. They don't even have to run the same<br>operating system. |
| Activities are synchronous methods, which block until they complete.                       | Activities are represented by asynchronous methods, which return immediately and allow the workflow<br>to perform other tasks while waiting for the activity to complete.                                                   |
| The workflow worker interacts with an activities worker by calling the appropriate method. | Workflow workers interact with activities workers by using HTTP requests, with Amazon SWF acting as an<br>intermediary.                                                                                                     |
| The workflow starter interacts with workflow worker by calling the appropriate method.     | Workflow starters interact with workflow workers by using HTTP requests, with Amazon SWF acting as an<br>intermediary.                                                                                                      |

You could implement a distributed asynchronous workflow application from scratch, for example, by having your
workflow worker interact with an activities worker directly through web services calls. However, you must then
implement all the complicated code required to manage the asynchronous execution of multiple activities, handle the
data flow, and so on. The AWS Flow Framework for Java and Amazon SWF take care of all those details, which allows you to focus on
implementing the business logic.

HelloWorldWorkflow is a modified version of HelloWorld that runs as an Amazon SWF workflow. The following figure
summarizes how the two applications work.

![Conventional and Amazon SWF versions of Hello World!](images/workflow_conceptual_welcome.png)
HelloWorld runs as a single process and the starter, workflow worker, and activities worker interact by using
conventional method calls. With `HelloWorldWorkflow`, the starter, workflow worker, and activities worker
are distributed components that interact through Amazon SWF by using HTTP requests. Amazon SWF manages the interaction by
maintaining lists of workflow and activities tasks, which it dispatches to the respective components. This section
describes how the framework works for HelloWorldWorkflow.

HelloWorldWorkflow is implemented by using the AWS Flow Framework for Java API, which handles the sometimes complicated
details of interacting with Amazon SWF in the background and simplifies the development process considerably. You can use
the same project that you did for HelloWorld, which is already configured for AWS Flow Framework for Java applications. However,
to run the application, you must set up an Amazon SWF account, as follows:

- Sign up for an AWS account, if you don't already have one, at [Amazon Web Services](https://aws.amazon.com/ "https://aws.amazon.com/").
- Assign your account's Access ID and secret ID to the AWS_ACCESS_KEY_ID and AWS_SECRET_KEY environment
  variables, respectively. It's a good practice to not expose the literal key values in your code. Storing them
  in environment variables is a convenient way to handle the issue.
- Sign up for Amazon SWF account at [Amazon Simple Workflow
  Service](https://aws.amazon.com/swf/ "https://aws.amazon.com/swf/").
- Log into the AWS Management Console and select the Amazon SWF service.
- Choose **Manage Domains** in the upper right corner and register a new Amazon SWF domain. A
  _domain_ is a logical container for your application resources, such as workflow and
  activity types, and workflow executions. You can use any convenient domain name, but the walkthroughs use
  "helloWorldWalkthrough".
  To implement the HelloWorldWorkflow, create a copy of the helloWorld.HelloWorld package in your project directory
  and name it helloWorld.HelloWorldWorkflow. The following sections describe how to modify the original HelloWorld
  code to use the AWS Flow Framework for Java and run as an Amazon SWF workflow application.

## HelloWorldWorkflow Activities Worker

HelloWorld implemented its activities worker as a single class. An AWS Flow Framework for Java activities worker has
three basic components:

- The _activity methods_—which perform the actual tasks—are
  defined in an interface and implemented in a related class.
- An [ActivityWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md") class manages the interaction between the activity methods and
  Amazon SWF.
- An _activities host_ application registers and starts the activities
  worker, and handles cleanup.

This section discusses the activity methods; the other two classes are discussed later.

HelloWorldWorkflow defines the activities interface in `GreeterActivities`, as follows:

```
import com.amazonaws.services.simpleworkflow.flow.annotations.Activities;
import com.amazonaws.services.simpleworkflow.flow.annotations.ActivityRegistrationOptions;

@ActivityRegistrationOptions(defaultTaskScheduleToStartTimeoutSeconds = 300,
                             defaultTaskStartToCloseTimeoutSeconds = 10)
@Activities(version="1.0")

public interface GreeterActivities {
   public String getName();
   public String getGreeting(String name);
   public void say(String what);
}
```

This interface wasn't strictly necessary for HelloWorld, but it is for an AWS Flow Framework for Java application. Notice
that the interface definition itself hasn't changed. However, you must apply two AWS Flow Framework for Java annotations,
[@ActivityRegistrationOptions](annotations.md#annotations-activityregistration "annotations.md#annotations-activityregistration") and
[@Activities](annotations.md#annotations-activities "annotations.md#annotations-activities"), to the interface definition. The
annotations provide configuration information and direct the AWS Flow Framework for Java annotation processor to use the
interface definition to generate an _activities client_ class, which is discussed
later.

`@ActivityRegistrationOptions` has several named values that are used to configure the
activities' behavior. HelloWorldWorkflow specifies two timeouts:

- `defaultTaskScheduleToStartTimeoutSeconds` specifies how long the tasks can be queued in the
  activities task list, and is set to 300 seconds (5 minutes).
- `defaultTaskStartToCloseTimeoutSeconds` specifies the maximum time the activity can take to
  perform the task and is set to 10 seconds.

These timeouts ensure that the activity completes its task in a reasonable amount of time. If either timeout
is exceeded, the framework generates an error and the workflow worker must decide how to handle the issue. For a
discussion of how to handle such errors, see [Error Handling](errorhandling.md "errorhandling.md").

`@Activities` has several values, but typically it just specifies the activities' version number,
which allows you to keep track of different generations of activity implementations. If you change an activity
interface after you have registered it with Amazon SWF, including changing the
`@ActivityRegistrationOptions` values, you must use a new version number.

HelloWorldWorkflow implements the activity methods in `GreeterActivitiesImpl`, as follows:

```
public class GreeterActivitiesImpl implements GreeterActivities {
   @Override
   public String getName() {
      return "World";
   }
   @Override
   public String getGreeting(String name) {
      return "Hello " + name;
   }
   @Override
   public void say(String what) {
      System.out.println(what);
   }
}
```

Notice that the code is identical to the HelloWorld implementation. At its core, an AWS Flow Framework activity is
just a method that executes some code and perhaps returns a result. The difference between a standard application
and an Amazon SWF workflow application lies in how the workflow executes the activities, where the activities execute,
and how the results are returned to the workflow worker.

## HelloWorldWorkflow Workflow Worker

An Amazon SWF workflow worker has three basic components.

- A _workflow implementation_, which is a class that performs the
  workflow-related tasks.
- An _activities client_ class, which is basically a proxy for the
  activities class and is used by a workflow implementation to execute activity methods asynchronously.
- A [WorkflowWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowWorker.md")
  class, which manages the interaction between the workflow and Amazon SWF.

This section discusses the workflow implementation and activities client; the `WorkflowWorker`
class is discussed later.

HelloWorldWorkflow defines the workflow interface in `GreeterWorkflow`, as follows:

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

This interface also isn't strictly necessary for HelloWorld but is essential for an AWS Flow Framework for Java
application. You must apply two AWS Flow Framework for Java annotations, [@Workflow](annotations.md#annotations-workflow "annotations.md#annotations-workflow") and
[@WorkflowRegistrationOptions](annotations.md#annotations-workflowregistrationoptions "annotations.md#annotations-workflowregistrationoptions"), to the workflow interface definition. The annotations
provide configuration information and also direct the AWS Flow Framework for Java annotation processor to generate a workflow
client class based on the interface, as discussed later.

`@Workflow` has one optional parameter, _dataConverter_, which is often used
with its default value, NullDataConverter, which indicates that JsonDataConverter should be used.

`@WorkflowRegistrationOptions` also has a number of optional parameters that can be used to
configure the workflow worker. Here, we set `defaultExecutionStartToCloseTimeoutSeconds`—which
specifies how long the workflow can run—to 3600 seconds (1 hour).

The `GreeterWorkflow` interface definition differs from HelloWorld in one important way, the
[@Execute](annotations.md#annotations-execute "annotations.md#annotations-execute") annotation. Workflow interfaces specify
the methods that can be called by applications such as the workflow starter and are limited to a handful of
methods, each with a particular role. The framework doesn't specify a name or parameter list for workflow
interface methods; you use a name and parameter list that is suitable for your workflow and apply an
AWS Flow Framework for Java annotation to identify the method's role.

`@Execute` has two purposes:

- It identifies `greet` as the workflow's entry point—the method that the workflow starter
  calls to start the workflow. In general, an entry point can take one or more parameters, which allows the
  starter to initialize the workflow, but this example doesn't require initialization.
- It specifies the workflow's version number, which allows you to keep track of different generations of
  workflow implementations. To change a workflow interface after you have registered it with Amazon SWF, including
  changing the timeout values, you must use a new version number.

For information about the other methods that can be included in a workflow interface, see [Workflow and Activity Contracts](features.md "features.md").

HelloWorldWorkflow implements the workflow in `GreeterWorkflowImpl`, as follows:

```
import com.amazonaws.services.simpleworkflow.flow.core.Promise;

public class GreeterWorkflowImpl implements GreeterWorkflow {
   private GreeterActivitiesClient operations = new GreeterActivitiesClientImpl();

   public void greet() {
     Promise<String> name = operations.getName();
     Promise<String> greeting = operations.getGreeting(name);
     operations.say(greeting);
   }
}
```

The code is similar to HelloWorld, but with two important differences.

- `GreeterWorkflowImpl` creates an instance of `GreeterActivitiesClientImpl`, the
  activities client, instead of `GreeterActivitiesImpl`, and executes activities by calling methods
  on the client object.
- The name and greeting activities return `Promise<String>` objects instead of
  `String` objects.

HelloWorld is a standard Java application that runs locally as a single process, so
`GreeterWorkflowImpl` can implement the workflow topology by simply creating an instance of
`GreeterActivitiesImpl`, calling the methods in order, and passing the return values from one activity
to the next. With an Amazon SWF workflow, an activity's task is still performed by an activity method from
`GreeterActivitiesImpl`. However, the method doesn't necessarily run in the same process as the
workflow—it might not even run on the same system—and the workflow needs to execute the activity asynchronously.
These requirements raise the following issues:

- How to execute an activity method that might be running in a different process, perhaps on a different
  system.
- How to execute an activity method asynchronously.
- How to manage activities' input and return values. For example, if the Activity A return value is an
  input to Activity B, you must ensure that Activity B doesn't execute until Activity A is complete.

You can implement a variety of workflow topologies through the application's control flow by using familiar
Java flow control combined with the activities client and the `Promise<T>`.

### Activities Client

`GreeterActivitiesClientImpl` is basically a proxy for `GreeterActivitiesImpl` that
allows a workflow implementation to execute the `GreeterActivitiesImpl` methods
asynchronously.

The `GreeterActivitiesClient` and `GreeterActivitiesClientImpl` classes are
generated automatically for you using the information provided in the annotations applied to your
`GreeterActivities` class. You don't need to implement these yourself.

###### Note

Eclipse generates these classes when you save your project. You can view the
generated code in the `.apt_generated` subdirectory of your project directory.

To avoid compilation errors in your `GreeterWorkflowImpl` class, it is
a good practice to move the `.apt_generated` directory to the top of the
**Order and Export** tab of the **Java Build
Path** dialog box.

A workflow worker executes an activity by calling the corresponding client method. The method is
asynchronous and immediately returns a `Promise<T>` object, where `T` is the
activity's return type. The returned `Promise<T>` object is basically a placeholder for the
value that the activity method will eventually return.

- When the activities client method returns, the `Promise<T>` object is initially in
  an _unready state_, which indicates that the object doesn't yet
  represent a valid return value.
- When the corresponding activity method completes its task and returns, the framework assigns the
  return value to the `Promise<T>` object and puts it in the _ready
  state_.

### Promise<T> Type

The primary purpose of `Promise<T>` objects is to manage data flow between asynchronous
components and control when they execute. It relieves your application of the need to explicitly manage
synchronization or depend on mechanisms such as timers to ensure that asynchronous components don't execute
prematurely. When you call an activities client method, it immediately returns but the framework defers
executing the corresponding activity method until any input `Promise<T>` objects are ready and
represent valid data.

From `GreeterWorkflowImpl` perspective, all three activities client methods return
immediately. From the `GreeterActivitiesImpl` perspective, the framework doesn't call
`getGreeting` until `name` completes, and doesn't call `say` until
`getGreeting` completes.

By using `Promise<T>` to pass data from one activity to the next,
`HelloWorldWorkflow` not only ensures that activity methods don't attempt to use invalid data, it
also controls when the activities execute and implicitly defines the workflow topology. Passing each activity's
`Promise<T>` return value to the next activity requires the activities to execute in sequence,
defining the linear topology discussed earlier. With AWS Flow Framework for Java, you don't need to use any special modeling
code to define even complex topologies, just standard Java flow control and `Promise<T>`. For
an example of how to implement a simple parallel topology, see [HelloWorldWorkflowParallel Activities Worker](getting-started-example-helloworldworkflowparallel.md#getting-started-example-helloworldworkflowparallel.activities "getting-started-example-helloworldworkflowparallel.md#getting-started-example-helloworldworkflowparallel.activities").

###### Note

When an activity method such as `say` doesn't return a value, the corresponding client
method returns a `Promise<Void>` object. The object doesn't represent data, but it is
initially unready and becomes ready when the activity completes. You can therefore pass a
`Promise<Void>` object to other activities client methods to ensure that they defer
execution until the original activity completes.

`Promise<T>` allows a workflow implementation to use activities client methods and their
return values much like synchronous methods. However, you must be careful about accessing a
`Promise<T>` object's value. Unlike the Java [Future<T>](http://docs.oracle.com/javase/6/docs/api/java/util/concurrent/Future.html "http://docs.oracle.com/javase/6/docs/api/java/util/concurrent/Future.html") type, the framework handles synchronization for
`Promise<T>`, not the application. If you call `Promise<T>.get` and the
object isn't ready, `get` throws an exception. Notice that `HelloWorldWorkflow` never
accesses a `Promise<T>` object directly; it simply passes the objects from one activity to
the next. When an object becomes ready, the framework extracts the value and passes it to the activity method
as a standard type.

`Promise<T>` objects should be accessed only by asynchronous code, where the framework
guarantees that the object is ready and represents a valid value. `HelloWorldWorkflow` deals with
this issue by passing `Promise<T>` objects only to activities client methods. You can access
a `Promise<T>` object's value in your workflow implementation by passing the object to an
_asynchronous workflow method_, which behaves much like an activity. For an example, see
[HelloWorldWorkflowAsync Application](getting-started-example-helloworldworkflowasync.md "getting-started-example-helloworldworkflowasync.md").

## HelloWorldWorkflow Workflow and Activities Implementation

The workflow and activities implementations have associated worker classes, [ActivityWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md") and
[WorkflowWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowWorker.md").
They handle communication between Amazon SWF and the activities and workflow implementations by polling the appropriate
Amazon SWF task list for tasks, executing the appropriate method for each task, and managing the data flow. For
details, see [AWS Flow Framework Basic Concepts: Application Structure](awsflow-basics-application-structure.md "awsflow-basics-application-structure.md")

To associate the activity and workflow implementations with the corresponding worker objects, you implement
one or more worker applications which:

- Register workflows or activities with Amazon SWF.
- Create worker objects and associate them with the workflow or activity worker implementations.
- Direct the worker objects to start communicating with Amazon SWF.

If you want to run the workflow and activities as separate processes, you must implement separate workflow
and activities worker hosts. For an example, see [HelloWorldWorkflowDistributed Application](getting-started-example-helloworldworkflowdistributed.md "getting-started-example-helloworldworkflowdistributed.md"). For simplicity, HelloWorldWorkflow
implements a single worker host that runs activities and workflow workers in the same process, as follows:

```
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflow;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient;
import com.amazonaws.services.simpleworkflow.flow.ActivityWorker;
import com.amazonaws.services.simpleworkflow.flow.WorkflowWorker;

public class GreeterWorker  {
   public static void main(String[] args) throws Exception {
     ClientConfiguration config = new ClientConfiguration().withSocketTimeout(70*1000);

     String swfAccessId = System.getenv("AWS_ACCESS_KEY_ID");
     String swfSecretKey = System.getenv("AWS_SECRET_KEY");
     AWSCredentials awsCredentials = new BasicAWSCredentials(swfAccessId, swfSecretKey);

     AmazonSimpleWorkflow service = new AmazonSimpleWorkflowClient(awsCredentials, config);
     service.setEndpoint("https://swf.us-east-1.amazonaws.com");

     String domain = "helloWorldWalkthrough";
     String taskListToPoll = "HelloWorldList";

     ActivityWorker aw = new ActivityWorker(service, domain, taskListToPoll);
     aw.addActivitiesImplementation(new GreeterActivitiesImpl());
     aw.start();

     WorkflowWorker wfw = new WorkflowWorker(service, domain, taskListToPoll);
     wfw.addWorkflowImplementationType(GreeterWorkflowImpl.class);
     wfw.start();
   }
}
```

`GreeterWorker` has no HelloWorld counterpart, so you must add a Java class named
`GreeterWorker` to the project and copy the example code to that file.

The first step is to create and configure an [AmazonSimpleWorkflowClient](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.md")
object, which invokes the underlying Amazon SWF service methods. To do so, `GreeterWorker`:

1. Creates a [ClientConfiguration](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.md") object and specifies a socket timeout of 70 seconds. This
   value specifies long to wait for data to be transferred over an established open connection before closing
   the socket.
2. Creates a [BasicAWSCredentials](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/auth/BasicAWSCredentials.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/auth/BasicAWSCredentials.md") object to identify the AWS account and passes the
   account keys to the constructor. For convenience, and to avoid exposing them as plain text in the code, the
   keys are stored as environment variables.
3. Creates an [AmazonSimpleWorkflowClient](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.md") object to represent the workflow, and passes the
   `BasicAWSCredentials` and `ClientConfiguration` objects to the constructor.
4. Sets the client object's service endpoint URL. Amazon SWF is currently available in all AWS regions.

For convenience, `GreeterWorker` defines two string constants.

- `domain` is the workflow's Amazon SWF domain name, which you created when you set up your Amazon SWF
  account. `HelloWorldWorkflow` assumes that you are running the workflow in the
  "helloWorldWalkthrough" domain.
- `taskListToPoll` is the name of the task lists that Amazon SWF uses to manage communication
  between the workflow and activities workers. You can set the name to any convenient string.
  HelloWorldWorkflow uses "HelloWorldList" for both workflow and activity task lists. Behind the scenes, the
  names end up in different namespaces, so the two task lists are distinct.

`GreeterWorker` uses the string constants and the [AmazonSimpleWorkflowClient](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.md")
object to create worker objects, which manage the interaction between the activities and worker implementations
and Amazon SWF. In particular, the worker objects handle the task of polling the appropriate task list for
tasks.

`GreeterWorker` creates an `ActivityWorker` object and configures it to handle
`GreeterActivitiesImpl` by adding a new class instance. `GreeterWorker` then calls the
`ActivityWorker` object's `start` method, which directs the object to start polling the
specified activities task list.

`GreeterWorker` creates a `WorkflowWorker` object and configures it to handle
`GreeterWorkflowImpl` by adding the class file name, `GreeterWorkflowImpl.class`. It then
calls the `WorkflowWorker` object's `start` method, which directs the object to start
polling the specified workflow task list.

You can run `GreeterWorker` successfully at this point. It registers the workflow and activities
with Amazon SWF and starts the worker objects polling their respective task lists. To verify this, run
`GreeterWorker` and go to the Amazon SWF console and select `helloWorldWalkthrough` from the
list of domains. If you choose **Workflow Types** in the **Navigation** pane, you
should see `GreeterWorkflow.greet`:

![HelloWorldWorkflow workflow type](images/Workflow_Type.png)

If you choose **Activity Types**, the `GreeterActivities` methods are displayed:

![HelloWorldWorkflow activity types](images/Activity_Types.png)

However, if you choose **Workflow Executions**, you will not see any active executions.
Although the workflow and activities workers are polling for tasks, we have not yet started a workflow
execution.

## HelloWorldWorkflow Starter

The final piece of the puzzle is to implement a workflow starter, which is an application that starts the
workflow execution. The execution state is stored by Amazon SWF, so that you can view its history and execution status.
HelloWorldWorkflow implements a workflow starter by modifying the `GreeterMain` class, as
follows:

```
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflow;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient;

public class GreeterMain {

   public static void main(String[] args) throws Exception {
     ClientConfiguration config = new ClientConfiguration().withSocketTimeout(70*1000);

     String swfAccessId = System.getenv("AWS_ACCESS_KEY_ID");
     String swfSecretKey = System.getenv("AWS_SECRET_KEY");
     AWSCredentials awsCredentials = new BasicAWSCredentials(swfAccessId, swfSecretKey);

     AmazonSimpleWorkflow service = new AmazonSimpleWorkflowClient(awsCredentials, config);
     service.setEndpoint("https://swf.us-east-1.amazonaws.com");

     String domain = "helloWorldWalkthrough";

     GreeterWorkflowClientExternalFactory factory = new GreeterWorkflowClientExternalFactoryImpl(service, domain);
     GreeterWorkflowClientExternal greeter = factory.getClient("someID");
     greeter.greet();
   }
}
```

`GreeterMain` creates an `AmazonSimpleWorkflowClient` object by using the same code as
`GreeterWorker`. It then creates a `GreeterWorkflowClientExternal` object, which acts as a
proxy for the workflow in much the same way that the activities client created in
`GreeterWorkflowClientImpl` acts as a proxy for the activity methods. Rather than create a workflow
client object by using `new`, you must:

1. Create an external client factory object and pass the `AmazonSimpleWorkflowClient` object
   and Amazon SWF domain name to the constructor. The client factory object is created by the framework's annotation
   processor, which creates the object name by simply appending "ClientExternalFactoryImpl" to the workflow
   interface name.
2. Create an external client object by calling the factory object's `getClient` method, which
   creates the object name by appending "ClientExternal" to the workflow interface name. You can optionally
   pass `getClient` a string which Amazon SWF will use to identify this instance of the workflow.
   Otherwise, Amazon SWF represents a workflow instance by using a generated GUID.

The client returned from the factory will only create workflows that are named with the string passed into
the [getClient](<../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowClientFactoryExternal.md#getClient(java.lang.String)> "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowClientFactoryExternal.md#getClient(java.lang.String)")
method, (the client returned from the factory already has state in Amazon SWF). To run a workflow with a different id,
you need to go back to the factory and create a new client with the different id specified.

The workflow client exposes a `greet` method that `GreeterMain` calls to begin the
workflow, as `greet()` was the method specified with the `@Execute` annotation.

###### Note

The annotation processor also creates an internal client factory object that is used to create child
workflows. For details, see [Child Workflow Executions](childworkflow.md "childworkflow.md").

Shut down `GreeterWorker` for the moment if it is still running, and run
`GreeterMain`. You should now see someID on the Amazon SWF console's list of active workflow executions:.

![HelloWorldWorkflow workflow executions](images/Active_Execution.png)

If you choose `someID` and choose the **Events** tab, the events are displayed:

![HelloWorldWorkflow initial workflow events](images/Events1.png)

###### Note

If you started `GreeterWorker` earlier, and it is still running, you will see a longer event
list for reasons discussed shortly. Stop `GreeterWorker` and try running `GreaterMain`
again.

The **Events** tab shows only two events:

- `WorkflowExecutionStarted` indicates that the workflow has started executing.
- `DecisionTaskScheduled` indicates that Amazon SWF has queued the first decision task.

The reason that the workflow is blocked at the first decision task is that the workflow is distributed
across two applications, `GreeterMain` and `GreeterWorker`. `GreeterMain`
started the workflow execution, but `GreeterWorker` isn't running, so the workers
aren't polling the lists and executing tasks. You can run either application independently, but you need both for
workflow execution to proceed beyond the first decision task. If you now run `GreeterWorker`, the
workflow and activity workers will start polling and the various tasks will be completed rapidly. If you now check
the `Events` tab, the first batch of events is displayed.

![HelloWorldWorkflow complete workflow events](images/Events2.png)

You can choose individual events to get more information. By the time you've finished looking, the workflow
should have printed "Hello World!" to your console.

After the workflow completes, it no longer appears on the list of active executions. However, if you want
to review it, choose the **Closed** execution status button and then choose **List
Executions**. This displays all the completed workflow instances in the specified domain
(`helloWorldWalkthrough`) that have not exceeded their retention time, which you specified when you
created the domain.

![HelloWorldWorkflow completed workflows](images/Closed_Workflows.png)

Notice that each workflow instance has a unique **Run ID** value. You can use the same
Workflow ID for different workflow instances, but only for one active execution at a time.
