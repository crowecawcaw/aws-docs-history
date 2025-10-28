# Designating the Detective administrator for an

organization

In the organization behavior graph, the Detective administrator account manages the behavior
graph membership for all organization accounts.

How the Detective administrator account is managed – The organization management account designates the Detective administrator account for the
organization in each AWS Region.

Setting the Detective administrator account as the delegated administrator account – The Detective administrator account also becomes the delegated administrator account for Detective
in AWS Organizations. The exception is if the organization management account designates itself as the
Detective administrator account. The organization management account cannot be a delegated
administrator in Organizations.

After the delegated administrator account is set in Organizations, the organization management
account can only choose either the delegated administrator account or their own account as the
Detective administrator account. We recommend that you choose the delegated administrator account in
all Regions.

Creating and managing the organization behavior graph – When the organization management account chooses a Detective administrator account, Detective
creates a new behavior graph for that account. That behavior graph is the organization behavior
graph.

If the Detective administrator account is an administrator account for an existing behavior
graph, then that behavior graph becomes the organization behavior graph.

The Detective administrator account chooses organization accounts to enable as member accounts
in the organization behavior graph.

![This diagram shows how the organization management account chooses the Detective administrator account. The Detective administrator account is the administrator account for the organization behavior graph and the delegated administrator account in Organizations. The Detective administrator account has access to all of the organization accounts.](images/diagram_account_delegation.png)
The Detective administrator account can also send invitations to accounts that do not belong to
the organization. For more information, see [Managing organization accounts as Detective member accounts](accounts-orgs-members.md "accounts-orgs-members.md") and [Managing invited member accounts in Detective](accounts-invited-members.md "accounts-invited-members.md").

Required permissions to configure the Detective administrator account – To ensure that the organization management account is able to configure the Detective
administrator account, you can attach the [AmazonDetectiveOrganizationsAccess managed policy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazondetectiveorganizationsaccesspolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-amazondetectiveorganizationsaccesspolicy") to your AWS Identity and Access Management
(IAM) entities.
