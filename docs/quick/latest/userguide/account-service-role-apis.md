

# Managing the account service role with the API


|  | 
| --- |
|    Intended audience:  AWS Quick Administrators and AWS Quick developers  | 

AWS Quick Sight uses an AWS Identity and Access Management (IAM) service role to access AWS resources on behalf of your account. Use the following API operations to inspect the account's service role and select a customer-managed role:
+ [DescribeResourcePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeResourcePermissions.html) returns the current role type and, for a customer-managed role, its Amazon Resource Name (ARN).
+ [UpdateResourcePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateResourcePermissions.html) selects a customer-managed role. You can switch from a service-managed role to a customer-managed role, or replace one customer-managed role with another.

Call both operations in the AWS Region where your AWS Quick Sight account is registered (the home Region).

## Prerequisites
<a name="account-service-role-apis-prerequisites"></a>

Before you update the service role, prepare a customer-managed IAM role that meets these requirements:
+ The role is in the same AWS account as your AWS Quick Sight account.
+ The trust policy allows the `quicksight.amazonaws.com` service principal to call `sts:AssumeRole`.
+ The role has permissions policies that allow access to the AWS resources that your account uses.

For role setup instructions, see [Passing IAM roles to Quick](https://docs.aws.amazon.com/quick/latest/userguide/security-create-iam-role.html).

The IAM identity that calls the API needs these permissions:
+ `quicksight:DescribeResourcePermissions` to inspect the configuration.
+ `quicksight:UpdateResourcePermissions` to update the configuration.
+ `iam:PassRole` on the customer-managed role that you select. This permission is required for every Update request. For more information, see [Grant a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in the *IAM User Guide*.

For features that use session tags, also allow `sts:TagSession` in the role trust policy. If you later add or remove this permission, call `UpdateResourcePermissions` again with the same role ARN to refresh the stored session-tag capability.

Use an AWS CLI or SDK version that includes both operations.

## Inspecting the current service role
<a name="account-service-role-apis-describe"></a>

**To inspect the account service role**

1. Run the following AWS CLI command. Replace {{111122223333}} with your AWS account ID and {{us-east-1}} with your home Region.

   ```bash
   aws quicksight describe-resource-permissions \
       --aws-account-id {{111122223333}} \
       --region {{us-east-1}}
   ```

   For example, an account that uses a service-managed role returns a response similar to the following:

   ```json
   {
       "Status": 200,
       "RoleType": "QUICKSIGHT_MANAGED",
       "RequestId": "00000000-0000-4000-8000-000000000000"
   }
   ```

1. Check `RoleType` in the response:  
`QUICKSIGHT_MANAGED`  
AWS Quick Sight manages the role.  
`CUSTOMER_MANAGED`  
You manage the role and its permissions. The response also contains `CustomerManagedRoleArn`.

## Selecting a customer-managed service role
<a name="account-service-role-apis-update"></a>

Both `RoleType` and `CustomerManagedRoleArn` are required. The only supported role type for this operation is `CUSTOMER_MANAGED`.

**To select a customer-managed service role**

1. Run the following AWS CLI command. Replace {{111122223333}} with your AWS account ID, {{arn:aws:iam::111122223333:role/QuickSightServiceRole}} with your prepared role ARN, and {{us-east-1}} with your home Region.

   ```bash
   aws quicksight update-resource-permissions \
       --aws-account-id {{111122223333}} \
       --role-type CUSTOMER_MANAGED \
       --customer-managed-role-arn {{arn:aws:iam::111122223333:role/QuickSightServiceRole}} \
       --region {{us-east-1}}
   ```

   A successful response returns the selected role type and ARN:

   ```json
   {
       "Status": 200,
       "RoleType": "CUSTOMER_MANAGED",
       "CustomerManagedRoleArn": "arn:aws:iam::111122223333:role/QuickSightServiceRole",
       "RequestId": "00000000-0000-4000-8000-000000000000"
   }
   ```

1. Run `describe-resource-permissions` again with your account ID and home Region:

   ```bash
   aws quicksight describe-resource-permissions \
       --aws-account-id {{111122223333}} \
       --region {{us-east-1}}
   ```

   Verify that `RoleType` is `CUSTOMER_MANAGED` and `CustomerManagedRoleArn` matches the role that you selected.

To replace this role with another customer-managed role, repeat the procedure with the replacement role ARN.

Verify that the selected role allows access to the resources that your data sources need. Updating the configuration does not attach permissions policies to the role.

**Returning to a service-managed role**  
You can't use `UpdateResourcePermissions` to switch back to a service-managed role. To make that change, use the Quick console's AWS resource permissions settings. For instructions to open these settings, see [Accessing AWS resources](https://docs.aws.amazon.com/quick/latest/userguide/accessing-data-sources.html).