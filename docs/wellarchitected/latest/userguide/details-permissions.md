# The AWS Well-Architected Tool Shares tab

To display or modify your workload invitations, choose the
**Shares** tab. This tab is only displayed for the owner of a
workload.

The following information is displayed for each AWS account and user that
has shared access to the workload:

**Principal**

The AWS account ID or user ARN with shared access to the
workload.

**Status**

The status of the workload invitation.

- Pending

The invitation is waiting to be accepted or rejected. If a
workload invitation is not accepted within seven days, it's
automatically expired.

- Accepted

The invitation was accepted.

- Rejected

The invitation was rejected.

- Expired

The invitation was not accepted or rejected within seven
days.

**Permission**

The permission granted to the AWS account or user.

- Read-Only

The principal has read-only access to the workload.

- Contributor

The principal can update answers and their notes, and has
read-only access to the rest of the workload.

**Permission details**

Detailed description of the permission.

To share the workload with another AWS account or user in the same AWS Region,
choose **Create**. A workload can be shared with up to 20 different
AWS accounts and users.

To delete a workload invitation, select the invitation and choose
**Delete**.

To modify a workload invitation, select the invitation and choose
**Edit**.
