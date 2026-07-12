The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Access for the Benefits API

Access control and permissions are managed by AWS Identity and Access Management (IAM). This section provides
guidance for configuring the necessary permissions to interact with the Benefits API.

## Prerequisites

Before configuring permissions, ensure that your AWS account is linked to and
that you created the necessary IAM roles and users. For more information, see [Setup and authentication](setup-authentication.md "setup-authentication.md").

## Using AWS managed policies

AWS provides managed policies that grant the required
permissions to interact with the Benefits API. To provide the necessary access to
manage benefits resources, attach the
`AWSPartnerCentralFullAccess` policy to your IAM
identities. For more information, see [AWS managed policies for users](../getting-started/managed-policies.md "../getting-started/managed-policies.md").

## Assigning policies to IAM roles and users

Follow these steps to assign policies to IAM roles and users:

1. Sign in to the AWS Management Console.
2. Navigate to the IAM service.
3. Select roles or users, and choose the IAM role or user to which you want to
   attach a policy.
4. Attach the
   `AWSPartnerCentralFullAccess` policy to the selected IAM role or user.

For more information, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

## Managing permissions using condition keys

Condition keys in IAM policies provide resource-level permissions for when to
enforce statement policies. You can use condition keys to specify conditions that
dictate when certain permissions are allowed or denied.

For more information, see [IAM JSON policy elements: Condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md").

Condition keys overview| Condition key | Description | Applicable actions | Valid values |
| --- | --- | --- | --- |
| partnercentral:Catalog | filters access by the type of the associated catalog entity | all actions | AWS, sandbox |

## Summary of required permissions

Summary of required permissions| Action | Description |
| --- | --- |
| partnercentral:AmendBenefitApplication | allows amending benefit applications |
| partnercentral:AssociateBenefitApplicationResource | allows associating resources with benefit applications |
| partnercentral:CancelBenefitApplication | allows canceling benefit applications |
| partnercentral:CreateBenefitApplication | allows creating benefit applications |
| partnercentral:DisassociateBenefitApplicationResource | allows disassociating resources from benefit applications |
| partnercentral:GetBenefit | allows retrieving benefit details |
| partnercentral:GetBenefitAllocation | allows retrieving benefit allocation details |
| partnercentral:GetBenefitApplication | allows retrieving benefit application details |
| partnercentral:ListBenefitAllocations | allows listing benefit allocations |
| partnercentral:ListBenefitApplications | allows listing benefit applications |
| partnercentral:ListBenefits | allows listing benefits |
| partnercentral:RecallBenefitApplication | allows recalling benefit applications |
| partnercentral:SubmitBenefitApplication | allows submitting benefit applications |
| partnercentral:UpdateBenefitApplication | allows updating benefit applications |
