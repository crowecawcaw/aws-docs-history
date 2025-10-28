# Requester tasks

## Associate a Multi-party approval

team with a LAG vault

Requester: **User with access to account that
owns the logically air-gapped vault**.

You can associate a Multi-party approval team with a logically air-gapped vault to
enable collaborative approval for access to the vault (step 5 in the [Overview](multipartyapproval.md#multipartyapproval-overview "multipartyapproval.md#multipartyapproval-overview")).

Console

###### Associate a Multi-party approval team with a LAG vault

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to the **Backup vaults** section in the left
   navigation pane.
3. Select the logically air-gapped backup vault you want to associate with an
   MPA team.
4. On the **vault details** page, select **Assign
   approval team**.
5. From the dropdown menu, select the approval team you want to associate
   with the vault
6. _Optional_ Enter a comment explaining the reason for the
   association.
7. Select **Send request** to submit the association
   request.

If this is the first approval team to be associated with the vault, the team
will be associated with the vault. If the vault already has an associated team,
see [Update Multi-party approval
team](#update-multpartyapproval-team "#update-multpartyapproval-team") for steps.

CLI
Use the CLI command `associate-backup-vault-mpa-approval-team`,
modified with the following parameters:

```
aws backup associate-backup-vault-mpa-approval-team \
--backup-vault-name `VAULT_NAME` \
--mpa-approval-team-arn `MPA_TEAM_ARN` \
--requester-comment "`OPTIONAL_COMMENT`" \
--region `REGION`
```

If this is the first approval team to be associated with the vault, the team
will be associated with the vault. If the vault already has an associated team,
see [Update Multi-party approval
team](#update-multpartyapproval-team "#update-multpartyapproval-team") for steps.

## Request access to a logically air-gapped

vault

Requester: **User with access to recovery account**.

You can request access to a logically air-gapped vault in another account (step 6 in
the [Overview](multipartyapproval.md#multipartyapproval-overview "multipartyapproval.md#multipartyapproval-overview")).

After an approval team
has granted the request, AWS Backup creates a restore access backup vault in your designated
recovery account so that account will have access to recovery points in the
connected logically air-gapped vault.

Console

###### Request access to a logically air-gapped vault

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to the **Backup vaults** section in the left
   navigation pane
3. Select the **Vaults accessible through MPA** tab
4. Select **Request vault access**.
5. Enter the source backup vault ARN of the logically air-gapped vault you
   want to access.
6. Enter an optional name for the restore access backup vault. If you do not
   input a name, AWS Backup will assign a name based on the name of the logically air
   gapped vault.
7. Enter an optional requester comment explaining the reason for the access
   request.
8. Select **Send request** to submit the access
   request.

The approval team members associated with the source vault will receive an
email notification to approve the request.

Once the request is approved by the required number ("threshold") of team
members, the restore access backup vault will be created in the recovery
account.

CLI
Use the CLI command `create-restore-access-backup-vault`:

```
aws backup create-restore-access-backup-vault \
--source-backup-vault-arn `SOURCE_VAULT_ARN` \
--backup-vault-name `OPTIONAL_VAULT_NAME` \
--requester-comment "`OPTIONAL_COMMENT`" \
--region `REGION`
```

The MPA approval team members associated with the source vault will receive a
notification to approve the request. Once the request is approved by the required
number ("threshold") of team members, the restore access backup vault will be
created in the recovery account.

You can check the status of the vault using:

```
aws backup describe-backup-vault \
--backup-vault-name `VAULT_NAME` \
--region `REGION`
```

## Disassociate Multi-party approval

team from logically air gapped vault

Requester: **Administrator of account that
owns the logically air-gapped vault**.

You can disassociate a Multi-party approval team from a logically air-gapped vault
(step 7 in the [Overview](multipartyapproval.md#multipartyapproval-overview "multipartyapproval.md#multipartyapproval-overview")).

Console

###### Disassociate approval team from LAG vault

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to the **Backup vaults** section in the left
   navigation pane.
3. Select the logically air-gapped backup vault from which you want to
   disassociate the approval team.
4. On the **Vault details** page, select
   **Disassociate approval team**.
5. Enter an optional requester comment explaining the reason for the
   disassociation.
6. Select **Send request** to submit the disassociation
   request.

The current approval team members will receive a notification to approve the
request.

Once approved by the required number of team members, the team will be
disassociated from the vault.

CLI
Use the CLI command
`disassociate-backup-vault-mpa-approval-team`:

```
aws backup disassociate-backup-vault-mpa-approval-team \
--backup-vault-name `VAULT_NAME` \
--requester-comment "`OPTIONAL_COMMENT`" \
--region `REGION`
```

The current MPA approval team members will receive a notification to approve
the request. Once approved by the required number of team members, the team will
be disassociated from the vault.

## Revoke restore access backup vault

Requester: **Administrator of account that
owns the logically air-gapped vault**.

You can revoke access to a restore access backup vault from the source vault
account.

Console

###### Revoke restore access backup vault

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to the **Backup vaults** section in the left
   navigation pane.
3. Select the logically air-gapped backup vault for which you want to revoke
   access.
4. On the **Vault details** page, scroll down to the
   **Access through Multi-party approval** section.
5. Find the restore access backup vault you want to revoke, then select
   **Request to remove vault access**.
6. Enter an optional requester comment explaining the reason for the
   revocation.
7. Select **Send request** to submit the revocation
   request.

The approval team members will receive a notification to approve the
request.

Once approved by the required number of team members, the restore access
backup vault will be deleted from the recovery account

CLI
First, list the restore access backup vaults associated with your source
vault:

```
aws backup list-restore-access-backup-vaults \
--backup-vault-name `SOURCE_VAULT_NAME` \
--region `REGION`
```

Then, use the CLI command
`revoke-restore-access-backup-vault`:

```
aws backup revoke-restore-access-backup-vault \
--backup-vault-name `SOURCE_VAULT_NAME` \
--restore-access-backup-vault-arn `RESTORE_ACCESS_VAULT_ARN` \
--requester-comment "`OPTIONAL_COMMENT`" \
--region `REGION`
```

The approval team members will receive a notification to approve the request.
Once approved by the required number of team members, the restore access backup
vault will be deleted from the recovery account.

## Update the Multi-party approval team

associated with a LAG vault

Requester: **Administrator of account that
owns the logically air-gapped vault**.

You can update the Multi-party approval team associated with a logically air-gapped
vault (step 8 in the [Overview](multipartyapproval.md#multipartyapproval-overview "multipartyapproval.md#multipartyapproval-overview")).

Console

###### Update the approval team associated with a logically air-gapped

vault

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to the **Backup vaults** section in the left
   navigation pane.
3. Select the logically air-gapped backup vault for which you want to update
   the approval team.
4. On the vault details page, select **Request approval team
   change**.
5. From the dropdown menu, select the new approval team you want to associate
   with the vault.
6. Enter an optional requester comment explaining the reason for the
   change.
7. Select **Send request** to submit the change
   request.

The current approval team members will receive an email notification to
approve the request.

Once approved by the required number of team members (threshold) from the
current MPA team, the new team will be associated with the vault.

CLI
Use the CLI command `associate-backup-vault-mpa-approval-team` with
the new team ARN:

```
aws backup associate-backup-vault-mpa-approval-team \
--backup-vault-name `VAULT_NAME` \
--mpa-approval-team-arn `NEW_MPA_TEAM_ARN` \
--requester-comment "`OPTIONAL_COMMENT`" \
--region `REGION`
```

The current approval team members will receive a notification to approve the
request. Once approved by the required number of team members (threshold) from the
current team, the new MPA team will be associated with the vault.
