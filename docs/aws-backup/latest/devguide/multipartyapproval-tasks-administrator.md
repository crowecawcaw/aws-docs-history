# Administrator tasks

Several tasks involving AWS Backup and Multi-party overview required a user with admin
permissions and access to the management account.

## Create an approval team

A user at your organization with admin permissions for an AWS account needs to
[set up
Multi-party approval](../../../mpa/latest/userguide/setting-up.md "../../../mpa/latest/userguide/setting-up.md") (step 3 in the [Overview](multipartyapproval.md#multipartyapproval-overview "multipartyapproval.md#multipartyapproval-overview")).

Before doing this step, it is recommended as a best practice you have both a primary
organization and a secondary organization (for recovery purposes) set up through
AWS Organizations (step 1 in [Overview](multipartyapproval.md#multipartyapproval-overview "multipartyapproval.md#multipartyapproval-overview").

See [Create an approval
team](../../../mpa/latest/userguide/create-team.md#create-team-steps "../../../mpa/latest/userguide/create-team.md#create-team-steps") in the _Multi-party approval user guide_ to create
your team.

During the [`aws mpa create-approval-team`](../../../mpa/latest/APIReference/API_CreateApprovalTeam.md "../../../mpa/latest/APIReference/API_CreateApprovalTeam.md") operation, one of the parameters
is `policies`. This is a list of ARNs (Amazon Resource Names) for Multi-party
approval resource policies that define permissions that protect the team.

The policy shown in the example in the _Multi-party approval User
Guide_ in the procedure [Create an approval
team](../../../mpa/latest/userguide/create-team.md#create-team-steps "../../../mpa/latest/userguide/create-team.md#create-team-steps") contains the policy
`["arn:aws:mpa::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault"]`
with several necessary permissions.

Follow these steps to return a list of available policies by using `mpa
 list-policies`:

1. List Policies:

```
aws mpa list-policies --region us-east-1
```

2. List all policy versions:

```
aws mpa list-policy-versions --policy-arn arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault --region us-east-1
```

3. Get details on a policy:

```
aws mpa get-policy-version --policy-version-arn arn:aws:mpa:::aws:policy/backup.amazonaws.com/CreateRestoreAccessVault/1 --region us-east-1
```

Expand below to see the policy that will created then attached to your approval team
by this operation:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VaultOwnerPermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Resource": "*",
 "Action": [
 "mpa:StartSession",
 "mpa:CancelSession"
 ],
 "Condition": {
 "StringEquals": {
 "mpa:RequestedOperation": "backup:RevokeRestoreAccessBackupVault",
 "mpa:ProtectedResourceAccount": "${aws:PrincipalAccount}"
 },
 "Bool": {
 "aws:ViaAWSService": "true"
 }
 }
 }
 ]
}`

```

## Share a Multi-party approval

team using AWS RAM

You can share a Multi-party approval team with other AWS accounts using [AWS Resource Access Manager (RAM)](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md"), step 4 in the [overview](multipartyapproval.md#multipartyapproval-overview "multipartyapproval.md#multipartyapproval-overview").

Console

###### Share a Multi-party approval team using AWS RAM

1. Sign in to the [AWS RAM
   console](https://console.aws.amazon.com/ram/home?region=us-east-1 "https://console.aws.amazon.com/ram/home?region=us-east-1").
2. In the navigation pane, choose **Resource
   shares**.
3. Choose **Create resource share**.
4. In the **Name** field, enter a descriptive name for your
   resource share.
5. Under **Resource type**, select **Multi-party
   approval Team** from the dropdown menu.
6. Under **Resources**, select the approval team you want to
   share.
7. Under **Principals**, specify the AWS accounts with
   whom you want to share the approval team.
8. To share with specific AWS accounts, select **AWS
   accounts** and enter the 12-digit account IDs.
9. To share with an organization or organizational unit, select
   **Organization** or **Organizational
   unit** and enter the appropriate ID.
10. (_Optional_) Under **Tags**, add any
    tags you want to associate with this resource share.
11. Choose **Create resource share**.

The resource share status will initially show as `PENDING`. Once
the recipient accounts accept the invitation, the status will change to
`ACTIVE`.

CLI
To share a Multi-party approval team using AWS RAM through the CLI, use the
following commands:

First, identify the ARN of the approval team you want to share:

```
aws mpa list-approval-teams --region `us-east-1`
```

Create a resource share using the create-resource-share command:

```
aws ram create-resource-share \
--name "MPA-Team-Share" \
--resource-arns "arn:aws:mpa:`us-east-1`:`ACCOUNT_ID`:approval-team/`TEAM_ID`" \
--principals "`ACCOUNT_ID_TO_SHARE_WITH`" \
--permission-arns "arn:aws:ram::aws:permission/AWSRAMMPAApprovalTeamAccess" \
--region `us-east-1`
```

To share with an organization instead of specific accounts:

```
aws ram create-resource-share \
--name "MPA-Team-Share" \
--resource-arns "arn:aws:mpa:`us-east-1`:`ACCOUNT_ID`:approval-team/`TEAM_ID`" \
--permission-arns "arn:aws:ram::aws:permission/AWSRAMMPAApprovalTeamAccess" \
--allow-external-principals \
--region `us-east-1`
```

Check the status of your resource share:

```
aws ram get-resource-shares \
--resource-owner SELF \
--region `us-east-1`
```

The recipient account(s) will need to accept the resource share
invitation:

```
aws ram get-resource-share-invitations --region `us-east-1`
```

Run in recipient account to accept an invitation:

```
aws ram accept-resource-share-invitation \
--resource-share-invitation-arn "arn:aws:ram:`REGION`:`ACCOUNT_ID`:resource-share-invitation/`INVITATION_ID`" \
--region `us-east-1`
```

Once the invitation is accepted, the Multi-party approval team will be
available for use in the recipient account.

AWS offers tools to share account access, including through [AWS Resource Access Manager](logicallyairgappedvault.md#lag-share "logicallyairgappedvault.md#lag-share") and [Multi-party access](../../../mpa/latest/userguide/share-team.md "../../../mpa/latest/userguide/share-team.md"). When you choose
to share a logically air-gapped vault with another account, consider the following
details:

| Feature                                   | AWS RAM based sharing                                                                                                                                                                                                                                             | Multi-party approval based access                                                                                                                                                                                                                                                                           |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Access to logically air-gapped vaults** | Once RAM share is complete, the vaults can be accessed.                                                                                                                                                                                                           | Any attempt by a different account must be approved by a threshold number of Multi-party approval team members. The approval session automatically expires 24 hours after the request is initiated.                                                                                                         |
| **Access removal**                        | The account which owns the logically air-gapped vault can end RAM based sharing at any time.                                                                                                                                                                      | Access to a vault can only be removed by a request to the Multi-party approval team.                                                                                                                                                                                                                        |
| **Copy across accounts and/or Regions**   | Not currently supported.                                                                                                                                                                                                                                          | Backups can be copied within the same account or with other accounts in the same organization as the recovery account.                                                                                                                                                                                      |
| **Cross-Region transfer billing**         |                                                                                                                                                                                                                                                                   | Cross-Region transfers are billed to the same account that owns the restore access backup vault.                                                                                                                                                                                                            |
| **Recommended use**                       | Primary use is for data loss recovery and for restore testing.                                                                                                                                                                                                    | Primary use is for situations where account access or security is suspected to be compromised.                                                                                                                                                                                                              |
| **Regions**                               | Available in all AWS Regions where logically air-gapped vaults are supported.                                                                                                                                                                                     | Available in all AWS Regions where logically air-gapped vaults are supported.                                                                                                                                                                                                                               |
| **Restores**                              | All supported resource types can be restored from a shared account.                                                                                                                                                                                               | All supported resource types can be restored from a shared account.                                                                                                                                                                                                                                         |
| **Setup**                                 | Sharing can occur as soon as the AWS Backup account sets up RAM sharing and the receiving account accepts the share.                                                                                                                                              | Sharing requires the management account to first create a team, then set up RAM sharing. Then, the management account opts in to Multi-party approval and assigns that team to a logically air-gapped vault.                                                                                                |
| **Sharing**                               | Sharing is done through RAM within same AWS organization or across AWS organizations. Access is granted according to the 'push' model, in which the account that owns the logically air-gapped vault first grants access. Then, the other account accepts access. | Access to a logically air-gapped vault is through Organizations supported approval teams within the same AWS organization or across organizations. Access is granted according to the 'pull' model, where the receiving account first requests access, then the approval team grants or denies the request. |
