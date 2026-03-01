# Library functions available for Java canary

The `executeStep` function is used to modularize the canary code and execute it in steps. In CloudWatch Synthetics, a Synthetics step is a way to break down your canary script into a series of clearly defined actions, allowing you to monitor different parts of your application journey separately.
For each step, CloudWatch Synthetics does the following:

- A report, including a summary of step execution details like the duration of a step, _pass_ or _fail_ status, and so on, is created for each canary run. When you choose a run in the CloudWatch Synthetics console, you can view execution details of each step
  on the **Step** tab.
- _SuccessPercent_ and _Duration_ CloudWatch metrics are emitted for each step, enabling users to monitor availability and latency of each step.

**Usage**

```
synthetics.executeStep(stepName,()->{
    try {
        //step code to be executed
        return null;
    } catch (Exception e) {
        throw e;
    }
}).get();
```

**Parameters**

    + *stepName*, String (required) – A descriptive name of the Synthetics step
    + *function to execute*, Callable<T> (required) – Represents the tasks to be executed
    + *stepOptions*, `com.amazonaws.synthetics.StepOptions (optional)` – StepOptions object that can be used to configure the step execution.




    *stepConfiguration*, `com.amazonaws.synthetics.StepConfiguration`(required as part of the stepOptions)

**Returns**

The value returned is _CompletableFuture<T>_.

###### Note

Synthetics only supports sequential steps. Make sure to call the `.get()` method as shown in the example to ensure that the step completes before proceeding to the subsequent step.
