# Creating safety rules for routing control

When you work with several routing controls at the same time, you might decide that you want safeguards in place
to avoid unintended consequences. For example, you might want to prevent inadvertently turning off all the routing controls for an
application, which would result in a fail-open scenario. Or you might want to implement a master
on-off switch to disable a set of routing controls, perhaps to prevent automation from rerouting traffic. To
establish safeguards like these for routing control in ARC, you create _safety rules_.

You configure safety rules for routing control with a combination of routing controls, rules, and other options that you specify. Each
safety rule is associated with a single control panel, but a control panel can have more than one safety rule.
When you create safety rules, keep in mind that safety rule names must be unique within each control panel.

###### Topics

- [Types of safety rules](#routing-control.about-safety-rule "#routing-control.about-safety-rule")
- [Creating a safety rule on the
  console](routing-control.md "routing-control.md")
- [Editing or deleting a safety rule on the
  console](routing-control.md "routing-control.md")
- [Overriding safety rules
  to reroute traffic](routing-control.md "routing-control.md")

## Types of safety rules

There are two types of safety rules, _assertion rules_ and _gating rules_,
which you can use to safeguard failover in different ways.

**Assertion rule**
With an assertion rule, when you change one or a set of routing control states, ARC enforces that the criteria that you set when you configured the
rule is met, or else the routing control states aren't changed.

An example of when this is useful is to prevent a fail-open scenario, like a scenario where you stop traffic from going to one cell but do not start
traffic flowing to another cell. To avoid this, an assertion rule makes sure that at least one routing control in a set of routing controls in a
control panel is `On` at any given time. This ensures that traffic flows to at least one Region or Availability Zone for an
application.

To see an example AWS CLI command that creates an assertion rule to enforce this criteria,
see _Create safety rules_ in
[Examples of using ARC routing control API operations with the AWS CLI](getting-started-cli-routing.md "getting-started-cli-routing.md").

For detailed information about the assertion rule API operation properties, see
[AssertionRule](../../../recovery-cluster/latest/api/safetyrule.md#safetyrule-model-assertionrule "../../../recovery-cluster/latest/api/safetyrule.md#safetyrule-model-assertionrule")
in the Routing Control API Reference Guide for Amazon Application Recovery Controller.

**Gating rule**
With a gating rule, you can enforce an overall on-off switch over a set of routing controls
so that whether those routing control states can be changed is enforced based on a set of criteria that you
specify in the rule. The simplest criteria is whether a single routing control that you specify as the switch is
set to `ON` or `OFF`.

To implement this, you create a _gating routing control_, to use as the overall switch,
and _target routing controls_, to control traffic flow to different Regions or Availability Zones.
Then, to prevent manual or automated state updates to the target routing controls that
you've configured for the gating rule, you set the gating routing control state to `Off`. To allow updates, you
set it to `On`.

To see an example AWS CLI command that creates a gating rule that implements this kind of overall
switch, see _Create safety rules_ in
[Examples of using ARC routing control API operations with the AWS CLI](getting-started-cli-routing.md "getting-started-cli-routing.md").

For detailed information about the gating rule API operation properties,
see [GatingRule](../../../recovery-cluster/latest/api/safetyrule.md#safetyrule-model-gatingrule "../../../recovery-cluster/latest/api/safetyrule.md#safetyrule-model-gatingrule")
in the Routing Control API Reference Guide for Amazon Application Recovery Controller.
