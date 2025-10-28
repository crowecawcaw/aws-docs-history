# AMS standard patching FAQs

This section provides answers to some frequently asked questions.

- Q: How do I opt out of patching globally?

A: To globally opt out of patching, file a service request. Note that you
can't opt out of AMS mandatory patches. All stacks will continue to be
scanned so that we can report on vulnerabilities.

- Q: How do I exclude specific stacks from patching?

A: To permanently exclude specific stacks from patching, submit a service
request. To exclude certain stacks from a particular patch cycle, respond to
the upcoming patching notice with the list of stacks to exclude. For
information, see [Changing what gets patched/opting out](patch-actions.md#patch-excluding-patching "patch-actions.md#patch-excluding-patching").
Note that you can't opt out of mandatory patches.

- Q: What happens if I don't approve a patching service notification?

A: You have 14 days to approve a standard patching service request and 10 days
to approve a critical patching notice. If you don't approve the service request
within the time period, the service commitment is nullified and no patching
occurs. In the case of mandatory patching, patches are applied regardless of
response to the service request.

- Q: How do I exclude specific patches and packages from being installed?

A: To permanently exclude specific patches or packages, submit a service
request. To exclude certain patches or packages from a particular patch
cycle, respond to the upcoming patching notice with the list of patches or
packages to exclude. For details, see
[Changing what gets patched/opting out](patch-actions.md#patch-excluding-patching "patch-actions.md#patch-excluding-patching").
Note that you can't opt out of mandatory patches.

- Q: What happens if a system fails as a result of patching?

A: AMS monitors each system. AMS sends a service notification to you of
the outcome of each update (that is, success or fail) per stack and
instance. If a failure is detected, AMS investigates, works to restore the
instance, and then an AMS operations engineer attempts to manually patch.
For information, see [AMS standard patching failures](patch-overview.md#patching-process-failures "patch-overview.md#patching-process-failures").

- Q: What updates are managed by AMS?

A: AMS manages operating system level updates that AMS is notified of by
the vendor. For more information, see [Supported patches](patch-overview.md#patch-supported "patch-overview.md#patch-supported").

- Q: What updates are not managed by AMS?

A: Application-level updates are not managed by AMS.

- Q: How are Auto Scaling groups updated?

A: Auto Scaling groups are updated with an AMI replacement in the Auto Scaling
group configuration and preform a rolling update. A rolling update observes
the HealthyHostThreshold setting of your patching configuration, which
determines how many Amazon EC2 instances in a stack must be maintained active
during patching. For more information, see [AMI updates patching (using patched AMIs
for Auto Scaling groups)](patching-method-immutable.md "patching-method-immutable.md").

- Q: How do I get updates installed outside the normal cycle?

A: For OS-level updates that you want installed outside of the normal patching
schedule, submit a service request by using the patching notification that
you received. This might happen if your testing of a proposed patch took
longer than 21 days (for a standard patch) or 14 days (for a critical
patch). Out-of-band patching can be done in-place for standalone Amazon EC2
instances.

- Q: How are newly deployed stacks or instances patched?

A: When creating a new Amazon EC2 stack instance or Auto Scaling group, you should
always specify the latest AMS AMI, which will have the latest patches on
it already. For mutable infrastructures, inline patching should be performed
as soon as the stack is deployed.
