# Mapping IAM roles to a channel management user

This section explains how to map AWS Partner Central AWS Identity and Access Management (IAM) roles to your channel management service users on AWS Partner Central. This IAM role mapping is required to enable Partner Central users to access Partner Central Channel Management features. Mapping enables Partner Central Channel Management users to perform actions on the AWS Partner Central AWS account. Selecting an IAM role to access AWS Partner Central Channel APIs by Partner Central users enables features such as Channel Program Management Account and Relationship management.

Before mapping, you must first complete the following:

- [Link your AWS Partner Central account to a Partner Central linked AWS account.](linking-apc-aws-marketplace.md "linking-apc-aws-marketplace.md")
- [Create IAM roles in the AWS Partner Central linked AWS account.](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md")
- While creating IAM roles, add the `AWSPartnerCentralChannelManagement` managed policy to the role to grant AWS Partner Central users permissions to perform channel management actions. For more information, refer to [Managed policies for AWS Partner Central users.](managed-policies.md "managed-policies.md")
- Add the following custom trust policy to the IAM roles, to allow AWS Partner Central to map the AWS IAM roles.

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

###### To map an AWS Partner Central IAM role to a non-cloud admin user

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or cloud admin role.
2. In the **AWS account linking** section of the AWS Partner Central homepage, choose **Manage Linked Account**.
3. On the **AWS account linking**, page, select **Manage IAM roles**.
4. In the non-cloud admin user section, select the partner users you wish to grant access, then choose **Map IAM role**.
5. Choose the IAM role created containing the above channel policy from the dropdown list.
6. Choose **Map role**.

###### To unmap an AWS Partner Central IAM role from a non-cloud admin user

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or cloud admin role.
2. In the **AWS account linking** section of the AWS Partner Central homepage, choose **Manage Linked Account**.
3. On the **AWS account linking**, page, select **Manage IAM roles**.
4. In the non-cloud admin user section, select the partner users you wish to revoke access, then choose **Unmap IAM role**.
5. Choose the IAM role from the dropdown list.
6. Choose **Unmap role**.

###### Important

AWS Partner Central channel management features require IAM roles to be configured in both the Partner Central linked AWS account and the AWS management account used to receive bills and administer channel programs. Work with your AWS Partner Central cloud admin to ensure IAM permissions are configured, and work with your alliance lead or cloud admin to map IAM roles to Partner Central users. Learn more about accessing channel management in the [API reference](../APIReference/channel-access-control.md "../APIReference/channel-access-control.md").
