# AMS Accelerate patch baseline

A patch baseline defines which patches are approved for installation on your instances.
You can specify approved or rejected patches one by one. You can also create auto-approval
rules to specify that certain types of updates (for example, critical updates) should be
automatically approved. The rejected list overrides both the rules and the approve list.

## Default patch baseline

When you onboard to AMS Accelerate patching, the default patch baselines are overridden by the AMS Accelerate default patch baselines for the following operating systems.

- **Windows**
- **Amazon Linux 1**
- **Amazon Linux 2**
- **CentOS**
- **Suse**
- **Rhel**
- **Ubuntu**

###### Important

Default patch baselines are managed by AMS. Do not edit default patch baselines as your changes may be lost. Instead, create a custom patch baseline.
See [Custom patch baseline with AMS Accelerate](acc-patch-baseline-custom.md "acc-patch-baseline-custom.md")

###### Note

The AMS Accelerate patch baselines defined as **product = \*** mean that all
patches are applied to the instance of all security and classifications.
