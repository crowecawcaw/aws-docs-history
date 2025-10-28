# Terms and concepts for Multi-party approval

To help you understand Multi-party approval, this topic describes some of the key terms and concepts.

###### Topics

- [Job functions for Multi-party approval](#job-functions "#job-functions")
- [AWS resources for Multi-party approval](#aws-resources "#aws-resources")
- [Multi-party approval resources](#mpa-resources "#mpa-resources")
- [Multi-party approval interfaces](#interfaces "#interfaces")

## Job functions for Multi-party approval

**Requester**

The _requester_ is the individual or entity that makes a request to execute a [protected operation](#mpa-protected-operation "#mpa-protected-operation"). The request triggers an [approval session](#mpa-session "#mpa-session").

**Administrator**

The _administrator_, or admin, is responsible for managing [approval teams](#mpa-team-term "#mpa-team-term"). When a Multi-party approval admin creates a team, they set the initial approval requirements and invite approvers to join the team.

When a team is [active](team-health.md "team-health.md"), the Multi-party approval admin can request to update the team description, approval threshold, and approvers assigned to a team. They can also request to delete the team. Requests by the Multi-party approval admin require team approval to take effect.

For more information, see [Administrator tasks](administrator.md "administrator.md").

**Approver**

An _approver_ is responsible for responding to [requested operations](#mpa-protected-operation "#mpa-protected-operation"). If an approver has accepted a team invitation and the team is [active](team-health.md "team-health.md"), the approver receives email notifications about [pending requests](#mpa-protected-operation "#mpa-protected-operation") for the team. The approver can view request details and respond to pending requests using the [Multi-party approval portal](#mpa-portal "#mpa-portal").

For more information, see [Approver tasks](approver.md "approver.md").

An _inactive approver_ is an approver who has not responded in two or more sessions, or who cannot respond to requests due to the state of their IAM Identity Center user credentials.
For example, a [deleted](../../../singlesignon/latest/userguide/deleteusers.md "../../../singlesignon/latest/userguide/deleteusers.md")
or [disabled](../../../singlesignon/latest/userguide/disableuser.md "../../../singlesignon/latest/userguide/disableuser.md") user.

## AWS resources for Multi-party approval

**Protected operation**

A _protected operation_ is a predefined list of operations that require [team approval](#mpa-team-term "#mpa-team-term") before they can be executed.
When a [requester](#mpa-requester-term "#mpa-requester-term") attempts to execute a protected operation, the operation enters a pending state until the approval threshold is met.

When the protected operation is pending, it is also referred to as a _requested operation_ or a _pending request_. For a list of supported protected operations, see [What operations are currently supported with Multi-party approval](what-is.md#mpa-integrations-supported "what-is.md#mpa-integrations-supported").

## Multi-party approval resources

**Approval team**

An _approval team_, or team, consists of [approvers](#mpa-approver-term "#mpa-approver-term"). To grant approval, teams require a specified number of approvals (M) out of the total approvers (N). This is the _approval threshold_.

A team becomes [active](team-health.md "team-health.md") if every invited
approver accepts the team invitation. When active, teams become _self-protecting_. This means changes to the team require team approval to take effect.

Teams can be shared across accounts using AWS Resource Access Manager (AWS RAM). For more information, see [Share team](share-team.md "share-team.md").

**Approval session**

An _approval session_, or session,
is a 24-hour workflow initiated when a [requester](#mpa-requester-term "#mpa-requester-term") attempts to execute a [protected operation](#mpa-protected-operation "#mpa-protected-operation"). Session details include the following non-exhaustive items:

- Approval team
- Requested operation, requester comments, and AWS Region where the request was made
- Initiation time and completion or expiration time for the requested operation
- Approver responses and response time
- Request status (`PENDING`, `CANCELLED`, `APPROVED`, `FAILED`, or `CREATING`)
- Completion strategy. Currently, only `AUTO_COMPLETION_UPON_APPROVAL` is supported. This means the operation is automatically executed using the requester's permissions, if approved.

Sessions expire 24 hours after the initial request. Expired sessions and non-responses from approvers count as rejections.

**Identity source**

An _identity source_
is a Multi-party approval resource that models the connection between Multi-party approval and the AWS IAM Identity Center instance that manages the user authentication for [approvers](#mpa-approver-term "#mpa-approver-term").

A Multi-party approval identity source is created when you [set up Multi-party approval](setting-up.md "setting-up.md"). This is a one-time operation.

When a Multi-party approval identity source is created, it adds the [Multi-party approval portal](#mpa-portal "#mpa-portal") application to the connected IAM Identity Center instance and creates a unique URL. A Multi-party approval identity source is required to create [approval teams](#mpa-team-term "#mpa-team-term").

## Multi-party approval interfaces

**Multi-party approval console**

The _Multi-party approval console_ is located in the AWS Organizations console, and is an interface for Multi-party approval [administrator](#mpa-administrator-term "#mpa-administrator-term") to create and manage their [approval teams](#mpa-team-term "#mpa-team-term").

**Multi-party approval portal**

The _Multi-party approval portal_, or approval portal, is used by approvers to view team invitations and requests, respond to requests, and view operation history.

The portal is an AWS managed application for AWS IAM Identity Center
that is accessed by [approvers](#mpa-approver-term "#mpa-approver-term") through the link in the team invitation or requested operation email notification.
