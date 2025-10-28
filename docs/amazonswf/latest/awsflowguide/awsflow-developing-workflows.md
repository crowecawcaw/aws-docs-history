# Implementing Workflow Applications with the AWS Flow Framework

The typical steps involved in developing a workflow with the AWS Flow Framework are:

1. **Define activity and workflow contracts**. Analyze your application's
   requirements, then determine the required activities and the workflow topology. The
   _activities_ handle the required processing tasks, while the _workflow
   topology_ defines the workflow's basic structure and business logic.

For example, a media processing application might need to download a file, process it, and then upload the
processed file to an Amazon Simple Storage Service (S3) bucket. This can broken down into four activity
tasks:

    1. download the file from a server
    2. process the file (for instance, by transcoding it to a different media format)
    3. upload the file to the S3 bucket
    4. perform cleanup by deleting the local files

This workflow would have an entry point method and would implement a simple linear topology that runs
the activities in sequence, much like the [HelloWorldWorkflow Application](getting-started-example-helloworldworkflow.md "getting-started-example-helloworldworkflow.md"). 2. **Implement activity and workflow interfaces**. The workflow and activity
contracts are defined by Java _interfaces_, making their calling conventions predictable by
SWF, and providing you flexibility when implementing your workflow logic and activity tasks. The various parts of
your program can act as consumers of each others' data, yet don't need to be aware of much of the
implementation details of any of the other parts.

For example, you can define a `FileProcessingWorkflow` interface and provide
different workflow implementations for video encoding, compression, thumbnails, and so on. Each of those
workflows can have different control flows and can call different activity methods; your workflow starter
doesn't need to know. By using interfaces, it is also simple to test your workflows by using mock
implementations that can be replaced later with working code. 3. **Generate activity and workflow clients**. The AWS Flow Framework eliminates the
need for you to implement the details of managing asynchronous execution, sending HTTP requests, marshaling
data, and so forth. Instead, the workflow starter executes a workflow instance by calling a method on the
workflow client, and the workflow implementation executes activities by calling methods on the activities
client. The framework handles the details of these interactions in the background.

If you are using Eclipse and you have configured your project, like in [Setting up the AWS Flow Framework for Java](setup.md "setup.md"), the AWS Flow Framework annotation processor uses the interface definitions to automatically
generate workflow and activities clients that expose the same set of methods as the corresponding
interface. 4. **Implement activity and workflow host applications**. Your workflow and
activity implementations must be embedded in host applications that poll Amazon SWF for tasks, marshal any data, and
call the appropriate implementation methods. AWS Flow Framework for Java includes [WorkflowWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/WorkflowWorker.md") and [ActivityWorker](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/ActivityWorker.md") classes that make implementing host applications
straightforward and easy to do. 5. **Test your workflow**. AWS Flow Framework for Java provides JUnit integration that you
can use to test your workflows inline and locally. 6. **Deploy the workers**. You can deploy your workers as
appropriate—for example, you can deploy them to Amazon EC2 instances or to computers in
your data center. Once deployed and started, the workers start polling Amazon SWF for tasks and
handle them as required. 7. **Start executions**. An application starts a workflow
instance by using the workflow client to call the workflow's entry point. You can also
start workflows by using the Amazon SWF console. Regardless of how you start a workflow
instance, you can use Amazon SWF console to monitor running workflow instance and examine the
workflow history for running, completed, and failed instances.
The [AWS SDK for Java](http://aws.amazon.com/sdkforjava/ "http://aws.amazon.com/sdkforjava/") includes a set
of AWS Flow Framework for Java samples that you can browse and run by following the instructions in the
readme.html file in the root directory. There are also a set of recipes —simple
applications — that show how to handle a variety of specific programming issue, which
are available from [AWS Flow Framework Recipes](https://aws.amazon.com/code/2535278400103493 "https://aws.amazon.com/code/2535278400103493").
