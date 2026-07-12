The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Access for the Channel API

Access control and permissions are managed by AWS Identity and Access Management (IAM). This section provides
guidance for configuring the necessary permissions to interact with the AWS Partner Central Channel API.

## Channel management account setup

Channel management features on AWS Partner Central require IAM roles to be deployed in two types of AWS accounts:

1. [AWS Partner Central linked AWS account](../getting-started/account-linking.md "../getting-started/account-linking.md"):

This is the AWS account associated with your AWS Partner Network and Partner Central account. There is only one AWS Partner Central linked AWS account per partner. As a one time set up activity, you will create an IAM role in this AWS account using a Partner Central channel managed policy. 2. [Program management account AWS account](../APIReference/working-with-channel-management.md#working-with-program-management-accounts "../APIReference/working-with-channel-management.md#working-with-program-management-accounts"):

This is the AWS account used as a Bill-Transfer account to manage billing and payment for end customer consumption. This AWS account is reported as a program management account in AWS Partner Central channel management. You may have multiple program management accounts, and you will need to create an IAM role in each AWS account you report as a program management account.

For each AWS account type, you will need to associate different IAM roles with specific permission and trust policies.

### Access for the AWS Partner Central linked AWS account

Within the AWS Partner Central linked AWS account, create an IAM role to manage channel resources, which will be granted to Partner Central users. This IAM role allows users to view and manage channel management resources on AWS Partner Central. The role name must start with `PartnerCentralRoleFor`, and the recommended name is `PartnerCentralRoleForChannel`. To configure the role, complete the following:

- Add the following custom trust policy to allow AWS Partner Central cloud admins and alliance leads to [map IAM roles to Partner Central users](../getting-started/channel-management-user-mapping.md "../getting-started/channel-management-user-mapping.md"):

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "partnercentral-account-management.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- Associate the [`AWSPartnerCentralChannelManagement`](../getting-started/managed-policies.md#security-iam-awsmanpol-AWSPartnerCentralChannelManagement "../getting-started/managed-policies.md#security-iam-awsmanpol-AWSPartnerCentralChannelManagement") managed policy to the `PartnerCentralRoleForChannel` role.

### Access for the program management account AWS account(s)

Within each AWS account reported as a program management account in AWS Partner Central, create the following IAM roles, with the required names below:

- `PartnerCentralChannelHandshakeApprovalManagement`: Utilize this role to manage handshakes between Partner Central and your program management AWS account. This IAM role can be utilized to respond to activate your program management accounts in AWS Partner Central. When creating this role, associate the `AWSPartnerCentralChannelHandshakeApprovalManagement` managed policy.
- `PartnerCentralChannelBillingTransferReadOnly`: Utilize this cross-account role to enable visibility to billing transfer status from AWS Partner Central. This role will share billing transfer status from your AWS account to AWS Partner Central to centrally view billing transfer status. If this role is created, users in AWS Partner Central can view billing transfer status in AWS Partner Central. However, this role does not grant AWS Partner Central users permission to access billing transfers in AWS Billing and Cost Management console.

  - Trust policy:

    - Within the JSON below, replace the `{PartnerCentralLinkedAccountID}` with your actual AWS Partner Central linked AWS account 12-digit ID when creating the role.

    ```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": "arn:aws:iam::{PartnerCentralLinkedAccountId}:root"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
    ```

  - Permission policy:

  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "BillingTransferReadOnly",
        "Effect": "Allow",
        "Action": [
          "organizations:DescribeResponsibilityTransfer",
          "organizations:ListHandshakesForOrganization",
          "organizations:ListInboundResponsibilityTransfers",
          "organizations:ListOutboundResponsibilityTransfers"
      ],
        "Resource": "*"
      }
    ]
  }
  ```

- `PartnerCentralChannelBillingTransferManagement` (optional): Utilize this cross-account role to enable creation and management of billing transfers from AWS Partner Central. This role will enable AWS Partner Central users accessing the IAM role containing `AWSPartnerCentralChannelManagement` managed policy to manage billing transfers in program management account AWS account. Using this cross-account role, AWS Partner Central users will be able to access and manage billing transfers in AWS Billing and Cost Management console using the "Manage in AWS Billing" button in AWS Partner Central channel management.

  - Trust policy:

    - Within the JSON below, replace the `{PartnerCentralLinkedAccountID}` with your actual AWS Partner Central linked AWS account 12-digit ID when creating the role.

    ```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": "arn:aws:iam::{PartnerCentralLinkedAccountId}:root"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
    ```

  - Permission policy:

  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "BillingTransferManagement",
        "Effect": "Allow",
        "Action": [
          "billingconductor:CreateBillingGroup",
          "billingconductor:ListPricingPlans",
          "organizations:AcceptHandshake",
          "organizations:CancelHandshake",
          "organizations:DeclineHandshake",
          "organizations:DescribeResponsibilityTransfer",
          "organizations:InviteOrganizationToTransferResponsibility",
          "organizations:ListHandshakesForAccount",
          "organizations:ListHandshakesForOrganization",
          "organizations:ListInboundResponsibilityTransfers",
          "organizations:ListOutboundResponsibilityTransfers",
          "organizations:TerminateResponsibilityTransfer",
          "organizations:UpdateResponsibilityTransfer"
      ],
        "Resource": "*"
      }
    ]
  }
  ```

## Using AWS managed policies

