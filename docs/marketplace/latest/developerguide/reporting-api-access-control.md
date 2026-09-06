

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Access control for the AWS Marketplace Reporting API
<a name="reporting-api-access-control"></a>

You use the AWS Marketplace Reporting API to get the **Procurement insights** dashboard. The API supports the [GetBuyerDashboard](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.html) action. 

To use the API, you must first create the `AWSServiceRoleForProcurementInsightsPolicy` service-linked role. The role does the following: 
+ Enables AWS Marketplace to access and describe the data for all the accounts in a buyer's organization.
+ Gets the **Procurement insights** dashboard
+ Enables you to register and deregister delegated administrators

Buyers create the role when they use the AWS Marketplace console to enable trusted access to the **Procurement insights** dashboard. For more information about that process, see [Activating the dashboard](https://docs.aws.amazon.com/marketplace/latest/buyerguide/enabling-procurement-insights.html#integrate-dashboard), in the *AWS Marketplace Buyer Guide*.

**Important**  
When using the API or the CLI, you must create the service-linked role before you enable trusted access to the dashboard.
In addition to the service-linked role, you must enable all features for your organization, and you must belong to an administrator account. For more information, see the following topics in the *AWS Organizations User Guide*:  
 [Enabling all features for an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html)
[Tutorial: Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html)
[Managing the management account with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-manage_accounts_management.html)

The `AWSServiceRoleForProcurementInsightsPolicy` must have the following IAM permissions in order to call the [GetBuyerDashboard](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.html) action, and to register and deregister delegated administrators:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [{
            "Sid": "CreateServiceLinkedRoleForProcurementInsights",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/procurement-insights.marketplace.amazonaws.com/AWSServiceRoleForProcurementInsights*",
            "Condition": {
                "StringLike": {
                    "iam:AWSServiceName": "procurement-insights.marketplace.amazonaws.com"
                }
            }
        },
        {
            "Sid": "EnableAWSServiceAccessForProcurementInsights",
            "Effect": "Allow",
            "Action": [
                "organizations:EnableAWSServiceAccess"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "organizations:ServicePrincipal": "procurement-insights.marketplace.amazonaws.com"
                }
            }
        },
        {
            "Sid": "ManageDelegatedAdministrators",
            "Effect": "Allow",
            "Action": [
                "organizations:ListDelegatedAdministrators",
                "organizations:DeregisterDelegatedAdministrator",
                "organizations:RegisterDelegatedAdministrator"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "organizations:ServicePrincipal": "procurement-insights.marketplace.amazonaws.com"
                }
            }
        },
        {
            "Sid": "GetBuyerDashboardStatement",
            "Effect": "Allow",
            "Action": "aws-marketplace:GetBuyerDashboard",
            "Resource": "*"
        },
        {
            "Sid": "ViewOrganizationDetails",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization",
                "organizations:ListAWSServiceAccessForOrganization"
            ],
            "Resource": "*"
        }
    ]
}
```

------

For more information about creating policies, see [Policies and permissions in AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html), in the *IAM User Guide*.

For more information about the AWS Organizations actions that the policy uses, see the [AWS Organizations API reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Operations.html).