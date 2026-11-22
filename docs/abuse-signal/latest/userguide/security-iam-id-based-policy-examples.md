

# AWS Abuse Signal API identity-based policy examples

By default, IAM users and roles don’t have permission to call AWS Abuse Signal API. An IAM administrator must create IAM policies that grant identities permission to perform the `abuse:` actions they need, and then attach those policies to the IAM users, groups, or roles that require them.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Note**  
The `abuse:` actions operate at the account level and do not support resource-level permissions. AWS Abuse Signal API has no report ARN that you can name in a policy, so you must set `"Resource"` to `"*"` in the following examples. The service still scopes results from `ListAbuseReportStatuses` to the caller’s own AWS account.

**Topics**
+ [Policy best practices](#security-iam-policy-best-practices)
+ [Least-privilege policy: submit only](#security-iam-policy-example-submit)
+ [Least-privilege policy: submit and track](#security-iam-policy-example-submit-track)

## Policy best practices
<a name="security-iam-policy-best-practices"></a>
+  **Apply least-privilege permissions** – Grant only the `abuse:` actions each identity needs.
+  **Use IAM roles and short-lived credentials** – Avoid long-lived access keys and the account root user.
+  **Require multi-factor authentication (MFA)** – Turn on MFA for identities that require it.

For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Least-privilege policy: submit only
<a name="security-iam-policy-example-submit"></a>

The following policy grants permission to submit abuse reports, but not to read or list them. Because the `abuse:` actions don’t support resource-level permissions, `"Resource"` is set to `"*"`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SubmitAbuseReports",
      "Effect": "Allow",
      "Action": "abuse:CreateAbuseReport",
      "Resource": "*"
    }
  ]
}
```

## Least-privilege policy: submit and track
<a name="security-iam-policy-example-submit-track"></a>

The following policy grants permission to submit, retrieve, and list abuse reports. Because the `abuse:` actions don’t support resource-level permissions, `"Resource"` is set to `"*"`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SubmitAndTrackAbuseReports",
      "Effect": "Allow",
      "Action": [
        "abuse:CreateAbuseReport",
        "abuse:GetAbuseReportStatus",
        "abuse:ListAbuseReportStatuses"
      ],
      "Resource": "*"
    }
  ]
}
```