# Migrating to the `AmazonECS_FullAccess` managed policy

The `AmazonEC2ContainerServiceFullAccess` managed IAM policy was phased
out on January 29, 2021, in response to a security finding with the
`iam:passRole` permission. This permission grants access to all resources
including credentials to roles in the account. Now that the policy is phased out, you
can't attach the policy to any new groups, users, or roles. Any groups, users, or roles
that already have the policy attached can continue using it. However, we recommend that
you update your groups, users, or roles to use the `AmazonECS_FullAccess`
managed policy instead.

The permissions that are granted by the `AmazonECS_FullAccess` policy
include the complete list of permissions that are necessary to use ECS as an
administrator. If you currently use permissions that are granted by the
`AmazonEC2ContainerServiceFullAccess` policy that aren't in the
`AmazonECS_FullAccess` policy, you can add them to an inline policy
statement. For more information, see [AWS managed policies for Amazon Elastic Container Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

Use the following steps to determine if you have any groups, users, or roles that are
currently using the `AmazonEC2ContainerServiceFullAccess` managed IAM
policy. Then, update them to detach the earlier policy and attach the
`AmazonECS_FullAccess` policy.

###### To update a group, user, or role to use the AmazonECS_FullAccess policy (AWS Management Console)

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies** and search for
   and select the `AmazonEC2ContainerServiceFullAccess` policy.
3. Choose the **Policy usage** tab that displays any IAM role
   that's currently using this policy.
4. For each IAM role that's currently using the
   `AmazonEC2ContainerServiceFullAccess` policy, select the role and
   use the following steps to detach the phased out policy and attach the
   `AmazonECS_FullAccess` policy.
   1. On the **Permissions** tab, choose the
      **X** next to the
      **AmazonEC2ContainerServiceFullAccess**
      policy.
   2. Choose **Add permissions**.
   3. Choose **Attach existing policies directly**, search
      for and select the **AmazonECS_FullAccess** policy, and
      then choose **Next: Review**.
   4. Review the changes and then choose **Add
      permissions**.
   5. Repeat these steps for each group, user, or role that's using the
      `AmazonEC2ContainerServiceFullAccess` policy.

###### To update a group, user, or role to use the `AmazonECS_FullAccess` policy (AWS CLI)

1. Use the [generate-service-last-accessed-details](../../../cli/latest/reference/iam/generate-service-last-accessed-details.md "../../../cli/latest/reference/iam/generate-service-last-accessed-details.md") command
   to generate a report that includes details about when the phased out policy was
   last used.

```
`aws iam generate-service-last-accessed-details \
 --arn arn:aws:iam::aws:policy/AmazonEC2ContainerServiceFullAccess`
```

Example output:

```
{
    "JobId": "32bb1fb0-1ee0-b08e-3626-ae83EXAMPLE"
}
```

2. Use the job ID from the previous output with the [get-service-last-accessed-details](../../../cli/latest/reference/iam/get-service-last-accessed-details.md "../../../cli/latest/reference/iam/get-service-last-accessed-details.md") command to
   retrieve the last accessed report of the service. This report displays the
   Amazon Resource Name (ARN) of the IAM entities that last used the phased out
   policy.

```
`aws iam get-service-last-accessed-details \
 --job-id `32bb1fb0-1ee0-b08e-3626-ae83EXAMPLE``
```

3. Use one of the following commands to detach the
   `AmazonEC2ContainerServiceFullAccess` policy from a group, user,
   or role.
   - [detach-group-policy](../../../cli/latest/reference/iam/detach-group-policy.md "../../../cli/latest/reference/iam/detach-group-policy.md")
   - [detach-role-policy](../../../cli/latest/reference/iam/detach-role-policy.md "../../../cli/latest/reference/iam/detach-role-policy.md")
   - [detach-user-policy](../../../cli/latest/reference/iam/detach-user-policy.md "../../../cli/latest/reference/iam/detach-user-policy.md")

4. Use one of the following commands to attach the
   `AmazonECS_FullAccess` policy to a group, user, or role.
   - [attach-group-policy](../../../cli/latest/reference/iam/attach-group-policy.md "../../../cli/latest/reference/iam/attach-group-policy.md")
   - [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md")
   - [attach-user-policy](../../../cli/latest/reference/iam/attach-user-policy.md "../../../cli/latest/reference/iam/attach-user-policy.md")
