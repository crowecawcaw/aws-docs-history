# Retry Failed Activities

Activities sometimes fail for ephemeral reasons, such as a temporary loss of connectivity. At another time,
the activity might succeed, so the appropriate way to handle activity failure is often to retry the activity,
perhaps multiple times.

There are a variety of strategies for retrying activities; the best one depends on the details of your
workflow. The strategies fall into three basic categories:

- The retry-until-success strategy simply keeps retrying the activity until it completes.
- The exponential retry strategy increases the time interval between retry attempts exponentially until the
  activity completes or the process reaches a specified stopping point, such as a maximum number of
  attempts.
- The custom retry strategy decides whether or how to retry the activity after each failed attempt.
  The following sections describe how to implement these strategies. The example workflow workers all use a
  single activity, `unreliableActivity`, which randomly does one of following:

- Completes immediately
- Fails intentionally by exceeding the timeout value
- Fails intentionally by throwing `IllegalStateException`

## Retry-Until-Success Strategy

The simplest retry strategy is to keep retrying the activity each time it fails until it eventually
succeeds. The basic pattern is:

1. Implement a nested `TryCatch` or `TryCatchFinally` class in
   your workflow's entry point method.
2. Execute the activity in `doTry`
3. If the activity fails, the framework calls `doCatch`, which runs the
   entry point method again.
4. Repeat Steps 2 - 3 until the activity completes successfully.

The following workflow implements the retry-until-success strategy. The workflow interface is implemented in
`RetryActivityRecipeWorkflow` and has one method, `runUnreliableActivityTillSuccess`,
which is the workflow's entry point. The workflow worker is implemented in
`RetryActivityRecipeWorkflowImpl`, as follows:

```
public class RetryActivityRecipeWorkflowImpl
    implements RetryActivityRecipeWorkflow {

    @Override
    public void runUnreliableActivityTillSuccess() {
        final Settable<Boolean> retryActivity = new Settable<Boolean>();

        new TryCatch() {
            @Override
            protected void doTry() throws Throwable {
                Promise<Void> activityRanSuccessfully
                    = client.unreliableActivity();
                setRetryActivityToFalse(activityRanSuccessfully, retryActivity);
            }

            @Override
            protected void doCatch(Throwable e) throws Throwable {
                retryActivity.set(true);
            }
        };
        restartRunUnreliableActivityTillSuccess(retryActivity);
    }

    @Asynchronous
    private void setRetryActivityToFalse(
            Promise<Void> activityRanSuccessfully,
            @NoWait Settable<Boolean> retryActivity) {
        retryActivity.set(false);
    }

    @Asynchronous
    private void restartRunUnreliableActivityTillSuccess(
            Settable<Boolean> retryActivity) {
        if (retryActivity.get()) {
            runUnreliableActivityTillSuccess();
        }
    }
}

```

The workflow works as follows:

1.  `runUnreliableActivityTillSuccess` creates a `Settable<Boolean>` object named
    `retryActivity` which is used to indicate whether the activity failed and should be retried.
    `Settable<T>` is derived from `Promise<T>` and works much the same way, but
    you set a `Settable<T>` object's value manually.
2.  `runUnreliableActivityTillSuccess` implements an anonymous nested `TryCatch` class
    to handle any exceptions that are thrown by the `unreliableActivity` activity. For more discussion
    of how to handle exceptions thrown by asynchronous code, see [Error Handling](errorhandling.md "errorhandling.md").
3.  `doTry` executes the `unreliableActivity` activity, which returns a
    `Promise<Void>` object named `activityRanSuccessfully`.
4.  `doTry` calls the asynchronous `setRetryActivityToFalse` method, which has two
    parameters:

        * `activityRanSuccessfully` takes the `Promise<Void>` object returned by the
         `unreliableActivity` activity.
        * `retryActivity` takes the `retryActivity` object.

    If `unreliableActivity` completes, `activityRanSuccessfully` becomes ready and
    `setRetryActivityToFalse` sets `retryActivity` to false. Otherwise,
    `activityRanSuccessfully` never becomes ready and `setRetryActivityToFalse` doesn't
    execute.

5.  If `unreliableActivity` throws an exception, the framework calls `doCatch` and
    passes it the exception object. `doCatch` sets `retryActivity` to true.
