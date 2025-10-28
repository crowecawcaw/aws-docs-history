# Jira approvals and access controls

This section describes approvals and access controls that
are available in Jira.

**Approvals**

The approval agent has access to a screen with the options to
approve or reject the product request. For a rejection, the agent can
add a comment explaining the rejection of the request. The requester can
view the status of the request, which includes **Waiting for Approval**, **Scheduled**, **Launching**, or
**Available**. Changes to approver group
members does not impact approvers identified for pre-existing issues,
but does affect whether AWS permits approval. Only approver users
assigned to the issue at the time of issue creation can approve the
request. The approver user must also be a member of the group to issue
an approval. If the approver user is not a member of the group, AWS
may reject the request. All post-provision actions, including
termination, receive pre-approval for the user or group approved to
provision it.

**Access controls**

You can set access controls on portfolios, as described earlier in
this guide. Those access controls are in addition to the per-project
enablement: users must have access to an AWS Connector-enabled project
and belong to the groups enabled for a portfolio to provision products
in that portfolio.
