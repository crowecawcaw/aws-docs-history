# Create non-admin roles

Users in the Administrators group for an account have access to all AWS services and
resources in that account. Granting direct access to all AWS resources goes against
the best practice of applying the least privileged permissions to a user. This section
describes how you can create roles with permissions that are limited to
AWS Elemental MediaConnect. This section also describes how your users can assume that role to
grant secure and temporary credentials.

###### Topics

- [Step 1: Create a
  non-admin policy](#setting-up-create-nonadmin-IAM-policies "#setting-up-create-nonadmin-IAM-policies")
- [Step 2: Create
  non-admin roles](#setting-up-create-nonadmin-roles-create-role "#setting-up-create-nonadmin-roles-create-role")
- [Step 3: Assume the
  role](#setting-up-create-nonadmin-roles-assume-role "#setting-up-create-nonadmin-roles-assume-role")

## Step 1: Create a

non-admin policy

Create two policies for AWS Elemental MediaConnect: one to provide read/write access and
one to provide read-only access. Perform these steps one time only for each policy.
Later, you will attach these policies to roles. Those roles can then be temporarily
assumed by users to grant access to MediaConnect.

###### To create policies

1. Use your AWS account ID or account alias, and the credentials for your
   admin user, to sign in to the [IAM
   console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
2. In the navigation pane of the console, choose
   **Policies**.
3. On the **Policies** page, create a policy named `MediaConnectAllAccess` that allows all actions on all resources in
   AWS Elemental MediaConnect:
   1. Choose **Create policy**.
   2. Choose the **JSON** tab and paste the following
      policy:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Action": [
    "mediaconnect:*"
    ],
    "Effect": "Allow",
    "Resource": "*"
    },
    {
    "Action": [
    "ec2:DescribeAvailabilityZones"
    ],
    "Effect": "Allow",
    "Resource": "*"
    },
    {
    "Action": [
    "cloudwatch:GetMetricData"
    ],
    "Effect": "Allow",
    "Resource": "*"
    },
    {
    "Action": [
    "iam:PassRole"
    ],
    "Effect": "Allow",
    "Resource": "*",
    "Condition": {
    "StringLike": {
    "iam:PassedToService": "mediaconnect.amazonaws.com"
    }
    }
    }
    ]
   }`

   ```

   This policy allows all actions on all resources in
   AWS Elemental MediaConnect. 3. Choose **Next: Tags**. 4. Choose **Next: Review**. 5. On the **Review and create** page, for **Policy name**, enter
   `MediaConnectAllAccess`, and then choose
   **Create policy**.

4. On the **Policies** page, create a read-only policy named `MediaConnectReadOnlyAccess` for AWS Elemental MediaConnect:
   1. Choose **Create policy**.
   2. Choose the **JSON** tab and paste the following policy:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Action": [
    "mediaconnect:List*",
    "mediaconnect:Describe*"
    ],
    "Effect": "Allow",
    "Resource": "*"
    },
    {
    "Action": [
    "ec2:DescribeAvailabilityZones"
    ],
    "Effect": "Allow",
    "Resource": "*"
    },
    {
    "Action": [
    "cloudwatch:GetMetricData"
    ],
    "Effect": "Allow",
    "Resource": "*"
    },
    {
    "Action": [
    "iam:PassRole"
    ],
    "Effect": "Allow",
    "Resource": "*",
    "Condition": {
    "StringLike": {
    "iam:PassedToService": "mediaconnect.amazonaws.com"
    }
    }
    }
    ]
   }`

   ```

   3. Choose **Next: Tags**.
   4. Choose **Next: Review**.
   5. On the **Review and create** page, for **Policy name**, enter
      `MediaConnectReadOnlyAccess`, and then
      choose **Create policy**.

## Step 2: Create

non-admin roles

You can create a role for each policy and users can assume that role, rather than
attaching individual policies to each user. Using the following procedure, create
two roles: one for the **MediaConnectAllAccess** policy and one for
the **MediaConnectReadOnlyAccess** policy.

###### To create roles

1. In the navigation pane of the IAM console, choose
   **Roles**.
2. On the **Roles** page, create an administrator role using the
   `MediaConnectAllAccess` policy:
   1. Choose **Create role**.
   2. In the **Select trusted entity** section, select
      **AWS account**.
   3. In the **An AWS account** section, select the
      account with the users that will be assuming this role.
      1. If a third-party will be accessing this role, it is a best
         practice to select **Require external ID**.
         For more information about external IDs, visit: [Using an external ID for third-party access](../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md "../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md") in
         the _IAM User Guide_.
      2. It is a best practice to require multi-factor
         authentication (MFA). You can select the checkbox next to
         **Require MFA**. For more information
         about MFA, visit: [Multi-factor authentication (MFA)](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the
         _IAM User Guide_.

   4. Choose **Next** to move to the **Add
      permissions** section.
   5. In the **Permissions policy** section, choose the
      **MediaConnectAllAccess** policy that you
      created in the procedure in [Step 3a:
      Create a Policy](#setting-up-create-nonadmin-IAM-policies "#setting-up-create-nonadmin-IAM-policies").
   6. Verify that the correct policies are added to this group, and then
      choose **Next**.
   7. In the **Name, review and create** section, name
      the role `MediaConnectAdmins`. (Optional) Add a
      description for the role. Select **Create
      role**.

3. On the **Roles** page, create an administrator role using the
   `MediaConnectReadOnlyAccess` policy:
   1. Choose **Create role**.
   2. In the **Select trusted entity** section, select
      **AWS account**.
   3. In the **An AWS account** section, select the
      account with the users that will be assuming this role.
      1. If a third-party will be accessing this role, it is a best
         practice to select **Require external ID**.
         For more information about external IDs, visit: [Using an external ID for third-party access](../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md "../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md") in
         the _IAM User Guide_.
      2. It is a best practice to require multi-factor
         authentication (MFA). You can select the checkbox next to
         **Require MFA**. For more information
         about MFA, visit: [Multi-factor authentication (MFA)](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the
         _IAM User Guide_.

   4. Choose **Next** to move to the **Add
      permissions** section.
   5. In the **Permissions policy** section, choose the
      **MediaConnectReadOnlyAccess** policy that you
      created in the procedure in [Step 3a:
      Create a Policy](#setting-up-create-nonadmin-IAM-policies "#setting-up-create-nonadmin-IAM-policies").
   6. Verify that the correct policies are added to this group, and then
      choose **Next**.
   7. In the **Name, review and create** section, name
      the role `MediaConnectReaders`. (Optional) Add a
      description for the role. Select **Create
      role**.

## Step 3: Assume the

role

After creating a policy and attaching that policy to a role, your users will need
to assume that role to be granted secure and temporary access to MediaConnect.

View the following resources for learning about granting permissions for users to
assume the role and how users can switch to the role from the console or
AWS CLI.

- Granting a user permissions to switch roles: [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html](../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md "../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md")
- Switching roles (console): [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md")
- Switching roles (AWS CLI): [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-cli.html](../../../IAM/latest/UserGuide/id_roles_use_switch-role-cli.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-cli.md")