6.  `runUnreliableActivityTillSuccess` calls the asynchronous
    `restartRunUnreliableActivityTillSuccess` method and passes it the `retryActivity`
    object. Because `retryActivity` is a `Promise<T>` type,
    `restartRunUnreliableActivityTillSuccess` defers execution until `retryActivity` is
    ready, which occurs after `TryCatch` completes.
7.  When `retryActivity` is ready, `restartRunUnreliableActivityTillSuccess` extracts
    the value.
    - If the value is `false`, the retry succeeded.
      `restartRunUnreliableActivityTillSuccess` doesn'thing and the retry sequence
      terminates.
    - If the value is true, the retry failed. `restartRunUnreliableActivityTillSuccess` calls
      `runUnreliableActivityTillSuccess` to execute the activity again.

8.  Steps 1 - 7 repeat until `unreliableActivity` completes.

###### Note

`doCatch` doesn't handle the exception; it simply sets the `retryActivity` object
to true to indicate that the activity failed. The retry is handled by the asynchronous
`restartRunUnreliableActivityTillSuccess` method, which defers execution until
`TryCatch` completes. The reason for this approach is that, if you retry an activity in
`doCatch`, you can't cancel it. Retrying the activity in
`restartRunUnreliableActivityTillSuccess` allows you to execute cancellable activities.

## Exponential Retry Strategy

With the exponential retry strategy, the framework executes a failed activity again after a specified period
of time, N seconds. If that attempt fails the framework executes the activity again after 2N seconds, and then
4N seconds and so on. Because the wait time can get quite large, you typically stop the retry attempts at some
point rather than continuing indefinitely.

The framework provides three ways to implement an exponential retry strategy:

- The `@ExponentialRetry` annotation is the simplest approach, but you must set the retry
  configuration options at compile time.
- The `RetryDecorator` class allows you to set retry configuration at run time and change it as
  needed.
- The `AsyncRetryingExecutor` class allows you to set retry configuration at run time and
  change it as needed. In addition, the framework calls a user-implemented `AsyncRunnable.run`
  method to run each retry attempt.

All approaches support the following configuration options, where time values are in seconds:

- The initial retry wait time.
- The back-off coefficient, which is used to compute the retry intervals, as follows:

```
retryInterval = initialRetryIntervalSeconds * Math.pow(backoffCoefficient, numberOfTries - 2)
```

The default value is 2.0.

- The maximum number of retry attempts. The default value is unlimited.
- The maximum retry interval. The default value is unlimited.
- The expiration time. Retry attempts stop when the total duration of the process exceeds this value. The
  default value is unlimited.
- The exceptions that will trigger the retry process. By default, every exception triggers the retry
  process.
- The exceptions that will not trigger a retry attempt. By default, no exceptions are excluded.

The following sections describe the various ways that you can implement an exponential retry strategy.

### Exponential Retry with @ExponentialRetry

The simplest way to implement an exponential retry strategy for an activity is to apply an
`@ExponentialRetry` annotation to the activity in the interface definition. If the activity fails,
the framework handles the retry process automatically, based on the specified option values. The basic pattern
is:

1. Apply `@ExponentialRetry` to the appropriate activities and specify the retry
   configuration.
2. If an annotated activity fails, the framework automatically retries the activity according to the
   configuration specified by the annotation's arguments.

The `ExponentialRetryAnnotationWorkflow` workflow worker implements the exponential retry
strategy by using an `@ExponentialRetry` annotation. It uses an `unreliableActivity`
activity whose interface definition is implemented in `ExponentialRetryAnnotationActivities`, as
follows:

```
@Activities(version = "1.0")
@ActivityRegistrationOptions(
    defaultTaskScheduleToStartTimeoutSeconds = 30,
    defaultTaskStartToCloseTimeoutSeconds = 30)
public interface ExponentialRetryAnnotationActivities {
    @ExponentialRetry(
        initialRetryIntervalSeconds = 5,
        maximumAttempts = 5,
        exceptionsToRetry = IllegalStateException.class)
    public void unreliableActivity();
}

```

The `@ExponentialRetry` options specify the following strategy:

- Retry only if the activity throws `IllegalStateException`.
- Use an initial wait time of 5 seconds.
- No more than 5 retry attempts.

