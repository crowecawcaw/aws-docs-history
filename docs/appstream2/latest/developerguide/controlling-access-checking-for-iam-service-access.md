

# Checking for the AmazonAppStreamServiceAccess Service Role and Policies
<a name="controlling-access-checking-for-iam-service-access"></a>

Complete the steps in this section to check whether the **AmazonAppStreamServiceAccess** service role is present and has the correct policies attached. If this role is not in your account and must be created, you or an administrator with the required permissions must perform the steps to get started with WorkSpaces Applications in your Amazon Web Services account.

**To check whether the AmazonAppStreamServiceAccess IAM service role is present**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**. 

1. In the search box, type **amazonappstreamservice** to narrow the list of roles to select, and then choose **AmazonAppStreamServiceAccess**. If this role is listed, select it to view the role **Summary** page. 

1. On the **Permissions** tab, confirm whether the **AmazonAppStreamServiceAccess** permissions policy is attached.

1. Return to the role **Summary** page.

1. On the **Trust relationships** tab, choose **Show policy document**, and then confirm whether the **AmazonAppStreamServiceAccess** trust relationship policy is attached and follows the correct format. If so, the trust relationship is correctly configured. Choose **Cancel** and close the IAM console. 

## AmazonAppStreamServiceAccess trust relationship policy
<a name="controlling-access-service-access-trust-policy"></a>

The **AmazonAppStreamServiceAccess** trust relationship policy must include the WorkSpaces Applications service as the principal. A *principal* is an entity in AWS that can perform actions and access resources. This policy must also include the `sts:AssumeRole` action. The following policy configuration defines WorkSpaces Applications as a trusted entity.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
      "Service": "appstream.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
    }
  ]
}
```

------

## Checking for and creating the service role (AWS CLI)
<a name="controlling-access-checking-for-iam-service-access-cli"></a>

To make sure that the required service role exists before you provision resources, perform the steps in this section when you get started with Amazon WorkSpaces Applications (WorkSpaces Applications) through the WorkSpaces Applications API or AWS Command Line Interface (AWS CLI) instead of the console. You check whether the `AmazonAppStreamServiceAccess` service role exists and verify that it has the correct policies attached. If this role is not in your account, create it before you provision resources with WorkSpaces Applications.

Creating this role requires administrator-level AWS Identity and Access Management (IAM) permissions. If you are not an administrator, ask an administrator to perform these steps or to grant you the required permissions.

**Note**  
WorkSpaces Applications automatically creates the `AmazonAppStreamServiceAccess` service role the first time you get started with WorkSpaces Applications in the console. To provision resources with the WorkSpaces Applications API or AWS CLI without using the console, first create this role manually with the API or AWS CLI.

### Checking whether the service role is present
<a name="controlling-access-service-access-cli-check"></a>

Before you begin, make sure that the following are true:
+ You installed and configured the AWS CLI with credentials for your AWS account.
+ Your AWS Identity and Access Management (IAM) principal has the `iam:GetRole` and `iam:ListAttachedRolePolicies` permissions.

**Checking whether the role exists (AWS CLI)**

1. Run the following AWS CLI command to check whether the `AmazonAppStreamServiceAccess` role is present in your account.

   ```
   PROMPT> aws iam get-role --role-name AmazonAppStreamServiceAccess
   ```

1. If the role exists, continue to the next procedure. If the role does not exist, you receive the following error.

   ```
   An error occurred (NoSuchEntity) when calling the GetRole operation:
   The role with name AmazonAppStreamServiceAccess cannot be found.
   ```

   If you receive this error, create the role as described in [Creating the service role (AWS CLI)](#controlling-access-service-access-cli-create).

**Verifying that the permissions policy is attached (AWS CLI)**

1. Run the following AWS CLI command to list the policies that are attached to the role.

   ```
   PROMPT> aws iam list-attached-role-policies --role-name AmazonAppStreamServiceAccess
   ```

1. Verify that the following policy is listed in the output.

   ```
   {
       "AttachedPolicies": [
           {
               "PolicyName": "AmazonAppStreamServiceAccess",
               "PolicyArn": "arn:aws:iam::aws:policy/service-role/AmazonAppStreamServiceAccess"
           }
       ]
   }
   ```

1. If this policy is not in the output, run the following AWS CLI command to attach it.

   ```
   PROMPT> aws iam attach-role-policy \
       --role-name AmazonAppStreamServiceAccess \
       --policy-arn arn:aws:iam::aws:policy/service-role/AmazonAppStreamServiceAccess
   ```

**Note**  
If you receive an `AccessDenied` error, verify that your IAM principal has the `iam:AttachRolePolicy` permission. If you do not have this permission, ask your AWS account administrator to attach the policy or to grant you the permission.

**Verifying the trust relationship (AWS CLI)**

1. Run the following AWS CLI command to view the trust relationship policy for the role.

   ```
   PROMPT> aws iam get-role \
       --role-name AmazonAppStreamServiceAccess \
       --query "Role.AssumeRolePolicyDocument" \
       --output json
   ```

1. Confirm that the output matches the following format.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "appstream.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

If the trust relationship specifies `appstream.amazonaws.com` as the trusted principal, the service role is ready and no further action is required.

**Note**  
If the trust relationship principal does not match `appstream.amazonaws.com`, someone might have modified the role. Contact your AWS account administrator to review and correct the trust policy before you use WorkSpaces Applications.

### Creating the service role (AWS CLI)
<a name="controlling-access-service-access-cli-create"></a>

If the `AmazonAppStreamServiceAccess` role is not in your account, complete the following steps to create it.

Before you begin, make sure that the following are true:
+ You installed and configured the AWS CLI with credentials for your AWS account.
+ Your IAM principal has the `iam:CreateRole`, `iam:AttachRolePolicy`, `iam:GetRole`, and `iam:ListAttachedRolePolicies` permissions.

**Creating the trust policy document (AWS CLI)**
+ To grant the WorkSpaces Applications service permission to assume the role, create a file named `trust-policy.json` with the following content.

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
                  "Service": "appstream.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
          }
      ]
  }
  ```

