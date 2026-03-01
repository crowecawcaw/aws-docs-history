# AWS Flow Framework Basic Concepts: Task Lists and Task Execution

Amazon SWF manages workflow and activity tasks by posting them to named lists. Amazon SWF maintains
at least two task lists, one for workflow workers and one for activity workers.

###### Note

You can specify as many task lists as you need, with different workers assigned to each
list. There is no limit to the number of task lists. You typically specify a worker's task
list in the worker host application when you create the worker object.

The following excerpt from the `HelloWorldWorkflow` host application creates a
new activity worker and assigns it to the `HelloWorldList` activities task
list.

```
public class GreeterWorker  {
    public static void main(String[] args) throws Exception {
    ...
    String domain = " helloWorldExamples";
    String taskListToPoll = "HelloWorldList";

    ActivityWorker aw = new ActivityWorker(service, domain, taskListToPoll);
    aw.addActivitiesImplementation(new GreeterActivitiesImpl());
    aw.start();
    ...
  }
}
```

By default, Amazon SWF schedules the worker's tasks on the `HelloWorldList` list. Then
the worker polls that list for tasks. You can assign any name to a task list. You can even use
the same name for both workflow and activity lists. Internally, Amazon SWF puts workflow and activity
task list names in different namespaces, so the two lists will be distinct.

If you don't specify a task list, the AWS Flow Framework specifies a default list when the worker
registers the type with Amazon SWF. For more information, see [Workflow and Activity Type Registration](features.md "features.md").

Sometimes it's useful to have a specific worker or group of workers perform certain tasks.
For example, an image processing workflow might use one activity to download an image and
another activity to process the image. It's more efficient to perform both tasks on the same
system, and avoid the overhead of transferring large files over the network.

To support such scenarios, you can explicitly specify a task list when you call an activity
client method by using an overload that includes a `schedulingOptions` parameter. You
specify the task list by passing the method an appropriately configured `ActivitySchedulingOptions` object.

For example, suppose that the `say` activity of the
`HelloWorldWorkflow` application is hosted by an activity worker different from
`getName` and `getGreeting`. The following example shows how to ensure
that `say` uses the same task list as `getName` and
`getGreeting`, even if they were originally assigned to different lists.

```
public class GreeterWorkflowImpl implements GreeterWorkflow {
  private GreeterActivitiesClient operations1 = new GreeterActivitiesClientImpl1(); //getGreeting and getName
  private GreeterActivitiesClient operations2 = new GreeterActivitiesClientImpl2(); //say
  @Override
  public void greet() {
    Promise<String> name = operations1.getName();
    Promise<String> greeting = operations1.getGreeting(name);
    runSay(greeting);
  }
  @Asynchronous
  private void runSay(Promise<String> greeting){
    String taskList = operations1.getSchedulingOptions().getTaskList();
    ActivitySchedulingOptions schedulingOptions = new ActivitySchedulingOptions();
    schedulingOptions.setTaskList(taskList);
    operations2.say(greeting, schedulingOptions);
  }
}
```

The asynchronous `runSay` method gets the `getGreeting` task list from
its client object. Then it creates and configures an `ActivitySchedulingOptions`
object that ensures that `say` polls the same task list as
`getGreeting`.

###### Note

When you pass a `schedulingOptions` parameter to an activity client method, it
overrides the original task list only for that activity execution. If you call the activities
client method again without specifying a task list, Amazon SWF assigns the task to the original
list, and the activity worker will poll that list.
