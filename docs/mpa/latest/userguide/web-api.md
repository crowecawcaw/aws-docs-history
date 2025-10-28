# Multi-party approval portal APIs

The APIs listed in this section are called by the Multi-party approval portal on behalf of approvers.
These APIs cannot be called directly and are not captured in the [Service Authorization Reference](../../../service-authorization/latest/reference/reference.md "../../../service-authorization/latest/reference/reference.md").
However, these APIs are logged in AWS CloudTrail events and log entries.

- `GetApprovalTeamForApprover`: Returns details for an approval team.
- `GetInvitationForApprover`: Returns details for an approval team invitation.
- `GetSessionForApprover`: Returns a list of sessions.
- `ListApprovalTeamsForApprover`: Returns a list of approval teams.
- `ListInvitationsForApprover`: Returns a list of approval team invitations.
- `ListSessionsForApprover`: Returns a list of sessions.
- `UpdateInvitationForApprover`: Sends a response to an approval team invitation.
- `UpdateSessionForApprover`: Sends a response in a session.
