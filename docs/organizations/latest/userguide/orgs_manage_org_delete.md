

# Deleting an organization with AWS Organizations
<a name="orgs_manage_org_delete"></a>

When you no longer need your organization, you can delete it. Deleting an organization does not close the management account, instead it removes the management account from the organization and deletes the organization itself.

The former management account becomes a standalone AWS account that is no longer managed by AWS Organizations. You then have three options:
+ You can continue to use it as a standalone account
+ You can use it to create a different organization
+ You can accept an invitation from another organization to add the account to that organization as a member account.

**Topics**
+ [Considerations](#orgs_manage_org_delete-considerations)
+ [Delete an organization](#orgs_manage_org_delete_procedure)

## Considerations
<a name="orgs_manage_org_delete-considerations"></a>

**Deleted organizations cannot be recovered**

If you delete an organization, you can't recover it. AWS also deletes any organization policies that you created in the organization, such as SCPs, RCPs, tag policies, backup policies, or AI services opt-out policies. You can't recover deleted policies.

**Organizations can only be deleted after all member account have been removed**

You can delete an organization only after you remove all member accounts from the organization. If you created some of your member accounts using AWS Organizations, you might be blocked from removing those accounts. You can remove a member account only if it has all the information that's required to operate as a standalone AWS account. For more information about how to provide that information and then remove the account, see [Leaving an organization from a member account with AWS Organizations](orgs_manage_accounts_leave-as-member.md).

**Member accounts in a 'suspended' state cannot be removed from an organization**

If you closed a member account before you remove it from the organization, it enters a `Closed` state for a period of time and you can't remove the account from the organization until it is finally closed. This can take up to 90 days and can prevent you from deleting the organization until all member accounts are completely closed. 

**Removing the management account from an organization by deleting the organization can affect the account in the following ways:**
+ The account is responsible for paying only its own charges and is no longer responsible for the charges incurred by any other account.
+ Integration with other services might be disabled. For example, AWS IAM Identity Center requires an organization to operate, so if you remove an account from an organization that supports IAM Identity Center, the users in that account can no longer use that service.

The management account of an organization is never affected by service control policies (SCPs), so there is no change in permissions after SCPs are no longer available.

**Back up all reports**

Make sure to export or back up reports from the management account, especially billing reports. Organizational level reports and history are not stored when you delete an organization. All cost data (such as the Cost Explorer data set) is deleted. It is recommended that you do a full export of all billing history.

For more information, see [Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html), [Cost Explorer Reports](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-reports.html), [Savings Plans Reports](https://docs.aws.amazon.com/savingsplans/latest/userguide/ce-sp-usingPR.html#ce-dl-pr), and [Reserved Instance (RI) utilization and coverage](https://repost.aws/knowledge-center/ec2-ri-utilization-coverage-cost-explorer).

## Delete an organization
<a name="orgs_manage_org_delete_procedure"></a>

Use the following procedure to delete an organization which reverts the former management account to a standalone AWS account that is no longer managed by AWS Organizations.

**Minimum permissions**  
To delete an organization, you must sign in as a user or role in the management account, and you must have the following permissions:  
`organizations:DeleteOrganization`
`organizations:DescribeOrganization` – required only when using the Organizations console

### AWS Management Console
<a name="orgs_manage_org_delete_console"></a>

**To delete an organization**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. Before you can delete the organization, you must first remove all accounts from the organization. For more information, see [Removing a member account from an organization with AWS Organizations](orgs_manage_accounts_remove.md).

1. Navigate to the **[Settings](https://console.aws.amazon.com/organizations/v2/home/settings)** page, and then choose **Delete organization**.

1. In the **Delete organization** confirmation dialog box, enter the organization's ID which is displayed in the line above the text box. Then, choose **Delete organization**.
**Important**  
This operation does **not** close the management account but does return it to a standalone AWS account. To close the account, follow the steps at [Closing a member account in an organization with AWS Organizations](orgs_manage_accounts_close.md).

### AWS CLI & AWS SDKs
<a name="orgs_manage_org_delete_cli_sdk"></a>

The following code examples show how to use `DeleteOrganization`.

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples). 

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Organizations;
    using Amazon.Organizations.Model;

    /// <summary>
    /// Shows how to delete an existing organization using the AWS
    /// Organizations Service.
    /// </summary>
    public class DeleteOrganization
    {
        /// <summary>
        /// Initializes the Organizations client and then calls
        /// DeleteOrganizationAsync to delete the organization.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var response = await client.DeleteOrganizationAsync(new DeleteOrganizationRequest());

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine("Successfully deleted organization.");
            }
            else
            {
                Console.WriteLine("Could not delete organization.");
            }
        }
    }
```
+  For API details, see [DeleteOrganization](https://docs.aws.amazon.com/goto/DotNetSDKV3/organizations-2016-11-28/DeleteOrganization) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To delete an organization**  
The following example shows how to delete an organization. To perform this operation, you must be an admin of the master account in the organization. The example assumes that you previously removed all the member accounts, OUs, and policies from the organization:  

```
aws organizations delete-organization
```
+  For API details, see [DeleteOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organization.html) in *AWS CLI Command Reference*. 

------