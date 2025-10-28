# HelloWorldWorkflowDistributed Application

With HelloWorldWorkflow and HelloWorldWorkflowAsync, Amazon SWF mediates the interaction between the workflow and
activities implementations, but they run locally as a single process. `GreeterMain` is in a separate
process, but it still runs on the same system.

A key feature of Amazon SWF is that it supports distributed applications. For example, you could run the workflow
worker on an Amazon EC2 instance, the workflow starter on a data center computer, and the activities on a client desktop
computer. You can even run different activities on different systems.

The HelloWorldWorkflowDistributed application extends HelloWorldWorkflowAsync to distribute the application
across two systems and three processes.

- The workflow and workflow starter run as separate processes on one system.
- The activities run on a separate system.
  To implement the application, create a copy of the helloWorld.HelloWorldWorkflowAsync package in your project
  directory and name it helloWorld.HelloWorldWorkflowDistributed. The following sections describe how to modify the
  original HelloWorldWorkflowAsync code to distribute the application across two systems and three processes.

You don't need to change the workflow or activities implementations to run them on separate systems, not even
the version numbers. You also don't need to modify `GreeterMain`. All you need to change is the activities
and workflow host.

With HelloWorldWorkflowAsync, a single application serves as the workflow and activity host. To run the
workflow and activity implementations on separate systems, you must implement separate applications. Delete
GreeterWorker from the project and add two new class files, GreeterWorkflowWorker and GreeterActivitiesWorker.

HelloWorldWorkflowDistributed implements its activities host in GreeterActivitiesWorker, as follows:

```
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflow;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient;
import com.amazonaws.services.simpleworkflow.flow.ActivityWorker;

public class GreeterActivitiesWorker {
   public static void main(String[] args) throws Exception {
      ClientConfiguration config = new ClientConfiguration().withSocketTimeout(70*1000);

      String swfAccessId = System.getenv("AWS_ACCESS_KEY_ID");
      String swfSecretKey = System.getenv("AWS_SECRET_KEY");
      AWSCredentials awsCredentials = new BasicAWSCredentials(swfAccessId, swfSecretKey);

      AmazonSimpleWorkflow service = new AmazonSimpleWorkflowClient(awsCredentials, config);
      service.setEndpoint("https://swf.us-east-1.amazonaws.com");

      String domain = "helloWorldExamples";
      String taskListToPoll = "HelloWorldAsyncList";

      ActivityWorker aw = new ActivityWorker(service, domain, taskListToPoll);
      aw.addActivitiesImplementation(new GreeterActivitiesImpl());
      aw.start();
   }
}
```

HelloWorldWorkflowDistributed implements its workflow host in `GreeterWorkflowWorker`, as
follows:

```
import com.amazonaws.ClientConfiguration;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflow;
import com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient;
import com.amazonaws.services.simpleworkflow.flow.WorkflowWorker;

public class GreeterWorkflowWorker {
   public static void main(String[] args) throws Exception  {
      ClientConfiguration config = new ClientConfiguration().withSocketTimeout(70*1000);

      String swfAccessId = System.getenv("AWS_ACCESS_KEY_ID");
      String swfSecretKey = System.getenv("AWS_SECRET_KEY");
      AWSCredentials awsCredentials = new BasicAWSCredentials(swfAccessId, swfSecretKey);

      AmazonSimpleWorkflow service = new AmazonSimpleWorkflowClient(awsCredentials, config);
      service.setEndpoint("https://swf.us-east-1.amazonaws.com");

      String domain = "helloWorldExamples";
      String taskListToPoll = "HelloWorldAsyncList";

      WorkflowWorker wfw = new WorkflowWorker(service, domain, taskListToPoll);
      wfw.addWorkflowImplementationType(GreeterWorkflowImpl.class);
      wfw.start();
   }
}
```

Note that `GreeterActivitiesWorker` is just `GreeterWorker` without the
`WorkflowWorker` code and `GreeterWorkflowWorker` is just `GreeterWorker` without
the `ActivityWorker` code.

###### To run the workflow:

1. Create a runnable JAR file with `GreeterActivitiesWorker` as the entry point.
2. Copy the JAR file from Step 1 to another system, which can be running any operating system that supports
   Java.
3. Ensure that AWS credentials with access to the same Amazon SWF domain are made available on the other
   system.
4. Run the JAR file.
5. On your development system, use Eclipse to run `GreeterWorkflowWorker` and
   `GreeterMain`.
   Other than the fact that the activities are running on a different system than the workflow worker and workflow
   starter, the workflow works in exactly the same way as HelloWorldAsync. However, because `println` call
   that prints "Hello World!" to the console is in the `say` activity, the output will appear on the system
   that is running the activities worker.
