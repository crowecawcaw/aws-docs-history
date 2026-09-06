

# AWS Organizations in AWS GovCloud (US)
<a name="govcloud-organizations"></a>

AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Organizations differs
<a name="govcloud-ao-diffs"></a>

The following differences apply to AWS Organizations:
+ You must use AWS Organizations with all features enabled. The consolidated billing feature set is not available in this Region.
+ You must meet the U.S. regulatory requirements as described in [Signing Up for AWS GovCloud (US).](https://docs.aws.amazon.com/govcloud-us/latest/ug-west/getting-started-sign-up.html) 
+ Creating accounts from within AWS Organizations operates differently in the AWS GovCloud (US) Regions compared to commercial AWS Regions:
  + You start creating AWS GovCloud (US) accounts by calling the [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) action from the management account of the organization in the commercial Region. Calling account creation APIs from the AWS GovCloud (US) Regions is not available.
  + When you call the CreateGovCloudAccount API action, you create two accounts: a standalone account in the AWS GovCloud (US) Regions, and an associated account in the commercial Region for billing and support purposes. The account in the commercial Region is automatically a member of the organization whose credentials made the request. Both accounts are associated with the same email address.
  + After creating the standalone account in the AWS GovCloud (US) Regions, you can invite it to an organization in the AWS GovCloud (US) Regions only.
  + Accounts created in other AWS Regions cannot be members of an organization in the AWS GovCloud (US) Regions.
+ Organizations that you create in the AWS GovCloud (US) Regions are independent from organizations created in commercial AWS Regions.
+ The [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) API action is not available from the AWS GovCloud (US) Regions.
+ To sign in to the AWS Organizations console in the AWS GovCloud (US) Regions, you must be signed in from a AWS GovCloud (US) account.
+ To learn what AWS services are currently available for trusted access with AWS Organizations, check the list in the AWS Organizations console from the AWS GovCloud (US) Regions.
+ The following Organizations API operations work only when you specify the AWS GovCloud (US-West) Region:
  +  [DeletePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeletePolicy.html) 
  +  [DisablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisablePolicyType.html) 
  +  [EnablePolicyType](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html) 
  + Any operation that references the organization root, such as [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html).
+ Organization policies – You can use only the following policy types in an AWS GovCloud (US) organization:
  +  [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) 
  +  [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) 
  +  [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) 
  +  [Declarative policies for EC2](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ec2.html) 
  +  [Declarative policies for S3](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html) 
**Note**  
As a rule, you can create tag policies that reference only those resource types whose services are supported in the AWS GovCloud (US) Regions. However, you can use the following additional resource types in a tag policy even though the associated service is not yet supported in the AWS GovCloud (US) Regions:
    +  `chime:meeting` 
    +  `codepipeline:pipeline` 

Tag policy compliance reporting works only in the AWS GovCloud (US-West) Region.

The following tagging API operations work only when you specify the AWS GovCloud (US-West) Region:
+  [DescribeReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.html) 
+  [GetComplianceSummary](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.html) 
+  [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) 
+  [StartReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_StartReportCreation.html) 
  + You can’t create or use [backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html), [chat application policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html), or [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html).

## Creating Your Account
<a name="create-account"></a>

When you create accounts in the AWS GovCloud (US) Regions from AWS Organizations, an associated account in the commercial Region is automatically created for billing and support purposes. The account in the commercial Region and the account in the AWS GovCloud (US) Regions are linked. The account in the commercial Region is automatically a member of the organization whose credentials made the request, but the account in the AWS GovCloud (US) Regions is a standalone account until you invite it to an organization in that same Region.

Before creating accounts in the AWS GovCloud (US) Regions from AWS Organizations, make sure that you meet specific U.S. regulatory requirements as described in [Signing Up for AWS GovCloud.](https://docs.aws.amazon.com/govcloud-us/latest/ug-west/getting-started-sign-up.html) 

**To create an account in the AWS GovCloud (US) Regions from AWS Organizations**

1. From the management account of your organization in the commercial Region, sign in to the Organizations console at https://console.aws.amazon.com/organizations

1. From the Command Line Interface (CLI), Call the [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) API action.

**Accounts and roles are created as follows**
+ An account is created in the commercial Region and it is automatically a member of the organization whose credentials made the request.
+ A role is created in the new account in the commercial Region that the management account in this same Region can assume.
+ The account in the AWS GovCloud (US) Regions is created and it links to the associated account that was created at the same time in the commercial Region.
+ The account in the AWS GovCloud (US) Regions is a standalone account and is not yet a member of an organization.
+ A role is created in the AWS GovCloud (US) account that the AWS GovCloud (US) account that is linked to the management account in the commercial Region can assume.

## Inviting Accounts to an Organization
<a name="inviting-accounts"></a>

After creating a standalone account in the AWS GovCloud (US) Regions, you can invite it to organizations in the AWS GovCloud (US) Regions. You cannot invite accounts in the AWS GovCloud (US) Regions to organizations in other AWS Regions.

The following diagram explains account access works so that you can invite standalone accounts in the AWS GovCloud (US) Regions to an organization in the same Region.

![Diagram showing AWS Standard and GovCloud(US) regions with account pairing and IAM role access.](http://docs.aws.amazon.com/govcloud-us/latest/UserGuide/images/GovCloud-account-access.png)


**To invite an account in the AWS GovCloud (US) Regions to an Organization**

1. From the AWS GovCloud (US) account that’s associated with the management account of your organization in the commercial Region, assume the role of the AWS GovCloud (US) account you just created.

   In the above example, start from AWS GovCloud (US) Account 1 and assume the role that was created in AWS GovCloud (US) Account 2.

1. Follow the procedure described in [Sending Invitations to AWS Accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html#orgs_manage_accounts_invite-account) in the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to invite the account in the AWS GovCloud (US) Regions to the organization.

**To access the new account in the AWS GovCloud (US) Regions**

1. Sign in to the GovCloud account that is mapped to your commercial organization’s management account.

1. Assume the role into the newly-created AWS GovCloud (US) management account.

The role is automatically created when you create the account. By default, the role is named ** ` OrganizationAccountAccessRole ` ** but you can change it using the `RoleName` parameter when you call the `CreateGovCloudAccount` operation.

## Documentation
<a name="govcloud-ao-docs"></a>

 [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

## Export-controlled content
<a name="govcloud-ao-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.