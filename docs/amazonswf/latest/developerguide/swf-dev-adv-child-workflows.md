# Child workflows in Amazon SWF

Complicated workflows can be broken into smaller, more manageable, and potentially reusable components by
using child workflows. A child workflow is a workflow execution that is initiated by another (parent) workflow
execution. To initiate a child workflow, the decider for the parent workflow uses the
`StartChildWorkflowExecution` decision. Input data specified with this decision is made available to
the child workflow through its history.

The attributes for the `StartChildWorkflowExecution` decision also specify the _child
policy_, that is, how Amazon SWF should handle the situation in which the parent workflow execution
terminates before the child workflow execution. There are three possible values:

- TERMINATE: Amazon SWF will terminate the child executions.
- REQUEST_CANCEL: Amazon SWF will attempt to cancel the child execution by placing a
  `WorkflowExecutionCancelRequested` event in the child's workflow execution history.
- ABANDON: Amazon SWF will take no action; the child executions will continue to run.
  After the child workflow execution starts, it runs like a regular execution. When it completes, Amazon SWF
  records the completion, along with its results, in the parent workflow execution's workflow history. Examples of
  child workflows include the following:

- Credit card processing child workflow used by workflows in different websites
- Email child workflow that verifies the customer email address, checks the opt-out list, sends the
  email, and verifies that it didn't bounce or fail.
- Database storage and retrieval child workflow that combines connection, setup, transaction, and
  verification.
- Source code compilation child workflow that combines building, packaging, and verification.
  In the e-commerce example, you might want to make the Charge Credit Card activity a child workflow. To do
  this, you could register a new Verify Customer workflow, register the Verify Customer Address and Check Fraud DB
  activities, and define coordination logic for the tasks. Then, a decider in the Customer Order workflow can
  initiate a Verify Customer child workflow by scheduling the `StartChildWorkflowExecution` decision that
  specifies this workflow type.

The following figure shows a customer order workflow that includes a new Verify Customer child workflow,
which checks the customer address, checks the fraud database, and charges the credit card.

![Diagram of child workflow](images/child-workflow.png)
Multiple workflows could create child workflow executions using the same workflow type. For example, the
Verify Customer child workflow could also be used in other parts of an organization. The events for a child
workflow are contained in its own workflow history and are not included in the parent's workflow history.

Because child workflows are simply workflow executions that are initiated by a decider, they could also be
started as normal stand-alone workflow executions.
