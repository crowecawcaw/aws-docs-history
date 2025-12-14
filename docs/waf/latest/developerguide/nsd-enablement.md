**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Enabling AWS Shield network security director

###### Note

AWS Shield network security director is in public preview release and is subject to change.

AWS Shield network security director is enabled for AWS accounts through AWS Organizations. This section of the documentation describes all the steps required to enable AWS Shield network security director for an AWS Organization.

This section includes two steps, both of which are necessary to complete network security director setup:

1. The AWS Organization management account enables AWS Shield network security director, designates a delegated administrator for the organization, and creates the corresponding delegated administrator policy.
2. The delegated administrator for the organization creates a policy that enables AWS Shield network security director for user-selected regions and target member accounts in the organization.

## Enabling AWS Shield network security director and delegating a service administrator

When assigning the delegated administrator account for AWS Shield network security director, AWS Shield network security director will recommend an existing delegated administrator if one is already configured for another AWS security service, such as **AWS Security Hub**. If no delegated administrator exists, you will be prompted to select a member account from your organization. The organization's management account cannot be designated as the delegated administrator.

###### To designate an administrator for AWS Shield network security director

1. Sign in to your AWS Account with your AWS Organization management account credentials and open the AWS Shield network security director console at [https://console.aws.amazon.com/wafv2/network-security-director/](https://console.aws.amazon.com/wafv2/network-security-director/ "https://console.aws.amazon.com/wafv2/network-security-director/").
2. From the network security director home page, choose **Get started**.
3. For **Delegated administrator account**, choose an administrator account based on the provided options. As a best practice, we recommend using the same delegated administrator across security services for consistent governance.
4. For **Delegated administrator policy**, choose one of the following options to add the policy statement:
   1. (Option 1) Choose **Update this for me**. Select the box under the policy statement to confirm AWS Shield network security director will automatically create a delegation policy granting all required permissions to the delegated administrator.
   2. (Option 2) Choose **I want to attach this manually**. Choose **Copy and attach**. In the AWS Organizations console, under **Delegated administrator for AWS Organizations**, choose **Delegate**, and paste the resource policy in the delegation policy editor and then Choose **Create Policy**. Open the tab where you are in the AWS Shield network security director console.

5. Choose **Complete get started**.

At the end of this step the following actions will be complete:

- [Trusted Access](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") enablement for AWS Shield network security director. This will allow network security director to create service-linked roles within member accounts that are in scope of the policy.
- Creation of the service-linked role **AWSServiceRoleForNetworkSecurityDirector** for the organization’s management account.
- Registration of the delegated administrator for AWS Shield network security director.
- Update of the resource policy, allowing the delegated administrator for AWS Shield network security director to make necessary calls to AWS Organizations APIs.

Now that the setup is complete, you will be redirected to the **Settings** page, where you can update or remove the delegated administrator, manage delegation policy, and disable network security director as a service. To access this settings page in the future with the organization's management account, navigate to the network security director console and choose **Manage settings**.

## Enabling AWS Shield network security director for member accounts with delegated administrator

This step must be completed by the delegated administrator. Once the AWS Organization's management account designates a delegated administrator, that administrator must create a policy that grants permission to enable regions within the organization. All configured policies are available in the **Region and Account Policies** section of the AWS Shield network security director console. The procedure below outlines how to create this policy.

###### To create and attach a policy that enables regions for targeted accounts

1. Sign in to your AWS account with your delegated administrator credentials and open the AWS Shield network security director console at [https://console.aws.amazon.com/wafv2/network-security-director/](https://console.aws.amazon.com/wafv2/network-security-director/ "https://console.aws.amazon.com/wafv2/network-security-director/").
2. From the AWS Shield network security director home page, choose **Enable**.
3. For **Details**, enter a name and an optional description for the policy.
4. For **Account selection**, select one of the following options. Choose **All organizational units and accounts** if you want to apply the policy to all organizational units and accounts. Choose **Specific organizational units and accounts** if you want to apply the policy to specific organizational units and accounts. Use the search bar or organizational structure tree to specify the organizational units and accounts where the policy will be applied.
5. For **Regions**, select the regions you want to enable or disable for this policy. Please refer to [Performance Considerations](troubleshooting.md#performance-considerations "troubleshooting.md#performance-considerations") before completing your selections.
6. Review your changes, and then choose **Enable network security director**.

At the end of this step the following actions will be complete:

- Creation of the service-linked role **AWSServiceRoleForNetworkSecurityDirector** for the current delegated administrator account.
- Creation of the policy that enables AWS Shield network security director to run scans in the enabled regions and on the attached targets.
- Redirection to the **Summary dashboard**, where you can view organization-wide insights as well as resource-level details for each account.

Now that the setup is complete, you will be redirected to the **Summary dashboard** page, where you can view organization-wide insights as well as resource-level details for each account. To manage the policies in the future with the delegated administrator account, navigate to the network security director console and choose **Manage settings**.
