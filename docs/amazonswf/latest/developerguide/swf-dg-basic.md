# Basic workflow concepts in Amazon SWF

###### Note

The concepts in this chapter provide an overview of the Amazon Simple Workflow Service and describe its major features. If you are looking for examples, see [Working with Amazon SWF APIs](swf-dg-using-swf-api.md "swf-dg-using-swf-api.md").

Using the Amazon Simple Workflow Service (Amazon SWF), you can implement distributed, asynchronous applications as
_workflows_. Workflows coordinate and manage the execution of activities that can be run
asynchronously across multiple computing devices and that can feature both sequential and parallel processing.

When designing a workflow, you analyze your application to identify its component _tasks_.
In Amazon SWF, these tasks are represented by _activities_. The order in which activities are performed
is determined by the workflow's coordination logic.

###### Example workflow for an e-commerce application

The following figure shows an e-commerce order-processing workflow involving both people and automated processes:

![Illustrative e-commerce example workflow](images/swf-overview-workflow.png)
The e-commerce application workflow starts when a customer places an order, and includes four _tasks_:

1. Verify the order.
2. If the order is valid, charge the customer.
3. If the payment is made, ship the order.
4. If the order is shipped, save the order details.
   The tasks in this workflow are _sequential_: an order must be verified before a credit card
   can be charged; a credit card must be charged successfully before an order can be shipped; and an order must be
   shipped before it can be recorded. Even so, because Amazon SWF supports distributed processes, these tasks can be carried
   out in different locations. If the tasks are programmatic in nature, they can also be written in different
   programming languages or using different tools.

In addition to sequential processing of tasks, Amazon SWF also supports workflows with parallel processing of tasks.
Parallel tasks are performed at the same time, and may be carried out independently by different applications or
human workers. Your workflow makes decisions about how to proceed once one or more of the parallel tasks have been
completed.

###### Additional concepts

- [Creating a workflow](swf-dg-create-workflow.md "swf-dg-create-workflow.md")
- [Running workflows](swf-dev-run-workflows.md "swf-dev-run-workflows.md")
- [Workflow history](swf-dev-about-workflow-history.md "swf-dev-about-workflow-history.md")
- [Object identifiers](swf-dev-obj-ident.md "swf-dev-obj-ident.md")
- [Domains](swf-dev-domains.md "swf-dev-domains.md")
- [Actors](swf-dev-actors.md "swf-dev-actors.md")
- [Tasks](swf-dev-tasks.md "swf-dev-tasks.md")
- [Task lists](swf-dev-task-lists.md "swf-dev-task-lists.md")
- [Workflow execution closure](swf-dev-workflow-exec-closure.md "swf-dev-workflow-exec-closure.md")
- [Workflow execution life cycle](swf-dev-workflow-exec-lifecycle.md "swf-dev-workflow-exec-lifecycle.md")
- [Polling for tasks](swf-dev-comm-proto.md "swf-dev-comm-proto.md")