AWS provides managed policies that grant the required
permissions to interact with the Channel API. To provide the necessary access to
manage all channel resources, attach the
`AWSPartnerCentralChannelManagement` policy to your IAM
identities. To provide necessary access to view and respond to channel handshake requests, attach the `AWSPartnerCentralChannelHandshakeApprovalManagement` policy to your IAM identities. For more information, see
[AWS managed policies for AWS Partner Central users](../getting-started/managed-policies.md "../getting-started/managed-policies.md").

### AWSPartnerCentralChannelManagement policy

This policy grants full access to Partner Central channel management actions.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ChannelManagement",
      "Effect": "Allow",
      "Action": [
        "partnercentral:CreateProgramManagementAccount",
        "partnercentral:UpdateProgramManagementAccount",
        "partnercentral:DeleteProgramManagementAccount",
        "partnercentral:ListProgramManagementAccounts",
        "partnercentral:GetProgramManagementAccount",
        "partnercentral:CreateRelationship",
        "partnercentral:UpdateRelationship",
        "partnercentral:DeleteRelationship",
        "partnercentral:GetRelationship",
        "partnercentral:ListRelationships",
        "partnercentral:CreateChannelHandshake",
        "partnercentral:AcceptChannelHandshake",
        "partnercentral:RejectChannelHandshake",
        "partnercentral:CancelChannelHandshake",
        "partnercentral:ListChannelHandshakes"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "partnercentral:Catalog": [
            "AWS",
            "Sandbox"
          ]
        }
      }
    },
    {
      "Sid": "ChannelBillingTransferRoleAccess",
      "Effect": "Allow",
      "Action": [
        "sts:AssumeRole"
      ],
      "Resource": [
        "arn:aws:iam::*:role/PartnerCentralChannelBillingTransferManagement",
        "arn:aws:iam::*:role/PartnerCentralChannelBillingTransferReadOnly"
      ]
    },
    {
      "Sid": "TaggingAccess",
      "Effect": "Allow",
      "Action": [
        "partnercentral:TagResource",
        "partnercentral:UntagResource",
        "partnercentral:ListTagsForResource"
      ],
      "Resource": [
        "arn:aws:partnercentral:*:*:catalog/*/program-management-account/*",
        "arn:aws:partnercentral:*:*:catalog/*/channel-handshake/*"
      ],
      "Condition": {
        "StringEquals": {
          "partnercentral:Catalog": [
            "AWS",
            "Sandbox"
          ]
        }
      }
    }
  ]
}
```

### AWSPartnerCentralChannelHandshakeApprovalManagement policy

This policy grants access to view and respond to channel handshake requests. This policy should be applied to roles in the AWS accounts receiving channel handshake requests.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ChannelHandshakeManagement",
      "Effect": "Allow",
      "Action": [
        "partnercentral:ListChannelHandshakes",
        "partnercentral:AcceptChannelHandshake",
        "partnercentral:RejectChannelHandshake"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "partnercentral:Catalog": [
            "AWS",
            "Sandbox"
          ]
        }
      }
    }
  ]
}
```

## Assigning policies to IAM roles and users

Follow these steps to assign policies to IAM roles and users:

1. Sign in to the AWS Management Console.
2. Navigate to the IAM service.
3. Select roles or users, and choose the IAM role or user to which you want to
   attach a policy.
4. Attach the
   `AWSPartnerCentralChannelManagement` policy or your
   custom policy to the selected IAM role or user.

For more information, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

## Managing permissions using condition keys

Condition keys in IAM policies provide resource-level permissions for when to
enforce statement policies. You can use condition keys to specify conditions that
dictate when certain permissions are allowed or denied.

For more information, see [IAM JSON policy elements: Condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md").

Condition keys overview| Condition key | Description | Applicable actions | Valid values |
| --- | --- | --- | --- |
| partnercentral:Catalog | Filters access by the type of the associated catalog entity | All Channel Management actions | AWS, Sandbox |
| partnercentral:ChannelHandshakeType | Filters access based on the type of channel handshake | CreateChannelHandshake, AcceptChannelHandshake, RejectChannelHandshake, CancelChannelHandshake, ListChannelHandshakes | PROGRAM\_MANAGEMENT\_ACCOUNT, START\_SERVICE\_PERIOD, REVOKE\_SERVICE\_PERIOD |

## Summary of required permissions

Summary of required permissions| Action | Description |
| --- | --- |
| partnercentral:CreateProgramManagementAccount | allows creating program management accounts |
| partnercentral:UpdateProgramManagementAccount | allows updating program management accounts |
| partnercentral:DeleteProgramManagementAccount | allows deleting program management accounts |
| partnercentral:ListProgramManagementAccounts | allows listing program management accounts |
| partnercentral:GetProgramManagementAccount | allows retrieving program management account details |
| partnercentral:CreateRelationship | allows creating relationships |
| partnercentral:UpdateRelationship | allows updating relationships |
| partnercentral:DeleteRelationship | allows deleting relationships |
| partnercentral:GetRelationship | allows retrieving relationship details |
| partnercentral:ListRelationships | allows listing relationships |
| partnercentral:CreateChannelHandshake | allows creating channel handshakes |
| partnercentral:AcceptChannelHandshake | allows accepting channel handshakes |
| partnercentral:RejectChannelHandshake | allows rejecting channel handshakes |
| partnercentral:CancelChannelHandshake | allows canceling channel handshakes |
| partnercentral:ListChannelHandshakes | allows listing channel handshakes |
