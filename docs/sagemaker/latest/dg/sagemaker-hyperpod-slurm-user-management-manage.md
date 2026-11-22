

# Managing users and groups

Every change to local users and groups is an `update-cluster-extension` call. HyperPod applies the change to every node, and nodes that you add later get it automatically. You don't need to connect to nodes or run scripts.

Updates follow the rules in [How updates apply to user sources](sagemaker-hyperpod-slurm-user-management-config.md#sagemaker-hyperpod-slurm-user-management-config-how-updates-apply-to-user-sources). Two catch people out: each list replaces the whole list, so to add one user, send the complete `users` list; and leaving a user out of `users` doesn't remove them. That user stays on the nodes that already have them, but new, replaced, and patched nodes don't get them, so nodes drift apart. To remove a user from every node, list them in `deleteUsers`.

We recommend that you keep the complete `localUsers` source in one file under version control, edit the file, and send the whole source each time. This avoids removing an entry from a list by mistake.

**To change local users by using the AWS CLI**

1. Edit your configuration file, for example `users-config.json`.

1. Run `update-cluster-extension` with the edited file.

   ```
   aws sagemaker update-cluster-extension \
      --cluster-arn arn:aws:sagemaker:{{us-west-2}}:{{111122223333}}:cluster/{{abcd1234efgh}} \
      --extension-arn {{extension-arn}} \
      --configuration-values "$(jq -c . {{users-config.json}})"
   ```

1. Run `describe-cluster-extension` until the status returns to `Active`.

The following examples start from the configuration in [Installing the extension](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-installing-the-extension). Each example is a complete update to send.

## Add a user
<a name="sagemaker-hyperpod-slurm-user-management-manage-add-a-user"></a>

Add the user to `users`, and send the whole list. The `groups` list isn't in the update, so it keeps its current value.

```json
{
  "userSources": {
    "localUsers": {
      "users": [
        { "username": "admin-1",  "uid": 2001, "groups": ["cluster-admins", "hpc-users"] },
        { "username": "user-1",   "uid": 2002, "groups": ["hpc-users"] },
        { "username": "user-2",   "uid": 2003, "groups": ["hpc-users"] },
        { "username": "new-user", "uid": 2004, "groups": ["hpc-users"] }
      ]
    }
  }
}
```

## Give a user more access
<a name="sagemaker-hyperpod-slurm-user-management-manage-give-a-user-more-access"></a>

Access comes from groups, so add a group to the user's `groups`. For example, to make user-2 an administrator, add `cluster-admins` to user-2's groups and send the complete `users` list.

The extension adds the user to the groups that you list, and removes the user from groups that the configuration defines but no longer lists for the user. It doesn't change the user's membership in groups that the configuration doesn't define. A user's new group memberships can take up to 10 minutes to appear inside Slurm jobs, because Slurm caches group membership.

To change the access of every member of a group, change the group's `ssh` or `sudo` targets in `groups` instead.

## Slurm accounting
<a name="sagemaker-hyperpod-slurm-user-management-manage-slurm-accounting"></a>

Every local user is registered under Slurm's `root` account, and you can't choose another. The extension leaves associations that you add with `sacctmgr` in place, and doesn't remove associations when you take a user out of `users`.

## Block a user's login
<a name="sagemaker-hyperpod-slurm-user-management-manage-block-a-user-s-login"></a>

To keep a user's account and files but stop them from logging in, set the user's `shell` to `nologin`, or remove the user from every group that grants SSH access. To restore access, set `shell` back to `bash` or add the group back.

## Settings that you can't change
<a name="sagemaker-hyperpod-slurm-user-management-manage-settings-that-you-can-t-change"></a>

You can't change the UID of an existing user or the GID of an existing group, and you can't move an existing user's home directory. To change one of these, remove the user or group, and create a new one with a new name.

## Retry after a failed update
<a name="sagemaker-hyperpod-slurm-user-management-manage-retry-after-a-failed-update"></a>

If an update fails on some nodes, Health in the `describe-cluster-extension` response shows why. Fix the cause, for example by removing a conflicting account or correcting a permission, and then run `update-cluster-extension` again without changing the configuration. HyperPod retries the nodes that failed. For more information, see [Retrying failed nodes](sagemaker-hyperpod-slurm-extensions.md#sagemaker-hyperpod-slurm-extensions-retrying-failed-nodes).

## Remove a user
<a name="sagemaker-hyperpod-slurm-user-management-manage-remove-a-user"></a>

When you remove a user, the extension does the following on every node:
+ Locks the account, and ends the user's sessions and processes.
+ Cancels the user's Slurm jobs, and removes the user's Slurm record, including every association, even ones that you added yourself.
+ Deletes the user's home directory, and the user's data directory at `/fsx/{{username}}` if it has one.
+ Deletes the account.

The extension removes an account only on nodes where both the user name and the UID match the `deleteUsers` entry.

**Warning**  
`deleteUsers` permanently deletes the user's home directory and data. Copy any files that you need before you remove a user. Don't reuse the UID for another user.

**To remove a user by using the AWS CLI**

1. Make sure that the extension's status is `Active`, so that every node has the current configuration.

1. In your configuration file, remove the user from `users`, and add the user's name and UID to `deleteUsers`. The following update removes `new-user`.

   ```json
   {
    "userSources": {
      "localUsers": {
        "users": [
          { "username": "admin-1", "uid": 2001, "groups": ["cluster-admins", "hpc-users"] },
          { "username": "user-1",  "uid": 2002, "groups": ["hpc-users"] },
          { "username": "user-2",  "uid": 2003, "groups": ["hpc-users"] }
        ],
        "deleteUsers": [ { "username": "new-user", "uid": 2004 } ]
      }
    }
   }
   ```

1. Run `update-cluster-extension` with the file, and wait for the status to return to `Active`.

You can leave removed users in `deleteUsers`. An entry has no effect on a node where the user doesn't exist. Because `deleteUsers` is a list, the next update that includes `deleteUsers` replaces it.

## Remove a group
<a name="sagemaker-hyperpod-slurm-user-management-manage-remove-a-group"></a>

In one update, remove the group from `groups`, remove it from every user's `groups` list, and add its name and GID to `deleteGroups`. The extension removes the group and its SSH and sudo rules from every node. If a user in `users` still lists the group, every node refuses the update. A group that is still a user's private group can't be removed.

If you remove a group from `groups` without listing it in `deleteGroups`, the group stays on the nodes, and its SSH and sudo rules can stay in effect. To revoke a group's access, use `deleteGroups`, or remove the group's `ssh` and `sudo` targets.

## Stop managing all local users
<a name="sagemaker-hyperpod-slurm-user-management-manage-stop-managing-all-local-users"></a>

To stop managing local users, set the `localUsers` source to `null`. The accounts stay on the nodes. To delete the accounts, first send an update that lists them in `deleteUsers` and their groups in `deleteGroups`, wait for the status to return to `Active`, and then remove the source.

```json
{ "userSources": { "localUsers": null } }
```

## Delete the extension
<a name="sagemaker-hyperpod-slurm-user-management-manage-delete-the-extension"></a>

When you delete the extension with `delete-cluster-extension`, it removes its SSH and sudo rules, its directory (SSSD) configuration, and its health check from every node. It keeps every user, group, home directory, SSH key, and Slurm association that it created, and HyperPod stops managing them. Nodes that you add afterward don't get them.

**Important**  
After you delete the extension, SSH access is no longer limited to the groups that you granted. Every remaining account can log in over SSH again. To remove users' access, remove them with `deleteUsers` before you delete the extension.

## Troubleshooting
<a name="sagemaker-hyperpod-slurm-user-management-manage-troubleshooting"></a>

To connect to a node while you troubleshoot, use AWS Systems Manager (SSM), which doesn't depend on the extension's SSH rules. Each run on a node is logged in the `SageMakerUserManagement/{{instance-group-name}}/{{instance-id}}` log stream.

### The status is CreateFailed or UpdateFailed
<a name="sagemaker-hyperpod-slurm-user-management-manage-the-status-is-createfailed-or-updatefailed"></a>

Each node refuses before it changes anything. Health shows the cause, and the message names the setting. Common messages:
+ **`… belongs to another account on this node`, or `… already exists on this node with a different uid`:** A user name or UID conflicts with an existing account. Use the existing values, or different ones.
+ **`… repeats an earlier entry`:** Two users have the same UID, or two groups have the same GID. The API doesn't check this.
+ **`… isn't this account's home on this node, and a home can't move`:** Set `homeDirectory` to the account's existing home directory.
+ **`DependencyUnreachable` on the controller node:** `slurmdbd` didn't respond within 2 minutes. Check that `slurmdbd` and its database are running. If `slurmdbd` answers but doesn't list the cluster yet, the code is `ConfigurationConflict`.
+ **`userSources.ldap.ldapDefaultBindDn doesn't bind to the directory …`:** Check the bind DN and the password in the bind secret.
+ **`userSources.ldap.ldapUri can't be reached from this node over TLS …`:** Check that the URI resolves, that the cluster's security group allows its port, and that `ldapTlsCacertSecretArn` holds the CA that signed the directory's certificate.
+ **`… names a secret this cluster's execution role can't read …`:** Allow `secretsmanager:GetSecretValue` on the secret, and `kms:Decrypt` on its key.
+ **`… names a secret that holds key/value pairs …`:** Store the password alone, as plain text.

HyperPod doesn't retry these failures. Send the corrected configuration, or, if you fixed the node or IAM, run `update-cluster-extension` without changes.

### The status is Degraded
<a name="sagemaker-hyperpod-slurm-user-management-manage-the-status-is-degraded"></a>

A node reports one of the codes in [Logs and health checks](sagemaker-hyperpod-slurm-user-management-extension.md#sagemaker-hyperpod-slurm-user-management-extension-logs-and-health-checks). For example, `DirectoryOffline` means that SSSD can't reach the directory, and `SSHDropInMissing` means that the extension's SSH rules file was removed from the node. Fix the cause on the node. The status returns to `Active` when the node reports healthy again.

### A user can't log in over SSH
<a name="sagemaker-hyperpod-slurm-user-management-manage-a-user-can-t-log-in-over-ssh"></a>

Check the following, in order:
+ **Group access:** A local user needs a group in their `groups` list whose `ssh` targets include the node's type. A directory user needs to be a member, in the directory, of a group in `ldapGroups` whose `ssh` targets include the node's type.
+ **Rollout:** Make sure that the extension is `Active` and that `ActiveCount` equals `TotalCount`.
+ **Directory resolution:** For a directory user, make sure that the user resolves on the node, for example with `id user-1@example.com`. If the user doesn't resolve, check `ldapSearchBase`, the network path to the directory, and the secrets. If `useFullyQualifiedNames` is `ENABLED`, the user must log in with the full name, and the `ldapGroups` names must end with `@{{domain}}`.
+ **Login method:** With `PUBLIC_KEY`, make sure that the user's public key is in the directory attribute that `ldapUserSshPublicKey` names. For local users, see [Local users](sagemaker-hyperpod-slurm-user-management-permissions.md#sagemaker-hyperpod-slurm-user-management-permissions-local-users).
+ **Shell:** A user whose shell is `nologin` can't log in.

### Users who had SSH access are refused
<a name="sagemaker-hyperpod-slurm-user-management-manage-users-who-had-ssh-access-are-refused"></a>

After the extension writes SSH rules on a node, only members of the groups that target the node, and the `ubuntu` user, can log in over SSH. Add every group that needs access to `localUsers.groups` or `ldapGroups`, with the right node types. This includes directory groups such as `ClusterAdmin`, which had access by default with the base lifecycle scripts.

### A removed user or group is still on the nodes
<a name="sagemaker-hyperpod-slurm-user-management-manage-a-removed-user-or-group-is-still-on-the-nodes"></a>

Removing a user from `users`, or a group from `groups`, doesn't delete it. List the user in `deleteUsers`, or the group in `deleteGroups`, with the matching UID or GID.

### The configuration is too long
<a name="sagemaker-hyperpod-slurm-user-management-manage-the-configuration-is-too-long"></a>

`ConfigurationValues` can be up to 10,240 characters, which fits about 40–60 users with groups and home directories. Send minified JSON, use shorter names, or move most users to Active Directory.

### A user's jobs fail on a new node
<a name="sagemaker-hyperpod-slurm-user-management-manage-a-user-s-jobs-fail-on-a-new-node"></a>

A node that HyperPod adds or replaces can accept Slurm jobs for 1–2 minutes before the extension creates the users on it. Resubmit the job.

### A user's new group doesn't apply inside Slurm jobs
<a name="sagemaker-hyperpod-slurm-user-management-manage-a-user-s-new-group-doesn-t-apply-inside-slurm-jobs"></a>

Slurm caches group membership. New memberships can take up to 10 minutes to appear inside jobs.

### Amazon EC2 Instance Connect stopped working
<a name="sagemaker-hyperpod-slurm-user-management-manage-amazon-ec2-instance-connect-stopped-working"></a>

The `ldap` source removes the `ec2-instance-connect` package from the nodes, and doesn't reinstall it. Use SSM or SSH instead.