The workflow interface is implemented in `RetryWorkflow` and has one method,
`process`, which is the workflow's entry point. The workflow worker is implemented in
`ExponentialRetryAnnotationWorkflowImpl`, as follows:

```
public class ExponentialRetryAnnotationWorkflowImpl implements RetryWorkflow {
    public void process() {
        handleUnreliableActivity();
    }

    public void handleUnreliableActivity() {
        client.unreliableActivity();
    }
}

```

The workflow works as follows:

1. `process` runs the synchronous `handleUnreliableActivity` method.
2. `handleUnreliableActivity` executes the `unreliableActivity` activity.

If the activity fails by throwing `IllegalStateException`, the framework automatically runs the
retry strategy specified in `ExponentialRetryAnnotationActivities`.

### Exponential Retry with the RetryDecorator Class

`@ExponentialRetry` is simple to use. However, the configuration is static and set at compile
time, so the framework uses the same retry strategy every time the activity fails. You can implement a more
flexible exponential retry strategy by using the `RetryDecorator` class, which allows you to
specify the configuration at run time and change it as needed. The basic pattern is:

1. Create and configure an `ExponentialRetryPolicy` object that specifies the retry
   configuration.
2. Create a `RetryDecorator` object and pass the `ExponentialRetryPolicy` object
   from Step 1 to the constructor.
3. Apply the decorator object to the activity by passing the activity client's class name to the
   `RetryDecorator` object's decorate method.
4. Execute the activity.

If the activity fails, the framework retries the activity according to the
`ExponentialRetryPolicy` object's configuration. You can change the retry configuration as needed
by modifying this object.

###### Note

The `@ExponentialRetry` annotation and the `RetryDecorator` class are mutually
exclusive. You can't use `RetryDecorator` to dynamically override a retry policy specified by an
`@ExponentialRetry` annotation.

The following workflow implementation shows how to use the `RetryDecorator` class to implement
an exponential retry strategy. It uses an `unreliableActivity` activity that doesn't have an
`@ExponentialRetry` annotation. The workflow interface is implemented in `RetryWorkflow`
and has one method, `process`, which is the workflow's entry point. The workflow worker is
implemented in `DecoratorRetryWorkflowImpl`, as follows:

```
public class DecoratorRetryWorkflowImpl implements RetryWorkflow {
   ...
  public void process() {
      long initialRetryIntervalSeconds = 5;
      int maximumAttempts = 5;
      ExponentialRetryPolicy retryPolicy = new ExponentialRetryPolicy(
              initialRetryIntervalSeconds).withMaximumAttempts(maximumAttempts);

      Decorator retryDecorator = new RetryDecorator(retryPolicy);
      client = retryDecorator.decorate(RetryActivitiesClient.class, client);
      handleUnreliableActivity();
  }

  public void handleUnreliableActivity() {
      client.unreliableActivity();
  }
}

```

The workflow works as follows:

1. `process` creates and configures an `ExponentialRetryPolicy` object by:
   - Passing the initial retry interval to the constructor.
   - Calling the object's `withMaximumAttempts` method to set the maximum number of attempts
     to 5. `ExponentialRetryPolicy` exposes other `with` objects that you can use
     to specify other configuration options.

2. `process` creates a `RetryDecorator` object named `retryDecorator`
   and passes the `ExponentialRetryPolicy` object from Step 1 to the constructor.
3. `process` applies the decorator to the activity by calling the
   `retryDecorator.decorate` method and passing it the activity client's class name.
4. `handleUnreliableActivity` executes the activity.

If the activity fails, the framework retries it according to the configuration specified in Step

1.

###### Note

Several of the `ExponentialRetryPolicy` class's `with` methods have a
corresponding `set` method that you can call to modify the corresponding configuration option
at any time: `setBackoffCoefficient`, `setMaximumAttempts`,
`setMaximumRetryIntervalSeconds`, and `setMaximumRetryExpirationIntervalSeconds`.

### Exponential Retry with the AsyncRetryingExecutor Class

The `RetryDecorator` class provides more flexibility in configuring the retry process than
`@ExponentialRetry`, but the framework still runs the retry attempts automatically, based on the
`ExponentialRetryPolicy` object's current configuration. A more flexible approach is to use the
`AsyncRetryingExecutor` class. In addition to allowing you to configure the retry process at run
time, the framework calls a user-implemented `AsyncRunnable.run` method to run each retry attempt
instead of simply executing the activity.

