# HelloWorld Application

To introduce the way Amazon SWF applications are structured, we'll create a Java application that behaves like a
workflow, but that runs locally in a single process. No connection to Amazon Web Services will be needed.

###### Note

The [HelloWorldWorkflow](getting-started-example-helloworldworkflow.md "getting-started-example-helloworldworkflow.md") example builds upon
this one, connecting to Amazon SWF to handle management of the workflow.

A workflow application consists of three basic components:

- An _activities worker_ supports a set of _activities_, each of which is a method that executes independently to perform a
  particular task.
- A _workflow worker_ orchestrates the activities' execution and
  manages data flow. It is a programmatic realization of a _workflow
  topology_, which is basically a flow chart that defines when the various activities execute,
  whether they execute sequentially or concurrently, and so on.
- A _workflow starter_ starts a workflow instance, called an _execution_, and can interact with it during execution.
  HelloWorld is implemented as three classes and two related interfaces, which are described in the following
  sections. Before starting, you should set up your development environment and create a new AWS Java project as
  described in [Setting up the AWS Flow Framework for Java](setup.md "setup.md"). The packages used for the following walkthroughs are
  all named `helloWorld.`XYZ``. To use those names, set the `within` attribute in aop.xml as follows:

```
...
<weaver options="-verbose">
   <include within="helloWorld..*"/>
</weaver>
```

To implement HelloWorld, create a new Java package in your AWS SDK project named
`helloWorld.HelloWorld` and add the following files:

- An interface file named `GreeterActivities.java`
- A class file named `GreeterActivitiesImpl.java`, which implements the activities
  worker.
- An interface file named `GreeterWorkflow.java`.
- A class file named `GreeterWorkflowImpl.java`, which implements the workflow
  worker.
- A class file named `GreeterMain.java`, which implements the workflow
  starter.
  The details are discussed in the following sections and include the complete code for each component, which
  you can add to the appropriate file.

## HelloWorld Activities Implementation

HelloWorld breaks the overall task of printing a `"Hello World!"` greeting to the console into three tasks,
each of which is performed by an _activity method_. The activity methods are
defined in the `GreeterActivities` interface, as follows.

```
public interface GreeterActivities {
   public String getName();
   public String getGreeting(String name);
   public void say(String what);
}
```

HelloWorld has one activity implementation, `GreeterActivitiesImpl`, which provides the
`GreeterActivities` methods as shown:

```
public class GreeterActivitiesImpl implements GreeterActivities {
   @Override
   public String getName() {
      return "World";
   }

   @Override
   public String getGreeting(String name) {
      return "Hello " + name + "!";
   }

   @Override
   public void say(String what) {
      System.out.println(what);
   }
}
```

Activities are independent of each other and can often be used by different workflows. For example, any
workflow can use the `say` activity to print a string to the console. Workflows can also have multiple
activity implementations, each performing a different set of tasks.

## HelloWorld Workflow Worker

To print "Hello World!" to the console, the activity tasks must execute in sequence in the correct order
with the correct data. The HelloWorld workflow worker orchestrates the activities' execution based on a simple
_linear workflow topology_, which is shown in the following figure.

![Linear workflow topology](images/helloworld_topology.png)

The three activities execute in sequence, and the data flows from one activity to the next.

The HelloWorld workflow worker has a single method, the workflow's entry point, which is defined in the
`GreeterWorkflow` interface, as follows:

```
public interface GreeterWorkflow {
   public void greet();
}
```

The `GreeterWorkflowImpl` class implements this interface, as follows:

```
public class GreeterWorkflowImpl implements GreeterWorkflow{
   private GreeterActivities operations = new GreeterActivitiesImpl();

   public void greet() {
      String name = operations.getName();
      String greeting = operations.getGreeting(name);
      operations.say(greeting);
   }
}
```

The `greet` method implements HelloWorld topology by creating an instance of
`GreeterActivitiesImpl`, calling each activity method in the correct order, and passing the
appropriate data to each method.

## HelloWorld Workflow Starter

A _workflow starter_ is an application that starts a workflow execution,
and might also communicate with the workflow while it is executing. The `GreeterMain` class implements
the HelloWorld workflow starter, as follows:

```
public class GreeterMain {
   public static void main(String[] args) {
      GreeterWorkflow greeter = new GreeterWorkflowImpl();
      greeter.greet();
   }
}
```

`GreeterMain` creates an instance of `GreeterWorkflowImpl` and calls
`greet` to run the workflow worker. Run `GreeterMain` as a Java application and you should
see "Hello World!" in the console output.
