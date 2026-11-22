

# Accept, run, and download a shared transformation definition

These steps are for the consumer account.

## See what's shared with you
<a name="custom-sharing-consumer-list"></a>

```bash
atx custom def share list --incoming
```

The output has two tables:
+ `Invitations waiting for you ({{Region}})` – The share ID, the TD name, the owner account (**Shared From**), the status (**Pending**), and the TD's ARN.
+ `Accepted shares` – TDs that you can use, with status **Available** and the permission.

Before you accept, check who the owner is. The incoming list doesn't show a pending share's permission, because AWS RAM doesn't let a consumer read it until the consumer accepts. Ask the owner what the share allows.

Shares from accounts in your organization don't need acceptance when sharing with AWS Organizations is turned on in AWS RAM. They appear under **Accepted shares** right away.

## Accept or decline an invitation
<a name="custom-sharing-consumer-accept"></a>

```bash
atx custom def share accept {{share-id}}        # asks you to confirm
atx custom def share accept {{share-id}} --yes  # no prompt
```

```
Accepted share {{share-id}} from 111122223333.
  Transformation: java17-upgrade
  ARN:            arn:aws:transform-custom:us-east-1:111122223333:package/java17-upgrade
```

{{share-id}} can be the share ID (a UUID) or the share ARN.

```bash
atx custom def share decline {{share-id}}        # asks you to confirm
atx custom def share decline {{share-id}} --yes  # no prompt
```

You can also accept or decline in the AWS RAM console, on **Shared with me**, **Resource shares**, or with `aws ram accept-resource-share-invitation` and `aws ram reject-resource-share-invitation`.

**Note**  
After you accept a share, you can't leave it. To lose access, ask the owner to revoke the share.

## Find a shared TD
<a name="custom-sharing-consumer-find"></a>

`atx custom def list` shows TDs shared with you in a separate section, **Shared with you**. Each one shows the name, the description, the owner account (**From**), and the version.

With `--json`, shared TDs are in a separate `sharedTransformations` array, with `name`, `description`, `from` (the owner account ID), `version`, `arn`, and `createdAt`.

In this release, shared TDs aren't available in the AWS Transform web application. Use the AWS Transform CLI.

## Run a shared TD
<a name="custom-sharing-consumer-run"></a>

Always identify a shared TD by its ARN. Two owners can publish TDs with the same name.

```bash
atx custom def exec \
  -n arn:aws:transform-custom:us-east-1:111122223333:package/java17-upgrade \
  -p ./my-repo
```

All the usual `atx custom def exec` options work, including `-c`, `-g`, `--limit`, and `--tv`. To run a specific version, add `--tv {{version}}`. The run happens in your account, and your account is charged for it.

## Download a shared TD to adapt it
<a name="custom-sharing-consumer-download"></a>

If the share's permission is `ExecuteWithLearningsAndPackageDownload`, you can download the TD's content.

```bash
atx custom def get -n arn:aws:transform-custom:us-east-1:111122223333:package/java17-upgrade --td ./
```

```
✓ Transformation definition 'java17-upgrade' from 111122223333 retrieved successfully and saved to directory './111122223333-java17-upgrade'
```

To adapt it, edit the downloaded files and publish the result as a new TD in your account with `atx custom def publish`. The new TD belongs to your account. It has its own versions, permissions, and lessons, and it starts with no lessons. Later changes to the owner's TD don't affect your copy, and your changes don't affect theirs. Your TD keeps working if the owner revokes the share.