# Enable backup on moved accounts

If you move an account into an AWS Control Tower OU that has AWS Backup enabled, and the account is
not enrolled in AWS Control Tower, your backup plan does not apply to the account
automatically.

**Console:** To enable AWS Backup for an individual account from the
AWS Control Tower console, you can choose **Update account** on the
**Account details** page, or you can choose
**Re-register OU** on the **OU detail**s page to
update several accounts at the same time.

**API:** From the API, if you move an account into an OU that has the
backup baseline enabled, you can call the `ResetEnabledBaseline` API on that
OU, specifying the OU's `EnabledBaseline` resource as a target, to trigger
backups on the account by inheritance from the OU.

Example command:

```
aws controltower reset-enabled-baseline --enabled-baseline-identifier arn:aws:controltower:`REGION`:`NAMESPACE`:enabledbaseline/XOSDORW8HDB5ZNWEE --region us-east-1
```

Example response:

```
{
        "operationIdentifier": "0bbdb587-c849-4152-95c6-7afa7664ee71"
}
```
