# Continuous Workflows

In some use cases, you may need a workflow that executes forever or runs for a long
duration, for example, a workflow that monitors the health of a server fleet.

###### Note

Because Amazon SWF keeps the entire history of a workflow execution, the history will keep
growing over time. The framework retrieves this history from Amazon SWF when it performs a
replay, and this will become expensive if the history size is too large. In such long running
or continuous workflows, you should periodically close the current execution and start a new
one to continue processing.

This is a logical continuation of the workflow execution. The generated self client can be
used for this purpose. In your workflow implementation, simply call the `@Execute`
method on the self client. Once the current execution completes, the framework will start a new
execution using the same workflow Id.

You can also continue the execution by calling the `continueAsNewOnCompletion`
method on the `GenericWorkflowClient` that you can retrieve from the current
`DecisionContext`. For example, the following workflow implementation sets a timer
to fire after a day and calls its own entry point to start a new execution.

```
public class ContinueAsNewWorkflowImpl implements ContinueAsNewWorkflow {

    private DecisionContextProvider contextProvider
         = new DecisionContextProviderImpl();

    private ContinueAsNewWorkflowSelfClient selfClient
         = new ContinueAsNewWorkflowSelfClientImpl();

    private WorkflowClock clock
         = contextProvider.getDecisionContext().getWorkflowClock();

    @Override
    public void startWorkflow() {
        Promise<Void> timer = clock.createTimer(86400);
        continueAsNew(timer);
    }

    @Asynchronous
    void continueAsNew(Promise<Void> timer) {
        selfClient.startWorkflow();
    }
}
```

When a workflow recursively calls itself, the framework will close the current workflow when
all pending tasks have completed and start a new workflow execution. Note that as long as there
are pending tasks, the current workflow execution will not close. The new execution will not
automatically inherit any history or data from the original execution; if you want to carry over
some state to the new execution, then you must pass it explicitly as input.
