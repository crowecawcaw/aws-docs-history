# Spot Instances not scaling down

AWS Batch introduced the **AWSServiceRoleForBatch** service-linked role on
March 10, 2021. If no role is specified in the `serviceRole` parameter of the compute
environment, this service-linked role is used as the service role. However, suppose that the
service-linked role is used in an EC2 Spot compute environment, but the Spot role used doesn't
include the **AmazonEC2SpotFleetTaggingRole** managed policy. Then, the Spot
Instance doesn't scale down. As a result, you will receive an error with the following message:
"You are not authorized to perform this operation." Use the following steps to update the spot
fleet role that you use in the `spotIamFleetRole` parameter. For more information,
see [Using
service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") and [Creating a role to delegate
permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Topics

- [Attach
  AmazonEC2SpotFleetTaggingRole managed policy to your Spot Fleet role in
  the AWS Management Console](#spot-fleet-not-authorized-console "#spot-fleet-not-authorized-console")
- [Attach
  AmazonEC2SpotFleetTaggingRole managed policy to your Spot Fleet role
  with the AWS CLI](#spot-fleet-not-authorized-cli "#spot-fleet-not-authorized-cli")

## Attach

**AmazonEC2SpotFleetTaggingRole** managed policy to your Spot Fleet role in
the AWS Management Console

###### To apply the current IAM managed policy to your Amazon EC2 Spot Fleet role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles**, and choose your Amazon EC2 Spot Fleet role.
3. Choose **Attach policy**.
4. Select the **AmazonEC2SpotFleetTaggingRole** and choose
   **Attach policy**.
5. Choose your Amazon EC2 Spot Fleet role again to remove the previous policy.
6. Select the **x** to the right of the
   **AmazonEC2SpotFleetRole** policy, and choose
   **Detach**.

## Attach

**AmazonEC2SpotFleetTaggingRole** managed policy to your Spot Fleet role
with the AWS CLI

The example commands assume that your Amazon EC2 Spot Fleet role is named
`AmazonEC2SpotFleetRole`. If your role uses a different name, adjust
the commands to match.

###### To attach the **AmazonEC2SpotFleetTaggingRole** managed policy to your

Spot Fleet role

1. To attach the **AmazonEC2SpotFleetTaggingRole** managed IAM policy to
   your `AmazonEC2SpotFleetRole` role, run the following command using
   the AWS CLI.

```
`$` `aws iam attach-role-policy \
 --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetTaggingRole \
 --role-name `AmazonEC2SpotFleetRole``
```

2. To detach the **AmazonEC2SpotFleetRole** managed IAM policy from your
   `AmazonEC2SpotFleetRole` role, run the following command using the
   AWS CLI.

```
`$` `aws iam detach-role-policy \
 --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetRole \
 --role-name `AmazonEC2SpotFleetRole``
```
