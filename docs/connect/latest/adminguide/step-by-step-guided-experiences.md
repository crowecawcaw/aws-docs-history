

# Step-by-step Guides to set up your Connect Customer agent workspace
<a name="step-by-step-guided-experiences"></a>

In the Connect Customer agent workspace, you can create workflows that walk agents through custom UI pages that suggest what to do at a given moment during a customer interaction. You can create workflows that give your agents screen pops and single page forms, or you can create detailed step-by-step guides that give your agents clear instructions on how to handle a particular use case. You can also customize the UI and the data that agents see. 

To learn more about the possible UI configurations, see our interactive [documentation](https://d3irlmavjxd3d8.cloudfront.net/?path=/story/overview--page).

To learn more about the pricing of step-by-step guides, on the Connect Customer [pricing page](https://aws.amazon.com/connect/pricing/), scroll to the **Agent productivity** section, and then choose the **Guides** tab. 

**Topics**
+ [Overview](#step-by-step-guided-experiences-overview)
+ [Complex JSON Object support](#step-by-step-guided-experiences-complex-json)
+ [Enable step-by-step guides in Connect Customer](enable-guided-experiences-sg.md)
+ [Views: UI templates to customize the Connect Customer agent workspace](view-resources-sg.md)
+ [Use the UI builder in Connect Customer for resources in step-by-step guides](no-code-ui-builder.md)
+ [Invoke a guide at the start of a contact in Connect Customer](how-to-invoke-a-flow-sg.md)
+ [Deploy step-by-step guides in Connect Customer chats](step-by-step-guides-chat.md)
+ [Display contact context in the agent workspace when a contact begins in Connect Customer](display-contact-attributes-sg.md)
+ [Enable Connect Customer contact center agents to enter disposition codes when a contact ends](disposition-codes-sg.md)
+ [Prevent PII from appearing in a contact record transcript using Connect Customer conversational analytics](step-by-step-guides-pii-redaction.md)
+ [Integrate Views with Connect Resources](integrate-views-with-connect-resources.md)
+ [Use Step by Step Guides in Workspace for Managers](use-guides-in-manager-workspace.md)

## Overview
<a name="step-by-step-guided-experiences-overview"></a>

You create workflows for agents by a creating a flow that uses the [Show view](show-view-block.md). The **Show view** block determines what View to render in the agent's UI. All pre-existing flow blocks can be used to create branching decision trees and send and receive data from external systems.

When using a flow with the **Show view** block to run the step-by-step guide, a separate chat contact is created in your Connect Customer instance. This contact creates a unique CTR. If you also use a [Set event flow](set-event-flow.md) block, the contact is associated with the inbound contact. Neither agents nor customers are aware of this underlying contact while interacting with the agent workspace or the Connect Customer widget.

When mapping a view to a **Show view** block, you will be able to select from a list of pre-built Views. For details and best practices about creating Guides, see [Show view](show-view-block.md).

## Complex JSON Object support
<a name="step-by-step-guided-experiences-complex-json"></a>

Use the [Show view](show-view-block.md) block to pass complex JSON objects between the agent workspace and flows. Use the [AWS Lambda function](invoke-lambda-function-block.md) block specify JSON objects as input and output parameters. With these blocks, you can pass larger quantities of data with fewer mapping steps.