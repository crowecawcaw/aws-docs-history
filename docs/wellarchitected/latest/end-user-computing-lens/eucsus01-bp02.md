# EUCSUS01-BP02 Choose the appropriate running mode for your Amazon WorkSpaces

The running mode of a WorkSpace determines its immediate
availability and how you pay for it (monthly or hourly). You can
choose between the following running modes when you create the
WorkSpace:

- **AlwaysOn:** You are paying
  a fixed monthly fee for unlimited usage of your WorkSpaces.
  This mode is best for users who use their WorkSpace full
  time as their primary desktop.
- **AutoStop:** You are paying
  for your WorkSpaces by the hour. With this mode, your
  WorkSpaces stop after a specified period of disconnection,
  and the state of apps and data is saved.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

AutoStop instances are stopped when users disconnect and
therefore help lower the carbon footprint associated with
WorkSpace instances in comparison to AlwaysOn instances. Below
a certain threshold, which depends on the bundle selected, we
recommend AutoStop mode.

Use
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/ "https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/") to set the
[appropriate
running mode](../../../workspaces/latest/adminguide/running-mode.md "../../../workspaces/latest/adminguide/running-mode.md") of a WorkSpaces based on past usage and
improve the sustainability position for WorkSpace
environments.
