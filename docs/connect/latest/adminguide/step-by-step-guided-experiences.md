# Step-by-step Guides to set up your

Amazon Connect agent workspace

In the Amazon Connect agent workspace, you can create workflows that walk agents through custom
UI pages that suggest what to do at a given moment during a customer interaction. You
can create workflows that give your agents screen pops and single page forms, or you can
create detailed step-by-step guides that give your agents clear instructions on how to
handle a particular use case. You can also customize the UI and the data that agents
see.

To learn more about the possible UI configurations, see our interactive [documentation](https://d3irlmavjxd3d8.cloudfront.net/?path=/story/overview--page "https://d3irlmavjxd3d8.cloudfront.net/?path=/story/overview--page").

To learn more about the pricing of step-by-step guides, on the Amazon Connect [pricing page](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/"), scroll to the
**Agent productivity** section, and then choose the
**Guides** tab.

## Overview

You create workflows for agents by a creating a flow that uses the [Show view](show-view-block.md "show-view-block.md"). The
**Show view** block determines what View to render in the
agent's UI. All pre-existing flow blocks can be used to create branching decision
trees and send and receive data from external systems.

When using a flow with the **Show view** block to run the
step-by-step guide, a separate chat contact is created in your Amazon Connect instance. This
contact creates a unique CTR. If you also use a [Set event flow](set-event-flow.md "set-event-flow.md") block, the contact is associated with the
inbound contact. Neither agents nor customers are aware of this underlying contact
while interacting with the agent workspace or the Amazon Connect widget.

When mapping a view to a **Show view** block, you will be able to
select from a list of pre-built Views. For details and best practices about creating
Guides, see [Show view](show-view-block.md "show-view-block.md").

## Complex JSON Object

support

Use the [Show view](show-view-block.md "show-view-block.md")
block to pass complex JSON objects between Amazon Connect agent workspaces and
flows. Use the [AWS Lambda
function](invoke-lambda-function-block.md "invoke-lambda-function-block.md") block specify JSON objects
as input and output parameters. These blocks allow you to pass larger quantities of
data with fewer mapping steps.
