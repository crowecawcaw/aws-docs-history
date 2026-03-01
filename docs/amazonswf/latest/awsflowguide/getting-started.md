# Getting Started with the AWS Flow Framework for Java

This section introduces the AWS Flow Framework by walking you through a series of simple example applications that
introduce the basic programming model and API. The example applications are based on the standard Hello World
application that is used to introduce C and related programming languages. Here is a typical Java implementation of
Hello World:

```
public class HelloWorld {
   public static void main(String[] args) {
      System.out.println("Hello World!");
   }
}
```

The following is a brief description of the example applications. They include complete source code so you can
implement and run the applications yourself. Before starting, you should first configure your development environment
and create an AWS Flow Framework for Java project, like in [Setting up the AWS Flow Framework for Java](setup.md "setup.md").

- [HelloWorld Application](getting-started-example-helloworld.md "getting-started-example-helloworld.md") introduces workflow applications by implementing
  Hello World as a standard Java application, but structuring it like a workflow application.
- [HelloWorldWorkflow Application](getting-started-example-helloworldworkflow.md "getting-started-example-helloworldworkflow.md") uses the
  AWS Flow Framework for Java to convert HelloWorld into an Amazon SWF workflow.
- [HelloWorldWorkflowAsync Application](getting-started-example-helloworldworkflowasync.md "getting-started-example-helloworldworkflowasync.md")
  modifies `HelloWorldWorkflow` to use an _asynchronous workflow_
  method.
- [HelloWorldWorkflowDistributed Application](getting-started-example-helloworldworkflowdistributed.md "getting-started-example-helloworldworkflowdistributed.md") modifies `HelloWorldWorkflowAsync` so that
  the workflow and activity workers can run on separate systems.
- [HelloWorldWorkflowParallel Application](getting-started-example-helloworldworkflowparallel.md "getting-started-example-helloworldworkflowparallel.md")
  modifies `HelloWorldWorkflow` to run two activities in parallel.
