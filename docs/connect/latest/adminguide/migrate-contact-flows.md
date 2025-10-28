# Migrate flows to an instance, Region, or environment

in Amazon Connect

Amazon Connect lets you efficiently migrate flows to another instance. For example, you might want
to expand into new Regions, or move flows from your development environment to your
production environment.

To migrate a few flows, use the [import/export
feature](contact-flow-import-export.md "contact-flow-import-export.md") in the flow designer.

To migrate hundreds of flows, you need developer skills. You use the following
procedure:

1.  Source instance
    - [ListContactFlow](../APIReference/API_ListContactFlows.md "../APIReference/API_ListContactFlows.md"): Retrieve the Amazon Resource Number (ARN) for
      the flows that you want to migrate.
    - [DescribeContactFlow](../APIReference/API_DescribeContactFlow.md "../APIReference/API_DescribeContactFlow.md"): Get information about each flow that you
      want to migrate.

2.  Destination instance

        * [CreateContactFlow](../APIReference/API_CreateContactFlow.md "../APIReference/API_CreateContactFlow.md"): Create the flows.
        * [UpdateContactFlowContent](../APIReference/API_UpdateContactFlowContent.md "../APIReference/API_UpdateContactFlowContent.md"): Update the flow content.

    You must also build an ARN-to-ARN mapping for queues,
    flows, and prompts between the source and target Amazon Connect instances, and replace every ARN in
    the source flow with the corresponding ARN from the target instance. Otherwise
    UpdateContactFlowContent fails with `InvalidContactFlow` error.

You can update the information in the flows that you migrate. For more information, see
[Flow
language](../APIReference/flow-language.md "../APIReference/flow-language.md") in the _Amazon Connect API Reference Guide_.
