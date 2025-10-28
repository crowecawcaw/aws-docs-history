# In-place patching

In-place patching refers to a method where AMS logs into each stack instance and
applies patches.

In-place patching occurs on mutable infrastructures using Amazon EC2 instances running a
supported operating system. Patching applies all non-excluded updates available up
to that point. When critical patches are released, there is an additional critical
patching process.

## Standard patching: in-place

Standard patching occurs on the agreed-to patch schedule suggested in the
patch service notification, and includes regular patch updates that are not
deemed critical.

Prior to the proposed patching window, and with your affirmative response to
the notification, a patch RFC is created and appears in your RFC
dashboard.

## Critical patching: in-place

When an OS vendor releases a critical security update, AMS notifies you of
the patch RFC by sending you a service notification (to the contact email for
your account) for each stack, according to the AMS service commitment. The
service notification includes the following for each update:

- Update release date
- Update criticality
- Update details (KB reference, etc.)
- IDs of stacks affected

You can test the updates listed in the notification, and approve or reject the
patches by replying to the service notification. If you approve the
notification, you need to provide a specific patch window per stack for
installing the updates.

###### Note

Patch windows that are within 24 hours of reply to the service
notification may be rescheduled based on available capacity.

If you don't reply within 10 days or if you reject the proposed patching, the
patching is canceled.

If you want to apply the updates after the allowed period (provided in the
notification), submit a service request for a new patch schedule based on the
details of the previous notification.

If you approve the service notification, AMS applies the updates within your
specified patch window, according to the service commitment.

In the case of multiple updates, you can exclude specific updates from the
patching by specifying the updates to be excluded in your response to the
service notification.

AMS sends you a service notification for each stack, of the outcome of each
update (that is, success or fail).
