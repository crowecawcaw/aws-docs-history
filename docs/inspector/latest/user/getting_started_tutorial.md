

# Getting started tutorial: Activating Amazon Inspector
<a name="getting_started_tutorial"></a>

 This topic describes how to activate Amazon Inspector for a standalone account environment (member account) and multi-account environment (delegated administrator account). When you activate Amazon Inspector, it automatically begins discovering workloads and scanning them for software vulnerabilities and unintended network exposure. 

------
#### [ Standalone account environment ]

 The following procedure describes how to activate Amazon Inspector in the console for a member account. To programatically activate Amazon Inspector, [inspector2-enablement-with-cli](https://github.com/aws-samples/inspector2-enablement-with-cli). 

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home).

1. Choose **Get Started**.

1. Choose **Activate Amazon Inspector**.

 When you activate Amazon Inspector for a standalone account, [all scan types](https://docs.aws.amazon.com/inspector/latest/user/scanning-resources.html) are activated by default. For information about member accounts, see [Understanding the delegated administrator account and member accounts in Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html). 

------
#### [ Multi-account (with AWS Organizations policy) ]

 AWS Organizations policies provide centralized governance for enabling Amazon Inspector across your organization. When you use an organization policy, Amazon Inspector enablement is automatically managed for all accounts covered by the policy, and member accounts cannot modify policy-managed scanning using Amazon Inspector API. 

 **Prerequisites** 
+  Your account must be part of an AWS Organizations organization. 
+  You must have permissions to create and manage organization policies in AWS Organizations. 
+  Trusted access for Amazon Inspector must be enabled in AWS Organizations. For instructions, see [Enabling trusted access for Amazon Inspector](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-inspector2.html#integrate-enable-ta-inspector2) in the *AWS Organizations User Guide*. 
+  The Amazon Inspector service-linked roles should exist in the management account. To create them, enable Amazon Inspector in the management account or run the following commands from the management account: 
  + `aws iam create-service-linked-role --aws-service-name inspector2.amazonaws.com`
  + `aws iam create-service-linked-role --aws-service-name agentless.inspector2.amazonaws.com`
+  An Amazon Inspector delegated administrator should be designated. 

**Note**  
 Without the service-linked Amazon Inspector roles of management account and delegated administrator, organization policies will enforce Amazon Inspector enablement, but member accounts will not be associated with the Amazon Inspector organization for centralized findings and account management. 

**To enable Amazon Inspector using AWS Organizations policies**

1.  Designate a delegated administrator for Amazon Inspector before creating organization policies to ensure member accounts are associated with the Amazon Inspector organization for centralized findings visibility. Sign in to the AWS Organizations management account, open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home), and follow the steps in [Designating a delegated administrator for your AWS organization](designating-admin.md#delegated-admin-proc). 
**Note**  
 We strongly recommend keeping your AWS Organizations Amazon Inspector delegated administrator account ID and Amazon Inspector designated delegated administrator account ID the same. If the AWS Organizations delegated administrator account ID differs from the Amazon Inspector delegated administrator account ID, Amazon Inspector prioritizes the Inspector-designated account ID. When the Amazon Inspector delegated administrator is not set but the AWS Organizations delegated administrator is set and the management account has the Amazon Inspector service-linked roles, Amazon Inspector automatically assigns the AWS Organizations delegated administrator account ID as the Amazon Inspector delegated administrator. 

1.  In the Amazon Inspector console, navigate to **General settings** from the management account. Under **Delegation policy**, choose **Attach statement**. In the **Attach policy statement** dialog, review the policy, select **I acknowledge that I have reviewed the policy and understand the permissions it grants**, and then choose **Attach statement**. 
**Important**  
 The management account must have the following permissions to attach the delegation policy statement:   
 Amazon Inspector permissions from the [AmazonInspector2FullAccess\_v2](https://docs.aws.amazon.com/inspector/latest/user/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonInspector2FullAccessV2) managed policy 
 AWS Organizations `organizations:PutResourcePolicy` permission from the [AWSOrganizationsFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.html) managed policy 
 If the `organizations:PutResourcePolicy` permission is missing, the operation fails with the error: `Failed to attach statement to the delegation policy`. 

1.  Next, create an Amazon Inspector AWS Organizations policy. From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  Configure vulnerability management policy. Provide **Details** with name and description (optional) for the policy. 

1.  On the Configure Inspector page, in the **Details** section, enter a name and a description for the policy. In the **Capability Selection**, do one of the following: 
   + Choose **Configure and enable all capabilities (Recommended)**. This turns on all of the Inspector capabilities including EC2, ECR, Lambda standard, Lambda code scan, and Code Security.
   + Choose **Select subset of capabilities**. Select any scan type capabilities that should be turned on.

1.  In the **Account selection** section, select one of the following options: 
   + Choose **All organizational units and accounts** if you want to apply the configuration to all organizational units and accounts.
   + Choose **Specific organizational units and accounts** if you want to apply the configuration to specific organizational units and accounts. If you choose this option, use the search bar or organizational structure tree to specify the organizational units and accounts where the policy will be applied.
   + Choose **No organizational units or accounts** if you do not want to apply the configuration to any organizational unit or account.

1.  In the **Regions** section, choose **Enable all Regions**, **Disable all Regions**, or **Specify Regions**. 
   + If you choose **Enable all Regions**, you can determine whether to automatically enable new Regions.
   + If you choose **Disable all Regions**, you can determine whether to automatically disable new Regions.
   + If you choose **Specify Regions**, you must choose which Regions you want to enable and disable.

   (Optional) For **Advanced settings**, refer to the guidance from AWS Organizations.

   (Optional) For **Resource tags**, add tags as key-value pairs to help you easily identify the configuration.

1.  Choose **Next**, review your changes, and then choose **Apply**. Your target accounts are configured based on the policy. The configuration status of your policy displays at the top of the Policies page. Each capability provides a status on whether it was configured or where there are deployment failures. For any failures, choose the link for the failure message to see more details. To view the effective policy at the account level, you can review the Organization tab on the Configurations page where you can choose an account. 

 When Amazon Inspector is enabled through organization policies, accounts covered by the policy cannot disable the policy-managed scan types through the Amazon Inspector API or console. For detailed information about what delegated administrators and member accounts can and cannot do under organization policies, see [Managing multiple accounts in Amazon Inspector with AWS Organizations](managing-multiple-accounts.md). 

------
#### [ Multi-account (without AWS Organizations policy) ]

**Note**  
 You must use the AWS Organizations management account to complete this procedure. Only the AWS Organizations management account can designate a delegated administrator. Permissions might be required to designate a delegated administrator. For more information, see [Permissions required to designate a delegated administrator](designating-admin.md#delegated-admin-permissions). 

 When you activate Amazon Inspector for the first time, Amazon Inspector creates the service linked role `AWSServiceRoleForAmazonInspector` for the account. For information about how Amazon Inspector uses service-linked roles, see [Using service-linked roles for Amazon Inspector](using-service-linked-roles.md). 

 **To designate a delegated administrator for Amazon Inspector** 

1.  Sign in to the AWS Organizations management account, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home). 

1.  Choose **Get started**. 

1.  Under **Delegated administrator**, enter the 12-digit ID of the AWS account you want to designate as the delegated administrator. 

1.  Choose **Delegate**, and then choose **Delegate** again. 

1.  (Optional) If you want to activate Amazon Inspector for the AWS Organizations management account, choose **Activate Amazon Inspector** under **Service permissions**. 

 When you designate a delegated administrator, [all scan types](https://docs.aws.amazon.com/inspector/latest/user/scanning-resources.html) are activated for the account by default. For information about the delegated administrator account,see [Understanding the delegated administrator account and member accounts in Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html). 

------