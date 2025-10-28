# Error Handling

###### Topics

- [TryCatchFinally Semantics](#errorhandling.trycatchfinally "#errorhandling.trycatchfinally")
- [Cancellation](#test.cancellation.resources "#test.cancellation.resources")
- [Nested TryCatchFinally](#errorhandling.nested "#errorhandling.nested")
  The `try`/`catch`/`finally` construct in Java makes it simple to handle errors
  and is used ubiquitously. It allows you to associate error handlers to a block of code. Internally, this works by
  stuffing additional metadata about the error handlers on the call stack. When an exception is thrown, the runtime
  looks at the call stack for an associated error handler and invokes it; and if no appropriate error handler is
  found, it propagates the exception up the call chain.

This works well for synchronous code, but handling errors in asynchronous and distributed programs poses
additional challenges. Because an asynchronous call returns immediately, the caller isn't on the call stack when the
asynchronous code executes. This means that unhandled exceptions in the asynchronous code can't be handled by the
caller in the usual way. Typically, exceptions that originate in asynchronous code are handled by passing error
state to a callback that is passed to the asynchronous method. Alternatively, if a `Future<?>` is
being used, it reports an error when you try to access it. This is less than ideal because the code that receives
the exception (the callback or code that uses the `Future<?>`) doesn't have the context of the
original call and may not be able to handle the exception adequately. Furthermore, in a distributed asynchronous
system, with components running concurrently, more than one error may occur simultaneously. These errors could be of
different types and severities and need to be handled appropriately.

Cleaning up resource after an asynchronous call is also difficult. Unlike synchronous code, you can't use
try/catch/finally in the calling code to clean up resources because work initiated in the try block may still be
ongoing when the finally block executes.

The framework provides a mechanism that makes error handling in distributed asynchronous code similar to, and
almost as simple as, Java's try/catch/finally.

```
ImageProcessingActivitiesClient activitiesClient
     = new ImageProcessingActivitiesClientImpl();

public void createThumbnail(final String webPageUrl) {

  new TryCatchFinally() {

    @Override
    protected void doTry() throws Throwable {
      List<String> images = getImageUrls(webPageUrl);
      for (String image: images) {
        Promise<String> localImage
            = activitiesClient.downloadImage(image);
        Promise<String> thumbnailFile
            = activitiesClient.createThumbnail(localImage);
        activitiesClient.uploadImage(thumbnailFile);
      }
    }

    @Override
    protected void doCatch(Throwable e) throws Throwable {

      // Handle exception and rethrow failures
      LoggingActivitiesClient logClient = new LoggingActivitiesClientImpl();
      logClient.reportError(e);
      throw new RuntimeException("Failed to process images", e);
    }

    @Override
    protected void doFinally() throws Throwable {
      activitiesClient.cleanUp();
    }
  };
}

```

The `TryCatchFinally` class and its variants, `TryFinally` and `TryCatch`, work
similar to Java's `try`/`catch`/`finally`. Using it, you can associate exception
handlers to blocks of workflow code that may execute as asynchronous and remote tasks. The `doTry()`
method is logically equivalent to the `try` block. The framework automatically executes the code in
`doTry()`. A list of `Promise` objects can be passed to the constructor of
`TryCatchFinally`. The `doTry` method will be executed when all `Promise` objects
passed in to the constructor become ready. If an exception is raised by code that was asynchronously invoked from
within `doTry()`, any pending work in `doTry()` is canceled and `doCatch()` is
called to handle the exception. For instance, in the listing above, if `downloadImage` throws an
exception, then `createThumbnail` and `uploadImage` will be canceled. Finally,
`doFinally()` is called when all asynchronous work is done (completed, failed, or canceled). It can be
used for resource cleanup. You can also nest these classes to suit your needs.

When an exception is reported in `doCatch()`, the framework provides a complete logical call stack
that includes asynchronous and remote calls. This can be helpful when debugging, especially if you have asynchronous
methods calling other asynchronous methods. For example, an exception from downloadImage will produce an exception
like this:

```

RuntimeException: error downloading image
  at downloadImage(Main.java:35)
  at ---continuation---.(repeated:1)
  at errorHandlingAsync$1.doTry(Main.java:24)
  at ---continuation---.(repeated:1)
…
```

## TryCatchFinally Semantics

The execution of an AWS Flow Framework for Java program can be visualized as a tree of concurrently executing branches. A
call to an asynchronous method, an activity, and `TryCatchFinally` itself creates a new branch in this
tree of execution. For example, the image processing workflow can be viewed as the tree shown in the following
figure.

![Asynchronous execution tree](images/trycatchfinally.png)

An error in one branch of execution will cause the unwinding of that branch, just as an exception causes the
unwinding of the call stack in a Java program. The unwinding keeps moving up the execution branch until either the
error is handled or the root of the tree is reached, in which case the workflow execution is terminated.

The framework reports errors that happen while processing tasks as exceptions. It associates the exception
handlers (`doCatch()` methods) defined in `TryCatchFinally` with all tasks that are created
by the code in the corresponding `doTry()`. If a task fails—for example, due to a timeout or an
unhandled exception—then the appropriate exception will be raised and the corresponding
`doCatch()` will be invoked to handle it. To accomplish this, the framework works in tandem with Amazon SWF
to propagate remote errors and resurrects them as exceptions in the caller's context.

## Cancellation

When an exception occurs in synchronous code, the control jumps directly to the `catch` block,
skipping over any remaining code in the `try` block. For example:

```
try {
    a();
    b();
    c();
}
catch (Exception e) {
    e.printStackTrace();
}

```

In this code, if `b()` throws an exception, then `c()` is never invoked. Compare that to
a workflow:

```
new TryCatch() {

    @Override
    protected void doTry() throws Throwable {
        activityA();
        activityB();
        activityC();
    }

    @Override
    protected void doCatch(Throwable e) throws Throwable {
        e.printStackTrace();
    }
};

```

In this case, calls to `activityA`, `activityB`, and `activityC` all return
successfully and result in the creation of three tasks that will be executed asynchronously. Let's say at a later
time that the task for `activityB` results in an error. This error is recorded in the history by Amazon SWF.
In order to handle this, the framework will first try to cancel all other tasks that originated within the scope
of the same `doTry()`; in this case, `activityA` and `activityC`. When all such
tasks complete (cancel, fail, or successfully complete), the appropriate `doCatch()` method will be
invoked to handle the error.

Unlike the synchronous example, where `c()` was never executed, `activityC` was invoked
and a task was scheduled for execution; hence, the framework will make an attempt to cancel it, but there is no
guarantee that it will be canceled. Cancellation can't be guaranteed because the activity may have already
completed, may ignore the cancellation request, or may fail due to an error. However, the framework does provide
the guarantee that `doCatch()` is called only after all tasks started from the corresponding
`doTry()` have completed. It also guarantees that `doFinally()` is called only after all
tasks started from the `doTry()` and `doCatch()` have completed. If, for instance, the
activities in the above example depend on each other, say `activityB` depends on `activityA`
and `activityC` on `activityB`, then the cancellation of `activityC` will be
immediate because it isn't scheduled in Amazon SWF until `activityB` completes:

```
new TryCatch() {

    @Override
    protected void doTry() throws Throwable {
        Promise<Void> a = activityA();
        Promise<Void> b = activityB(a);
        activityC(b);
    }

    @Override
    protected void doCatch(Throwable e) throws Throwable {
        e.printStackTrace();
    }
};

```

### Activity Heartbeat

The AWS Flow Framework for Java's cooperative cancellation mechanism allows in-flight activity tasks to be canceled
gracefully. When cancellation is triggered, tasks that blocked or are waiting to be assigned to a worker are
automatically canceled. If, however, a task is already assigned to a worker, the framework will request the
activity to cancel. Your activity implementation must explicitly handle such cancellation requests. This is done
by reporting heartbeat of your activity.

Reporting heartbeat allows the activity implementation to report the progress of an ongoing activity task,
which is useful for monitoring, and it lets the activity check for cancellation requests. The
`recordActivityHeartbeat` method will throw a `CancellationException` if a cancellation
has been requested. The activity implementation can catch this exception and act on the cancellation request, or
it can ignore the request by swallowing the exception. In order to honor the cancellation request, the activity
should perform the desired clean up, if any, and then rethrow `CancellationException`. When this
exception is thrown from an activity implementation, the framework records that the activity task has been
completed in canceled state.

The following example shows an activity that downloads and processes images. It heartbeats after processing
each image, and if cancellation is requested, it cleans up and rethrows the exception to acknowledge
cancellation.

```
@Override
public void processImages(List<String> urls) {
    int imageCounter = 0;
    for (String url: urls) {
        imageCounter++;
        Image image = download(url);
        process(image);
        try {
            ActivityExecutionContext context
                 = contextProvider.getActivityExecutionContext();
            context.recordActivityHeartbeat(Integer.toString(imageCounter));
        } catch(CancellationException ex) {
            cleanDownloadFolder();
            throw ex;
        }
    }
}

```

Reporting activity heartbeat isn't required, but it is recommended if your activity is long running or may
be performing expensive operations that you wish to be canceled under error conditions. You should call
`heartbeatActivityTask` periodically from the activity implementation.

If the activity times out, the `ActivityTaskTimedOutException` will be thrown and
`getDetails` on the exception object will return the data passed to the last successful call to
`heartbeatActivityTask` for the corresponding activity task. The workflow implementation may use this
information to determine how much progress was made before the activity task was timed out.

###### Note

It isn't a good practice to heartbeat too frequently because Amazon SWF
may throttle heartbeat requests. See the [Amazon Simple Workflow Service Developer Guide](../developerguide.md "../developerguide.md") for limits placed by Amazon SWF.

### Explicitly Canceling a Task

Besides error conditions, there are other cases where you may explicitly cancel a task. For example, an
activity to process payments using a credit card may need to be canceled if the user cancels the order. The
framework allows you to explicitly cancel tasks created in the scope of a `TryCatchFinally`. In the
following example, the payment task is canceled if a signal is received while the payment was being
processed.

```
public class OrderProcessorImpl implements OrderProcessor {
    private PaymentProcessorClientFactory factory
        = new PaymentProcessorClientFactoryImpl();
    boolean processingPayment = false;
    private TryCatchFinally paymentTask = null;

    @Override
    public void processOrder(int orderId, final float amount) {
        paymentTask = new TryCatchFinally() {

            @Override
            protected void doTry() throws Throwable {
                processingPayment = true;

                PaymentProcessorClient paymentClient = factory.getClient();
                paymentClient.processPayment(amount);
            }

            @Override
            protected void doCatch(Throwable e) throws Throwable {
                if (e instanceof CancellationException) {
                    paymentClient.log("Payment canceled.");
                } else {
                    throw e;
                }
            }

            @Override
            protected void doFinally() throws Throwable {
                processingPayment = false;
            }
        };

    }

    @Override
    public void cancelPayment() {
        if (processingPayment) {
            paymentTask.cancel(null);
        }
    }
}

```

### Receiving Notification of Canceled Tasks

When a task is completed in canceled state, the framework informs the workflow logic by
throwing a `CancellationException`. When an activity completes in canceled state,
a record is made in the history and the framework calls the appropriate `doCatch()` with a
`CancellationException`. As shown in the previous example, when the payment
processing task is canceled, the workflow receives a `CancellationException`.

An unhandled `CancellationException` is propagated up the execution branch
just like any other exception. However, the `doCatch()` method will receive the
`CancellationException` only if there is no other exception in the scope; other
exceptions are prioritized higher than cancellation.

## Nested TryCatchFinally

You may nest `TryCatchFinally`'s to suit your needs. Because each `TryCatchFinally`
creates a new branch in the execution tree, you can create nested scopes. Exceptions in the parent scope will
cause cancellation attempts of all tasks initiated by nested `TryCatchFinally`'s within it. However,
exceptions in a nested `TryCatchFinally` don't automatically propagate to the parent. If you wish to
propagate an exception from a nested `TryCatchFinally` to its containing `TryCatchFinally`,
you should rethrow the exception in `doCatch()`. In other words, only unhandled exceptions are bubbled
up, just like Java's `try`/`catch`. If you cancel a nested `TryCatchFinally` by
calling the cancel method, the nested `TryCatchFinally` will be canceled but the containing
`TryCatchFinally` will not automatically get canceled.

![Nested TryCatchFinally](images/nested.png)

```
new TryCatch() {
    @Override
    protected void doTry() throws Throwable {
        activityA();

        new TryCatch() {
            @Override
            protected void doTry() throws Throwable {
                activityB();
            }

            @Override
            protected void doCatch(Throwable e) throws Throwable {
                reportError(e);
            }
        };

        activityC();
    }

    @Override
    protected void doCatch(Throwable e) throws Throwable {
        reportError(e);
    }
};

```
