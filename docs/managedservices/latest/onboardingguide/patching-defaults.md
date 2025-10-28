# Patching defaults

This section describes AMS patching defaults; for more information on
AMS patching, see the AMS User Guide Patch Management chapter.

AMS releases patched AMIs on a monthly basis; all new stack requests should be configured with the latest AMS AMI.

###### Important

AMS Patch Orchestrator, tag-based patching, uses AWS Systems Manager (SSM) functionality to allow you to tag,
or have AMS tag for you, instances and have those instances patched using a baseline and a window that you configure. To learn more, see
[Patch Orchestrator: a tag-based patching model](../userguide/patch-orchestrator.md "../userguide/patch-orchestrator.md").

AMS-standard, account-based, patching: For each account with stacks that receive in-place patching, a notification of upcoming applicable patches is sent out shortly after
“patch Tuesday”. The notification contains a list of all stacks and the applicable patches as well as the suggested patch window.
For critical patches, the window is set no longer than 10 days in advance, and for standard patching no more than 14 days
in advance. If you do not reply to the notification, patching does not occur. If
you would like to exclude certain patches, reply to the notification, or submit a service request. If you reply with consent to patching, but don’t
specifically request a different schedule, patches are applied as described in the notification that you receive.

###### Note

The patch service notification is an email sent to the account contacts and contains a link to the AWS Support console. You
can reply through the AWS Support console or through the AMS service request page, where the notification appears as a service notification.

At the time of the AMS-standard patching process, AMS performs the following:

1. You are sent a patching service notification fourteen days before the proposed patch window.
   The patching service notification is sent via email to the contact email address that you have on file for your account.
2. Identifies all reachable EC2 instances in the stack based on the list of stacks provided in the patching notification. In this case,
   "Reachable" means instances that are in the "Running" EC2 state, and have the EC2 Run Command agent fully operational.
3. AMS performs patching in a manner that ensures that a sufficient number of EC2 instances are running concurrently (configured through
   the `healthy-host-threshold` setting) so that the stack remains healthy.
4. After the patching operation is complete for all EC2 instances, AMS updates the RFC with the patching status:
   Success, Partial Success or Failure. In the case of any status other than Success, a ticket is created for an operator
   to follow up on the patching results and take any corrective actions.
