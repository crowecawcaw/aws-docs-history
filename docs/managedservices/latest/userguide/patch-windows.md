# Patch windows

Instances in a specific patch group are patched during one or more patch
windows. Patch windows run on a schedule defined as a cron or rate expression,
and have a configurable duration intended to keep patching-related disruption
within a chosen time interval. AMS recommends creating multiple patch windows
that collectively cover all of your instances, to match your organization’s
specific patching routines, and to use the default maintenance window as a
fallback. Patch windows are created with the RFC change type Deployment |
Patching | SSM patch window | Create (ct-0el2j07llrxs7). All instances that are
not part of a patch window are patched during the default maintenance window
created during onboarding.

Normally, a patch window does not need to be updated to include new instances.
Typically, this is done by modifying instance tags. For example, consider the
following sequence of events:

1. Two instances are tagged with `AppId:MyApplication`, `Environment:Production`, `Group:1`.

This produces a tag on these instances, assuming First Tag Key = AppId, Second Tag Key = Environment, Third Tag Key = Group and a
patch window for MyApplication-Production-1 patch group is created. 2. Three more instances are created and tagged with `AppId:MyApplication`, `Environment:Production`, `Group:1`.

This produces a tag for Patch Group:MyApplication-Production-1.
No change to the patch window is needed because it picks up all five instances at the time of the next scheduled run.

For a more detailed discussion and a walkthrough on using this change type,
see [SSM Patch Window | Create](../ctref/deployment-patching-ssm-patch-window-create.md "../ctref/deployment-patching-ssm-patch-window-create.md").