The basic pattern is:

1. Create and configure an `ExponentialRetryPolicy` object to specify the retry
   configuration.
2. Create an `AsyncRetryingExecutor` object, and pass it the
   `ExponentialRetryPolicy` object and an instance of the workflow clock.
3. Implement an anonymous nested `TryCatch` or `TryCatchFinally` class.
4. Implement an anonymous `AsyncRunnable` class and override the `run` method to
   implement custom code for running the activity.
5. Override `doTry` to call the `AsyncRetryingExecutor` object's
   `execute` method and pass it the `AsyncRunnable` class from Step 4. The
   `AsyncRetryingExecutor` object calls `AsyncRunnable.run` to run the activity.
6. If the activity fails, the `AsyncRetryingExecutor` object calls the
   `AsyncRunnable.run` method again, according to the retry policy specified in Step 1.

The following workflow shows how to use the `AsyncRetryingExecutor` class to implement an
exponential retry strategy. It uses the same `unreliableActivity` activity as the
`DecoratorRetryWorkflow` workflow discussed earlier. The workflow interface is implemented in
`RetryWorkflow` and has one method, `process`, which is the workflow's entry point. The
workflow worker is implemented in `AsyncExecutorRetryWorkflowImpl`, as follows:

```
public class AsyncExecutorRetryWorkflowImpl implements RetryWorkflow {
  private final RetryActivitiesClient client = new RetryActivitiesClientImpl();
  private final DecisionContextProvider contextProvider = new DecisionContextProviderImpl();
  private final WorkflowClock clock = contextProvider.getDecisionContext().getWorkflowClock();

  public void process() {
      long initialRetryIntervalSeconds = 5;
      int maximumAttempts = 5;
      handleUnreliableActivity(initialRetryIntervalSeconds, maximumAttempts);
  }
  public void handleUnreliableActivity(long initialRetryIntervalSeconds, int maximumAttempts) {

      ExponentialRetryPolicy retryPolicy = new ExponentialRetryPolicy(initialRetryIntervalSeconds).withMaximumAttempts(maximumAttempts);
      final AsyncExecutor executor = new AsyncRetryingExecutor(retryPolicy, clock);

      new TryCatch() {
          @Override
          protected void doTry() throws Throwable {
              executor.execute(new AsyncRunnable() {
                  @Override
                  public void run() throws Throwable {
                      client.unreliableActivity();
                  }
              });
          }
          @Override
          protected void doCatch(Throwable e) throws Throwable {
          }
      };
  }
}

```

The workflow works as follows:

1. `process` calls the `handleUnreliableActivity` method and passes it the
   configuration settings.
2. `handleUnreliableActivity` uses the configuration settings from Step 1 to create an
   `ExponentialRetryPolicy` object, `retryPolicy`.
3. `handleUnreliableActivity` creates an `AsyncRetryExecutor` object,
   `executor`, and passes the `ExponentialRetryPolicy` object from Step 2 and an instance
   of the workflow clock to the constructor
4. `handleUnreliableActivity` implements an anonymous nested `TryCatch` class and
   overrides the `doTry` and `doCatch` methods to run the retry attempts and handle any
   exceptions.
5. `doTry` creates an anonymous `AsyncRunnable` class and overrides the
   `run` method to implement custom code to execute `unreliableActivity`. For simplicity,
   `run` just executes the activity, but you can implement more sophisticated approaches as
   appropriate.
6. `doTry` calls `executor.execute` and passes it the `AsyncRunnable`
   object. `execute` calls the `AsyncRunnable` object's `run` method to run
   the activity.
7. If the activity fails, executor calls `run` again, according to the `retryPolicy`
   object configuration.

For more discussion of how to use the `TryCatch` class to handle errors, see [AWS Flow Framework for Java Exceptions](errorhandling.md "errorhandling.md").

## Custom Retry Strategy

The most flexible approach to retrying failed activities is a custom strategy, which recursively calls an
asynchronous method that runs the retry attempt, much like the retry-until-success strategy. However, instead of
simply running the activity again, you implement custom logic that decides whether and how to run each successive
retry attempt. The basic pattern is:

