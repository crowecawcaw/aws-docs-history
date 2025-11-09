Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Sequencing gates and actions

In Amazon CodeCatalyst, you can set up a gate to run before or after a workflow action, action
group, or gate. For example, you might set up an `Approval` gate to run
before a `Deploy` action. In this case, the `Deploy` action is
said to _depend on_ the `Approval` gate.

To set up dependencies between gates and actions, configure the gate or action's
**Depends on** property. For instructions, see [Setting up dependencies between
actions](workflows-depends-on-set-up.md "workflows-depends-on-set-up.md").
The referenced instructions refer to workflow _actions_ but apply
equally to gates.

For an example of how to set up the **Depends on** property with a
gate, see [Example: An 'Approval' gate](workflows-approval-example.md "workflows-approval-example.md").

For more information about gates, see [Gating a workflow run](workflows-gates.md "workflows-gates.md").

For more information about workflow actions, see [Configuring workflow actions](workflows-actions.md "workflows-actions.md").
