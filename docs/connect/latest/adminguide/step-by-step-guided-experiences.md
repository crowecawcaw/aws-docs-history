

# Set up step-by-step guides in Connect Customer
<a name="step-by-step-guided-experiences"></a>

Step-by-step guides walk users through custom user interfaces (UIs) that show them what to do at any given moment in a workflow. You can create single-step or complex workflows like claim submissions or travel rebookings for human agents, or you can create interactive forms and cards for end customer chat conversations.

To learn more about the possible UI configurations, see the interactive [UI component reference](https://d3irlmavjxd3d8.cloudfront.net/?path=/story/overview--page).

**Topics**
+ [How step-by-step guides work](#step-by-step-guided-experiences-overview)
+ [Enable step-by-step guides in Connect Customer](enable-guided-experiences-sg.md)
+ [Use views to customize the user interface for agents, customers, and other user personas in Connect Customer](view-resources-sg.md)
+ [Build views with the UI builder in Connect Customer](no-code-ui-builder.md)
+ [Use step-by-step guides](use-step-by-step-guides.md)

## How step-by-step guides work
<a name="step-by-step-guided-experiences-overview"></a>

You create workflows for agents by creating a flow that uses the [Show view](show-view-block.md) block. The **Show view** block determines which view to show. You can use any flow block to build branching decision trees and to send and receive data from external systems.

When a step-by-step guide runs, Connect Customer creates a separate chat contact in your instance. This contact has its own contact record. If you also use a [Set event flow](set-event-flow.md) block, Connect Customer associates it with the inbound contact. Users don't see this contact.

When mapping a view to a **Show view** block, you can choose from a list of prebuilt views. For details and best practices about creating guides, see [Flow block in Connect Customer: Show view](show-view-block.md).

Use the [Show view](show-view-block.md) block to pass complex JSON objects between views and flows. Use the [AWS Lambda function](invoke-lambda-function-block.md) block to specify JSON objects as input and output parameters. With these blocks, you can pass larger quantities of data with fewer mapping steps.