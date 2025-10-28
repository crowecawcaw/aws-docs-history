# Collaborations and memberships in

AWS Clean Rooms

A _collaboration_ is a secure logical boundary in AWS Clean Rooms
in which members can perform analysis on configured tables.

Any member in AWS Clean Rooms can create a collaboration.

The collaboration creator can designate a single member to analyze configured tables and
receive results. However, the collaboration creator might want to prevent the member who can run
the analysis from having access to the query results. In that case, the collaboration creator
can designate one [member to who can query](glossary.md#glossary-member-who-can-query "glossary.md#glossary-member-who-can-query") or [one member who can run queries and
jobs](glossary.md#glossary-member-who-can-run-queries-jobs "glossary.md#glossary-member-who-can-run-queries-jobs") and another [member who can receive
results](glossary.md#glossary-member-who-can-receive-results "glossary.md#glossary-member-who-can-receive-results").

In most cases, the member who can query or the member who can query and run jobs is also the
[member paying for compute
costs](glossary.md#glossary-member-paying-for-query-compute "glossary.md#glossary-member-paying-for-query-compute"). However, the collaboration creator can configure a different member to be
responsible for paying for the query compute costs.

For information about how to create a collaboration using the AWS SDKs, see the [_AWS Clean Rooms API Reference_](../apireference/Welcome.md "../apireference/Welcome.md").

###### Topics

- [Creating a collaboration](create-collaboration.md "create-collaboration.md")
- [Creating a membership and joining a
  collaboration](create-membership.md "create-membership.md")
- [Editing collaborations](edit-collaboration.md "edit-collaboration.md")
- [Deleting collaborations](delete-collaboration.md "delete-collaboration.md")
- [Viewing collaborations](review-collab-console.md "review-collab-console.md")
- [Inviting members to a collaboration](invite-members.md "invite-members.md")
- [Monitoring members](monitor-status.md "monitor-status.md")
- [Adding members to a collaboration](add-member.md "add-member.md")
- [Removing members from a collaboration](remove-member.md "remove-member.md")
- [Leaving a collaboration](leave-collab.md "leave-collab.md")
