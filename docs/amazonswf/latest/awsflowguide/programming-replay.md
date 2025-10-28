# AWS Flow Framework for Java Replay Behavior

This topic discusses examples of replay behavior, using the examples in the [What is the AWS Flow Framework for Java?](welcome.md "welcome.md") section. Both [synchronous](#programming-replay-synchronous "#programming-replay-synchronous") and [asynchronous](#programming-replay-asynchronous "#programming-replay-asynchronous") scenarios are discussed.

## Example 1: Synchronous Replay

For an example of how replay works in a synchronous workflow, modify the [HelloWorldWorkflow](getting-started-example-helloworldworkflow.md "getting-started-example-helloworldworkflow.md") workflow and activity
implementations by adding `println` calls within their respective implementations, as follows:

```
public class GreeterWorkflowImpl implements GreeterWorkflow {
...
   public void greet() {
      System.out.println("greet executes");
      Promise<String> name = operations.getName();
      System.out.println("client.getName returns");
      Promise<String> greeting = operations.getGreeting(name);
      System.out.println("client.greeting returns");
      operations.say(greeting);
      System.out.println("client.say returns");
   }
}
**************
public class GreeterActivitiesImpl implements GreeterActivities {
   public String getName() {
      System.out.println("activity.getName completes");
      return "World";
   }

   public String getGreeting(String name) {
      System.out.println("activity.getGreeting completes");
      return "Hello " + name + "!";
   }

   public void say(String what) {
      System.out.println(what);
   }
}
```

For details about the code, see [HelloWorldWorkflow Application](getting-started-example-helloworldworkflow.md "getting-started-example-helloworldworkflow.md"). The following is an edited version of the output,
with comments that indicate the start of each replay episode.

```
//Episode 1
greet executes
client.getName returns
client.greeting returns
client.say returns

activity.getName completes
//Episode 2
greet executes
client.getName returns
client.greeting returns
client.say returns

activity.getGreeting completes
//Episode 3
greet executes
client.getName returns
client.greeting returns
client.say returns

Hello World! //say completes
//Episode 4
greet executes
client.getName returns
client.greeting returns
client.say returns
```

The replay process for this example works as follows:

- The first episode schedules the `getName` activity task, which has no dependencies.
- The second episode schedules the `getGreeting` activity task, which depends on
  `getName`.
- The third episode schedules the `say` activity task, which depends on
  `getGreeting`.
- The final episode schedules no additional tasks and finds no uncompleted activities, which terminates the
  workflow execution.

###### Note

The three activities client methods are called once for each episode. However, only one of those calls
results in an activity task, so each task is performed only once.

## Example 2: Asynchronous Replay

Similarly to the [synchronous replay example](#programming-replay-synchronous "#programming-replay-synchronous"), you can
modify [HelloWorldWorkflowAsync
Application](getting-started-example-helloworldworkflowasync.md "getting-started-example-helloworldworkflowasync.md") to see how an asynchronous replay works. It
produces the following output:

```
//Episode 1
greet executes
client.name returns
workflow.getGreeting returns
client.say returns

activity.getName completes
//Episode 2
greet executes
client.name returns
workflow.getGreeting returns
client.say returns
workflow.getGreeting completes

Hello World! //say completes
//Episode 3
greet executes
client.name returns
workflow.getGreeting returns
client.say returns
workflow.getGreeting completes
```

HelloWorldAsync uses three replay episodes because there are only two activities. The
`getGreeting` activity was replaced by the _getGreeting_ asynchronous workflow
method, which doesn't initiate a replay episode when it completes.

The first episode doesn't call `getGreeting`, because it depends on the completion of the
_name_ activity. However, after _getName_ completes, replay calls
_getGreeting_ once for each succeeding episode.

## See Also

- [AWS Flow Framework Basic Concepts: Distributed Execution](awsflow-basics-distributed-execution.md "awsflow-basics-distributed-execution.md")
