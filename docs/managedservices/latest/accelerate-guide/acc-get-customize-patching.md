# Customize patching in Accelerate

Patching ensures that your software is up-to-date and meets your compliance policies.

**When to patch**: Patching occurs during a
_maintenance window_. You can schedule maintenance windows so that patches are only applied during preset times.

**What to patch**: You have to associate the Amazon EC2 instances you want to patch with a maintenance window.
To associate the instances with a maintenance window, the Amazon EC2 instances must be tagged, and the maintenance window should have those tags as a target.

**Which patches to install**: Using patch baselines, you set rules to auto-approve certain types of patches, such
as operating system or high-severity patches. You can also specify exceptions to your rules, for example, lists of patches that are always approved or rejected.

- For general patching recommendations, see [Patching recommendations](acc-patching.md#acc-patching-recos "acc-patching.md#acc-patching-recos").
- To create custom maintenance windows, see [Create a patch maintenance window in AMS](acc-p-maint-window.md "acc-p-maint-window.md").
- To create custom patch baselines, see [Custom patch baseline with AMS Accelerate](acc-patch-baseline-custom.md "acc-patch-baseline-custom.md").
- To route patch alerts to the resource owner, see [Understand patch notifications and patch failures in AMS Accelerate](acc-patch-mon-remediate.md "acc-patch-mon-remediate.md").
