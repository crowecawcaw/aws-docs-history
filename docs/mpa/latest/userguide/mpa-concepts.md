

# Terms and concepts for Multi-party approval
<a name="mpa-concepts"></a>

To help you understand Multi-party approval, this topic describes some of the key terms and concepts.

**Topics**
+ [Job functions for Multi-party approval](#job-functions)
+ [AWS resources for Multi-party approval](#aws-resources)
+ [Multi-party approval resources](#mpa-resources)
+ [Multi-party approval interfaces](#interfaces)

## Job functions for Multi-party approval
<a name="job-functions"></a>

**Requester**  <a name="mpa-requester-term"></a>
The *requester* is the individual or entity that makes a request to execute a [protected operation](#mpa-protected-operation). The request triggers an [approval session](#mpa-session).

**Administrator**  <a name="mpa-administrator-term"></a>
The *administrator*, or admin, is responsible for managing [approval teams](#mpa-team-term). When a Multi-party approval admin creates a team, they set the initial approval requirements and invite approvers to join the team.  
When a team is [active](team-health.md), the Multi-party approval admin can request to update the team description, approval threshold, and approvers assigned to a team. They can also request to delete the team. Requests by the Multi-party approval admin require team approval to take effect.  
For more information, see [Administrator tasks](administrator.md).

**Approver**  <a name="mpa-approver-term"></a>
An *approver* is responsible for responding to [requested operations](#mpa-protected-operation). If an approver has accepted a team invitation and the team is [active](team-health.md), the approver receives email notifications about [pending requests](#mpa-protected-operation) for the team. The approver can view request details and respond to pending requests using the [Multi-party approval portal](#mpa-portal).  
For more information, see [Approver tasks](approver.md).  
An *inactive approver* is an approver who has not responded in two or more sessions, or who cannot respond to requests due to the state of their IAM Identity Center user credentials. For example, a [deleted](https://docs.aws.amazon.com/singlesignon/latest/userguide/deleteusers.html) or [disabled](https://docs.aws.amazon.com/singlesignon/latest/userguide/disableuser.html) user. 

## AWS resources for Multi-party approval
<a name="aws-resources"></a>

**Protected operation**  <a name="mpa-protected-operation"></a>
A *protected operation* is a predefined list of operations that require [team approval](#mpa-team-term) before they can be executed. When a [requester](#mpa-requester-term) attempts to execute a protected operation, the operation enters a pending state until the approval threshold is met.  
When the protected operation is pending, it is also referred to as a *requested operation* or a *pending request*. For a list of supported protected operations, see [What operations are currently supported with Multi-party approval](what-is.md#mpa-integrations-supported).

## Multi-party approval resources
<a name="mpa-resources"></a>

**Approval team**  <a name="mpa-team-term"></a>
An *approval team*, or team, consists of [approvers](#mpa-approver-term). To grant approval, teams require a specified number of approvals (M) out of the total approvers (N). This is the *approval threshold*.  
A team becomes [active](team-health.md) if every invited approver accepts the team invitation. When active, teams become *self-protecting*. This means changes to the team require team approval to take effect.  
Teams can be shared across accounts using AWS Resource Access Manager (AWS RAM). For more information, see [Share team](share-team.md).

**Approval session**  <a name="mpa-session"></a>
An *approval session*, or session, is a 24-hour workflow initiated when a [requester](#mpa-requester-term) attempts to execute a [protected operation](#mpa-protected-operation). Session details include the following non-exhaustive items:  
+ Approval team
+ Requested operation, requester comments, and AWS Region where the request was made
+ Initiation time and completion or expiration time for the requested operation
+ Approver responses and response time
+ Request status (`PENDING`, `CANCELLED`, `APPROVED`, `FAILED`, or `CREATING`)
+ Completion strategy. Currently, only `AUTO_COMPLETION_UPON_APPROVAL` is supported. This means the operation is automatically executed using the requester's permissions, if approved.
Sessions expire 24 hours after the initial request. Expired sessions and non-responses from approvers count as rejections.

**Identity source**  <a name="mpa-identity-source"></a>
An *identity source* is a Multi-party approval resource that models the connection between Multi-party approval and the AWS IAM Identity Center instance that manages the user authentication for [approvers](#mpa-approver-term).  
A Multi-party approval identity source is created when you [set up Multi-party approval](setting-up.md). This is a one-time operation.  
When a Multi-party approval identity source is created, it adds the [Multi-party approval portal](#mpa-portal) application to the connected IAM Identity Center instance and creates a unique URL. A Multi-party approval identity source is required to create [approval teams](#mpa-team-term).

## Multi-party approval interfaces
<a name="interfaces"></a>

**Multi-party approval console**  <a name="mpa-console"></a>
The *Multi-party approval console* is located in the AWS Organizations console, and is an interface for Multi-party approval [administrator](#mpa-administrator-term) to create and manage their [approval teams](#mpa-team-term).

**Multi-party approval portal**  <a name="mpa-portal"></a>
The *Multi-party approval portal*, or approval portal, is used by approvers to view team invitations and requests, respond to requests, and view operation history.  
The portal is an AWS managed application for AWS IAM Identity Center that is accessed by [approvers](#mpa-approver-term) through the link in the team invitation or requested operation email notification.