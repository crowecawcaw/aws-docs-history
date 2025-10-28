# Understanding a Task in AWS Flow Framework for Java

###### Topics

- [Task](#details.task "#details.task")
- [Order of Execution](#details.order "#details.order")
- [Workflow Execution](#details.workflow "#details.workflow")
- [Nondeterminism](#details.non "#details.non")

## Task

The underlying primitive that the AWS Flow Framework for Java uses to manage the execution of
asynchronous code is the `Task` class. An object of type `Task`
represents work that has to be performed asynchronously. When you call an asynchronous method,
the framework creates a `Task` to execute the code in that method and puts it in a
list for execution at a later time. Similarly, when you invoke an `Activity`, a
`Task` is created for it. The method call returns after this, usually returning a
`Promise<T>` as the future result of the call.

The `Task` class is public and may be used directly. For example, we can
rewrite the Hello World example to use a `Task` instead of an asynchronous
method.

```
@Override
public void startHelloWorld(){
       final Promise<String> greeting = client.getName();
        new Task(greeting) {
        @Override
        protected void doExecute() throws Throwable {
        	client.printGreeting("Hello " + greeting.get() +"!");
        }
    };
}

```

The framework calls the `doExecute()` method when all the `Promise`s
passed to the constructor of the `Task` become ready. For more details about the
`Task` class, see the AWS SDK for Java documentation.

The framework also includes a class called `Functor` which represents a
`Task` that is also a `Promise<T>`. The `Functor` object
becomes ready when the `Task` completes. In the following example, a
`Functor` is created to get the greeting message:

```

Promise<String> greeting = new Functor<String>() {
    @Override
    protected Promise<String> doExecute() throws Throwable {
        return client.getGreeting();
    }
};
client.printGreeting(greeting);
```

## Order of Execution

Tasks become eligible for execution only when all `Promise<T>` typed
parameters, passed to the corresponding asynchronous method or activity, become ready. A
`Task` that is ready for execution is logically moved to a ready queue. In other
words, it is scheduled for execution. The worker class executes the task by invoking the code
that you wrote in the body of the asynchronous method, or by scheduling an activity task in
Amazon Simple Workflow Service (AWS) in case of an activity method.

As tasks execute and produce results, they cause other tasks to become ready and the
execution of the program keeps moving forward. The way the framework executes tasks is important
to understand the order in which your asynchronous code executes. Code that appears
sequentially in your program may not actually execute in that order.

```
Promise<String> name = getUserName();
printHelloName(name);
printHelloWorld();
System.out.println("Hello, Amazon!");

@Asynchronous
private Promise<String> getUserName(){
	return Promise.asPromise("Bob");
}
@Asynchronous
private void printHelloName(Promise<String> name){
	System.out.println("Hello, " + name.get() + "!");
}
@Asynchronous
private void printHelloWorld(){
	System.out.println("Hello, World!");
}
```

The code in the listing above will print the following:

```
Hello, Amazon!
Hello, World!
Hello, Bob

```

This may not be what you expected but can be easily explained by thinking through how the
tasks for the asynchronous methods were executed:

1. The call to `getUserName` creates a `Task`. Let's call it
   `Task1`. Because `getUserName` doesn't take any parameters,
   `Task1` is immediately put in the ready queue.
2. Next, the call to `printHelloName` creates a `Task` that needs
   to wait for the result of `getUserName`. Let's call it `Task2`.
   Because the requisite value isn't ready yet, `Task2` is put in the wait
   list.
3. Then a task for `printHelloWorld` is created and added to the ready queue.
   Let's call it `Task3`.
4. The `println` statement then prints "Hello, Amazon!" to the console.
5. At this point, `Task1` and `Task3` are in the ready queue and
   `Task2` is in the wait list.
6. The worker executes `Task1`, and its result makes `Task2` ready.
   `Task2` gets added to ready queue behind `Task3`.
7. `Task3` and `Task2` are then executed in that order.

The execution of activities follows the same pattern. When you call a method on the
activity client, it creates a `Task` that, upon execution, schedules an activity in
Amazon SWF.

The framework relies on features like code generation and dynamic proxies to inject the logic
for converting method calls to activity invocations and asynchronous tasks in your program.

## Workflow Execution

The execution of the workflow implementation is also managed by the worker class. When you
call a method on the workflow client, it calls Amazon SWF to create a workflow instance. The tasks
in Amazon SWF should not be confused with the tasks in the framework. A task in Amazon SWF is either an
activity task or a decision task. The execution of activity tasks is simple. The activity
worker class receives activity tasks from Amazon SWF, invokes the appropriate activity method in
your implementation, and returns the result to Amazon SWF.

The execution of decision tasks is more involved. The workflow worker receives decision
tasks from Amazon SWF. A decision task is effectively a request asking the workflow logic what to
do next. The first decision task is generated for a workflow instance when it is started
through the workflow client. Upon receiving this decision task, the framework starts executing
the code in the workflow method annotated with `@Execute`. This method executes the
coordination logic that schedules activities. When the state of the workflow instance
changes—for example, when an activity completes—further decision tasks get
scheduled. At this point, the workflow logic can decide to take an action based on the result
of the activity; for example, it may decide to schedule another activity.

The framework hides all these details from the developer by seamlessly translating
decision tasks to the workflow logic. From a developer's point of view, the code looks just
like a regular program. Under the covers, the framework maps it to calls to Amazon SWF and decision
tasks using the history maintained by Amazon SWF. When a decision task arrives, the framework
replays the program execution plugging in the results of the activities completed so far.
Asynchronous methods and activities that were waiting for these results get unblocked, and the
program execution moves forward.

The execution of the example image processing workflow and the corresponding history is
shown in the following table.

| Execution of thumbnail workflow                                                                                                                                                                           | Workflow program execution                                                                                                                                                                                                             | History maintained by Amazon SWF                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Initial execution                                                                                                                                                                                         |                                                                                                                                                                                                                                        | 1. Dispatch loop 2. _getImageUrls_ 3. downloadImage 4. createThumbnail (task in wait queue) 5. uploadImage (task in wait queue) 6. <next iteration of the loop>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 1. Workflow instance started, id="1" 2. downloadImage scheduled                                                                                                                                           |                                                                                                                                                                                                                                        | Replay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1. Dispatch loop 2. _getImageUrls_ 3. _downloadImage image_ path="foo" 4. createThumbnail 5. uploadImage (task in wait queue) 6. <next iteration of the loop>                                             | 1. Workflow instance started, id="1" 2. downloadImage scheduled 3. downloadImage completed, return="foo" 4. createThumbnail scheduled                                                                                                  |
| Replay                                                                                                                                                                                                    |                                                                                                                                                                                                                                        | 1. Dispatch loop 2. _getImageUrls_ 3. _downloadImage image_ path="foo" 4. _createThumbnail_ thumbnail path="bar" 5. uploadImage 6. <next iteration of the loop>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 1. Workflow instance started, id="1" 2. downloadImage scheduled 3. downloadImage completed, return="foo" 4. createThumbnail scheduled 5. createThumbnail completed, return="bar" 6. uploadImage scheduled |                                                                                                                                                                                                                                        | Replay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1. Dispatch loop 2. _getImageUrls_ 3. _downloadImage image_ path="foo" 4. _createThumbnail_ thumbnail path="bar" 5. _uploadImage_ 6. <next iteration of the loop>                                         | 1. Workflow instance started, id="1" 2. downloadImage scheduled 3. downloadImage completed, return="foo" 4. createThumbnail scheduled 5. createThumbnail completed, return="bar" 6. uploadImage scheduled 7. uploadImage completed ... | When a call to `processImage` is made, the framework creates a new workflow instance in Amazon SWF. This is a durable record of the workflow instance being started. The program executes until the call to the `downloadImage` activity, which asks Amazon SWF to schedule an activity. The workflow executes further and creates tasks for subsequent activities, but they can't be executed until the `downloadImage` activity completes; hence, this episode of replay ends. Amazon SWF dispatches the task for `downloadImage` activity for execution, and once it is completed, a record is made in the history along with the result. The workflow is now ready to move forward and a decision task is generated by Amazon SWF. The framework receives the decision task and replays the workflow plugging in the result of the downloaded image as recorded in the history. This unblocks the task for `createThumbnail`, and the execution of the program continues farther by scheduling the `createThumbnail` activity task in Amazon SWF. The same process repeats for `uploadImage`. The execution of the program continues this way until the workflow has processed all images and there are no pending tasks. Because no execution state is stored locally, each decision task may be potentially executed on a different machine. This allows you to easily write programs that are fault tolerant and easily scalable. ## Nondeterminism Because the framework relies on replay, it is important that the orchestration code (all workflow code with the exception of activity implementations) be deterministic. For example, the control flow in your program should not depend on a random number or the current time. Because these things will change between invocations, the replay may not follow the same path through the orchestration logic. This will lead to unexpected results or errors. The framework provides a `WorkflowClock` that you can use to get the current time in a deterministic way. See the section on [Execution Context](executioncontext.md "executioncontext.md") for more details. ###### Note Incorrect Spring wiring of workflow implementation objects can also lead to nondeterminism. Workflow implementation beans as well as beans that they depend on must be in the workflow scope (`WorkflowScope`). For example, wiring a workflow implementation bean to a bean that keeps state and is in the global context will result in unexpected behavior. See the [Spring Integration](test.md#test.spring "test.md#test.spring") section for more details. |
