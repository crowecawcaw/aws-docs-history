# Activity Implementation

Activities are implemented by providing an implementation of the `@Activities`
interface. The AWS Flow Framework for Java uses the activity implementation instances configured on the
worker to process activity tasks at run time. The worker automatically looks up the activity
implementation of the appropriate type.

You can use properties and fields to pass resources to
activity instances, such as database connections. Because the activity implementation object may be accessed from multiple
threads, shared resources must be thread safe.

Note that the activity implementation doesn't take parameters of type `Promise<>` or return objects of that type.
This is because the implementation of the activity should not depend on how it was invoked (synchronously or asynchronously).

The activities interface shown before can be implemented like this:

```
public class MyActivitiesImpl implements MyActivities {

   @Override
   @ManualActivityCompletion
   public int activity1(){
      //implementation
   }

   @Override
   public void activity2(int foo){
     //implementation
   }
}
```

A thread local context is available to the activity implementation that can be used to
retrieve the task object, data converter object being used, etc. The current context can be
accessed through `ActivityExecutionContextProvider.getActivityExecutionContext()`.
For more details, see the AWS SDK for Java documentation for
`ActivityExecutionContext` and the section [Execution Context](executioncontext.md "executioncontext.md").

## Manually Completing Activities

The `@ManualActivityCompletion` annotation in the example above is an optional annotation.
It is allowed only on methods that implement an activity and is used to configure the
activity to not automatically complete when the activity method returns. This could be
useful when you want to complete the activity asynchronously—for example, manually after a
human action has been completed.

By default, the framework considers the activity completed when your activity method returns.
This means that the activity worker reports activity task completion to Amazon SWF and provides
it with the results (if any). However, there are use cases where you don't want the
activity task to be marked completed when the activity method returns. This is especially
useful when you are modeling human tasks. For example, the activity method may send an
email to a person who must complete some work before the activity task is completed. In
such cases, you can annotate the activity method with `@ManualActivityCompletion` annotation
to tell the activity worker that it should not complete the activity automatically. In
order to complete the activity manually, you can either use the
`ManualActivityCompletionClient` provided in the framework or use the
`RespondActivityTaskCompleted` method on the Amazon SWF Java client provided in the Amazon SWF SDK.
For more details, see the AWS SDK for Java documentation.

In order to complete the activity task, you need to provide a task token. The task token
is used by Amazon SWF to uniquely identify tasks. You can access this token from the
`ActivityExecutionContext` in your activity implementation. You must pass this token to the
party that is responsible for completing the task. This token can be retrieved from the
`ActivityExecutionContext` by calling
`ActivityExecutionContextProvider.getActivityExecutionContext().getTaskToken()`.

The `getName` activity of the Hello World example can be implemented to send an email
asking someone to provide a greeting message:

```
@ManualActivityCompletion
@Override
public String getName() throws InterruptedException {
    ActivityExecutionContext executionContext
         = contextProvider.getActivityExecutionContext();
    String taskToken = executionContext.getTaskToken();
    sendEmail("abc@xyz.com",
         "Please provide a name for the greeting message and close task with token: " + taskToken);
    return "This will not be returned to the caller";
}
```

The following code snippet can be used to provide the greeting and close the task by
using the `ManualActivityCompletionClient`. Alternatively, you can also fail the task:

```
public class CompleteActivityTask {

    public void completeGetNameActivity(String taskToken) {

        AmazonSimpleWorkflow swfClient
           = new AmazonSimpleWorkflowClient(...); // use AWS access keys
        ManualActivityCompletionClientFactory manualCompletionClientFactory
           = new ManualActivityCompletionClientFactoryImpl(swfClient);
        ManualActivityCompletionClient manualCompletionClient
           = manualCompletionClientFactory.getClient(taskToken);
        String result = "Hello World!";
        manualCompletionClient.complete(result);
    }

    public void failGetNameActivity(String taskToken, Throwable failure) {
        AmazonSimpleWorkflow swfClient
           = new AmazonSimpleWorkflowClient(...); // use AWS access keys
        ManualActivityCompletionClientFactory manualCompletionClientFactory
           = new ManualActivityCompletionClientFactoryImpl(swfClient);
        ManualActivityCompletionClient manualCompletionClient
           = manualCompletionClientFactory.getClient(taskToken);
        manualCompletionClient.fail(failure);
    }
}
```
