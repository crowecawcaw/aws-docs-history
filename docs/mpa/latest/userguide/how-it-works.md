# How Multi-party approval works

To help you understand Multi-party approval, this topic describes the three-step approval process.

![Diagram showing AWS Management Console request flow to Approval Portal for protected operations.](images/how-it-works.png)
_Figure 1: Diagram depicting how Multi-party approval works. You can also use the AWS CLI & AWS SDKs instead of the AWS Management Console._

Step 1: Operation request**Requester attempts to execute a protected operation**

When a requester attempts to execute a protected operation and has the necessary `mpa:StartSession` permission:

1. The protected operation enters a pending state
2. Multi-party approval creates an approval session
3. Approvers receive email notifications prompting them to respond to the requested operation

**Viewing the request status as the requester**

The requester can view the status of a request if the following conditions are met:

- The requester has `mpa:` permissions for the associated approval team and session.
- The requester has access to the approval team. For example, if the team has been shared.

If these conditions are met, the requester can use Multi-party approval APIs (such as [GetSession](../APIReference/API_GetSession.md "../APIReference/API_GetSession.md")) to check the status of the request (`PENDING`, `CANCELLED`, `APPROVED`, `FAILED`, `CREATING`).

The service that you are using with Multi-party approval determines whether requester is provided with the Amazon Resource Name (ARN) for the approval session.

For information, see the **Learn More** column in [What operations are currently supported with Multi-party approval](what-is.md#mpa-integrations-supported "what-is.md#mpa-integrations-supported").

Step 2: Approval session**Approvers respond to the request in an approval session**

1.  Approvers access the approval portal using the link in the email notification for the requested operation
2.  Approvers view details for the request including the following non-exhaustive items:
    - Requester IAM principal
    - Requested operation and timestamp
    - Requester AWS account and AWS Region
    - Requester comments
    - Approval session status

3.  Approvers can choose to:

        * Approve the request
        * Reject the request

    Non-responses count as rejections.

**Sessions and approval thresholds**

When a session meets its approval threshold, the requested operation is executed automatically (`AUTO_COMPLETION_UPON_APPROVAL`). Approvers who have not yet responded don't need to take any action.

For example, in a session with five approvers and an approval threshold of three, the requested operation is executed automatically after receiving the third approval, regardless of pending responses from the remaining approvers.

Step 3: Session result
**Approval session determines if the requested operation is executed**

Protected operations can only be executed when the approval threshold is met and before the approval session expires. Otherwise, the request is rejected.

- If the approval threshold is met:
  - Request is approved
  - Requested operation is automatically executed using the requester's permissions (`AUTO_COMPLETION_UPON_APPROVAL)`.

- If the approval threshold is not met:
  - Request is rejected
  - Requested operation is not executed

Approvers do not receive email notifications about the session result or the execution status for the protected operation. However, approvers can view the session result in the Multi-party approval portal.
For more information, see [View operation history](view-operation-history.md "view-operation-history.md").

**Viewing the execution status as the requester**

After an approval session ends, the service you are using with Multi-party approval determines whether the requester can view the execution status for the protected operation (`EXECUTED`, `FAILED`, or `PENDING`).

For information, see the **Learn More** column in [What operations are currently supported with Multi-party approval](what-is.md#mpa-integrations-supported "what-is.md#mpa-integrations-supported").

## Considerations

**Multi-party approval does not replace IAM**

Multi-party approval works with IAM permissions, it does not replace them.
When a requester attempts to execute a protected operation, AWS first evaluates the requester's IAM permissions.

The Multi-party approval workflow is only triggered if the requester has the necessary IAM permissions to perform the requested operation,
and the requested operation is only executed if the requester still has the necessary IAM permissions when the request is approved.

This workflow is designed to add an additional layer of security through team-based approval requirements.
