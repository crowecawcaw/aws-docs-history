# Default queue transfer flow in Amazon Connect: "Now

transferring"

This flow manages what the agent experiences when they transfer a customer to another
queue.

It starts with a **Check hours of operation** block to check the
hours of operation for the current queue. The **In hours** option
branches to the **Check staffing** block to determine whether agents
are available, staffed, or online.

If it returns **True** (agents are available), the flow goes to the
**Transfer to queue** block. If it returns
**False** (no agents are available), the flow plays a prompt and
disconnects the call.

For instructions about how to override and change a default flow, see [Change a default flow in your Amazon Connect
contact center](change-default-contact-flow.md "change-default-contact-flow.md").

###### Tip

Wondering if a default flow has been changed? Use [flow version control](flow-version-control.md "flow-version-control.md") to view the original
version of the flow.
