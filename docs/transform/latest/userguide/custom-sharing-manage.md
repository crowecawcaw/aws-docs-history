

# Manage your shares

## List the shares that you own
<a name="custom-sharing-manage-list"></a>

```bash
atx custom def share list --outgoing
```

The output is a table titled `Shares you own ({{Region}})`. For each share, it shows the TD, who it's shared with, the status, the managed policy, and the share ID. An `ARN:` line under each row shows the TD's ARN.


| Status | Meaning | 
| --- | --- | 
| Pending | The invitation was sent and hasn't been accepted yet. | 
| Active | The consumer has access. | 
| Declined or removed | The consumer declined, or the consumer was removed. | 
| Expired or no target | The invitation expired before it was accepted, or the target no longer exists. | 
| Failed: {{reason}} | AWS RAM couldn't give the target access. The reason is AWS RAM's message. If the reason is that you aren't authorized, the CLI adds Your IAM identity needs transform-custom:PutResourcePolicy. Fix the cause, and then run share create again. It creates a new share. | 
| Revoke incomplete | A revoke didn't finish, and the target might still have access. This happens when your IAM identity lacks transform-custom:DeleteResourcePolicy or transform-custom:PutResourcePolicy. Add them, and then run share revoke again. | 
| Definition deleted | The TD in the share was deleted. Revoke the share. | 

## Change a share's permission
<a name="custom-sharing-manage-update"></a>

```bash
atx custom def share update {{share-id}} --managed-policy ExecuteWithLearningsAndPackageDownload
```

```
Share {{share-id}} now uses the 'ExecuteWithLearningsAndPackageDownload' managed policy for 'java17-upgrade'.
Note: 444455556666 can also read this transformation definition's learnings.
```

If the share already has that permission, nothing changes.

## Revoke a share
<a name="custom-sharing-manage-revoke"></a>

```bash
atx custom def share revoke {{share-id}}        # asks you to confirm
atx custom def share revoke {{share-id}} --yes  # no prompt
```

```
Revoke share {{share-id}}? 444455556666 will lose access to 'java17-upgrade'. (y/N)
Revoked share {{share-id}}. 444455556666 can no longer use 'java17-upgrade'.
```

After you revoke a share, the consumer can't start new runs, use your lessons, or download the TD. This takes effect within seconds. Revoking doesn't retract content that the consumer already downloaded. Lessons that the consumer already contributed stay in your TD.

## Delete a shared TD
<a name="custom-sharing-manage-delete"></a>

Before you delete a shared TD with `atx custom def delete`, revoke its shares. After the delete, consumers lose access right away, but the CLI doesn't warn you that the TD is shared, and the AWS RAM resource share isn't removed.