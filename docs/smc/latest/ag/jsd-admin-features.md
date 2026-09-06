

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Jira approvals and access controls
<a name="jsd-admin-features"></a>

The following sections describe approvals and access controls that are available in Jira.

**Approvals**

The approval agent has access to a screen with the options to approve or reject the product request. For a rejection, the agent can add a comment explaining the rejection of the request. The requester is able to see the status of the request, such as *Waiting for Approval*, *Scheduled*, *Launching*, or *Available*.

Changes to approver group members do not impact approvers identified for pre-existing issues, but do affect whether we permit approval. Only approver users assigned to the issue at the time of issue creation can approve the request. The approver user must still be a member of the group to issue an approval. Otherwise, we reject the request.

As with Service Catalog, all post-provision actions, including termination, receive pre-approval for the user or group approved to provision it.

**Access controls**

You can set access controls on portfolios, as described earlier in this guide. Those access controls are in addition to the per-project enablement: users must have access to an AWS Connector-enabled project and belong to the groups enabled for a portfolio to provision products in that portfolio.