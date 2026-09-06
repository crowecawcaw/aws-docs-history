

# Prerequisites
<a name="linking-prerequisites"></a>

The following topics list the prerequisites needed to link AWS Partner Central and AWS accounts. We recommend following the topics in the order listed.

**Note**  
Due to user interface, feature, and performance issues, account linking does not support Firefox Extended Support Release (Firefox ESR). We recommend using the regular version of Firefox or one of the chrome browsers.

**Topics**
+ [User roles and permissions](#people-roles)
+ [Select an AWS account for AWS Partner Central](#which-accounts-to-link)
+ [Granting IAM permissions](#grant-iam-permissions)
+ [Understanding the role permissions](#standard-role-permissions)
+ [Creating a permission set for single sign-on](#create-permission-set)

## User roles and permissions
<a name="people-roles"></a>

To link your AWS account with an AWS Partner Central account, you need people in the following roles:

**Identity and Access Management (IAM ) Administrator**  
Manages user permissions through IAM . Typically works in IT Security, Information Security, dedicated IAM teams, or Governance and Compliance organizations. Responsible for implementing IAM policies, configuring SSO solutions, handling compliance reviews, and maintaining role-based access control structures.

**AWS Partner Central Alliance Lead or Cloud Administrator**  
Your company's primary account administrator. This person must have a business development or business leadership role and legal authority to accept AWS Partner Network terms and conditions. The Alliance Lead can delegate account linking to a Partner Central user with the Cloud Admin user role.

## Select an AWS account for AWS Partner Central
<a name="which-accounts-to-link"></a>

Choose the AWS account you'll link to your AWS Partner Central profile. This applies whether you're registering as a new AWS partner or migrating from the legacy AWS Partner Network (APN) portal.

The AWS account you choose for AWS Partner Central will manage APN fee payments, solutions, and APN Customer Engagement (ACE) opportunity tracking. All APN resources, including ACE opportunities, opportunity history, and multi-partner opportunity invitations, are created in the account and cannot be transferred to other AWS accounts.

If you are an AWS Partner who has access to legacy Partner Central and needs to link an AWS account to pay APN fees or for Partner Central migration, **account linking is permanent after migration**. Before migration, you can unlink your account and select a different one. After migration, the linked account cannot be changed. All AWS Partner Network resources, including ACE opportunities, opportunity history, and multi-partner opportunity invitations, are permanently associated with this account.

Use the information in the following table to help decide which AWS account you should link or select for your AWS Partner Central account.

**Account selection checklist**  
**Your account must:**  
**Use a paid AWS account plan and be in good standing** — The account must use a paid AWS account plan (not Free Tier) and maintain good standing with AWS and APN. To upgrade to a paid account plan, see [Choosing an AWS Free Tier plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-free-tier.html) in the *AWS Billing User Guide*.
**Be owned by your company** — The account must be owned by your company and belong to an AWS organization that your company controls. It must **not** be owned by a distributor or another organization, or be a member account within a distributor's organization.
**Be able to onboard future AWS Partner Central users** — Users who need to create opportunities, solutions, and fund requests will need access to this account.
**Have a legal entity (tax) address matching your primary business location** — The account's billing address becomes the headquarters location for your partner profile. Choose an account with a billing address that matches your primary business location.
**Your account must not be:**  
**Developer or sandbox accounts** for code development and testing
**Personal accounts** for individual learning or projects
**Test accounts**
**Recommended not to choose:**  
**Management (or primary payer) accounts** for AWS Organizations


| AWS Partner scenario | Example | AWS account options | Considerations | 
| --- | --- | --- | --- | 
| Scenario 1: You own AWS account(s) managed by a third-party and you are not registered as an AWS Marketplace seller | AWS Partners working with AWS Distributor partners | **Option 1:** Create an AWS account and link to it.<br />**Option 2:** Link to an existing AWS account | **Option 1:**+  Is it acceptable to bill the APN fee to this account? The AWS Management account can pay the fee if the account is in an AWS Organization. <br />+  Is this where you want to access AWS Partner Network features and APIs? <br />**Option 2:**+  Same considerations as Option 1 <br />+  Is this an AWS Management, Production, Developer, or personal account? <br />+  Can you allow external personnel to access the account that manages AWS Partner Central engagements? <br />+  Is this account appropriate for managing Partner Central user access?  | 
| Scenario 2: You own AWS account(s) and are not registered as an AWS Marketplace seller | AWS Partners who don't transact through AWS Marketplace or partners in countries where AWS Marketplace is not available | Same as Scenario 1 | Same as Scenario 1 | 
| Scenario 3: You own AWS account(s) and are registered as an AWS Marketplace seller with a single Marketplace seller account | AWS Partners who have a consolidated product listing in a single country or operate globally | **Option 1:** Create and link to a new AWS account<br />**Option 2:** Link to an existing AWS account<br />**Option 3:** Link to an AWS Marketplace seller account | **Option 1:**+  Do you need access to AWS Marketplace features that require a linked Marketplace seller account? <br />+  Do you plan to join the AWS ISV Accelerate Program? See the [program requirements](https://aws.amazon.com/partners/programs/isv-accelerate/). <br />+  Do you need to share AWS Partner Central and Marketplace resources like opportunities, offers, solutions, and product listings? <br />+  Would it be better to designate an AWS Marketplace seller account with the most product listings or transactions as a primary Marketplace seller account? <br />+  Is it acceptable to bill the APN fee to this account? <br />**Option 2:**+  Same considerations as Option 1 <br />+  Is this an AWS Management, Production, Developer, or personal account? <br />+  Is this account appropriate for managing Partner Central user access? <br />**Option 3:**+  Same considerations as Options 1 and 2 <br />+  Do you plan to create additional AWS Marketplace seller accounts? If so, is it acceptable to designate the current Marketplace seller account as a primary Marketplace seller account?  | 
| Scenario 4: You own AWS account(s) and are registered as an AWS Marketplace seller with multiple seller accounts | AWS Partners who have multiple product listings under different lines of business or have to meet regulatory and compliance requirements | Same as Scenario 3 | Same as Scenario 3 | 

## Granting IAM permissions
<a name="grant-iam-permissions"></a>

The IAM policy listed in this section grants AWS Partner Central users limited access to a linked AWS account. The level of access depends on the IAM role assigned to the user. For more information about permission levels, refer to [Understanding the role permissions](#standard-role-permissions) later in this topic.

To create the policy, you must be an IT administrator responsible for an AWS environment. When finished, you must assign the policy to an IAM user or role.

The steps in this section explain how to use the IAM console to create the policy.

**Note**  
If you're an alliance lead or cloud admin, and you already have an IAM user or role with AWS administrator permissions, skip to [Linking AWS Partner Central and AWS accounts](linking-apc-aws-marketplace.md).

**To create the policy**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/).

1. Under **Access management**, choose **Policies**.

1. Choose **Create policy**, choose **JSON**, and add the following policy:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "CreatePartnerCentralRoles",
               "Effect": "Allow",
               "Action": [
                   "iam:CreateRole"
               ],
               "Resource": [
                   "arn:aws:iam::*:role/PartnerCentralRoleForCloudAdmin*",
                   "arn:aws:iam::*:role/PartnerCentralRoleForAce*",
                   "arn:aws:iam::*:role/PartnerCentralRoleForAlliance*"
               ]
           },
           {
               "Sid": "AttachPolicyToPartnerCentralCloudAdminRole",
               "Effect": "Allow",
               "Action": "iam:AttachRolePolicy",
               "Resource": "arn:aws:iam::*:role/PartnerCentralRoleForCloudAdmin*",
               "Condition": {
                   "ArnLike": {
                       "iam:PolicyARN": [
                           "arn:aws:iam::*:policy/PartnerCentralAccountManagementUserRoleAssociation",
                           "arn:aws:iam::*:policy/AWSPartnerCentralFullAccess",
                           "arn:aws:iam::*:policy/AWSMarketplaceSellerFullAccess"
                       ]
                   }
               }
           },
           {
               "Sid": "AttachPolicyToPartnerCentralAceRole",
               "Effect": "Allow",
               "Action": [
                   "iam:AttachRolePolicy"
               ],
               "Resource": "arn:aws:iam::*:role/PartnerCentralRoleForAce*",
               "Condition": {
                   "ArnLike": {
                       "iam:PolicyARN": [
                           "arn:aws:iam::*:policy/AWSPartnerCentralOpportunityManagement",
                           "arn:aws:iam::*:policy/AWSMarketplaceSellerOfferManagement"
                       ]
                   }
               }
           },
           {
               "Sid": "AttachPolicyToPartnerCentralAllianceRole",
               "Effect": "Allow",
               "Action": [
                   "iam:AttachRolePolicy"
               ],
               "Resource": "arn:aws:iam::*:role/PartnerCentralRoleForAlliance*",
               "Condition": {
                   "ArnLike": {
                       "iam:PolicyARN": [
                           "arn:aws:iam::*:policy/AWSPartnerCentralFullAccess",
                           "arn:aws:iam::*:policy/AWSMarketplaceSellerFullAccess"
                       ]
                   }
               }
           },
           {
               "Sid": "AssociatePartnerAccount",
               "Effect": "Allow",
               "Action": [
                   "partnercentral-account-management:AssociatePartnerAccount"
               ],
               "Resource": "*"
           },
           {
               "Sid": "SellerRegistration",
               "Effect": "Allow",
               "Action": [
                   "aws-marketplace:ListChangeSets",
                   "aws-marketplace:DescribeChangeSet",
                   "aws-marketplace:StartChangeSet",
                   "aws-marketplace:ListEntities",
                   "aws-marketplace:DescribeEntity"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Choose **Next**.

1. Under **Policy details**, in the **Policy name** box, enter a name for the policy and an optional description.

1. Review the policy permissions, add tags as needed, and then choose **Create policy**.

1. Attach your IAM user or role to the policy. For information on attaching, refer to [Adding IAM identity permissions (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) in the *IAM User Guide*.

## Understanding the role permissions
<a name="standard-role-permissions"></a>

After the IT administrator completes the steps in the previous section, alliance leads and others in AWS Partner Central can assign security policies and map user roles. The following table lists and describes the standard roles created during account linking, and the tasks available to each role.


|  **Standard IAM role**  |  **AWS Partner Central managed policies used**  |  **Can do**  |  **Cannot do**  | 
| --- | --- | --- | --- | 
| Cloud admin  |  +  [PartnerCentralAccountManagementUserRoleAssociation](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/PartnerCentralAccountManagementUserRoleAssociation.html) <br />+  [AWSPartnerCentralFullAccess:](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.html) <br />+  [AWSMarketplaceSellerFullAccess:](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.html)   |  +  Map and assign IAM roles to AWS Partner Central users. <br />+  Complete the same tasks as alliance and ACE teams.   |   | 
| Alliance team |  +  [AWSPartnerCentralFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.html) <br />+  [AWSMarketplaceSellerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.html)   |  +  Full access to all seller operations on AWS Marketplace, including the AWS Marketplace Management Portal. You can also manage the Amazon EC2 AMI used in AMI-based products. <br />+  Link AWS customer engagement opportunities with AWS Marketplace private offers. <br />+  Associate APN solutions with AWS Marketplace product listings. <br />+  Access the Partner Analytics dashboard.   | Map or assign IAM roles to AWS Partner Central users. Only alliance leads and cloud admins map or assign roles. | 
| ACE team  |  +  [AWSMarketplaceSellerOfferManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerOfferManagement.html) <br />+  [AWSPartnerCentralOpportunityManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement.html)    |  +  Create AWS Marketplace private offers. <br />+  Link AWS customer engagement opportunities with AWS Marketplace private offers.    |  +  Map or assign IAM roles to AWS Partner Central users. Only alliance leads and cloud admins can map or assign roles. <br />+  Use all the AWS Marketplace tools and features.  <br />+  Use the Partners Analytics dashboard.   | 

## Creating a permission set for single sign-on
<a name="create-permission-set"></a>

The following steps explain how to use the IAM Identity Center to create a permission set that enables single sign-on for accessing AWS Partner Central.

For more information about permission sets, refer to [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.

1. Sign in to the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon). 

1. Under **Multi-account permissions**, choose **Permission sets**. 

1. Choose **Create permission set**.

1. On the **Select permission set type** page, under **Permission set type**, choose **Custom permission set**, then choose **Next**. 

1. Do the following:

   1. On the **Specify policies and permission boundary** page, choose the types of IAM policies that you want to apply to the permission set.

      By default, you can add any combination of up to 10 AWS managed policies and customer managed policies to your permission set. IAM sets this quota. To raise it, request an increase to the IAM quota **Managed policies attached to an IAM role** in the Service Quotas console in each AWS account where you want to assign the permission set.

   1. Expand **Inline policy** to add custom JSON-formatted policy text. Inline policies don't correspond to existing IAM resources. To create an inline policy, enter custom policy language in the provided form. IAM Identity Center adds the policy to the IAM resources that it creates in your member accounts. For more information, see [Inline policies](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetcustom.html#permissionsetsinlineconcept). 

   1. Copy and paste the JSON policy from [AWS Partner Central and AWS Account Linking pre-requisite](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html#linking-prerequisites) 

1. On the **Specify permission set details** page, do the following: 

   1. Under **Permission set name**, type a name to identify this permission set in IAM Identity Center. The name that you specify for this permission set appears in the AWS access portal as an available role. Users sign into the AWS access portal, choose an AWS account, and then choose the role. 

   1. (Optional) You can also type a description. The description appears in the IAM Identity Center console only, not the AWS access portal. 

   1. (Optional) Specify the value for **Session duration**. This value determines the length of time that a user can be logged on before the console logs them out of their session. For more information, see [Set session duration for AWS accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html). 

   1. (Optional) Specify the value for **Relay state**. This value is used in the federation process to redirect users within the account. For more information, refer to [Set relay state for quick access to the AWS Management Console](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtopermrelaystate.html). 
**Note**  
You must use an AWS Management Console URL for the relay state. For example: `https://console.aws.amazon.com/ec2/` 

   1. Expand **Tags (optional)**, choose **Add tag**, and then specify values for **Key** and **Value (optional)**. 

      For information about tags, refer to [Tagging AWS IAM Identity Center resources](https://docs.aws.amazon.com/singlesignon/latest/userguide/tagging.html). 

   1. Choose **Next**.

1. On the **Review and create** page, review the selections that you made, and then choose **Create**.

   By default, when you create a permission set, the permission set isn't provisioned (used in any AWS accounts). To provision a permission set in an AWS account, you must assign IAM Identity Center access to users and groups in the account, and then apply the permission set to those users and groups. For more information, refer to [Assign user access to AWS accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/assignusers.html) in the *AWS IAM Identity Center User Guide*. 