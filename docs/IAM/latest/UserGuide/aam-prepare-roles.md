

# Prepare your IAM roles
<a name="aam-prepare-roles"></a><a name="aam-identify-and-update-roles"></a>

Before you start assigning IAM roles to IAM Identity Center users and groups, you need to:

1. Identify the relevant IAM roles in the accounts of interest, and

1. Make sure the [trust policy](id_roles.md#id_roles_terms-and-concepts) of the IAM roles contains the Statement provided below.

If the role has an existing trust policy, add this statement to its Statement array. If you're creating a new role, you can use the entire policy document. This policy statement allows account access manager to assume the role and set context on behalf of users. The `Condition` block provides confused-deputy protection by ensuring that account access manager can assume the role only on behalf of your own account and your account access manager application. For more information, see [Update a role trust policy](id_roles_update-role-trust-policy.md).

Replace `<your-account-id>` with your AWS account ID, `<region>` with your IAM Identity Center primary Region, and `<application-id>` with your account access manager application ID. You can find the application ARN on the **Settings** page in the account access manager console.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AccountAccessManagerIAMRoleTrustPolicyStatement",
      "Effect": "Allow",
      "Principal": {
        "Service": "account-access.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:SetContext"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<your-account-id>",
          "aws:SourceArn": "arn:aws:account-access:<region>:<your-account-id>:application/<application-id>"
        }
      }
    }
  ]
}
```

**Optional — `sts:TagSession`**. Add `sts:TagSession` to the `Action` list if you want upstream assertion attributes from your identity provider (for example, group memberships, department, cost-center) to propagate as principal tags on the session that account access manager issues. Without this action, role assumption still succeeds; only session-tag propagation is suppressed. Add it when downstream IAM policies in the target account use principal tags (`aws:PrincipalTag/<key>`); leave it out otherwise. Keep the same `Condition` block.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AccountAccessManagerIAMRoleTrustPolicyStatement",
      "Effect": "Allow",
      "Principal": {
        "Service": "account-access.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:SetContext",
        "sts:TagSession"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<your-account-id>",
          "aws:SourceArn": "arn:aws:account-access:<region>:<your-account-id>:application/<application-id>"
        }
      }
    }
  ]
}
```

**Note**  
We recommend you update your IAM role creation workflows to add this trust policy statement automatically where needed.