

# Workflow execution closure in Amazon SWF
<a name="swf-dev-workflow-exec-closure"></a>

Once you start a workflow execution, it is *open*. An open workflow execution could be closed as completed, canceled, failed, or timed out. It could also be continued as a new execution, or it could be terminated. A workflow execution could be closed by the decider, by the person administering the workflow, or by Amazon SWF.

If the decider determines that the activities of the workflow have finished, it should close the workflow execution as completed by using the `[RespondDecisionTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html)` action and pass the `[CompleteWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CompleteWorkflowExecutionDecisionAttributes.html)` decision.

Alternatively, a decider might close the workflow execution as canceled or failed. In order to cancel the execution, the decider should use the `RespondDecisionTaskCompleted` action and pass the `[CancelWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CancelWorkflowExecutionDecisionAttributes.html)` decision.

A decider should fail the workflow execution if it enters a state outside the realm of normal completion. In order to fail the execution, the decider should use the `RespondDecisionTaskCompleted` action and pass the `[FailWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_FailWorkflowExecutionDecisionAttributes.html)` decision.

Amazon SWF monitors workflow executions to ensure that they don't exceed any user-specified timeout settings. If a workflow execution times out, Amazon SWF automatically closes it. For more information about timeout values, see the [Amazon SWF Timeout Types](swf-timeout-types.md) section.

A decider might also close the execution and logically continue it as a new execution using the `RespondDecisionTaskCompleted` action and passing the `[ContinueAsNewWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ContinueAsNewWorkflowExecutionDecisionAttributes.html)` decision. This is a useful strategy for long-running workflow executions for which the history may grow too large over time.

Finally, you could terminate workflow executions directly from the Amazon SWF console or programmatically by using the `[TerminateWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TerminateWorkflowExecution.html)` API. Termination forces closure of the workflow execution. Cancellation is preferred over termination, because your deciders can manage closure of the workflow execution.

Amazon SWF terminates a workflow execution if the execution exceeds certain service-defined limits. Amazon SWF terminates a child workflow if the parent workflow has terminated and the applicable child policy indicates that the child workflow should also be terminated.