1. Create a `Settable<T>` status object, which is used to indicate whether the activity
   failed.
2. Implement a nested `TryCatch` or `TryCatchFinally` class.
3. `doTry` executes the activity.
4. If the activity fails, `doCatch` sets the status object to indicate that the activity
   failed.
5. Call an asynchronous failure handling method and pass it the status object. The method defers execution
   until `TryCatch` or `TryCatchFinally` completes.
6. The failure handling method decides whether to retry the activity, and if so, when.

The following workflow shows how to implement a custom retry strategy. It uses the same
`unreliableActivity` activity as the `DecoratorRetryWorkflow` and
`AsyncExecutorRetryWorkflow` workflows. The workflow interface is implemented in
`RetryWorkflow` and has one method, `process`, which is the workflow's entry point. The
workflow worker is implemented in `CustomLogicRetryWorkflowImpl`, as follows:

```
public class CustomLogicRetryWorkflowImpl implements RetryWorkflow {
  ...
  public void process() {
      callActivityWithRetry();
  }
  @Asynchronous
  public void callActivityWithRetry() {
      final Settable<Throwable> failure = new Settable<Throwable>();
      new TryCatchFinally() {
          protected void doTry() throws Throwable {
              client.unreliableActivity();
          }
          protected void doCatch(Throwable e) {
              failure.set(e);
          }
          protected void doFinally() throws Throwable {
              if (!failure.isReady()) {
                  failure.set(null);
              }
          }
      };
      retryOnFailure(failure);
  }
  @Asynchronous
  private void retryOnFailure(Promise<Throwable> failureP) {
      Throwable failure = failureP.get();
      if (failure != null && shouldRetry(failure)) {
          callActivityWithRetry();
      }
  }
  protected Boolean shouldRetry(Throwable e) {
      //custom logic to decide to retry the activity or not
      return true;
  }
}

```

The workflow works as follows:

1. `process` calls the asynchronous `callActivityWithRetry` method.
2. `callActivityWithRetry` creates a `Settable<Throwable>` object named failure
   which is used to indicate whether the activity has failed. `Settable<T>` is derived from
   `Promise<T>` and works much the same way, but you set a `Settable<T>`
   object's value manually.
3. `callActivityWithRetry` implements an anonymous nested `TryCatchFinally` class to
   handle any exceptions that are thrown by `unreliableActivity`. For more discussion of how to
   handle exceptions thrown by asynchronous code, see [AWS Flow Framework for Java Exceptions](errorhandling.md "errorhandling.md").
4. `doTry` executes `unreliableActivity`.
5. If `unreliableActivity` throws an exception, the framework calls `doCatch` and
   passes it the exception object. `doCatch` sets `failure` to the exception object,
   which indicates that the activity failed and puts the object in a ready state.
6. `doFinally` checks whether `failure` is ready, which will be true only if
   `failure` was set by `doCatch`.
   - If `failure` is ready, `doFinally` does nothing.
   - If `failure` isn't ready, the activity completed and
     `doFinally` sets failure to `null`.

7. `callActivityWithRetry` calls the asynchronous `retryOnFailure` method and passes
   it failure. Because failure is a `Settable<T>` type, `callActivityWithRetry`
   defers execution until failure is ready, which occurs after `TryCatchFinally` completes.
8. `retryOnFailure` gets the value from failure.
   - If failure is set to null, the retry attempt was successful. `retryOnFailure` does
     nothing, which terminates the retry process.
   - If failure is set to an exception object and `shouldRetry` returns true,
     `retryOnFailure` calls `callActivityWithRetry` to retry the activity.

   `shouldRetry` implements custom logic to decide whether to retry a failed activity. For
   simplicity, `shouldRetry` always returns `true` and `retryOnFailure`
   executes the activity immediately, but you can implement more sophisticated logic as needed.

9. Steps 2–8 repeat until `unreliableActivity` completes or `shouldRetry` decides
   to stop the process.

###### Note

`doCatch` doesn't handle the retry process; it simply sets failure to indicate that the
activity failed. The retry process is handled by the asynchronous `retryOnFailure` method, which
defers execution until `TryCatch` completes. The reason for this approach is that, if you retry an
activity in `doCatch`, you can't cancel it. Retrying the activity in `retryOnFailure`
allows you to execute cancellable activities.
