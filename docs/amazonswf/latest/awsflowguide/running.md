# Running Programs Written with the AWS Flow Framework for Java

###### Topics

- [WorkflowWorker](#running.workflowworker "#running.workflowworker")
- [ActivityWorker](#running.activityworker "#running.activityworker")
- [Worker Threading Model](#running.threadingmodel "#running.threadingmodel")
- [Worker Extensibility](#running.workerextend "#running.workerextend")
  The framework provides _worker classes_ to initialize the
  AWS Flow Framework for Java runtime and communicate with Amazon SWF. In order to implement a workflow or an activity worker,
  you must create and start an instance of a worker class. These worker classes are responsible
  for managing ongoing asynchronous operations, invoking asynchronous methods that become
  unblocked, and communicating with Amazon SWF. They can be configured with workflow and activity
  implementations, the number of threads, the task list to poll, and so on.

The framework comes with two worker classes, one for activities and one for workflows.
In order to run the workflow logic, you use the `WorkflowWorker` class. Similarly for activities
the `ActivityWorker` class is used. These classes automatically poll Amazon SWF for activity tasks and
invoke the appropriate methods in your implementation.

The following example shows how to instantiate a `WorkflowWorker` and start polling for
tasks:

```
AmazonSimpleWorkflow swfClient = new AmazonSimpleWorkflowClient(awsCredentials);
WorkflowWorker worker = new WorkflowWorker(swfClient, "domain1", "tasklist1");
// Add workflow implementation types
worker.addWorkflowImplementationType(MyWorkflowImpl.class);

// Start worker
worker.start();
```

The basic steps to create an instance of the `ActivityWorker` and starting polling for tasks
are as follows:

```
AmazonSimpleWorkflow swfClient
      = new AmazonSimpleWorkflowClient(awsCredentials);
ActivityWorker worker = new ActivityWorker(swfClient,
                                           "domain1",
                                           "tasklist1");
worker.addActivitiesImplementation(new MyActivitiesImpl());

// Start worker
worker.start();
```

When you want to shut down an activity or decider, your application should shut down the
instances of the worker classes being used as well as the Amazon SWF Java client instance. This will
ensure that all resources used by the worker classes are properly released.

```

worker.shutdown();
worker.awaitTermination(1, TimeUnit.MINUTES);

```

In order to start an execution, simply create an instance of the generated external client
and call the `@Execute` method.

```
MyWorkflowClientExternalFactory factory = new MyWorkflowClientExternalFactoryImpl();
MyWorkflowClientExternal client = factory.getClient();
client.start();
```

## WorkflowWorker

As the name suggests, this worker class is intended for use by the workflow implementation.
It is configured with a task list and the workflow implementation type. The worker class runs a
loop to poll for decision tasks in the specified task list. When a decision task is received, it
creates an instance of the workflow implementation and calls the
`@Execute` method to process the task.

## ActivityWorker

For implementing activity workers, you can use the `ActivityWorker` class to conveniently poll a
task list for activity tasks. You configure the activity worker with activity implementation
objects. This worker class runs a loop to poll for activity tasks in the specified task list.
When an activity task is received, it looks up the appropriate implementation that you
provided and calls the activity method to process the task. Unlike the `WorkflowWorker`, which
calls the factory to create a new instance for every decision task, the `ActivityWorker` simply
uses the object you provided.

The `ActivityWorker` class uses the AWS Flow Framework for Java annotations to determine the registration and
execution options.

## Worker Threading Model

In the AWS Flow Framework for Java, the embodiment of an activity or decider is an instance of the worker class.
Your application is responsible for configuring and instantiating the worker object on each
machine and process that should act as a worker. The worker object then automatically receives
tasks from Amazon SWF, dispatches them to your activity or workflow implementation and reports
results to Amazon SWF. It is possible for a single workflow instance to span many workers. When Amazon SWF
has one or more pending activity tasks, it assigns a task to the first available worker, then
the next one, and so on. This makes it possible for tasks belonging to the same workflow
instance to be processed on different workers concurrently.

![Topology of AWS Flow Framework for Java–based applications](images/threading.png)

Moreover, each worker can be configured to process tasks on multiple threads. This means
that the activity tasks of a workflow instance can run concurrently even if there is only one
worker.

Decision tasks behave similarly with the exception that Amazon SWF guarantees that for a given
workflow execution only one decision can be executed at a time. A single workflow execution
will typically require multiple decision tasks; hence, it may end up executing on multiple
processes and threads as well. The decider is configured with the type of the workflow
implementation. When a decision task is received by the decider, it creates an instance
(object) of the workflow implementation. The framework provides an extensible factory pattern for
creating these instances. The default workflow factory creates a new object every time. You
can provide custom factories to override this behavior.

Contrary to deciders, which are configured with workflow implementation types, activity
workers are configured with instances (objects) of the activity implementations. When an
activity task is received by the activity worker, it is dispatched to the appropriate activity
implementation object.

![Threading model of worker classes](images/executor.png)

The workflow worker maintains a single pool of threads and executes the workflow on the same
thread that was used to poll Amazon SWF for the task. Because activities are long running (at least
when compared to the workflow logic), the activity worker class maintains two separate pools
of threads; one for polling Amazon SWF for activity tasks and the other for processing tasks by
executing the activity implementation. This allows you to configure the number of threads to
poll for tasks separate from the number of threads to execute them. For example, you can have a
small number of threads to poll and a large number of threads to execute the tasks. The
activity worker class polls Amazon SWF for a task only when it has a free poll thread as well as a
free thread to process the task.

This threading and instancing behavior implies that:

1. Activity implementations must be stateless. You should not use instance variables to store
   application state in activity objects. You may, however, use fields to store resources such
   as database connections.
2. Activity implementations must be thread safe. Because the same instance may be used to process
   tasks from different threads at the same time, access to shared resources from the
   activity code must be synchronized.
3. Workflow implementation can be stateful, and instance variables may be used to store state.
   Even though a new instance of the workflow implementation is created to process each
   decision task, the framework will ensure that state is properly recreated. However, the workflow
   implementation must be deterministic. See the section [Understanding a Task in AWS Flow Framework for Java](details.md "details.md") for more details.
4. Workflow implementations don't need to be thread safe when using the default factory. The
   default implementation ensures that only one thread uses an instance of the workflow
   implementation at a time.

## Worker Extensibility

The AWS Flow Framework for Java also contains a couple of low-level worker classes that give you
fine-grained control as well as extensibility. Using them, you can completely customize
workflow and activity type registration and set factories for creating implementation
objects. These workers are `GenericWorkflowWorker` and
`GenericActivityWorker`.

The `GenericWorkflowWorker` can be configured with a factory for creating
workflow definition factories. The workflow definition factory is responsible for creating
instances of the workflow implementation and for providing configuration settings such as
registration options. Under normal circumstances, you should use the
`WorkflowWorker` class directly. It will automatically create and configure
implementation of the factories provided in the framework,
`POJOWorkflowDefinitionFactoryFactory` and
`POJOWorkflowDefinitionFactory`. The factory requires that the workflow
implementation class must have a no argument constructor. This constructor is used to create
instances of the workflow object at run time. The factory looks at the annotations you used
on the workflow interface and implementation to create appropriate registration and
execution options.

You may provide your own implementation of the factories by implementing
`WorkflowDefinitionFactory`, `WorkflowDefinitionFactoryFactory`, and `WorkflowDefinition`. The
`WorkflowDefinition` class is used by the worker class to dispatch decision tasks and signals.
By implementing these base classes, you can completely customize the factory and the dispatch
of requests to the workflow implementation. For example, you can use these extensibility
points to provide a custom programming model for writing workflows, for instance, based on
your own annotations or generating it from WSDL instead of the code first approach used by the
framework. In order to use your custom factories, you will have to use the
`GenericWorkflowWorker` class. For more details about these classes, see the AWS SDK for Java documentation.

Similarly, `GenericActivityWorker` allows you to provide a custom activity implementation
factory. By implementing the `ActivityImplementationFactory` and `ActivityImplementation` classes
you can completely control activity instantiation as well as customize registration and
execution options. For more details of these classes, see the AWS SDK for Java documentation.
