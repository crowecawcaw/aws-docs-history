# How AMS standard patching works

AMS uses the Systems Manager Run Command service for regularly scheduled monthly and as-needed
critical patching, with two principal patching methods, in-place and AMI replacement,
depending on your infrastructure deployment strategy (mutable vs. immutable). This
section describes the AMS patching service, types, methods, and processes.

AMS defines two patch types, which are scheduled differently:

- _Critical patching_: Updates are applied as quickly as possible, after acceptance of the notice.
- _Standard patching_: Regular OS vendor updates and applied monthly.
  Patches are applied through either in-place patching or AMI replacement (upon request).

## Update scanning

AMS uses the [Amazon EC2 Run Command Service](https://aws.amazon.com/ec2/run-command/ "https://aws.amazon.com/ec2/run-command/") to contact your Amazon EC2 stacks and deploy the required scanning and patching scripts. AMS uses the native package management component already installed on the supported operating system to perform all the required
scanning and patching behavior on the Amazon EC2 stack. For Red Hat and Amazon Linux, the service uses yum. For Windows, the service uses the Windows Update Agent.

Scans are performed daily using
[SSM Maintenance Windows](../../../systems-manager/latest/userguide/systems-manager-maintenance.md "../../../systems-manager/latest/userguide/systems-manager-maintenance.md")
and the AMS default AWS-RunPatchBaseline document. Every reachable Amazon EC2 stack is scanned, using the update repositories for
Linux and Windows. The AMS patching process detects all reachable Amazon EC2 stacks and then performs the scans in a batch process so that the
stack always remains in a healthy state, even if a failure occurs while running the scan. The scan results are then saved for each Amazon EC2 stack.

To view the scan results for a stack or instance, submit a service request with the stack ID or instance ID.

The default AMS patching process is to install all available patches regardless of patch classification or severity (for example, critical versus standard).
The exception to this are patches that you have explicitly excluded for the stack (patches defined as mandatory by AMS should not be excluded).

You're sent a patching service notification 14 days before the proposed maintenance window. This gives you time to test the proposed patches and accept
or reject them. If you don't reply to the patching service notification, your instances aren't patched. When the time comes to install the patches, AMS
creates a Request for Change (RFC) for each stack, and that RFC appears in your account's RFC list.

## AMS configured maintenance window and notice

With AMS configured patching, each account has a monthly maintenance window,
which you define when you onboard your account. The AWS Managed Services Maintenance Window (or Maintenance Window) performs maintenance activities for AWS Managed Services (AMS) and recurs the second Thursday of every month from
3 PM to 4 PM Pacific Time. AMS may change the maintenance window with 48 hours notice.

The patching window is different. The patching outbound service request (also known as a _service notification_) includes a
suggested patch window.

###### Note

For information about replying to the patching service notification, see [Actions you can take in AMS standard patching](patch-actions.md "patch-actions.md").

The patching service notification is sent by email to the contact email address on
file for your account. The notification includes a link to the AWS Support
console where you can respond to it. You can also respond to the notification
using the AMS Service Request page. The service notification includes:

- A list of update IDs (CSUs, IUs, and OUs) that apply to the stack, and those updates that you
  have requested be excluded from patching (if any).
- IDs of instances that will be affected.
- A proposed patching window when the updates will be applied. You can
  request a different patching window.
- A request that you accept the proposed patching, or ask for additional
  information. AMS gives you time to test the impact of the updates and
  approve or reject the patching, or ask that specific updates be excluded. If
  you need more time to test, and want the updates to be applied after your
  testing, respond to the service notification and describe what you want, or
  submit a service request for a new patch RFC based on the details of the
  previous RFC. If you don't reply to the service notification at all, no
  patching action is taken and the RFC is cancelled.

If you approve the service notification, AMS runs the patch RFC and applies
the updates within the agreed-to patch window, as per the service commitment.

When patching is finished, AMS sends you a correspondence in the Service
Request, with a summary of the outcome of the patching activity (that is, success or
failed).
