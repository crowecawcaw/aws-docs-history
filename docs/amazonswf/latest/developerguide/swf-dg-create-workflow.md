# Creating a workflow in Amazon SWF

Creating a basic sequential workflow involves the following stages.

- Modeling a workflow, registering its type, and registering its activity types
- Developing and launching activity workers that perform activity tasks
- Developing and launching deciders that use the workflow history to determine what to do next
- Developing and launching workflow starters, that is, applications that start workflow executions

## Modeling Your Workflow and Its Activities

To use Amazon SWF, model the logical steps in your application as activities. An activity represents a single
logical step or task in your workflow. For example, authorizing a credit card is an activity that involves
providing a credit card number and other information, and receiving an approval code or a message that the card
was declined.

In addition to defining activities, you also need to define the coordination logic that handles decision
points. For example, the coordination logic might schedule a different follow-up activity depending on whether the
credit card was approved or declined.

The following figure shows an example of a sequential customer order workflow with four activities (Verify
Order, Charge Credit Card, Ship Order, and Record Completion).

![Customer Order Workflow](images/swf-overview-workflow.png)