**Creating the role (AWS CLI)**
+ Run the following AWS CLI command to create the `AmazonAppStreamServiceAccess` role with the trust policy document that you created. The command returns the Amazon Resource Name (ARN) and details of the new role.

  ```
  PROMPT> aws iam create-role \
      --role-name AmazonAppStreamServiceAccess \
      --assume-role-policy-document file://trust-policy.json \
      --description "Service role that lets AppStream manage resources on your behalf"
  ```

**Note**  
If you receive an `EntityAlreadyExists` error, the role already exists in your account. If you receive an `AccessDenied` error, verify that your IAM principal has the `iam:CreateRole` permission, or ask your AWS account administrator to create the role.

**Attaching the permissions policy (AWS CLI)**
+ Run the following AWS CLI command to attach the `AmazonAppStreamServiceAccess` AWS managed policy to the role.

  ```
  PROMPT> aws iam attach-role-policy \
      --role-name AmazonAppStreamServiceAccess \
      --policy-arn arn:aws:iam::aws:policy/service-role/AmazonAppStreamServiceAccess
  ```

**Note**  
If you receive an `AccessDenied` error, verify that your IAM principal has the `iam:AttachRolePolicy` permission, or ask your AWS account administrator to attach the policy.

**Verifying that the role exists (AWS CLI)**
+ Run the following AWS CLI command to confirm that you created the role.

  ```
  PROMPT> aws iam get-role --role-name AmazonAppStreamServiceAccess
  ```

**Verifying that the permissions policy is attached (AWS CLI)**
+ Run the following AWS CLI command to verify that the permissions policy is attached.

  ```
  PROMPT> aws iam list-attached-role-policies --role-name AmazonAppStreamServiceAccess
  ```

**Verifying the trust relationship (AWS CLI)**
+ Run the following AWS CLI command to confirm that the trust relationship specifies `appstream.amazonaws.com` as the trusted principal.

  ```
  PROMPT> aws iam get-role \
      --role-name AmazonAppStreamServiceAccess \
      --query "Role.AssumeRolePolicyDocument" \
      --output json
  ```

The `AmazonAppStreamServiceAccess` service role is ready to use with WorkSpaces Applications when all of the following are true:
+ The role exists.
+ You see the permissions policy listed.
+ The trust relationship shows `appstream.amazonaws.com` as the trusted principal.

**Important**  
WorkSpaces Applications must have this role to manage resources on your behalf. Keep the role name, permissions policy, and trust relationship unchanged so that the service continues to function correctly. To make changes, contact your AWS account administrator.

### Finding related service role resources
<a name="controlling-access-service-access-cli-resources"></a>

For more information about controlling access to WorkSpaces Applications resources, see the following resources:
+ For information about the AWS managed policies for WorkSpaces Applications, see [AWS Managed Policies Required to Access WorkSpaces Applications Resources](managed-policies-required-to-access-appstream-resources.md).
+ For information about getting started with WorkSpaces Applications, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md).
+ For information about IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide*.