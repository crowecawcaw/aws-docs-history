# Actions you can take in AMS standard patching

In addition to testing new AMIs, there are several actions you can take to manage the
patching of your infrastructure:

- If it took longer to test the updates than the patch window allowed, you can
  request that AMS apply the updates that were canceled when you're ready by
  submitting a service request (use the details in the original service
  notification as the basis).
- You can request that an important update (IU) or other update (OU) be applied
  before the next automated update window by submitting a service request
  providing a list of the updates, the applicable instances, and other details
  as appropriate. Since this CT is not automated, it takes longer to schedule
  and run. Check the service level objectives (SLOs) for the appropriate time.
  For more information, see [AMS service level objectives (SLOs)](apx-slo.md "apx-slo.md").
  Additionally, you can use existing, patched, AMS AMIs to create custom AMIs. For
  information, see [AMI | Create](../ctref/deployment-advanced-ami-create.md "../ctref/deployment-advanced-ami-create.md").

###### Note

You can't request a new AMS AMI based on an important update or other update
before the next maintenance window because the AMS AMI release process follows
a uniform cadence for the benefit of all AMS customers.

## Changing what gets patched/opting out

With AMS configured patching, in your response to the patching service
notification or in a Service Request, you can change what resources get patched. You
can do the following:

- Define a list of patches that should be excluded from remediation, per stack and per operating system.
- Define a list of resources that should be excluded from certain patches or all patching.
- Define a list of resources that should be always be excluded from all patching.
- Define a list of resources that should be patched on a certain day and certain time (good if
  you haven't defined a maintenance window).

To exclude one or more patches, submit a service request, or respond to the
patching service notification using the template provided next. Do not submit an
RFC. Include in the request the patch name or names that you want excluded and why.
Include this information in a Service Request as follows:

- Name: The name of the patch. For Windows patches, this is the KB name,
  such as `KB3145384`. For Linux patches, this is the package name,
  such as `openssh-6.6.1p1-25.61.amzn1.x86_64`.
- Reason: A comment indicating why the patch is being excluded.
- Expiration Time: The date/time when the exclusion expires.

If an excluded patch is already installed, it is removed.

The request is reviewed by an operator who will discuss it with you if excluding
those patches poses a significant security risk. The expiry date for excluded
patches is also negotiated. After the agreed upon expiry date, the exclusion
expires, and the patch is installed on any subsequent patching.

Patches on the exclusion list are still returned in scan results, if applicable.

###### Note

Unlike Windows, Linux patches are version-specific. This distinction is
important because new versions of an excluded patch are not automatically
excluded. It is your responsibility to notify AMS to exclude new versions of a
Linux patch if that's what you want to do.

### Patch service notification reply templates

You must reply to patching service notifications, using the specified format, in order for patching to be
performed on your instances. You should do this if you haven't already set a
maintenance window with AMS.

When you reply to a service notification, use the format given.

If no maintenance window is set, let us know when to patch what as shown
following:

```
UTC                 StartTime       StackId                     InstanceId (Optional)
2019-04-01          15:00           stack-123456789012          i-1234566789
2019-04-01          15:00           stack-123456789013          i-1234566784
2019-04-01          15:00           stack-123456789014          i-1234566783
2019-04-01          15:00           stack-123456789015          i-1234566782
```

If you have a set maintenance window and want certain resources to be excluded
from certain patches, use the following format:

```
StackId                     InstanceId (Optional)       Exclude Patches
stack-123456789012          i-1234566789                `PATCH`
stack-123456789013          i-1234566784                `PATCH`
stack-123456789014          i-1234566783                `PATCH`
stack-123456789015          i-1234566782                `PATCH`
```

If you have a set maintenance window and want certain resources to always be
excluded from all patching, use the following format:

```
StackId                     InstanceId (Optional)       Exclude Patches
stack-123456789012          i-1234566789                ALL
stack-123456789015          i-1234566782                ALL
```

## Preparing for patching

To prepare your environment for automated patching, we recommend the
following:

- Be sure you have a complete inventory of all instances to be patched.
- Ensure that your resources are backed up regularly as part of your Continuity of Business
  strategy. Additional backups are created as part of the patch sequence,
  and these are automatically deleted according to your configured Patch
  Orchestrator retention policy (default is 60 days).
- Ensure that all relevant licenses are up to date.
- Modify your stack maintenance windows to stagger patching so that testing
  stacks are patched before production stacks. That way, any errors with
  patching are found in the testing stacks and can be identified before
  production stacks are patched.

## Viewing patch settings

To find out what your current patching configuration is you can do the following:

- Submit a service request to AMS with the query.
- Wait for a patch service notification. The patching notice advises you of
  all patches to be applied and instances to be patched, and also suggests a patch window.

You can submit a service request to modify the following:

- Scan Interval: The amount of time, in minutes, between compliance scans
  performed on instances of this stack.

Default is `240` (4 hours).

- NotificationWindow: How far in advance (in minutes) of a scheduled change
  (patch) the notification should be sent to you.  Default is `10080` (7 days).
