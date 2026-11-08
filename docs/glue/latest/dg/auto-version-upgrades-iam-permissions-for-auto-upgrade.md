

# IAM permissions for auto upgrade
<a name="auto-version-upgrades-iam-permissions-for-auto-upgrade"></a>

This section describes the IAM permissions that users and the job role need for auto upgrade.

## Permissions for users
<a name="auto-version-upgrades-permissions-for-users"></a>

Users who manage auto upgrade need these permissions:
+ To turn it on, they need the same rights as to edit a job: `glue:UpdateJob` or `glue:CreateJob`, and `iam:PassRole` on the job role.
+ To view, approve, or decline an upgrade, they need the rights in the following policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ViewAutoUpgradeEvaluations",
      "Effect": "Allow",
      "Action": [
        "glue:GetJobUpgradeAnalysis",
        "glue:ListJobUpgradeAnalyses"
      ],
      "Resource": "arn:aws:glue:us-west-2:111122223333:job/my-etl-job"
    },
    {
      "Sid": "ApproveDeclineOrStopUpgrades",
      "Effect": "Allow",
      "Action": [
        "glue:StartJobUpgradeAnalysis",
        "glue:StopJobUpgradeAnalysis",
        "glue:GetJob"
      ],
      "Resource": "arn:aws:glue:us-west-2:111122223333:job/my-etl-job"
    }
  ]
}
```

If you encrypt the summaries with your own AWS KMS key, users who download and read them also need `kms:Decrypt` on that key. For more information, see [Encryption](auto-version-upgrades-security-for-auto-upgrade.md#auto-version-upgrades-encryption).

## Permissions for the job role
<a name="auto-version-upgrades-permissions-for-the-job-role"></a>

AWS Glue runs the compatibility check with the job's own IAM role, so the analysis can read only what the job itself can read. Make sure that the job role meets the following requirements.

**Trust policy** – The role must trust `glue.amazonaws.com`, which every AWS Glue job role already does. If you scope the trust policy with `aws:SourceAccount` or `aws:SourceArn` conditions, they must allow your account and the job's ARN.

```
{
  "Effect": "Allow",
  "Principal": { "Service": "glue.amazonaws.com" },
  "Action": "sts:AssumeRole",
  "Condition": {
    "StringEquals": { "aws:SourceAccount": "111122223333" },
    "ArnLike": { "aws:SourceArn": "arn:aws:glue:us-west-2:111122223333:job/*" }
  }
}
```

**Read access to the job's code** – The role needs `s3:GetObject` on the script and on every file in `--extra-py-files`, `--extra-jars`, and `--extra-files`. A job that runs successfully already has this access.

**AWS KMS (optional)** – If you set a key to encrypt the summaries, the role needs `kms:GenerateDataKey` and `kms:Decrypt` on it. For more information, see [Encryption](auto-version-upgrades-security-for-auto-upgrade.md#auto-version-upgrades-encryption).