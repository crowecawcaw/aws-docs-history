

# AWS Control Tower in AWS GovCloud (US)
<a name="govcloud-controltower"></a>

 AWS Control Tower offers a straightforward way to set up and govern an AWS multi-account environment, following prescriptive best practices. AWS Control Tower orchestrates the capabilities of several other AWS services, including AWS Organizations, AWS Service Catalog, and IAM Identity Center, to build a landing zone in less than an hour. Resources are set up and managed on your behalf.

You can utilize AWS Control Tower with workloads that require FedRAMP High categorization level in the AWS GovCloud (US) Regions. AWS Control Tower is [in scope for numerous compliance programs and standards](https://aws.amazon.com/compliance/services-in-scope/), including HIPAA (Health Insurance Portability and Accountability Act), PCI DSS (Payment Card Industry – Data Security Standard), ISO (International Organization for Standardization), SOC 1, 2, and 3 (System and Organization Controls). To learn more, visit the [AWS Control Tower homepage](https://aws.amazon.com/controltower/) or see the [AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html).

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Control Tower differs
<a name="govcloud-diffs-35"></a>

The following differences apply to AWS Control Tower:

**Overview of differences**
+ As in the commercial Region, you must use AWS Control Tower with all features enabled for AWS Organizations in AWS GovCloud (US) Regions. However, the consolidated billing feature set is not available.
+ You must meet the U.S. regulatory requirements as described in [Signing Up for AWS GovCloud (US).](https://docs.aws.amazon.com/govcloud-us/latest/ug-west/getting-started-sign-up.html) 
+ Organizations that you create in the AWS GovCloud (US) Regions are independent from organizations created in commercial AWS Regions.
+ Creating accounts from within AWS Control Tower operates differently in the AWS GovCloud (US) Regions compared to commercial AWS Regions:
  + You start creating AWS GovCloud (US) accounts by calling the [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) action from the management account of the landing zone in the commercial Region. Calling account creation APIs from the AWS GovCloud (US) Regions is not available.
  + When you call the `CreateGovCloudAccount` API action, you create *two accounts*: a standalone account in the AWS GovCloud (US) Regions, and an associated account in the commercial Region for billing and support purposes. The account in the commercial Region automatically becomes a member of the organization whose credentials made the request. Both accounts are associated with the same email address.
  + After you create the standalone account in the AWS GovCloud (US) Regions, you can invite it to an organization in the AWS GovCloud (US) Regions only.
  + Accounts created in other AWS Regions cannot be members of an organization in the AWS GovCloud (US) Regions.
+ To learn what AWS services are currently available for trusted access with AWS Control Tower, check the list in the AWS Control Tower console from the AWS GovCloud (US) Regions.

For more information about AWS Control Tower, see the [AWS Control Tower Documentation](https://docs.aws.amazon.com/servicecatalog/index.html).

**Feature-level differences**
+  **Inability to create accounts in AWS GovCloud (US) ** 

   AWS Control Tower does not support the ability to create accounts within AWS GovCloud (US). The AWS Organizations **CreateGovCloudAccount** API is available in the Commercial Region (US East (N. Virginia)) only. Therefore, AWS Control Tower cannot programmatically create accounts with Account Factory, nor during Landing Zone setup. This difference affects setup regarding the creation of the Audit account and the Log Archive account.
+  **Must enroll existing AWS GovCloud (US) accounts for Audit and Log Archive** 

   AWS Control Tower in AWS GovCloud (US) requires you to bring your own, existing Audit and Log Archive accounts during Landing Zone setup. These accounts must exist in your AWS GovCloud (US) organization before you enroll them. AWS Control Tower supports single account enrollment only, for Account Factory.
+  **Changes for Account Factory** 

  The **Create account** feature in Account Factory is removed in AWS GovCloud (US) Regions. During the **Create account** workflow, you will see an error if the member account does not already exist.
+  **Home Region** 

  You are redirected to the appropriate AWS GovCloud (US) home Region (AWS GovCloud (US-West) or AWS GovCloud (US-East)) when running AWS Control Tower in the AWS GovCloud (US) console.
+  **Verifying an account email address** 

  An account in the commercial Region and the associated account in the AWS GovCloud (US) Region share an email adress. AWS Control Tower cannot verify account email addresses independently.
+  **Control changes** 

  Certain controls include functionality that has no effect in AWS GovCloud (US) Regions, based on other underlying differences. No error messages are reported for the differences in control functionality. These controls include:
  +  [Disallow cross-region networking for Amazon EC2](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-controls.html#prevent-cross-region-networking) 
  +  [Disallow delete actions on Amazon S3 buckets without MFA](https://docs.aws.amazon.com/controltower/latest/controlreference/elective-guardrails.html#disallow-s3-delete-mfa) 
  +  [Disallow changes to replication configuration for Amazon S3 buckets](https://docs.aws.amazon.com/controltower/latest/controlreference/elective-guardrails.html#disallow-s3-ccr) 
  +  [Disallow creation of access keys for the root user](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-guardrails.html#disallow-root-access-keys) 
  +  [Disallow actions as a root user](https://docs.aws.amazon.com/controltower/latest/controlreference/strongly-recommended-guardrails.html#disallow-root-auser-actions) 
  +  [Disallow the specified actions except in Regions with status Governed by AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-guardrails.html#primary-region-deny-policy) 
+  **Marketplace** 

  The Marketplace link in the left navigation of the AWS Control Tower console is not available.
+  ** Security Hub CSPM controls** 

  Some controls in the Security Hub CSPM standard named **Service-Managed Standard: AWS Control Tower ** are not available in AWS GovCloud (US) Regions. For a complete list of these controls by Region, see [Security Hub CSPM](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ash.html).
+  ** AWS Control Tower Account Factory for Terraform (AFT)** cannot be deployed by new AFT customers in AWS GovCloud (US) Regions, because AWS CodeStar Connections is not available to connect to a third-party version control system (VCS):
+  **Resource control policy (RCP) controls** are not available.
+  **Preventive and detective controls that support digital sovereignty** 

  Preventive and detective controls, including enhanced Region deny capabilities, are available to help meet digital sovereignty requirements. These controls can detect resource changes for data residency, granular access restriction, encryption, and resiliency capabilities. View these controls under a digital sovereignty group in the AWS Control Tower console. For more information, see [Digital sovereignty controls](https://docs.aws.amazon.com/controltower/latest/userguide/digital-sovereignty-controls.html).
+  **OU Region deny control** 

  The preventive control `CT.MULTISERVICE.PV.1`, commonly called the **OU Region deny** control, is available in AWS GovCloud (US) Regions. It allows you to deny access to any of the AWS GovCloud (US) Regions.
+  **Support for FedRamp Levels 4 and 5** 

   AWS Control Tower is authorized for Department of Defense Cloud Computing Security Requirements Guide Impact Levels 4 and 5 (DoD SRG IL4 and IL5) in the AWS GovCloud (US-East and US-West) Regions.

  This capability builds on the existing FedRamp High categorization level, as well as numerous compliance programs and standards, including HIPAA (Health Insurance Portability and Accountability Act), PCI DSS (Payment Card Industry – Data Security Standard), ISO (International Organization for Standardization), SOC 1, 2, and 3 (System and Organization for Standardization), SOC 1, 2, and 3 (System and Organization Controls). To learn more, visit the AWS Control Tower homepage or see the [AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html).
+  **Certain API permissions unavailable** 

  If your workload operates in AWS and AWS GovCloud (US) Regions, you may notice a difference in behavior, for the same policy. The `controltower:EnableGuardrail` and `controltower:DisableGuardrail` permissions don’t exist in AWS GovCloud (US) Regions, and so they won’t have any effect in your policies. Use `controltower:EnableControl` and `controltower:DisableControl` permissions instead to control access to **EnableControl** and **DisableControl** APIs.

## Creating your accounts
<a name="create-account-127"></a>

 AWS Control Tower must be set up in the commercial Region before you can sign in to the AWS Control Tower management account to create AWS Control Tower accounts. When you create an account in the AWS GovCloud (US) Regions from AWS Control Tower, an associated account in the commercial Region is created for billing and support purposes, automatically. The account in the commercial Region and the account in the AWS GovCloud (US) Regions are linked.

The account in the commercial Region is a member of the organization whose credentials made the request, automatically, but the account in the AWS GovCloud (US) Regions is a standalone account until you invite it to an organization in that same Region.

Before creating accounts in the AWS GovCloud (US) Regions from AWS Control Tower, make sure that you meet specific U.S. regulatory requirements as described in [Signing Up for AWS GovCloud (US).](https://docs.aws.amazon.com/govcloud-us/latest/ug-west/getting-started-sign-up.html) 

For more information about getting started with AWS GovCloud (US) see [AWS GovCloud (US) Sign Up](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-sign-up.html).

**To create an account in the AWS GovCloud (US) Regions from AWS Control Tower**

1. From the management account of your organization in the commercial Region, sign in and authenticate to the AWS Control Tower console at [https://console.aws.amazon.com/controltower](https://console.aws.amazon.com/organizations) 

1. While signed into your management account in a commercial Region, with AWS CloudShell, or by means of a CLI script, you can call the the [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) API action.

1. Go to your AWS GovCloud (US) Region and invite the new standalone account to an organization.

**Accounts and roles are created as follows**
+ An account is created in the commercial Region and it automatically is a member of the organization whose credentials made the request.
+ A role is created in the new account in the commercial Region, which the management account in this same Region can assume.
+ The account in the AWS GovCloud (US) Regions is created, and it links to the associated account that was created at the same time in the commercial Region.
+ The account in the AWS GovCloud (US) Regions is a standalone account. It is not yet a member of an organization.
+ The AWS GovCloud (US) account, which is linked to the management account in the commercial Region, can assume the role that is created during setup of that AWS GovCloud (US) account.

## Inviting accounts to an organization
<a name="inviting-accounts-128"></a>

After creating a standalone account in the AWS GovCloud (US) Regions, you can invite it to an organization in the AWS GovCloud (US) Regions. You cannot invite accounts in the AWS GovCloud (US) Regions to organizations in other AWS Regions.

The following diagram shows how account access works, so that you can invite standalone accounts in the AWS GovCloud (US) Regions to an organization in the same Region.

![Diagram showing AWS Standard and GovCloud(US) regions with account pairing and IAM role access.](http://docs.aws.amazon.com/govcloud-us/latest/UserGuide/images/GovCloud-account-access.png)


**Example: Account 1 invites Account 2 in the AWS GovCloud (US) Regions to an organization**

1. In this example, ** AWS GovCloud (US) Account 1** is the AWS GovCloud (US) account that’s associated with the management account of your organization in the commercial Region. ** AWS GovCloud (US) Account 2** is going to become a member account in the organization of ** AWS GovCloud (US) Account 1**.
   + Sign into ** AWS GovCloud (US) Account 1**. Assume the administrative role of the AWS GovCloud (US) account you just created.
   + Send an invitation to **Account 2**. Sign out of **Account 1**.
   + Sign into and assume the IAM role that was created in ** AWS GovCloud (US) Account 2**.
   + Accept the invitation.

1. Alternatively, another ** AWS GovCloud (US) Account 2** user can sign into **Account 2** with the IAM user credentials you provided, then view and accept the invitation.

For more information, see the procedure described in [Sending Invitations to AWS Accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html#orgs_manage_accounts_invite-account) in the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to invite the account in the AWS GovCloud (US) Regions to the AWS GovCloud (US) organization.

## Setting up your landing zone
<a name="govcloud-landing-zone-setup-overview"></a>

Here’s an overview and a recommended sequence of steps for setting up an AWS Control Tower landing zone in AWS GovCloud (US) Regions. It is slightly different than the process for commercial Regions, because of the way you must create accounts.

**AWS Control Tower setup process overview**

1.  **In the commercial Region**: Create the two AWS accounts you’ll require in AWS GovCloud (US), which will become log archive and audit accounts for your AWS GovCloud (US) organization.

1.  **In the AWS GovCloud (US) home Region**: Create an organization in your AWS GovCloud (US) home Region, or choose which organization and Region you’ll require for your AWS Control Tower landing zone. In AWS GovCloud (US) Regions, you can deploy AWS Control Tower in an existing AWS GovCloud (US) organization.

1.  **In the AWS GovCloud (US) home Region**: Invite the two new accounts into your selected AWS GovCloud (US) organization. Go to those accounts and accept the invitations.

1.  **In the AWS GovCloud (US) home Region**: Follow the procedure to set up AWS Control Tower in an existing organization. Specify the two existing accounts, which you’ve already created in the first step and just invited to your organization, as your audit and log archive accounts.

1.  **In the AWS GovCloud (US) home Region**: Use AWS Control Tower to set up OUs in your landing zone, for your AWS Control Tower workloads in AWS GovCloud (US) Regions. (Use AWS Organizations to set up any other required organizations. AWS Control Tower supports one landing zone per organization.)

1.  **In the commercial Region**: Create the necessary member accounts to run your AWS GovCloud (US) Regions workloads.

1.  **In the AWS GovCloud (US) home Region**: Invite each account that you created in the previous step into its proper organization and OU, presumably into the organization in which you have already set up the AWS Control Tower landing zone.

After you’ve performed these tasks, it’s a good idea to check the guardrails (also called controls) that are enabled on your OUs, and apply any optional controls that are applicable to your business requirements.

## Documentation
<a name="govcloud-docs-74"></a>
+  [AWS Control Tower documentation](https://docs.aws.amazon.com/controltower/index.html) 

## Export-controlled content
<a name="govcloud-itar-content-113"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ AWS Control Tower metadata is not permitted to contain export-controlled data. This metadata includes all of the configuration data that you enter when creating and maintaining your AWS Control Tower landing zone and AWS accounts, including AWS account names and email addresses, or Organizational Unit names.